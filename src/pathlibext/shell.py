import shutil
from pathlib import Path


def _copy(self, dest: Path, follow_symlinks: bool = True):
    return Path(shutil.copy(str(self), str(dest), follow_symlinks=follow_symlinks))


def _copy_preserve_metadata(self, dest: Path, follow_symlinks: bool = True):
    return Path(shutil.copy2(str(self), str(dest), follow_symlinks=follow_symlinks))


def _move(self, dest: Path):
    return Path(shutil.move(str(self), str(dest)))
