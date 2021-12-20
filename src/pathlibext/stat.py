from datetime import datetime


def _size(self, unit="bytes"):
    # follow_symlinks=True
    size_bytes = self.stat().st_size
    if unit in ("bytes", "byte", "B"):
        return size_bytes
    if unit in ("kilobytes", "kilobyte", "KB"):
        return size_bytes / 1024
    if unit in ("megabytes", "megabyte", "MB"):
        return size_bytes / (1024 ** 2)
    if unit in ("gigabytes", "gigabyte", "GB"):
        return size_bytes / (1024 ** 3)
    if unit in ("terabytes", " terabyte", "TB"):
        return size_bytes / (1024 ** 4)
    raise ValueError("unknown unit of measure for file size")


def _access_time(self):
    t = self.stat().st_atime
    return datetime.fromtimestamp(t)


def _modification_time(self):
    t = self.stat().st_mtime
    return datetime.fromtimestamp(t)


def _ctime(self):
    t = self.stat().st_ctime
    return datetime.fromtimestamp(t)
