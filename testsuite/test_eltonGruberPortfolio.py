from unittest import TestCase
from logic.test_portf import *
import numpy.testing as npt


class TestEltonGruberPortfolio(TestCase):

    s1 = ShareFactory.create('ERM', '2009-01-01', '2014-12-31')
    s2 = ShareFactory.create('AML', '2009-01-01', '2014-12-31')
    s3 = ShareFactory.create('CGL', '2009-01-01', '2014-12-31')
    s4 = ShareFactory.create('NG', '2009-01-01', '2014-12-31')
    mkt = ShareFactory.create('^FTSE', '2009-01-01', '2014-12-31')
    rf = 1.5
    shares = [s1, s2, s3, s4]

    def test_class_inst(self):

        s = [s1, s2, s3, s4]
        p = EltonGruberPortfolio(s, mkt, rf)
        self.assertTrue(p.candidates == [s1, s2, s3, s4])
        self.assertTrue(len(s) == len(p.candidates))
        self.assertTrue(type(p.rfr) == float)
        self.assertIsInstance(p, EltonGruberPortfolio)
        p_fail = EltonGruberPortfolio
        self.assertRaises(TypeError, p_fail, s, mkt, "10")
        self.assertEqual(len(p.final), 0)

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
        p = EltonGruberPortfolio(shares, mkt, rf)

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
        p = EltonGruberPortfolio(shares, mkt, rf)

        self.assertEquals(len(p.shs_specrisk), len(shares))
        self.assertTrue(
            all(type(value) == float for value in p.shs_specrisk))
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
        p = EltonGruberPortfolio(shares, mkt, rf)

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
        p = EltonGruberPortfolio(shares, mkt, rf)

        self.assertEquals(p.mkt_return, 8.680909161455878)
        self.assertTrue(type(p.mkt_return) == float)

    def test_order(self):
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
        shares1 = [s2, s3, s1]

        p = EltonGruberPortfolio(shares, mkt, rf)
        self.assertTrue(p.order() == [s1, s3, s4, s2])

        p = EltonGruberPortfolio(shares1, mkt, rf)
        self.assertTrue(p.order() == [s1, s3, s2])

    def test_cutoff_rate(self):

        s1 = ShareFactory.create('ERM', '2009-01-01', '2014-12-31')
        s2 = ShareFactory.create('AML', '2009-01-01', '2014-12-31')
        s3 = ShareFactory.create('CGL', '2009-01-01', '2014-12-31')
        s4 = ShareFactory.create('NG', '2009-01-01', '2014-12-31')
        s5 = ShareFactory.create('RBS', '2009-01-01', '2014-12-31')
        mkt = ShareFactory.create('^FTSE', '2009-01-01', '2014-12-31')
        rf = 1.5
        shares = [s1, s2, s3, s4]
        shares1 = [s2, s3, s1]
        shares2 = [s1]
        shares3 = [s1, s2, s3, s4, s5]

        p = EltonGruberPortfolio(shares, mkt, rf)
        # Excel calculation yield to 7.34521531833
        npt.assert_almost_equal(list(p.cut_off_rate())[0], 7.34521531833, 1)

        p = EltonGruberPortfolio(shares1, mkt, rf)
        # Excel calculation yield to 5.92075245998
        npt.assert_almost_equal(list(p.cut_off_rate())[0], 5.92075245998, 1)

        p = EltonGruberPortfolio(shares2, mkt, rf)
        # Excel calculation yield to 3.3806189770
        npt.assert_almost_equal(list(p.cut_off_rate())[0], 3.3806189770, 1)

        p = EltonGruberPortfolio(shares2, mkt, rf)
        # Excel calculation yield to 3.3806189770
        npt.assert_almost_equal(list(p.cut_off_rate())[0], 3.3806189770, 1)

        p = EltonGruberPortfolio(shares3, mkt, rf)
        npt.assert_almost_equal(list(p.cut_off_rate())[0], 7.9804492260, 1)

        p = EltonGruberPortfolio(shares, mkt, rf)
        self.assertTrue(type(p.cut_off_rate()) == dict)
        self.assertTrue(len(p.cut_off_rate()) == 1)

    def test_filtered(self):

        s1 = ShareFactory.create('ERM', '2009-01-01', '2014-12-31')
        s2 = ShareFactory.create('AML', '2009-01-01', '2014-12-31')
        s3 = ShareFactory.create('CGL', '2009-01-01', '2014-12-31')
        s4 = ShareFactory.create('NG', '2009-01-01', '2014-12-31')
        s5 = ShareFactory.create('RBS', '2009-01-01', '2014-12-31')
        s6 = ShareFactory.create('AAL', '2009-01-01', '2014-12-31')
        s7 = ShareFactory.create('BRBY', '2009-01-01', '2014-12-31')
        s8 = ShareFactory.create('BP', '2009-01-01', '2014-12-31')
        s9 = ShareFactory.create('TSCO', '2009-01-01', '2014-12-31')
        s10 = ShareFactory.create('SGE', '2009-01-01', '2014-12-31')
        mkt = ShareFactory.create('^FTSE', '2009-01-01', '2014-12-31')
        rf = 1.5
        shares = [s1,s2,s3,s4,s5,s6,s7,s8,s9,s10]
        shares1 = [s1, s2, s3, s4]

        p = EltonGruberPortfolio(shares, mkt, rf)
        self.assertEqual(p.filtered(), [s1, s3, s5, s7, s10, s4])

        p = EltonGruberPortfolio(shares1, mkt, rf)
        self.assertEqual(p.filtered(), [s1, s3, s4])


















            # def test_ordered(self):
    #     self.fail()
    #
    # def test_cut_off_rate(self):
    #     self.fail()
    #
    # def test_shares_filter(self):
    #     self.fail()
    #
    # def test_unadjusted(self):
    #     self.fail()
    #
    # def test_adjusted(self):
    #     self.fail()
    #
    # def test_adjusted_percent(self):
    #     self.fail()
    #
    # def test_shs_zip_props(self):
    #     self.fail()
