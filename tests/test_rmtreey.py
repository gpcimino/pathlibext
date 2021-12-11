import unittest
from collections import Counter
from pathlib import Path
import tempfile
import pathlibext.find  # pylint: disable=unused-import


class TestRmtree(unittest.TestCase):
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

    def test_remove_files(self):
        self.root.rmtree()
        self.assertFalse(self.root.exists())

    def test_should_raise_on_file(self):
        with self.assertRaises(ValueError):
            self.files[0].rmtree()

    def test_should_raise_if_path_doesnt_exist(self):
        non_exists = Path("/all/your/base/are/belong/to/us")
        with self.assertRaises(ValueError):
            non_exists.rmtree()

    def tearDown(self):
        self.tmp_dir.cleanup()
