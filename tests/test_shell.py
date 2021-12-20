import pathlibext  # pylint: disable=unused-import

from tests.base_test import BaseTest


class TestShell(BaseTest):
    def setUp(self):
        super().setUp()
        self.src = self.root / "test.txt"
        self.src.write_text("abc")
        self.dst = self.root / "target"
        self.dst.mkdir()

    def test_copy_to_dir(self):
        copied = self.src.copy(self.dst)
        self.assertTrue(copied.exists())
        self.assertEqual(self.root / "target" / "test.txt", copied)

    def test_copy_and_rename(self):
        dst = self.dst / "newname.dat"
        copied = self.src.copy(dst)
        self.assertTrue(copied.exists())
        self.assertEqual(self.root / "target" / "newname.dat", copied)

    def test_move(self):
        moved = self.src.move(self.dst)
        self.assertFalse(self.src.exists())
        self.assertTrue(moved.exists())
