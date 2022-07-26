import tempfile
from pathlibext import Path  # pylint: disable=unused-import


def _write_text_tmpfile(text, encoding=None, newline=None, errors=None):
    if not isinstance(text, str):
        raise TypeError(f"data must be str, not {text.__class__.__name__}")
    with tempfile.NamedTemporaryFile(
        mode="w", encoding=encoding, newline=newline, errors=errors, delete=False
    ) as f:
        f.write(text)
        return Path(f.name)


def _tmpfile():
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as f:
        return Path(f.name)
