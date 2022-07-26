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