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