import inspect
from pathlib import Path


def _current_file_dir():
    return Path(inspect.stack()[1][1]).absolute().parent


def _current_file_path():
    return Path(inspect.stack()[1][1]).absolute()
