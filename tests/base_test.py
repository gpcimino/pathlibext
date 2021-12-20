import tempfile
import unittest
from collections import Counter
from pathlib import Path

import pathlibext.find  # pylint: disable=unused-import


class BaseTest(unittest.TestCase):
    def setUp(self):
        # pylint: disable=consider-using-with
        self.__tmpdir = tempfile.TemporaryDirectory()
        self.root = Path(self.__tmpdir.name)
        self.files = []

    def create_file_tree(self):
        self.files = [
            self.root / "f1.txt",
            self.root / "f2.dat",
            self.root / "a" / "f1.txt",
            self.root / "a" / "f2.dat",
            self.root / "a" / "b" / "f1.txt",
            self.root / "a" / "b" / "f2.dat",
            self.root / "a" / "b" / "c" / "f1.txt",
            self.root / "a" / "b" / "c" / "f2.dat",
            self.root / "a" / "b" / "c" / "d" / "f1.txt",
            self.root / "a" / "b" / "c" / "d" / "f2.dat",
        ]
        for f in self.files:
            f.parent.mkdir(parents=True, exist_ok=True)
            f.touch()

    def _dirs(self):
        return [f.parent for f in self.files]

    def assert_list_equal_unordered(self, expected, actual):
        # pylint: disable=no-self-use
        return Counter(expected) == Counter(actual)

    def tearDown(self):
        self.__tmpdir.cleanup()
