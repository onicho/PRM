from unittest import TestCase
from unittest.mock import patch
from presentation.input import *


#Ref: https://docs.python.org/3/library/unittest.mock-examples.html


class TestInput(TestCase):

    def test_valid_epic(self):

        self.assertTrue(valid_epic("TSCO"))
        self.assertFalse(valid_epic("6575096859"))

    def test_get_tickers(self):

        with patch('builtins.input', side_effect = ['BP', 'LLOY', '0']):
            self.assertEqual(get_tickers(), ['BP', 'LLOY'])

        # can only accept 10 elements even if more than 10 were given
        with patch('builtins.input', side_effect=['BP', 'LLOY', 'RBS', 'BRBY',
                                                  'ERM', 'CGL', 'NG', 'III',
                                                  'VOD', 'BA', 'TSCO']):

            self.assertEqual(get_tickers(), ['BP', 'LLOY', 'RBS', 'BRBY',
                                                  'ERM', 'CGL', 'NG', 'III',
                                                  'VOD', 'BA']) # no TSCO

        with patch('builtins.input', side_effect=['9068958', 'LLOY', '0']):
            self.assertEqual(get_tickers(), ['LLOY'])

        with patch('builtins.input', side_effect=['0']):
            self.assertEqual(get_tickers(), [])

    def test_valid_date(self):

        self.assertTrue(valid_date("2009-08-11"))
        self.assertTrue(valid_date("2016-09-19"))
        self.assertTrue(valid_date("2020-12-31"))

        self.assertFalse(valid_date("6575096859"))
        self.assertFalse(valid_date("02.05.16"))
        self.assertFalse(valid_date("2 Sen 2015"))

    def test_get_period(self):
        pass



