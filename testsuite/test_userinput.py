from unittest import TestCase
from presentation.input import *


class TestInput(TestCase):

    def test_valid(self):

        self.assertTrue(valid("TSCO"))
