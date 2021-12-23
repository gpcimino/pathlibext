# Pathlib Extensions

![example workflow](https://github.com/gpcimino/pathlibext/actions/workflows/python-package.yml/badge.svg)

Add convenience methods to Python [Pathlib](https://docs.python.org/3/library/pathlib.html) via [monkey patching](https://en.wikipedia.org/wiki/Monkey_patch).

## Installation

Pathlibext is available in PyPI. To Install it use `pip`:

```bash
pip install pathlibext
```


## Usage

Just import pathlibext once and Path object will be extended with a series of convenience methods:

```python
from pathlib import Path
import pathlibext  # pylint: disable=unused-import


if __name__ == '__main__':
    tmp = Path.tmpdir()  # from pathlibext
    files = [
        tmp / "1" / "a.txt",
        tmp / "1" / "b.txt",
        tmp / "2" / "a.txt",
        tmp / "2" / "b.txt",
    ]
    for f in files:
        f.parent.mkdir(exist_ok=True)
        f.touch()
    for d in tmp.find(type_="d", name="2"):  # from pathlibext
        print(f"removing {d}...")
        d.rmtree()  # from pathlibext
    tmp.rmtree()
```

## List of added methods

 - **Unix-like find**: `Path(".").find(type_f, name="*.py", maxdepth=4)`
 - **File name match**: Path("/tmp/Something.txt).match("S*.txt)
 - **File name matchcase**: Path("/tmp/Something.txt).matchcase("s*.txt)
 - **Remove non-empty directory tree**: Path("/tmp/something/").rmtree()
 - **Copy**: Path("tmp/something.txt).copy("~/tmp")
 - **Copy preserve metadata**: Path("tmp/something.txt).copy_preserve_metadata("~/tmp")
 - **Move**: Path("tmp/something.txt).move("~/tmp")
 - **File size**: Path("tmp/something.txt).size()
 - **File access time**: Path("tmp/something.txt).access_time()
 - **File modification time**: Path("tmp/something.txt).modification_time()
 - **File creation time (Windows only)**: Path("tmp/something.txt).creation_time()
 - **File metadata change time (Posix only)**: Path("tmp/something.txt).metadatachange_time()
 - **System temporary directory as Path**: Path.systmpdir()
 - **Create temporary directory as Path in existing directory**: Path("tmp").tmpdir_in()
 - **Create temporary directory as Path**: Path().tmpdir()
 - **Current file path**: Path.current_file_path()
 - **Current file directory**: Path.current_file_dir()
