from pathlib import Path
from base_test import BaseTest
import pathlibext  # pylint: disable=unused-import


class TestRmtree(BaseTest):
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
