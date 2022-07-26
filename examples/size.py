from pathlib import Path
import pathlibext  # pylint: disable=unused-import

f = Path.tmpdir() / "test.txt"
f.write_text("abc")
print(f.size()) # 3
print(f.size("MB")) # 2.86102294921875e-06