"""This module contains methods that perform calculations and statistical
assessments for Share objects by using Shares' historical prices values
"""

import numpy as np
import statistics


def average(nums):
    r"""
    Calculates the average of the numbers in a list

    The primary use is to calculate the average of historical prices for a share
    or the average return on a share for a defined period of time.

    Parameters
    ----------
    :param nums: return values for a share for a period of time
    :type nums: list[float]
    :returns: float, the average (mean) value of a list of prices or
    share returns
    """
    avg = np.average(nums)
    return avg


def returns(prices):
    r"""
    Calculates returns on share's prices

    A return over a single period is calculated for each price. To calculate
    the monthly return on a share's prices, the following financial formula
    is applied:

    Return(R)  = Pt / Pt-1 - 1, where
    Pt is a final price
    Pt-1 is an original price

    Iterating through the prices in a given list a return is calculated for
    every single period.

       Parameters
       ----------
       :param nums: return values for a share for a period of time
       :type nums: list[float]
       :returns: float, the average (mean) value of a list of prices or
       share returns
       """
    rs_result = []
    position = 0

    while position < len(list_of_hist_prices) - 1:
        r = float(
            (list_of_hist_prices[position + 1] / list_of_hist_prices[
                position]) - 1)
        rs_result.append(r)
        position += 1

    return rs_result

    # def std(self, list_of_hist_prices):
    #     # NB: stdev  == excel stdev.p!!! numpy gives you stdev.s!!
    #
    #     sd = statistics.stdev(
    #         [float(item) for item in self.returns(list_of_hist_prices)])
    #
    #     return float(self.annualise(sd))
    #
    # @staticmethod
    # def annualise(num):
    #     r"""
    #     Returns
    #     -------
    #     float: annualised (percent)
    #     :param num:
    #     :return:
    #     """
    #     annualised_num = num * 12 * 100
    #     return annualised_num
    #
    # @staticmethod
    # def correlate(list_of_shares):
    #     lists_of_prices_to_correlate = []
    #
    #     if len(list_of_shares) > 1:
    #
    #         for share in list_of_shares:
    #             lists_of_prices_to_correlate.append(
    #                 share.get_historical_prices())
    #         correlations = corrcoef(lists_of_prices_to_correlate)
    #         return correlations
    #
    #     else:
    #         print("Insufficient number of shares to perform correlation " +
    #               " (minimum 2 required, but %(num)d were provided)" % {
    #                   "num": len(list_of_shares)})
    #
    # def beta(self, lst_share_prices, lst_market_prices):
    #     # cov(x,y)/ var(y)
    #     # ddof=0`` provides a maximum likelihood estimate of the variance for normally distributed variables(ref!!!)
    #
    #     returns_share = [float(item) for item in self.returns(lst_share_prices)]
    #     returns_market = [float(item) for item in
    #                       self.returns(lst_market_prices)]
    #
    #     beta_result = float((cov(returns_share, returns_market, ddof=0)[0][1]) /
    #                         (var(returns_market)))
    #
    #     return beta_result
    #
    # def alpha(self, lst_hist_prices_share, lst_hist_prices_market, rf):
    #     # Alpha %  --> α = Rs – [Rf + (Rm – Rf) β]
    #
    #     returns_share = [float(item) for item in
    #                      self.returns(lst_hist_prices_share)]
    #     rs = self.annualise(self.average(returns_share))
    #
    #     returns_market = [float(item) for item in
    #                       self.returns(lst_hist_prices_market)]
    #     rm = self.annualise(self.average(returns_market))
    #
    #     beta_s = self.beta(lst_hist_prices_share, lst_hist_prices_market)
    #
    #     alpha_s = rs - (rf + (rm - rf) * beta_s)
    #
    #     return alpha_s
    #
    # def erb(self, lst_share_prices, lst_market_prices, rf):
    #     # ERB --> Treynor ratio = (Rs – Rf) ÷ β
    #
    #     rs = self.annualise(
    #         self.average(
    #             [float(item) for item in self.returns(lst_share_prices)]))
    #
    #     erb_result = float(
    #         (rs - rf) / self.beta(lst_share_prices, lst_market_prices))
    #
    #     return erb_result
    #
    # def t_risk(self, lst_hist_prices):
    #     tr = pow(self.std(lst_hist_prices), 2)
    #     return tr
    #
    # def s_risk(self, share_histprices, market_histprices):
    #
    #     sr = float(self.t_risk(share_histprices) - (
    #     pow(self.beta(share_histprices, market_histprices), 2) *
    #     self.t_risk(market_histprices)))
    #
    #     return sr
