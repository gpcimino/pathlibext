from pathlib import Path

import pathlibext  # pylint: disable=unused-import

from tests.base_test import BaseTest


class TestWorkDir(BaseTest):
    def test_current_file_path(self):
        self.assertEqual("test_workdir.py", Path.current_file_path().parts[-1])
        self.assertEqual("unit", Path.current_file_path().parts[-2])
        self.assertEqual("tests", Path.current_file_path().parts[-3])

    def test_current_file_dir(self):
        self.assertEqual("unit", Path.current_file_dir().parts[-1])
        self.assertEqual("tests", Path.current_file_dir().parts[-2])
