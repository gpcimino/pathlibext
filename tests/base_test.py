import unittest
from collections import Counter
from pathlib import Path
import tempfile
import pathlibext.find  # pylint: disable=unused-import


class BaseTest(unittest.TestCase):
    def setUp(self):
        self.__tmpdir = tempfile.TemporaryDirectory()
        self.root = Path(self.__tmpdir.name)
        # self.root = Path.mktempdir()
        self.files = [
            self.root / "a.txt",
            self.root / "b.dat",
            self.root / "d" / "a.txt",
            self.root / "d" / "b.dat",
        ]
        for f in self.files:
            f.parent.mkdir(parents=True, exist_ok=True)
            f.touch()

    def _dirs(self):
        return [f.parent for f in self.files]

    def assert_list_equal_unordered(self, expected, actual):
        return Counter(expected) == Counter(actual)

    def tearDown(self):
        self.__tmpdir.cleanup()
