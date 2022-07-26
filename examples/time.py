from pathlib import Path
import pathlibext  # pylint: disable=unused-import

f = Path.tmpfile() 
f.write_text("abc")
print(f.access_time()) 
f.unlink()