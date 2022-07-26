from pathlib import Path
import os
import pathlibext  # pylint: disable=unused-import

from tests.base_test import BaseTest


class TestMatch(BaseTest):
    def test_match(self):
        self.assertTrue(Path("/foo/BAR.txt").match("*BAR*"))
        if os.name == "Windows":
            # On windows match() is case insensitive
            self.assertTrue(Path("/foo/BAR.txt").match("*bar*"))
        else:
            # On POSIX match() is case sensitive
            self.assertFalse(Path("/foo/BAR.txt").match("*bar*"))

    def test_matchcase(self):
        self.assertTrue(Path("/foo/BAR.txt").matchcase("*BAR*"))
        self.assertFalse(Path("/foo/BAR.txt").matchcase("*bar*"))