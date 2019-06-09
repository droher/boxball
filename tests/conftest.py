import subprocess
from pathlib import Path
import os
from shutil import rmtree
import sys
sys.path.insert(0, os.getcwd())

from extract.parsers.util import OUTPUT_PATH

TMP = Path("/tmp/boxball")


def pytest_sessionstart(session):
    TMP.mkdir()
    unzip = "unzip extract/fixtures/{0}.zip -d . && mv {0}-master /tmp/boxball/{0}"
    for archive in ("retrosheet", "baseballdatabank"):
        subprocess.run(unzip.format(archive), cwd=str(Path.cwd()), shell=True)

    # Move to same folder structure to avoid import issues
    copy_code = "cp -r {} /tmp/boxball"
    for d in ("extract/parsers", "transform/src"):
        subprocess.run(copy_code.format(d), cwd=str(Path.cwd()), shell=True)

    os.chdir(TMP)
    OUTPUT_PATH.mkdir()


def pytest_sessionfinish(session, exitstatus):
    rmtree(TMP)
