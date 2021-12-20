import os

from pathlib import Path
from pathlibext.rmtree import _rmtree
from pathlibext.find import _find
from pathlibext.tmpdir import _systmpdir, _tmpdir_in, _tmpdir
from pathlibext.stat import _size, _access_time, _modification_time,_ctime

Path.rmtree = _rmtree
Path.find = _find

Path.systmpdir = _systmpdir
Path.tmpdir_in = _tmpdir_in
Path.tmpdir = _tmpdir

Path.size = _size
Path.access_time = _access_time
Path.modification_time = _modification_time

if os.name == 'Windows':
    Path.creation_time = _ctime
else:
    Path.metadatachange_time = _ctime


# name matches = fnmatch (Path("whatever").match("w*") == True)
