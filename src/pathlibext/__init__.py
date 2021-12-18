from pathlib import Path
from pathlibext.rmtree import _rmtree
from pathlibext.find import _find
from pathlibext.tmpdir import _systmpdir, _tmpdir_in, _tmpdir

Path.rmtree = _rmtree
Path.find = _find

Path.systmpdir = _systmpdir
Path.tmpdir_in = _tmpdir_in
Path.tmpdir = _tmpdir

# name matches = fnmatch (Path("whatever").match("w*") == True)
