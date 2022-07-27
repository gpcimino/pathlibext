from pathlib import Path
import os
import pathlibext  # pylint: disable=unused-import

from tests.base_test import BaseTest


class TestMatch(BaseTest):
    def test_match(self):
        self.assertTrue((self.root / "foo" / "BAR.txt").match("*BAR*"))
        if os.name == "nt":
            # On Windows match() is case insensitive
            self.assertTrue((self.root / "foo" / "BAR.txt").match("*bar*"))
        else:
            # On POSIX match() is case sensitive
            self.assertFalse((self.root / "foo" / "BAR.txt").match("*bar*"))

    def test_matchcase(self):
        self.assertTrue((self.root / "foo" / "BAR.txt").matchcase("*BAR*"))
        self.assertFalse((self.root / "foo" / "BAR.txt").matchcase("*bar*"))
