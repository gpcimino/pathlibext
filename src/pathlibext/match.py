import fnmatch


def match(self, wildcards):
    return fnmatch.fnmatch(str(self), wildcards)


def matchcase(self, wildcards):
    return fnmatch.fnmatchcase(str(self), wildcards)
