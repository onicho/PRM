from unittest import TestCase

import numpy.testing as npt
from numpy import *

from data.share import *
from logic.calculator import *

test = [
    228.75,
    180,
    204,
    252,
    207.5,
    204,
    228,
    269.7,
    373.3,
    380,
    393,
    435.7,
    470.3,
    470.2,
    520,
    516,
    588.5,
    599.5,
    605,
    588.5,
    611,
    649,
    695,
    692,
    693,
    698,
    697,
    713,
    663,
    653,
    682,
    571,
    615,
    678,
    696,
    625,
    690,
    717,
    760,
    785,
    801,
    746.5,
    714,
    770,
    770,
    800,
    783,
    870.5,
    890,
    921,
    966.5,
    980,
    942,
    1023,
    1065,
    1202,
    1160,
    1075,
    1243,
    1350,
    1326,
    1319,
    1198,
    1070,
    1189,
    1110,
    1084,
    1082,
    1015,
    1051,
    1019,
    1047
]

returns_test = [

    -0.213114754,
    0.133333333,
    0.235294118,
    -0.176587302,
    -0.01686747,
    0.117647059,
    0.182894737,
    0.384130515,
    0.017948031,
    0.034210526,
    0.108651399,
    0.07941244,
    -0.00021263,
    0.105912378,
    -0.007692308,
    0.140503876,
    0.018691589,
    0.009174312,
    -0.027272727,
    0.038232795,
    0.062193126,
    0.070878274,
    -0.004316547,
    0.001445087,
    0.007215007,
    -0.001432665,
    0.022955524,
    -0.070126227,
    -0.015082956,
    0.044410413,
    -0.162756598,
    0.077057793,
    0.102439024,
    0.026548673,
    -0.102011494,
    0.104,
    0.039130435,
    0.059972106,
    0.032894737,
    0.020382166,
    -0.06803995,
    -0.043536504,
    0.078431373,
    0,
    0.038961039,
    -0.02125,
    0.111749681,
    0.022400919,
    0.034831461,
    0.049402823,
    0.013967926,
    -0.03877551,
    0.085987261,
    0.041055718,
    0.128638498,
    -0.034941764,
    -0.073275862,
    0.15627907,
    0.08608206,
    -0.017777778,
    -0.005279035,
    -0.091736164,
    -0.106844741,
    0.111214953,
    -0.066442389,
    -0.023423423,
    -0.001845018,
    -0.061922366,
    0.03546798,
    -0.030447193,
    0.02747792
]


class TestCalculations(TestCase):

    # def test_average(self):
    #     """Tests that the average value of a list of values is returned
    #     :return: float
    #     """
    #     nums = [1, 2, 3, 4, 5, 6, 0, 5, 78, 9]
    #     nums1 = test
    #     nums3 = [10, 15, 100, 11]
    #
    #     self.assertEqual(average(nums), 11.3)
    #     self.assertAlmostEqual(average(nums1), 748.325694444444)
    #     self.assertNotEqual(average(nums3), 3.5)

    def test_returns(self):
        """

        :return:
        """
        prices = [1, 1.2, 0.9]
        result = [0.2, -0.25]
        prices1 = test
        npt.assert_almost_equal(returns(prices), result)
        npt.assert_almost_equal(returns(prices1), returns_test)

    def test_returns_len(self):
        """

        :return:
        """
        # instantiating a Share object with prices
        s = ShareFactory.create('ERM', '2009-01-01', '2014-12-31')

        # variables for the test
        prices = s.prices
        result = returns(prices)

        self.assertTrue(len(prices) > len(result))
        self.assertTrue(len(prices) == len(result) + 1)

    def test_returns_type(self):
        """

        :return:
        """
        # instantiating a Share object with prices
        s = ShareFactory.create('^FTSE', '2009-01-01', '2014-12-31')

        # variables for the test
        prices = s.prices
        result = returns(prices)

        self.assertTrue(type(result) == list)
        self.assertTrue(type(result[0]) == float)

    def test_stdvt(self):
        """

        :return:
        """
        # instantiating a Share object with prices
        s = ShareFactory.create('CGL', '2009-01-01', '2014-12-31')

        # variables for the test
        prices = returns(s.prices)
        result = stdvt(prices)

        npt.assert_almost_equal(result, 75.350371, decimal=3)
        self.assertAlmostEqual(result, 75.350371, 3)
        self.assertTrue(type(result) == float)
        self.assertFalse(type(result) == int)


class TestAnnualise(TestCase):
    def test_annualise_type(self):
        """

        :return:
        """
        # instantiating a Share object with prices
        s = ShareFactory.create('CGL', '2009-01-01', '2014-12-31')

        # variables for the test
        num = stdvt(s.prices)
        result = annualise(num)

        self.assertTrue(type(result) == float)

    def test_annualise_logic(self):
        """

        :return:
        """
        # instantiating a Share object with prices
        s = ShareFactory.create('CGL', '2009-01-01', '2014-12-31')

        # variables for the test
        num = stdvt(s.prices)
        result = annualise(num)

        self.assertTrue(num * 12 * 100 == result)


class TestCorrelate(TestCase):

    def test_correlate(self):
        """

        :return:
        """
        # instantiating a Share objects with prices
        s1 = ShareFactory.create('ERM', '2009-01-01', '2014-12-31')
        s2 = ShareFactory.create('AML', '2009-01-01', '2014-12-31')

        sharelist = [s1.prices, s2.prices]
        # Result produced by Excel's correl function = 0.659850802
        # Result produced by a scientific calculator = 0.6598508
        npt.assert_almost_equal(correlation(sharelist)[1][0], 0.659850802)

    def test_correlate1(self):
        """

        :return:
        """
        # instantiating a Share objects with prices
        s1 = ShareFactory.create('ERM', '2009-01-01', '2014-12-31')
        s2 = ShareFactory.create('AML', '2009-01-01', '2014-12-31')
        sharelist = [returns(s1.prices), returns(s2.prices)]

        # Result produced by Excel's correl function = 0.310297815057478
        # Result produced by a scientific calculator = 0.3102978150
        npt.assert_almost_equal(correlation(sharelist)[1][0], 0.3102978150)

    def test_correlate_values(self):
        """

        :return:
        """
        # instantiating a Share objects with prices
        s1 = ShareFactory.create('ERM', '2009-01-01', '2014-12-31')
        s2 = ShareFactory.create('AML', '2009-01-01', '2014-12-31')
        s3 = ShareFactory.create('CGL', '2009-01-01', '2014-12-31')
        s4 = ShareFactory.create('NG', '2009-01-01', '2014-12-31')
        s5 = ShareFactory.create('^FTSE', '2009-01-01', '2014-12-31')

        sharelist = [returns(s1.prices), returns(s2.prices), returns(s3.prices),
                     returns(s4.prices), returns(s5.prices)]

        result = np.ravel(correlation(sharelist))
        self.assertTrue(all(0 <= value <= 1 for value in result))

    def test_correlate_noreturn(self):
        """

        :return:
        """
        # instantiating a Share objects with prices
        s1 = ShareFactory.create('ERM', '2009-01-01', '2014-12-31')
        sharelist = [returns(s1.prices)]

        self.assertEquals(correlation(sharelist), None)


class TestBeta(TestCase):

    def test_beta(self):
        """

        :return:
        """
        # instantiating Share objects with prices
        s = ShareFactory.create('NG', '2009-01-01', '2014-12-31')
        m = ShareFactory.create('^FTSE', '2009-01-01', '2014-12-31')

        # Result produced by Excel's slope function = 0.4177679640016210
        # Result produced by a scientific calculator = 0.41776796400162000
        npt.assert_almost_equal(beta(s, m), 0.4177679640016, 2)

    def test_beta1(self):
        """
        Tests mathematical accuracy of results produced by the beta function
        """
        # instantiating Share objects with prices
        s = ShareFactory.create('ERM', '2009-01-01', '2014-12-31')
        m = ShareFactory.create('^FTSE', '2009-01-01', '2014-12-31')

        # Result produced by Excel's slope function = 0.627308583277
        # Result produced by a scientific calculator = 0.6273085833
        npt.assert_almost_equal(beta(s, m), 0.627308583277, 2)

    def test_beta2(self):
        """

        :return:
        """
        # instantiating Share objects with prices
        s = ShareFactory.create('AML', '2009-01-01', '2014-12-31')
        m = ShareFactory.create('^FTSE', '2009-01-01', '2014-12-31')

        # Result produced by Excel's slope function = 0.8166701
        # Result produced by a scientific calculator = 0.816670132347
        npt.assert_almost_equal(beta(s, m), 0.8166701, 2)

    def test_beta_market(self):
        """

        :return:
        """
        # instantiating Share objects with prices
        m = ShareFactory.create('^FTSE', '2009-01-01', '2014-12-31')

        npt.assert_almost_equal(beta(m, m), 1)

    def test_beta_type(self):
        """

        :return:
        """
        # instantiating Share objects with prices
        s = ShareFactory.create('ERM', '2009-01-01', '2014-12-31')
        m = ShareFactory.create('^FTSE', '2009-01-01', '2014-12-31')

        self.assertTrue(type(beta(s, m)), float)


class TestAlpha(TestCase):

    def test_alpha(self):
        """

        :return:
        """
        # instantiating a Share objects with prices
        s1 = ShareFactory.create('ERM', '2009-01-01', '2014-12-31')
        s2 = ShareFactory.create('AML', '2009-01-01', '2014-12-31')
        s3 = ShareFactory.create('CGL', '2009-01-01', '2014-12-31')
        s4 = ShareFactory.create('NG', '2009-01-01', '2014-12-31')
        mkt = ShareFactory.create('^FTSE', '2009-01-01', '2014-12-31')
        rf = 1.5

        # Result produced by Excel = 24.69476867   cell A5 in
        # Result produced by a scientific calculator = 24.6947686724029
        npt.assert_almost_equal(alpha(s1, mkt, rf), 24.6947686724029, 1)

        # Result produced by Excel = -0.98543348578
        # Result produced by a scientific calculator = -1.00581290854
        npt.assert_almost_equal(alpha(s2, mkt, rf), -0.98543348578, 1)

        # Result produced by Excel = 12.8146278
        # Result produced by a scientific calculator = 12.81462
        npt.assert_almost_equal(alpha(s3, mkt, rf), 12.8146278, 1)

        # Result produced by Excel = 4.66718239333
        # Result produced by a scientific calculator = 4.65654162
        npt.assert_almost_equal(alpha(s4, mkt, rf), 4.66718239333, 1)

    def test_alpha_type(self):
        """

        :return:
        """
        # instantiating a Share objects with prices
        s1 = ShareFactory.create('ERM', '2009-01-01', '2014-12-31')
        mkt = ShareFactory.create('^FTSE', '2009-01-01', '2014-12-31')
        rf = 1.5

        self.assertTrue(type(alpha(s1, mkt, rf)), float)

    def test_alpha_maket(self):
        """

        :return:
        """
        # instantiating a Share objects with prices
        mkt = ShareFactory.create('^FTSE', '2009-01-01', '2014-12-31')
        rf = 1.5

        self.assertFalse(alpha(mkt, mkt, rf) == 0)


class TestErb(TestCase):

    def test_erb(self):
        """

        :return:
        """
        # instantiating a Share objects with prices
        s1 = ShareFactory.create('ERM', '2009-01-01', '2014-12-31')
        s2 = ShareFactory.create('AML', '2009-01-01', '2014-12-31')
        s3 = ShareFactory.create('CGL', '2009-01-01', '2014-12-31')
        s4 = ShareFactory.create('NG', '2009-01-01', '2014-12-31')
        mkt = ShareFactory.create('^FTSE', '2009-01-01', '2014-12-31')
        rf = 1.5

        # Result produced by Excel = 46.477516946807484
        # Result produced by a scientific calculator = 46.550222295

        npt.assert_almost_equal(erb(s1, mkt, rf), 46.477516946807484, 1)

        # Result produced by Excel = 5.95239832333
        # Result produced by a scientific calculator = 5.9705760
        npt.assert_almost_equal(erb(s2, mkt, rf), 5.95239832333, 1)

        # Result produced by Excel = 34.31128049810
        # Result produced by a scientific calculator = 34.31128
        npt.assert_almost_equal(erb(s3, mkt, rf), 34.31128049810219, 1)

        # Result produced by Excel = 18.282891578920
        # Result produced by a scientific calculator = 18.28289
        npt.assert_almost_equal(erb(s4, mkt, rf), 18.282891578920, 1)

        # Result produced by Excel = 7.184000740
        # Result produced by a scientific calculator = 7.1809091
        npt.assert_almost_equal(erb(mkt, mkt, rf), 7.184000740, 1)

    def test_erb_type(self):
        """

        :return:
        """
        # instantiating a Share objects with prices
        s1 = ShareFactory.create('ERM', '2009-01-01', '2014-12-31')
        mkt = ShareFactory.create('^FTSE', '2009-01-01', '2014-12-31')
        rf = 1.5

        self.assertTrue(type(erb(s1, mkt, rf)), float)


class TestTotalRisk(TestCase):
    def test_total_risk(self):
        """

        :return:
        """
        # instantiating a Share objects with prices
        s1 = ShareFactory.create('ERM', '2009-01-01', '2014-12-31')
        s2 = ShareFactory.create('AML', '2009-01-01', '2014-12-31')
        s3 = ShareFactory.create('CGL', '2009-01-01', '2014-12-31')
        s4 = ShareFactory.create('NG', '2009-01-01', '2014-12-31')
        mkt = ShareFactory.create('^FTSE', '2009-01-01', '2014-12-31')

        # Result produced by Excel = 11953.4398822
        # Result produced by a scientific calculator = 11953.43989
        npt.assert_almost_equal(total_risk(s1), 11953.4398822, 1)

        # Result produced by Excel = 6309.56183350
        # Result produced by a scientific calculator = 6309.56183
        npt.assert_almost_equal(total_risk(s2), 6309.56183350, 1)

        # Result produced by Excel = 5677.743650
        # Result produced by a scientific calculator = 5677.67844
        npt.assert_almost_equal(total_risk(s3), 5677.7436500, 1)

        # Result produced by Excel = 2915.4816440
        # Result produced by a scientific calculator = 2915.62032
        npt.assert_almost_equal(total_risk(s4), 2915.4816440, 1)

        # Result produced by Excel = 2198.494453394
        # Result produced by a scientific calculator = 2205.9970
        npt.assert_almost_equal(total_risk(mkt), 2198.494453394, 1)

    def test_total_risk_type(self):
        """

        :return:
        """
        # instantiating a Share objects with prices
        s1 = ShareFactory.create('ERM', '2009-01-01', '2014-12-31')
        self.assertTrue(type(total_risk(s1)), float)


class TestSpecificRisk(TestCase):

    def test_specific_risk(self):
        """

        :return:
        """
        # instantiating a Share objects with prices
        s1 = ShareFactory.create('ERM', '2009-01-01', '2014-12-31')
        s3 = ShareFactory.create('CGL', '2009-01-01', '2014-12-31')
        s4 = ShareFactory.create('NG', '2009-01-01', '2014-12-31')
        mkt = ShareFactory.create('^FTSE', '2009-01-01', '2014-12-31')

        # Result produced by Excel = 11085.58818574
        # Result produced by a scientific calculator = 11085.3446570
        npt.assert_almost_equal(specific_risk(s1, mkt), 11085.58818574, 1)

        # Result produced by Excel = 5184.4459091
        # Result produced by a scientific calculator = 5182.40429337
        npt.assert_almost_equal(specific_risk(s3, mkt), 5184.4459090, 1)

        # Result produced by Excel = 2528.7129779
        # Result produced by a scientific calculator = 2530.60751
        npt.assert_almost_equal(specific_risk(s4, mkt), 2528.7129779, 1)

    def test_specific_risk_mkt(self):
        """

        :return:
        """
        # instantiating a Share objects with prices
        mkt = ShareFactory.create('^FTSE', '2009-01-01', '2014-12-31')
        self.assertAlmostEqual(specific_risk(mkt, mkt), 0)

    def test_specific_risk_type(self):
        """

        :return:
        """
        # instantiating a Share objects with prices
        mkt = ShareFactory.create('^FTSE', '2009-01-01', '2014-12-31')
        self.assertTrue(type(specific_risk(mkt, mkt)) == float)



