"""Verify the duplicated _logging modules are equivalent and configurable."""
import importlib
import logging
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]


def _reload(modname: str):
    """Reload module so module-level state (`_configured`, root handlers) reset."""
    if modname in sys.modules:
        del sys.modules[modname]
    return importlib.import_module(modname)


@pytest.fixture
def reset_root_logger():
    """Snapshot + restore root logger state so test pollution is bounded."""
    root = logging.getLogger()
    saved = (root.level, list(root.handlers))
    root.handlers.clear()
    yield
    root.handlers.clear()
    root.setLevel(saved[0])
    for h in saved[1]:
        root.addHandler(h)


@pytest.mark.parametrize("module_name", ["parsers._logging", "src._logging"])
def test_get_logger_returns_logger(monkeypatch, reset_root_logger, module_name):
    monkeypatch.delenv("BOXBALL_LOG_LEVEL", raising=False)
    monkeypatch.delenv("BOXBALL_STAGE", raising=False)
    mod = _reload(module_name)
    logger = mod.get_logger("boxball.test")
    assert isinstance(logger, logging.Logger)
    # Default level INFO
    assert logging.getLogger().level == logging.INFO


@pytest.mark.parametrize("module_name", ["parsers._logging", "src._logging"])
def test_log_level_env(monkeypatch, reset_root_logger, module_name):
    monkeypatch.setenv("BOXBALL_LOG_LEVEL", "DEBUG")
    mod = _reload(module_name)
    mod.get_logger("boxball.test")
    assert logging.getLogger().level == logging.DEBUG


@pytest.mark.parametrize("module_name", ["parsers._logging", "src._logging"])
def test_invalid_level_falls_back_to_info(monkeypatch, reset_root_logger, module_name):
    monkeypatch.setenv("BOXBALL_LOG_LEVEL", "BOGUS")
    mod = _reload(module_name)
    mod.get_logger("boxball.test")
    assert logging.getLogger().level == logging.INFO


@pytest.mark.parametrize("module_name", ["parsers._logging", "src._logging"])
def test_stage_env_appears_in_format(monkeypatch, reset_root_logger, capsys, module_name):
    monkeypatch.setenv("BOXBALL_STAGE", "extract")
    monkeypatch.setenv("BOXBALL_LOG_LEVEL", "INFO")
    mod = _reload(module_name)
    logger = mod.get_logger("boxball.test")
    logger.info("hello")
    captured = capsys.readouterr()
    assert "[extract]" in captured.err
    assert "hello" in captured.err


def test_extract_and_transform_modules_match():
    extract_src = (REPO_ROOT / "extract" / "parsers" / "_logging.py").read_text()
    transform_src = (REPO_ROOT / "transform" / "src" / "_logging.py").read_text()
    # Strip the docstring's first line (which differs by stage name) and compare body.
    def body(src: str) -> str:
        # Drop first triple-quoted docstring block.
        first = src.find('"""')
        second = src.find('"""', first + 3)
        return src[second + 3:]
    assert body(extract_src) == body(transform_src), (
        "extract/parsers/_logging.py and transform/src/_logging.py must stay in sync"
    )
