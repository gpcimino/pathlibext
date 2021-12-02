import os
import fnmatch
from pathlib import Path


def _find(root: Path = ".", type_: str = "fd", wildcards: str = None):
    for top, dirs, files in os.walk(root):
        top = Path(top)
        pass
        if "f" in type_:
            for name in files:
                if wildcards is None or fnmatch.fnmatch(name, wildcards):
                    yield top / name
        if "d" in type_:
            for name in dirs:
                if wildcards is None or fnmatch.fnmatch(name, wildcards):
                    yield top / name


Path.find = _find

if __name__ == "__main__":
    for item in _find(Path("."), "d", "py*"):
        print(item)
