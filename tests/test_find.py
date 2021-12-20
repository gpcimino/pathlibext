from pathlib import Path
from base_test import BaseTest
import pathlibext  # pylint: disable=unused-import


class TestFind(BaseTest):
    def setUp(self):
        super().setUp()
        self.create_file_tree()

    def test_find_all(self):
        files = list(Path.find(self.root))
        self.assert_list_equal_unordered(self._dirs() + self.files, files)

    def test_find_dir(self):
        files = list(Path.find(self.root, type_="d"))
        self.assert_list_equal_unordered(self._dirs(), files)

    def test_find_files(self):
        files = list(Path.find(self.root, type_="f"))
        self.assert_list_equal_unordered(self.files, files)

    def test_find_with_maxdepth_0(self):
        files = list(Path.find(self.root, type_="f", maxdepth=0))
        self.assertEqual(2, len(files))

    def test_find_with_maxdepth_1(self):
        files = list(Path.find(self.root, type_="f", maxdepth=1))
        self.assertEqual(4, len(files))

    def test_find_with_maxdepth_2(self):
        files = list(Path.find(self.root, type_="f", maxdepth=2))
        self.assertEqual(6, len(files))

    def test_find_with_mindepth_0_should_be_same_as_default(self):
        files = list(Path.find(self.root, type_="f", mindepth=0))
        self.assert_list_equal_unordered(self.files, files)

    def test_find_with_mindepth_1(self):
        files = list(Path.find(self.root, type_="f", mindepth=1))
        self.assertEqual(8, len(files))

    def test_find_with_mindepth_2(self):
        files = list(Path.find(self.root, type_="f", mindepth=2))
        self.assertEqual(6, len(files))

    def test_find_with_mindepth_3_and_maxdepth_4(self):
        files = list(Path.find(self.root, type_="f", mindepth=3, maxdepth=4))
        self.assertEqual(4, len(files))

    def test_find_with_mindepth_2_and_maxdepth_4(self):
        files = list(Path.find(self.root, type_="f", mindepth=2, maxdepth=4))
        self.assertEqual(6, len(files))
