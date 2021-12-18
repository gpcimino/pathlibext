import tempfile
from pathlib import Path


def _systmpdir():
    return Path(tempfile.gettempdir())


def _tmpdir_in(self, suffix=None, prefix=None):
    return Path(tempfile.mkdtemp(suffix, prefix, self))


def _tmpdir(suffix=None, prefix=None):
    return Path(tempfile.mkdtemp(suffix, prefix))
