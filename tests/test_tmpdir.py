from pathlib import Path
from base_test import BaseTest
import pathlibext  # pylint: disable=unused-import


class TestTmpDir(BaseTest):
    def test_sys_tmpdir_is_created(self):
        tmpdir = Path.systmpdir()
        self.assertTrue(tmpdir.exists())
        self.assertTrue(tmpdir.is_dir())

    def test_tmpdir_in_existing_directory(self):
        tmpdir = self.root.tmpdir_in()
        self.assertEqual(self.root, tmpdir.parent)
        self.assertTrue(tmpdir.exists())
        self.assertTrue(tmpdir.is_dir())

    def test_tmpdir_in_existing_directory_has_proper_name(self):
        tmpdir = self.root.tmpdir_in(prefix="A", suffix="ZZZ")
        self.assertTrue(tmpdir.name.startswith("A"))
        self.assertTrue(tmpdir.name.endswith("ZZZ"))

    def test_tmpdir_is_created(self):
        tmpdir = Path.tmpdir()
        self.assertTrue(tmpdir.exists())
        self.assertTrue(tmpdir.is_dir())
