from unittest import TestCase
from logic.test_portf import *


class TestWeightedPortfolio(TestCase):

    s1 = ShareFactory.create('ERM', '2009-01-01', '2014-12-31')
    s2 = ShareFactory.create('AML', '2009-01-01', '2014-12-31')
    s3 = ShareFactory.create('CGL', '2009-01-01', '2014-12-31')
    s4 = ShareFactory.create('NG', '2009-01-01', '2014-12-31')
    mkt = ShareFactory.create('^FTSE', '2009-01-01', '2014-12-31')
    rf = 1.5
    shares = [s1, s2, s3, s4]

    def test_class_inst(self):

        p = WeightedPortfolio(shares, mkt, rf)
        self.assertTrue(p.candidates == [s1, s2, s3, s4])
        self.assertTrue(len(shares) == len(p.candidates))
        self.assertTrue(type(p.rfr) == float)
        self.assertIsInstance(p, WeightedPortfolio)
        p_fail = WeightedPortfolio
        self.assertRaises(TypeError, p_fail, shares, mkt, "10")
        self.assertEqual(len(p.final), 0)

    def test_unadjusted(self):

        p = WeightedPortfolio(shares, mkt, rf)
        self.assertRaises(NotImplementedError, p.unadjusted)

    def test_adjusted(self):

        p = WeightedPortfolio(shares, mkt, rf)
        self.assertRaises(NotImplementedError, p.adjusted)

    def test_shs_zip_props(self):

        p = WeightedPortfolio(shares, mkt, rf)
        self.assertRaises(NotImplementedError, p.shs_zip_props)

    def test_adjusted_percent(self):
        p = WeightedPortfolio(shares, mkt, rf)
        self.assertRaises(NotImplementedError, p.adjusted_percent)
