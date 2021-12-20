from datetime import  datetime


def _size(self, unit="bytes"):
    # follow_symlinks=True
    bytes = self.stat().st_size
    if unit == "bytes" or unit == "byte" or unit == "B":
        return bytes
    elif unit == "kilobytes" or unit == "kilobyte" or unit == "KB":
        return bytes / 1024
    elif unit == "megabytes" or unit == "megabyte" or unit == "MB":
        return bytes / (1024 ** 2)
    elif unit == "gigabytes" or unit == "gigabyte" or unit == "GB":
        return bytes / (1024 ** 3)
    elif unit == "terabytes" or unit == "terabyte" or unit == "TB":
        return bytes / (1024 ** 4)
    else:
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

