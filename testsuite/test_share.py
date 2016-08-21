from unittest import TestCase

from BusinessLogic.share import Share


class TestShare(TestCase):
    def test_getName_success(self):
        s = Share("OLYA")
        self.assertEqual(s.getName(), "OLYA")

    def test_getName_fails(self):
        s = Share("OLYA")
        self.assertFalse(s.getName() == "MARIA")
