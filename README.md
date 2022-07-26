# Pathlib Extensions

![example workflow](https://github.com/gpcimino/pathlibext/actions/workflows/python-package.yml/badge.svg)

Add convenience methods to Python [Pathlib](https://docs.python.org/3/library/pathlib.html) via [monkey patching](https://en.wikipedia.org/wiki/Monkey_patch).

## Installation

Pathlibext is available in PyPI. To Install it use `pip`:

```bash
pip install pathlibext
```

## Usage

Just import pathlibext once and the Path class will be extended with a series of convenience methods:

```python
from pathlib import Path
import pathlibext  # pylint: disable=unused-import


if __name__ == '__main__':

    tmp = Path.tmpdir()  # from pathlibext
    print(f"Create temp directory {tmp}")

    for f in [
        tmp / "dir1" / "a.txt",
        tmp / "dir1" / "b.txt",
        tmp / "dir2" / "a.txt",
        tmp / "dir2" / "b.txt",
    ]:
        f.parent.mkdir(exist_ok=True)
        f.touch()
        print(f"Create file {f}")
    

    for d in tmp.find(type_="d", name="dir2"): # from pathlibext
        d.rmtree() # from pathlibext
        print(f"Remove non-empty directory {d}")

    print("Existing directories after rmtree()")
    for d in tmp.find(type_="d"): # from pathlibext
        print(f"{d}")

    tmp.rmtree() # from pathlibext
    print(f"Remove non-empty temp dir {tmp}")
```

## List of pathlibext methods

### find

Extends the `Path` object with `find` method which resembles POSIX find.
The `find` method returns a [generator](https://docs.python.org/3/howto/functional.html#generators).

```python
from pathlib import Path
import pathlibext  # pylint: disable=unused-import

print(list(Path(".").resolve().find("f", name="*.py", maxdepth=4)))
```

### match

Test whether the `Path` object matches the pattern string, returning a boolean.
Match is not case sensitive on Windows.  
Same as [fnmatch.match](https://docs.python.org/3/library/fnmatch.html#fnmatch.fnmatch).

```python
import os
from pathlib import Path
import pathlibext  # pylint: disable=unused-import

print(Path("/foo/BAR.txt").match("*BAR*")) # True

if os.name == "Windows":
    # On windows match() is case insensitive
    print(Path("/foo/BAR.txt").match("*bar*")) # True
else:
    # On POSIX match() is case sensitive
    print(Path("/foo/BAR.txt").match("*bar*")) # False
```

### matchcase

Test whether the `Path` object matches pattern, returning boolean.
The comparison is case-sensitive.
Same as [fnmatch.macthcase](https://docs.python.org/3/library/fnmatch.html#fnmatch.fnmatchcase).

```python
from pathlib import Path
import pathlibext  # pylint: disable=unused-import

print(Path("/foo/BAR.txt").matchcase("*BAR*")) # True
print(Path("/foo/BAR.txt").matchcase("*bar*")) # False
```

### rmtree

Delete non empty directory tree starting from the root represented as `Path` object.

```python
from pathlib import Path
import pathlibext  # pylint: disable=unused-import

tmp = Path.tmpdir()
f = tmp / "foo" / "test.txt"
d = f.parent
d.mkdir()
f.touch() # touchpath !
tmp.rmtree()
print(f.exists()) # False
print(d.exists()) # False
```

### copy and copy_preserve_metadata

Copies the file represented as `Path` object to destination file or directory provided as `Path` object.
Same as [shutil.copy](https://docs.python.org/3.7/library/shutil.html#shutil.copy).
To preserve metadata use copy_preserve_metadata() which is imlpemented with [shutil.copy2](https://docs.python.org/3.7/library/shutil.html#shutil.copy2).

```python
from pathlib import Path
import pathlibext  # pylint: disable=unused-import

src = Path.tmpdir() 
dst =  Path.tmpdir() 
f = src / "test.txt"
f.touch()

copied = f.copy(dst)

print(f.exists()) # True
print(copied.exists()) # True

src.rmtree() # cleanup
dst.rmtree() # cleanup
```

### move

Move the file represented by the `Path` object to another location again represented as `Path` object. It is implemented with [shutil.move](https://docs.python.org/3.7/library/shutil.html#shutil.move).

```python
from pathlib import Path
import pathlibext  # pylint: disable=unused-import

src = Path.tmpdir() 
dst =  Path.tmpdir() 
f = src / "test.txt"
f.touch()

moved = f.move(dst)

print(f.exists()) # False
print(moved.exists()) # True

src.rmtree() # cleanup
dst.rmtree() # cleanup
```

### size

Return the file size in bytes or in the specified unit of measure. Short hand for `Path.stat().st_size`.

```python
from pathlib import Path
import pathlibext  # pylint: disable=unused-import

f = Path.tmpdir() / "test.txt"
f.write_text("abc")
print(f.size()) # 3
print(f.size("MB")) # 2.86102294921875e-06
```

### access_time, modification_time, creation_time and metadatachange_time

`access_time()` and `modification_time()` are short hand methods for `Path().stat().st_atime` and `Path().stat().st_mtime`.

`creation_time()` is available only on Windows and returns the file creation, same as `Path().stat().st_ctime`.

`metadatachange_time()` is available only on POSIX and returns the file metadata change time, same as `Path().stat().st_ctime`.

All methods and are wrapper around [Path().stat()](https://docs.python.org/3/library/pathlib.html#pathlib.Path.stat).

CAUTION! All methods return time as **datetime objects** and are **local time**.

```python
from pathlib import Path
import pathlibext  # pylint: disable=unused-import

f = Path.tmpfile() 
f.write_text("abc")
print(f.access_time()) 
f.unlink()
```

### systmpdir

Return OS temporary directory as `Path`.

```python
from pathlib import Path
import pathlibext  # pylint: disable=unused-import

print(Path.systmpdir()) # Path('/tmp')
```

### tmpdir

Return a temporary directory as `Path`. This is a wrapper of [tempfile.mkdtemp](https://docs.python.org/3/library/tempfile.html#tempfile.mkdtemp).

```python
from pathlib import Path
import pathlibext  # pylint: disable=unused-import

print(Path.tmpdir())
```

### tmpdir_in

Creates a temporary directory as `Path` object inside an existing directory represented as `Path`.

```python
from pathlib import Path
import pathlibext  # pylint: disable=unused-import

print(Path("/tmp").tmpdir_in())
```

### current_file_path

Convinient method to get the file path as `Path` object of the currently executed file.
See `examples/current_file.py` on how to use it.

### current_file_dir

Convinient method to get the directory as `Path` object of the currently executed file.
See `examples/current_file.py` on how to use it.
