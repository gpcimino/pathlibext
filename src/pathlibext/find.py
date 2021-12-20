import os
import fnmatch
from pathlib import Path


def _find(self: Path = ".", type_: str = "fd", wildcards: str = None, mindepth=0, maxdepth=float("inf")):
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
            continue # need to go deeper
#
# def _find(self, mindepth=0, maxdepth=float("inf"), type_=None, name=None):
#     rootdir = str(self)
#     root_depth = rootdir.rstrip(os.path.sep).count(os.path.sep) - 1
#     for dirpath, dirs, files in os.walk(rootdir):
#         depth = dirpath.count(os.path.sep) - root_depth
#         if mindepth <= depth <= maxdepth:
#             if type_ is None or type_ == "d":
#                 for dirname in dirs:
#                     if name is None or fnmatch.fnmatch(dirname, name):
#                         yield Path(os.path.join(dirpath, dirname))
#             if type_ is None or type_ == "f":
#                 for filename in files:
#                     if name is None or fnmatch.fnmatch(filename, name):
#                         yield Path(os.path.join(dirpath, filename))
#         elif depth > maxdepth:
#             del dirs[:]  # too deep, don't recurse

