from unittest import TestCase

from data.share import ShareFactory
from logic.portfolio import *


class TestWeightedPortfolio(TestCase):
    """

    """

    s1 = ShareFactory.create('ERM', '2009-01-01', '2014-12-31')
    s2 = ShareFactory.create('AML', '2009-01-01', '2014-12-31')
    s3 = ShareFactory.create('CGL', '2009-01-01', '2014-12-31')
    s4 = ShareFactory.create('NG', '2009-01-01', '2014-12-31')
    mkt = ShareFactory.create('^FTSE', '2009-01-01', '2014-12-31')
    rf = 1.5


    def test_class_inst(self):

        s1 = ShareFactory.create('ERM', '2009-01-01', '2014-12-31')
        s2 = ShareFactory.create('AML', '2009-01-01', '2014-12-31')
        s3 = ShareFactory.create('CGL', '2009-01-01', '2014-12-31')
        s4 = ShareFactory.create('NG', '2009-01-01', '2014-12-31')
        mkt = ShareFactory.create('^FTSE', '2009-01-01', '2014-12-31')
        rf = 1.5
        shares = [s1, s2, s3, s4]

        p = WeightedPortfolio(shares, mkt, rf)
        self.assertTrue(p.candidates == [s1, s2, s3, s4])
        self.assertTrue(len(shares) == len(p.candidates))
        self.assertTrue(type(p.rfr) == float)
        self.assertIsInstance(p, WeightedPortfolio)
        p_fail = WeightedPortfolio
        self.assertRaises(TypeError, p_fail, shares, mkt, "10")
        self.assertEqual(len(p.final), 0)
        self.assertEqual(len(p.final), 0)
        self.assertTrue(p.market.name == '^FTSE')

    def test_unadjusted(self):

        s1 = ShareFactory.create('ERM', '2009-01-01', '2014-12-31')
        s2 = ShareFactory.create('AML', '2009-01-01', '2014-12-31')
        s3 = ShareFactory.create('CGL', '2009-01-01', '2014-12-31')
        s4 = ShareFactory.create('NG', '2009-01-01', '2014-12-31')
        mkt = ShareFactory.create('^FTSE', '2009-01-01', '2014-12-31')
        rf = 1.5
        shares = [s1, s2, s3, s4]

        p = WeightedPortfolio(shares, mkt, rf)
        self.assertRaises(NotImplementedError, p.unadjusted)

    def test_adjusted(self):

        s1 = ShareFactory.create('ERM', '2009-01-01', '2014-12-31')
        s2 = ShareFactory.create('AML', '2009-01-01', '2014-12-31')
        s3 = ShareFactory.create('CGL', '2009-01-01', '2014-12-31')
        s4 = ShareFactory.create('NG', '2009-01-01', '2014-12-31')
        mkt = ShareFactory.create('^FTSE', '2009-01-01', '2014-12-31')
        rf = 1.5
        shares = [s1, s2, s3, s4]

        p = WeightedPortfolio(shares, mkt, rf)
        self.assertRaises(NotImplementedError, p.adjusted)

    def test_shs_zip_props(self):

        s1 = ShareFactory.create('ERM', '2009-01-01', '2014-12-31')
        s2 = ShareFactory.create('AML', '2009-01-01', '2014-12-31')
        s3 = ShareFactory.create('CGL', '2009-01-01', '2014-12-31')
        s4 = ShareFactory.create('NG', '2009-01-01', '2014-12-31')
        mkt = ShareFactory.create('^FTSE', '2009-01-01', '2014-12-31')
        rf = 1.5
        shares = [s1, s2, s3, s4]

        p = WeightedPortfolio(shares, mkt, rf)
        self.assertRaises(NotImplementedError, p.shs_zip_props)

    def test_adjusted_percent(self):

        s1 = ShareFactory.create('ERM', '2009-01-01', '2014-12-31')
        s2 = ShareFactory.create('AML', '2009-01-01', '2014-12-31')
        s3 = ShareFactory.create('CGL', '2009-01-01', '2014-12-31')
        s4 = ShareFactory.create('NG', '2009-01-01', '2014-12-31')
        mkt = ShareFactory.create('^FTSE', '2009-01-01', '2014-12-31')
        rf = 1.5
        shares = [s1, s2, s3, s4]
        p = WeightedPortfolio(shares, mkt, rf)
        self.assertRaises(NotImplementedError, p.adjusted_percent)

    def test_shs_alphas(self):
        """

        :return:
        """
        s1 = ShareFactory.create('ERM', '2009-01-01', '2014-12-31')
        s2 = ShareFactory.create('AML', '2009-01-01', '2014-12-31')
        s3 = ShareFactory.create('CGL', '2009-01-01', '2014-12-31')
        s4 = ShareFactory.create('NG', '2009-01-01', '2014-12-31')
        mkt = ShareFactory.create('^FTSE', '2009-01-01', '2014-12-31')
        rf = 1.5
        shares = [s1, s2, s3, s4]
        p = WeightedPortfolio(shares, mkt, rf)

        self.assertEquals(len(p.shs_alphas), len(shares))
        self.assertTrue(all(type(value) == float for value in p.shs_alphas))
        self.assertAlmostEqual(p.shs_alphas[0], 24.689661373391942, 1)
        self.assertAlmostEqual(p.shs_alphas[1], -0.9854334857795548, 1)
        self.assertAlmostEqual(p.shs_alphas[2], 12.851315692543585, 1)
        self.assertAlmostEqual(p.shs_alphas[3], 4.66718239333, 1)

    def test_shs_specrisk(self):
        """

        :return:
        """
        s1 = ShareFactory.create('ERM', '2009-01-01', '2014-12-31')
        s2 = ShareFactory.create('AML', '2009-01-01', '2014-12-31')
        s3 = ShareFactory.create('CGL', '2009-01-01', '2014-12-31')
        s4 = ShareFactory.create('NG', '2009-01-01', '2014-12-31')
        mkt = ShareFactory.create('^FTSE', '2009-01-01', '2014-12-31')
        rf = 1.5
        shares = [s1, s2, s3, s4]
        p = WeightedPortfolio(shares, mkt, rf)

        self.assertEquals(len(p.shs_specrisk), len(shares))
        self.assertTrue(all(type(value) == float for value in p.shs_specrisk))
        self.assertAlmostEqual(p.shs_specrisk[0], 11085.588185744395)
        self.assertAlmostEqual(p.shs_specrisk[1], 4852.190528206953)
        self.assertAlmostEqual(p.shs_specrisk[2], 5184.445909093038)
        self.assertAlmostEqual(p.shs_specrisk[3], 2528.7129778776757)

    def test_shs_betas(self):
        """

        :return:
        """
        s1 = ShareFactory.create('ERM', '2009-01-01', '2014-12-31')
        s2 = ShareFactory.create('AML', '2009-01-01', '2014-12-31')
        s3 = ShareFactory.create('CGL', '2009-01-01', '2014-12-31')
        s4 = ShareFactory.create('NG', '2009-01-01', '2014-12-31')
        mkt = ShareFactory.create('^FTSE', '2009-01-01', '2014-12-31')
        rf = 1.5
        shares = [s1, s2, s3, s4]
        p = WeightedPortfolio(shares, mkt, rf)

        self.assertEquals(len(p.shs_betas), len(shares))
        self.assertTrue(all(type(value) == float for value in p.shs_betas))
        self.assertAlmostEqual(p.shs_betas[0], 0.6282898897597817)
        self.assertAlmostEqual(p.shs_betas[1], 0.8141837308926254)
        self.assertAlmostEqual(p.shs_betas[2], 0.4736874233337413)
        self.assertAlmostEqual(p.shs_betas[3], 0.41943334521384473)

    def test_mkt_return(self):
        """

        :return:
        """
        s1 = ShareFactory.create('ERM', '2009-01-01', '2014-12-31')
        s2 = ShareFactory.create('AML', '2009-01-01', '2014-12-31')
        s3 = ShareFactory.create('CGL', '2009-01-01', '2014-12-31')
        s4 = ShareFactory.create('NG', '2009-01-01', '2014-12-31')
        mkt = ShareFactory.create('^FTSE', '2009-01-01', '2014-12-31')
        rf = 1.5
        shares = [s1, s2, s3, s4]
        p = WeightedPortfolio(shares, mkt, rf)

        self.assertEquals(p.mkt_return, 8.680909161455878)
        self.assertTrue(type(p.mkt_return) == float)


