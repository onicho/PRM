from unittest import TestCase
from logic.share import Share


class TestShare(TestCase):

    def test_name_success(self):
        """Test that a string given to the class at instantiation
        is assigned as a name to a share object
        """
        s = Share("BP")
        self.assertEqual(s.name, "BP")

    def test_name_fails(self):
        s = Share("BP")
        self.assertFalse(s.name == "LLOY")

    def test_prices(self):
        """Test that a list of values can be assigned to the class
        instance variable prices
        """
        s = Share("BP")
        p = [20, 30, 432, 7876, 432487, 9876, 6456]
        s.prices = p
        self.assertEqual(s.prices, p)

    def test_pricetype(self):
        """Test they type of the class instance variable prices. It
        must be a list
        """
        s = Share("BP")
        self.assertEqual(type(s.prices), list)

    def test_share(self):
        """Test that two Share objects even with the same name are not
        equal
        """
        s = Share("BP")
        s1 = Share("BP")
        self.assertNotEqual(s, s1)





