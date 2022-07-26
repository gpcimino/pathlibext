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