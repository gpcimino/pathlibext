import pathlibext  # pylint: disable=unused-import

from tests.base_test import BaseTest


class TestMatch(BaseTest):
    def test_match(self):
        self.assertTrue(self.root / "whatever", "w*")

    def test_matchcase(self):
        self.assertTrue(self.root / "Whatever", "what*")
