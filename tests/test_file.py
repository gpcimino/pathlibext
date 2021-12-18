from pathlib import Path
from base_test import BaseTest
import pathlibext  # pylint: disable=unused-import


class TestFile(BaseTest):
    def test_tes_size_in_byte(self):
        file = self.root / "test.txt"
        file.write_text("abc")
        self.assertEqual(3, file.size())
