import fnmatch


def _match(self, wildcards: str):
    return fnmatch.fnmatch(str(self), wildcards)


def _matchcase(self, wildcards: str):
    return fnmatch.fnmatchcase(str(self), wildcards)
