import unittest
from collections import Counter
from pathlib import Path
import tempfile
import pathlibext.find  # pylint: disable=unused-import


class TestFind(unittest.TestCase):
    def setUp(self):
        self.tmp_dir = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp_dir.name)
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

    def test_find_all(self):
        files = list(Path.find(self.root))
        self.assert_list_equal_unordered(self._dirs() + self.files, files)

    def test_find_dir(self):
        files = list(Path.find(self.root, type_="d"))
        self.assert_list_equal_unordered(self._dirs(), files)

    def test_find_files(self):
        files = list(Path.find(self.root, type_="f"))
        self.assert_list_equal_unordered(self.files, files)

    def tearDown(self):
        self.tmp_dir.cleanup()
