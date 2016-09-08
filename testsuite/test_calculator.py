from unittest import TestCase
from logic.calculator import *
import numpy.testing as npt
from numpy import *
from logic.share import *

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
    def test_average(self):
        """Tests that the average value of a list of values is returned
        :return: float
        """
        nums = [1, 2, 3, 4, 5, 6, 0, 5, 78, 9]
        nums1 = test
        nums3 = [10, 15, 100, 11]

        self.assertEqual(average(nums), 11.3)
        self.assertAlmostEqual(average(nums1), 748.325694444444)
        self.assertNotEqual(average(nums3), 3.5)

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
        prices = s.prices
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
        my_hypot = all(0 <= value <= 1 for value in result)

        self.assertTrue(my_hypot)

    def test_correlate_noreturn(self):
        """

        :return:
        """
        # instantiating a Share objects with prices
        s1 = ShareFactory.create('ERM', '2009-01-01', '2014-12-31')
        s2 = ShareFactory.create('AML', '2009-01-01', '2014-12-31')
        s3 = ShareFactory.create('CGL', '2009-01-01', '2014-12-31')
        s4 = ShareFactory.create('NG', '2009-01-01', '2014-12-31')
        s5 = ShareFactory.create('^FTSE', '2009-01-01', '2014-12-31')

        sharelist = [returns(s1.prices)]

        self.assertEquals(correlation(sharelist), None)



