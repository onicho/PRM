from unittest import TestCase
from BusinessLogic.share import Share


class TestShare(TestCase):
    def test_getName_success(self):
        s = Share("BP")
        self.assertEqual(s.getName(), "BP")

    def test_getName_fails(self):
        s = Share("BP")
        self.assertFalse(s.getName() == "LLOY")

    def test_set_historical_prices(self):
        s = Share("BP")
        hist_pr = {'2009-01-01': 30, '2010-01-01': 35, '2011-01-01': 40}
        s.set_historical_prices(hist_pr)
        self.assertEqual(s.get_historical_prices(), hist_pr)



