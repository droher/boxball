"""Shared logging config for the transform stage.

Mirror of `extract/parsers/_logging.py`; kept duplicated because each Docker
build context only sees its own subtree. Edit both copies together.
"""
import logging
import os
import sys

_DEFAULT_LEVEL = "INFO"
_configured = False


def _build_format() -> str:
    stage = os.environ.get("BOXBALL_STAGE", "").strip()
    # Escape % in stage label so a typo like BOXBALL_STAGE=foo%bar can't break
    # logging.Formatter's % substitution at format time.
    stage_field = f"[{stage.replace('%', '%%')}] " if stage else ""
    return f"%(asctime)s [%(levelname)s] {stage_field}%(name)s: %(message)s"


def _configure() -> None:
    global _configured
    if _configured:
        return
    level_name = os.environ.get("BOXBALL_LOG_LEVEL", _DEFAULT_LEVEL).upper()
    level = logging.getLevelNamesMapping().get(level_name, logging.INFO)
    handler = logging.StreamHandler(sys.stderr)
    handler.setFormatter(logging.Formatter(_build_format()))
    root = logging.getLogger()
    root.handlers.clear()
    root.addHandler(handler)
    root.setLevel(level)
    _configured = True


def get_logger(name: str) -> logging.Logger:
    _configure()
    return logging.getLogger(name)
