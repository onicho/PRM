from audioop import avg
from numpy import *


class Calculator(object):

    @staticmethod
    def average_return(list_of_nums):
        result = float(sum(list_of_nums) / len(list_of_nums))
        return result




calc = Calculator()
print(calc.average_return([12]))
print(calc.average_return([1, 2, 4]) == mean([1, 2, 4]))