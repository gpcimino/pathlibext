from pathlib import Path
from base_test import BaseTest
import pathlibext  # pylint: disable=unused-import


class TestFind(BaseTest):
    def test_find_all(self):
        files = list(Path.find(self.root))
        self.assert_list_equal_unordered(self._dirs() + self.files, files)

    def test_find_dir(self):
        files = list(Path.find(self.root, type_="d"))
        self.assert_list_equal_unordered(self._dirs(), files)

    def test_find_files(self):
        files = list(Path.find(self.root, type_="f"))
        self.assert_list_equal_unordered(self.files, files)
