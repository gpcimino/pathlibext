import fnmatch
import os
from pathlib import Path


def _find(
    self: Path = ".",
    type_: str = "fd",
    wildcards: str = None,
    mindepth=0,
    maxdepth=float("inf"),
):
    def _depth(path):
        return str(path).count(os.path.sep)

    rootdir = str(self)
    root_depth = _depth(rootdir)
    for top, dirs, files in os.walk(rootdir):
        depth = _depth(top) - root_depth
        if mindepth <= depth <= maxdepth:
            top = Path(top)
            if "f" in type_:
                for name in files:
                    if wildcards is None or fnmatch.fnmatch(name, wildcards):
                        yield top / name
            if "d" in type_:
                for name in dirs:
                    if wildcards is None or fnmatch.fnmatch(name, wildcards):
                        yield top / name
        elif depth > maxdepth:
            del dirs[:]  # too deep, don't recurse
        else:
            continue  # need to go deeper
