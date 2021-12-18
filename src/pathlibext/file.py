def size(self, unit="bytes"):
    # follow_symlinks=True
    bytes = self.stat().st_size
    if unit == "bytes":
        return bytes
    elif unit == "kilobytes":
        return bytes / 1024
    elif unit == "megabytes":
        return bytes / (1024 ** 2)
    elif unit == "gigabytes":
        return bytes / (1024 ** 3)
    elif unit == "terabytes":
        return bytes / (1024 ** 4)
    else:
        raise ValueError("unknown unit of measure for file size")
