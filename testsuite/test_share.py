from unittest import TestCase
from logic.share import *


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


class TestShareFactory(TestCase):

    def test_create_success(self):
        """Test that a new Share object called 'NG' is created and that Share's
        assigned prices are equal to the list of historica prices copied from
        PRM database for the same period
        """
        factory = ShareFactory.create("NG", "2009-01-01", "2009-12-31")
        p = [
                574.407000000,
                555.349000000,
                474.684000000,
                500.390000000,
                530.529000000,
                485.321000000,
                495.071000000,
                525.210000000,
                535.404000000,
                537.620000000,
                585.487000000,
                601.886000000
        ]
        self.assertEqual(factory.name, "NG")
        self.assertEqual(factory.prices, p)

    def test_create_priceless(self):
        """
        Test that if the end date precedes the start date for the prices
        period, the database does not return any results and the Share object is
        assigned an empty list of prices.
        """
        factory = ShareFactory.create("LLOY", "2009-01-01", "2000-01-01")
        self.assertEqual(factory.name, "LLOY")
        self.assertEqual(factory.prices, [])

    def test_create_type(self):
        """
        Test a new object of the type Share is returned
        """
        factory = ShareFactory.create("TSCO", "2009-01-01", "2014-01-05")
        self.assertEqual(type(factory), Share)

    def test_create_fail(self):
        """
        Test that even if a new object Share is created with an invalid name, no
        prices are assigned to the Share object because the database cannot
        retrieve historical prices for invalid share name.
        """
        factory = ShareFactory.create("", "2009-01-01", "2014-01-05")
        self.assertEqual(factory.name, "")
        self.assertFalse(len(factory.prices) > 0)



