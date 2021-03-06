from pathlib import Path

import pathlibext  # pylint: disable=unused-import

from tests.base_test import BaseTest


class TestRmtree(BaseTest):
    def setUp(self):
        super().setUp()
        self.create_file_tree()

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
