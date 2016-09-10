from unittest import TestCase
from logic.share import *
import numpy.testing as npt
from logic.exceptions import *


class TestShare(TestCase):

    def test_name_success(self):
        """Tests that a string given to the class at instantiation
        is assigned as a name to a share object
        """
        s = Share("BP")
        self.assertEqual(s.name, "BP")

    def test_name_fails(self):
        s = Share(999)   # assert_raises in numpy.testing
        self.assertFalse(s.name == "LLOY")

    def test_prices(self):
        """Tests that a list of values can be assigned to the class
        instance variable prices
        """
        s = Share("BP")
        p = [20, 30, 432, 7876, 432487, 9876, 6456]
        s.prices = p
        self.assertEqual(s.prices, p)

    def test_pricetype(self):
        """Tests they type of the class instance variable prices. It
        must be a list
        """
        s = Share("BP")
        self.assertEqual(type(s.prices), list)

    def test_share(self):
        """Tests that two Share objects even with the same name are not
        equal
        """
        # look up __eq__  and __hash__
        s = Share("BP")
        s1 = Share("BP")
        self.assertNotEqual(s, s1)


class TestShareFactory(TestCase):

    def test_create_success(self):
        """Tests that a new Share object called 'NG' is created and that Share's
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
        Tests that if the end date precedes the start date for the prices
        period, the database does not return any results and the Share object is
        assigned an empty list of prices.
        """
        factory = ShareFactory.create("LLOY", "2009-01-01", "2000-01-01")
        self.assertEqual(factory.name, "LLOY")
        self.assertEqual(factory.prices, [])

    def test_create_type(self):
        """
        Tests that a new object of the type Share is returned
        """
        factory = ShareFactory.create("TSCO", "2009-01-01", "2014-01-05")
        self.assertEqual(type(factory), Share)

    def test_create2(self):
        """Tests that a new Share object called '^FTSE' is created and that Share's
        assigned prices are equal to the list of historica prices copied from
        PRM database for the same period
        """
        factory = ShareFactory.create("^FTSE", "2016-01-01", "2016-08-01")
        p = [
            6083.790000000,
            6097.090000000,
            6174.900000000,
            6241.890000000,
            6230.790000000,
            6504.330000000,
            6724.430000000
        ]
        self.assertEqual(factory.name, "^FTSE")
        self.assertEqual(factory.prices, p)

    def test_create_error(self):
        r"""Tests that an error is raised when the wrong type parameters are
        passed in.
        """
        factory = ShareFactory()

        self.assertRaises(InputError, factory.create, "hi",
                          "2015-08-01", "2016-08-01")
