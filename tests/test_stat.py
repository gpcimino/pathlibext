import os
from datetime import datetime
from pathlib import Path
from base_test import BaseTest
import pathlibext  # pylint: disable=unused-import


class TestStat(BaseTest):
    def test_file_size_in_byte(self):
        file = self.root / "test.txt"
        file.write_text("abc")
        self.assertEqual(3, file.size())


    def test_file_size_in_gigabyte(self):
        file = self.root / "test.txt"
        file.write_text("abc")
        self.assertEqual(3/(1024*1024*1024), file.size("gigabytes"))

    def test_access_time(self):
        file = self.root / "test.txt"
        file.write_text("abc")
        expected_access_time = os.stat(str(file)).st_atime
        self.assertEqual(datetime.fromtimestamp(expected_access_time), file.access_time())

    def test_modification_time(self):
        file = self.root / "test.txt"
        file.write_text("abc")
        expected_access_time = os.stat(str(file)).st_ctime
        self.assertEqual(datetime.fromtimestamp(expected_access_time), file.modification_time())
