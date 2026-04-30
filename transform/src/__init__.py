import os
from pathlib import Path


def _resolve(env_key: str, default_subdir: str) -> Path:
    """
    Returns Path from env var if set; otherwise repo-anchored default.
    Default is computed lazily so containers (which set the env var) never
    rely on resolving a repo root that may not exist at /.
    """
    val = os.environ.get(env_key)
    if val:
        return Path(val)
    return Path(__file__).resolve().parents[2] / default_subdir


OUTPUT_PATH = _resolve("BOXBALL_OUTPUT_PATH", "ddl")
EXTRACT_PATH_PREFIX = _resolve("BOXBALL_EXTRACT_PATH", "extract")
TRANSFORM_PATH_PREFIX = _resolve("BOXBALL_TRANSFORM_PATH", "transform")
# DATA_PATH_PREFIX is the in-container path baked into emitted COPY DDL — it
# refers to the runtime DB container's filesystem, not the build host's. Not
# derived from the repo root; the env-var override is for unusual cases where
# a load stage mounts CSVs at a non-default path.
DATA_PATH_PREFIX = Path(os.environ.get("BOXBALL_DATA_PATH", "/data"))
