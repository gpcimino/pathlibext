import tempfile
import io
from pathlibext import Path


def _write_text_tmp_file(text, encoding=None, newline=None, errors=None):
        if not isinstance(text, str):
            raise TypeError('data must be str, not %s' % text.__class__.__name__)
        #encoding = io.text_encoding(encoding)
        with tempfile.NamedTemporaryFile(mode='w', encoding=encoding, newline=newline, errors=errors, delete=False) as f:
            f.write(text)  
            return Path(f.name)

def _tmp_file():
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
        return Path(f.name)