from pathlib import Path
import pathlibext  # pylint: disable=unused-import

print(list(Path(".").resolve().find("f", name="*.py", maxdepth=4)))