import pathlibext  # pylint: disable=unused-import

from tests.base_test import BaseTest


class TestMatch(BaseTest):
    def test_write_read_json(self):
        json_f = self.root / "test.json"
        json_f.write_json({"a": 1})
        self.assertEqual(1, json_f.read_json()["a"])
