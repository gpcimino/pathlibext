import tempfile
from pathlib import Path


def _systmpdir():
    return Path(tempfile.gettempdir())


def _tmpdir_in(self, suffix: str = None, prefix: str = None):
    return Path(tempfile.mkdtemp(suffix, prefix, self))


def _tmpdir(suffix: str = None, prefix: str = None):
    return Path(tempfile.mkdtemp(suffix, prefix))
