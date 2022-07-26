from pathlib import Path

import pathlibext  # pylint: disable=unused-import

from tests.base_test import BaseTest


class TestTmpFile(BaseTest):
    def test_write_text_to_tmpfile(self):
        self.assertTrue(Path.write_text_tmpfile("whatever").exists())
        self.assertEqual("whatever", Path.write_text_tmpfile("whatever").read_text())

    def test_tmp_file(self):
        self.assertTrue(Path.tmpfile().exists())

