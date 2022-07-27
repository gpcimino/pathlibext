import os
import unittest
from datetime import datetime

import pathlibext  # pylint: disable=unused-import

from tests.base_test import BaseTest


class TestStat(BaseTest):
    def test_file_size_in_byte(self):
        file = self.root / "test.txt"
        file.write_text("abc")
        self.assertEqual(3, file.size())

    def test_file_size_in_gigabyte(self):
        file = self.root / "test.txt"
        file.write_text("abc")
        self.assertEqual(3 / (1024 * 1024 * 1024), file.size("gigabytes"))

    def test_access_time(self):
        file = self.root / "test.txt"
        file.write_text("abc")
        expected_access_time = os.stat(str(file)).st_atime
        self.assertEqual(datetime.fromtimestamp(expected_access_time), file.access_time())

    @unittest.skipIf(os.name == "nt", "Run only on POSIX")
    def test_creation_time(self):
        file = self.root / "test.txt"
        file.write_text("abc")
        expected_access_time = os.stat(str(file)).st_ctime
        self.assertEqual(datetime.fromtimestamp(expected_access_time), file.metadatachange_time())

    @unittest.skipIf(os.name != "nt", "Run only on Windows")
    def test_metadatachange_time(self):
        file = self.root / "test.txt"
        file.write_text("abc")
        expected_access_time = os.stat(str(file)).st_ctime
        self.assertEqual(datetime.fromtimestamp(expected_access_time), file.creation_time())
