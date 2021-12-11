import shutil


def _rmtree(self, ignore_errors=False, onerror=None):
    """Delete an entire directory tree. This is a wrapper around shutil.rmtree"""
    if not self.is_dir():
        raise ValueError("rmtree called on Path that is not a directory")
    if not self.exists():
        raise ValueError(f"File system path {self} doesn't exists")
    return shutil.rmtree(str(self), ignore_errors, onerror)
