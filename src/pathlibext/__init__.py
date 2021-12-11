from pathlib import Path
from pathlibext.rmtree import _rmtree
from pathlibext.find import _find

Path.rmtree = _rmtree
Path.find = _find
