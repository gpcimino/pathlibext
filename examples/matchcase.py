from pathlib import Path
import pathlibext  # pylint: disable=unused-import

print(Path("/foo/BAR.txt").matchcase("*BAR*")) # True
print(Path("/foo/BAR.txt").matchcase("*bar*")) # False