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
    sys.path.insert(0, str(Path(os.getcwd()).joinpath("extract")))
    sys.path.insert(0, str(Path(os.getcwd()).joinpath("transform")))
    unzip = "unzip extract/fixtures/{0}.zip -d . && mv {0}-master /tmp/boxball/{0}"
    for archive in ("retrosheet", "baseballdatabank"):
        subprocess.run(unzip.format(archive), shell=True)
    code_tables = "cp -r extract/code_tables /tmp/boxball"
    subprocess.run(code_tables, shell=True)

    TMP.joinpath(OUTPUT_PATH).mkdir()


def pytest_sessionfinish(session, exitstatus):
    rmtree(TMP)
