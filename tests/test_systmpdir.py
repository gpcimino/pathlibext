from pathlib import Path
from base_test import BaseTest
import pathlibext  # pylint: disable=unused-import


class TestSysTmpDir(BaseTest):
    def test_tmp_dir_is_created(self):
        tmpdir = Path.systmpdir()
        self.assertTrue(tmpdir.exists())
        self.assertTrue(tmpdir.is_dir())
