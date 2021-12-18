from pathlib import Path
from pathlibext.rmtree import _rmtree
from pathlibext.find import _find
from pathlibext.systmpdir import _systmpdir

Path.rmtree = _rmtree
Path.find = _find
Path.systmpdir = _systmpdir
