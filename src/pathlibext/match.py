import fnmatch


def match(self, wildcards: str):
    return fnmatch.fnmatch(str(self), wildcards)


def matchcase(self, wildcards: str):
    return fnmatch.fnmatchcase(str(self), wildcards)
