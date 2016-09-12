from unittest import TestCase
from unittest.mock import patch
from presentation.input import *


class TestInput(TestCase):

    def test_valid(self):

        self.assertTrue(valid("TSCO"))
        self.assertFalse(valid("6575096859"))

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

