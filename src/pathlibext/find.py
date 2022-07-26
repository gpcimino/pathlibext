import fnmatch
import os
from pathlib import Path


def _find(
    self: Path,
    type_: str = "fd",
    name: str = None,
    mindepth: int = 0,
    maxdepth: int = 64000,
):
    def _depth(path: Path):
        return str(path).count(os.path.sep)

    rootdir = str(self)
    root_depth = _depth(rootdir)
    for top, dirs, files in os.walk(rootdir):
        depth = _depth(top) - root_depth
        if mindepth <= depth <= maxdepth:
            top = Path(top)
            if "f" in type_:
                for filename in files:
                    if name is None or fnmatch.fnmatch(filename, name):
                        yield top / filename
            if "d" in type_:
                for dirname in dirs:
                    if name is None or fnmatch.fnmatch(dirname, name):
                        yield top / dirname
        elif depth > maxdepth:
            del dirs[:]  # too deep, don't recurse
        else:
            continue  # need to go deeper
