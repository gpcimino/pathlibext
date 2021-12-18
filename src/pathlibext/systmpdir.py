import tempfile
from pathlib import Path


def _systmpdir():
    return Path(tempfile.gettempdir())
