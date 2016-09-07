from unittest import TestCase
from logic.calculator import *


class TestCalculations(TestCase):

    def test_average(self):
        """Tests that the average value of a list of values is returned
        :return: float
        """
        nums = [1, 2, 3, 4, 5, 6, 0, 5, 78, 9]
        nums1 = test_lst
        nums3 = [10, 15, 100, 11]

        self.assertEqual(average(nums), 11.3)
        self.assertAlmostEqual(average(nums1), 748.325694444444)
        self.assertNotEqual(average(nums3), 3.5)




test_lst = [
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
