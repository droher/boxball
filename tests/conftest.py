import os
import subprocess
import sys
from pathlib import Path
from shutil import rmtree

REPO_ROOT = Path(__file__).resolve().parents[1]
TMP = Path("/tmp/boxball")

# Point all BOXBALL_* path env vars at the fixture sandbox before importing
# any module that resolves them at import time (transform/src/__init__.py,
# extract/parsers/util.py).
os.environ.setdefault("BOXBALL_PARSED_PATH", str(TMP / "parsed"))
os.environ.setdefault("BOXBALL_RETROSHEET_PATH", str(TMP / "retrosheet"))
os.environ.setdefault("BOXBALL_CODE_TABLES_PATH", str(TMP / "code_tables"))
os.environ.setdefault("BOXBALL_BASEBALLDATABANK_CORE_PATH", str(TMP / "baseballdatabank" / "core"))
os.environ.setdefault("BOXBALL_BASEBALLDATABANK_CONTRIB_PATH", str(TMP / "baseballdatabank" / "contrib"))
os.environ.setdefault("BOXBALL_OUTPUT_PATH", str(TMP / "ddl"))
os.environ.setdefault("BOXBALL_EXTRACT_PATH", str(TMP / "extract"))
os.environ.setdefault("BOXBALL_TRANSFORM_PATH", str(TMP / "transform"))

sys.path.insert(0, str(REPO_ROOT))
sys.path.insert(0, str(REPO_ROOT / "extract"))
sys.path.insert(0, str(REPO_ROOT / "transform"))

from extract.parsers.util import OUTPUT_PATH  # noqa: E402


def pytest_sessionstart(session):
    # rmtree first so a crashed prior run can't leave /tmp/boxball behind and
    # block startup with FileExistsError.
    rmtree(TMP, ignore_errors=True)
    TMP.mkdir()
    TMP.joinpath("extract").mkdir()
    # Fixture inner layouts mirror the matching extract/Dockerfile test stages:
    # retrosheet → canonical alldata.zip top-level tree at zip root; landed under
    # /tmp/boxball/retrosheet/. baseballdatabank → CSVs at zip root, landed under
    # /tmp/boxball/baseballdatabank/core/ to match BOXBALL_BASEBALLDATABANK_CORE_PATH.
    csv = "cp -r {repo}/extract/fixtures/extract/{name} /tmp/boxball/extract/{name}"
    subprocess.run(
        f"unzip -q {REPO_ROOT}/extract/fixtures/raw/retrosheet.zip -d /tmp/boxball/retrosheet",
        shell=True, check=True,
    )
    subprocess.run(
        f"mkdir -p /tmp/boxball/baseballdatabank/core && "
        f"unzip -q {REPO_ROOT}/extract/fixtures/raw/baseballdatabank.zip -d /tmp/boxball/baseballdatabank/core",
        shell=True, check=True,
    )
    for archive in ("retrosheet", "baseballdatabank"):
        subprocess.run(csv.format(repo=REPO_ROOT, name=archive), shell=True, check=True)
    subprocess.run("cp -r {repo}/extract/code_tables /tmp/boxball".format(repo=REPO_ROOT), shell=True, check=True)

    OUTPUT_PATH.mkdir(parents=True, exist_ok=True)


def pytest_sessionfinish(session, exitstatus):
    rmtree(TMP)
