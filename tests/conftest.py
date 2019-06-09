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
    TMP.joinpath("extract").mkdir()
    sys.path.insert(0, str(Path(os.getcwd()).joinpath("extract")))
    sys.path.insert(0, str(Path(os.getcwd()).joinpath("transform")))
    raw = "unzip extract/fixtures/raw/{0}.zip -d /tmp/ && mv /tmp/{0}-master /tmp/boxball/{0}"
    csv = "cp -r extract/fixtures/extract/{0} /tmp/boxball/extract/{0}"
    for archive in ("retrosheet", "baseballdatabank"):
        subprocess.run(raw.format(archive), shell=True, check=True)
        subprocess.run(csv.format(archive), shell=True, check=True)
    code_tables = "cp -r extract/code_tables /tmp/boxball"
    subprocess.run(code_tables, shell=True)

    TMP.joinpath(OUTPUT_PATH).mkdir()


def pytest_sessionfinish(session, exitstatus):
    rmtree(TMP)
