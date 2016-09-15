from unittest import TestCase

import numpy.testing as npt

from data.share import *
from logic.portfolio import *


class TestEltonGruberPortfolio(TestCase):

    def test_class_inst(self):
        """

        :return:
        """
        s1 = ShareFactory.create('ERM', '2009-01-01', '2014-12-31')
        s2 = ShareFactory.create('AML', '2009-01-01', '2014-12-31')
        s3 = ShareFactory.create('CGL', '2009-01-01', '2014-12-31')
        s4 = ShareFactory.create('NG', '2009-01-01', '2014-12-31')
        mkt = ShareFactory.create('^FTSE', '2009-01-01', '2014-12-31')
        rf = 1.5
        s = [s1, s2, s3, s4]
        p = EltonGruberPortfolio(s, mkt, rf)

        self.assertTrue(p.candidates == [s1, s2, s3, s4])
        self.assertTrue(len(s) == len(p.candidates))
        self.assertTrue(type(p.rfr) == float)
        self.assertIsInstance(p, EltonGruberPortfolio)
        p_fail = EltonGruberPortfolio
        self.assertRaises(TypeError, p_fail, s, mkt, "10")


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

    def test_cutoff(self):

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
        npt.assert_almost_equal(list(p.cutoff())[0], 7.34521531833, 1)

        p = EltonGruberPortfolio(shares1, mkt, rf)
        # Excel calculation yield to 5.92075245998
        npt.assert_almost_equal(list(p.cutoff())[0], 5.92075245998, 1)

        p = EltonGruberPortfolio(shares2, mkt, rf)
        # Excel calculation yield to 3.3806189770
        npt.assert_almost_equal(list(p.cutoff())[0], 3.3806189770, 1)

        p = EltonGruberPortfolio(shares2, mkt, rf)
        # Excel calculation yield to 3.3806189770
        npt.assert_almost_equal(list(p.cutoff())[0], 3.3806189770, 1)

        p = EltonGruberPortfolio(shares3, mkt, rf)
        npt.assert_almost_equal(list(p.cutoff())[0], 7.9804492260, 1)

        p = EltonGruberPortfolio(shares, mkt, rf)
        self.assertTrue(type(p.cutoff()) == dict)
        self.assertTrue(len(p.cutoff()) == 1)

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

    def test_unadjusted(self):
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
        shares = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10]
        shares1 = [s1, s2, s3, s4]

        p = EltonGruberPortfolio(shares1, mkt, rf)
        self.assertEqual(p.unadjusted(), [0.0022197084879073507,
                                         0.0024667678423211897,
                                         0.001819584861198741])

        p = EltonGruberPortfolio(shares, mkt, rf)
        self.assertEqual(p.unadjusted(), [0.0018518641189718167,
                                          0.0018737711261152996,
                                          5.729847026799712e-05,
                                          0.001984782239823533,
                                          0.001360209193855437,
                                          0.0007430547080424998])

        p = EltonGruberPortfolio(shares1, mkt, rf)
        self.assertTrue(type(p.unadjusted()) == list)
        self.assertTrue(all(type(w) is float for w in p.unadjusted()))

    def test_adjusted(self):

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
        shares = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10]
        shares1 = [s1, s2, s3, s4]
        shares2 = [s2]
        shares3 = [s4,s5]

        p = EltonGruberPortfolio(shares1, mkt, rf)
        self.assertTrue(sum(p.adjusted()) == 1.0)
        self.assertEqual(p.adjusted(), [0.34117547047238844,
                                        0.37914919176775175,
                                        0.2796753377598598])

        p = EltonGruberPortfolio(shares, mkt, rf)
        self.assertTrue(sum(p.adjusted()) == 1.0)
        self.assertEqual(p.adjusted(), [0.2352774562504891,
                                        0.23806071926745476,
                                        0.007279712476519888,
                                        0.25216456856246044,
                                        0.17281319715645185,
                                        0.09440434628662396])

        p = EltonGruberPortfolio(shares2, mkt, rf)
        self.assertEqual(p.adjusted(), [1.0])

        p = EltonGruberPortfolio(shares3, mkt, rf)
        self.assertEqual(p.adjusted(), [0.03402189122906981,
                                        0.9659781087709303])

    def test_adjusted_percent(self):

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
        shares = [s4, s5]
        shares1 = [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10]
        shares2 = [s7]

        p = EltonGruberPortfolio(shares, mkt, rf)
        self.assertEqual(p.adjusted_percent(), [3.4, 96.6])

        p = EltonGruberPortfolio(shares1, mkt, rf)
        self.assertEqual(p.adjusted_percent(),
                         [23.53, 23.81, 0.73, 25.22, 17.28, 9.44])

        npt.assert_almost_equal(sum(p.adjusted_percent()), 100.00, 1)

        p = EltonGruberPortfolio(shares2, mkt, rf)
        self.assertEqual(p.adjusted_percent(), [100.00])

    def test_shs_zip_props(self):

        s1 = ShareFactory.create('ERM', '2009-01-01', '2014-12-31')
        s2 = ShareFactory.create('AML', '2009-01-01', '2014-12-31')
        s3 = ShareFactory.create('CGL', '2009-01-01', '2014-12-31')
        s4 = ShareFactory.create('NG', '2009-01-01', '2014-12-31')
        mkt = ShareFactory.create('^FTSE', '2009-01-01', '2014-12-31')
        rf = 1.5
        shares = [s1,s2,s3,s4]

        p = EltonGruberPortfolio(shares, mkt, rf)
        self.assertTrue(len(p.final) >= 1)

        filtered = [i.name for i in p.filtered()]
        percent = p.adjusted_percent()
        s = [i.name for i in list(p.final.keys())]
        w = list(p.final.values())

        self.assertEqual(set(percent), set(w))
        self.assertEqual(set(filtered), set(s))

































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
