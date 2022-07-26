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