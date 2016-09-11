from unittest import TestCase
from logic.test_portf import *


class TestTreynorBlackPortfolio(TestCase):

    def test_class_inst(self):
        s1 = ShareFactory.create('ERM', '2009-01-01', '2014-12-31')
        s2 = ShareFactory.create('AML', '2009-01-01', '2014-12-31')
        s3 = ShareFactory.create('CGL', '2009-01-01', '2014-12-31')
        s4 = ShareFactory.create('NG', '2009-01-01', '2014-12-31')
        mkt = ShareFactory.create('^FTSE', '2009-01-01', '2014-12-31')
        rf = 1.5
        s = [s1, s2, s3, s4]
        p = TreynorBlackPortfolio(s, mkt, rf)

        self.assertTrue(p.candidates == [s1, s2, s3, s4])
        self.assertTrue(len(s) == len(p.candidates))
        self.assertTrue(type(p.rfr) == float)
        self.assertIsInstance(p, TreynorBlackPortfolio)
        p_fail = TreynorBlackPortfolio
        self.assertRaises(TypeError, p_fail, s, mkt, "10")

    def test_non_zero_alpha(self):

        s1 = ShareFactory.create('ERM', '2009-01-01', '2014-12-31')
        s2 = ShareFactory.create('AML', '2009-01-01', '2014-12-31')
        s3 = ShareFactory.create('CGL', '2009-01-01', '2014-12-31')
        s4 = ShareFactory.create('NG', '2009-01-01', '2014-12-31')
        mkt = ShareFactory.create('^FTSE', '2009-01-01', '2014-12-31')
        rf = 1.5
        s = [s1, s2, s3, s4]

        p = TreynorBlackPortfolio(s, mkt, rf)
        self.assertTrue(p.non_zero_alpha == True)

        s11 = ShareFactory.create('BRBY', '2015-09-30', '2016-08-31')
        s21 = ShareFactory.create('TSCO', '2015-09-30', '2016-08-31')
        s31 = ShareFactory.create('RBS', '2015-09-30', '2016-08-31')
        s41 = ShareFactory.create('BP', '2015-09-30', '2016-08-31')
        mkt1 = ShareFactory.create('^FTSE', '2015-09-30', '2016-08-31')

        s1 = [s11, s21, s31, s41]

        p = TreynorBlackPortfolio(s1, mkt1, rf)
        self.assertTrue(p.non_zero_alpha == True)

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
        s = [s1, s2, s3, s4]
        p = TreynorBlackPortfolio(s, mkt, rf)

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
        s = [s1, s2, s3, s4]
        p = TreynorBlackPortfolio(s, mkt, rf)

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
        s = [s1, s2, s3, s4]
        p = TreynorBlackPortfolio(s, mkt, rf)

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
        s = [s1, s2, s3, s4]
        p = TreynorBlackPortfolio(s, mkt, rf)

        self.assertEquals(p.mkt_return, 8.680909161455878)
        self.assertTrue(type(p.mkt_return) == float)

    def unadjusted(self):
        """

        :return:
        """
        s1 = ShareFactory.create('ERM', '2009-01-01', '2014-12-31')
        s2 = ShareFactory.create('CGL', '2009-01-01', '2014-12-31')
        s3 = ShareFactory.create('NG', '2009-01-01', '2014-12-31')
        mkt = ShareFactory.create('^FTSE', '2009-01-01', '2014-12-31')
        rf = 1.5
        s = [s1, s2, s3]
        p = TreynorBlackPortfolio(s, mkt, rf)

        self.assertEqual(p.unadjusted(), [0.0022271855096639634,
                                          0.0018414670484946665,
                                          0.002478821443580609])

        s5 = ShareFactory.create('RBS', '2009-01-01', '2015-07-31')
        s6 = ShareFactory.create('AAL', '2009-01-01', '2015-07-31')
        s7 = ShareFactory.create('BRBY', '2009-01-01', '2015-07-31')
        s8 = ShareFactory.create('BP', '2009-01-01', '2015-07-31')
        mkt1 = ShareFactory.create('^FTSE', '2009-01-01', '2015-07-31')
        s1 = [s5, s6, s7,s8]
        p = TreynorBlackPortfolio(s1, mkt1, rf)

        self.assertEqual(p.unadjusted(), [7.548270543767005e-05,
                                          -0.001678107417717914,
                                          0.002693161115938313,
                                          -0.0026965374431083123])

    def adjusted(self):

        s1 = ShareFactory.create('ERM', '2009-01-01', '2014-12-31')
        s2 = ShareFactory.create('CGL', '2009-01-01', '2014-12-31')
        s3 = ShareFactory.create('NG', '2009-01-01', '2014-12-31')
        mkt = ShareFactory.create('^FTSE', '2009-01-01', '2014-12-31')
        rf = 1.5
        s = [s1, s2, s3]
        p = TreynorBlackPortfolio(s, mkt, rf)

        self.assertEqual(p.adjusted(), [0.3401595041190458,
                                        0.2812484704796855,
                                        0.3785920254012688])

        self.assertTrue(sum(p.adjusted()) == 1.0)

        s11 = ShareFactory.create('BRBY', '2015-09-30', '2016-08-31')
        s21 = ShareFactory.create('TSCO', '2015-09-30', '2016-08-31')
        s31 = ShareFactory.create('RBS', '2015-09-30', '2016-08-31')
        s41 = ShareFactory.create('BP', '2015-09-30', '2016-08-31')
        mkt1 = ShareFactory.create('^FTSE', '2015-09-30', '2016-08-31')

        s1 = [s11,s21,s31,s41]

        p = TreynorBlackPortfolio(s1,mkt1,rf)

        self.assertEqual(p.adjusted(), [0.43713692392277076,
                                        0.06686035227836598,
                                        0.4291886385951165,
                                        0.06681408520374679])














