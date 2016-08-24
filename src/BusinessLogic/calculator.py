from numpy import *
import statistics


class Calculator(object):
    @staticmethod
    def average_return(list_of_nums):
        ar_result = float(sum(list_of_nums) / len(list_of_nums))
        return ar_result

    @staticmethod
    def return_on_share_prices(list_of_prices):
        rs_result = []
        position = 0

        while position < len(list_of_prices) - 1:
            r = float(
                (list_of_prices[position + 1] / list_of_prices[position]) - 1)  # format(..., '.5f')  # !!!!! check
            rs_result.append(r)
            position += 1

        return rs_result

    @staticmethod
    def standard_deviation(list_of_num):
        #NB: stdev  == excel stdev.p!!! numpy gives you stdev.s!!
        sd_result = statistics.stdev(list_of_num)
        return sd_result

    @staticmethod
    def annualise_as_percentage(num):
        annualised_num = num * 12 * 100
        return annualised_num

    #@staticmethod
    #def correlation_coefficent(list_of_shares):


