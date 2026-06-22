"""Project path utilities.

This module centralizes repository-relative paths so scripts do not rely on
fragile assumptions about the current working directory.
"""

from __future__ import annotations

from pathlib import Path


def find_project_root(start: Path | None = None) -> Path:
    """Find the repository root by searching upward for pyproject.toml.

    Parameters
    ----------
    start
        Optional starting path. If omitted, this file's location is used.

    Returns
    -------
    Path
        Absolute path to the repository root.

    Raises
    ------
    FileNotFoundError
        If no pyproject.toml is found in this path's parents.
    """
    current = (start or Path(__file__)).resolve()

    if current.is_file():
        current = current.parent

    for path in [current, *current.parents]:
        if (path / "pyproject.toml").exists():
            return path

    raise FileNotFoundError(
        "Could not find project root. Expected a pyproject.toml file in this "
        "directory or one of its parents."
    )


ROOT_DIR = find_project_root()

DATA_DIR = ROOT_DIR / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
INTERIM_DATA_DIR = DATA_DIR / "interim"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

CONFIG_DIR = ROOT_DIR / "configs"
REPORTS_DIR = ROOT_DIR / "reports"
ARTIFACTS_DIR = ROOT_DIR / "artifacts"