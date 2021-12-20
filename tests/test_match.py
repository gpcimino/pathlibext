from pathlib import Path
from base_test import BaseTest
import pathlibext  # pylint: disable=unused-import


class TestMatch(BaseTest):
    def test_match(self):
        self.assertTrue(self.root / "whatever", "w*")

    def test_matchcase(self):
        self.assertTrue(self.root / "Whatever", "what*")
