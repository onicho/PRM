"""This module contains methods that perform calculations and statistical
assessments for Share objects by using Shares' historical prices values
"""

import numpy as np
import statistics
from logic.share import *


def average(nums):
    r"""
    Calculates the average of the numbers in a list

    The primary use is to calculate the average of historical prices for a share
    or the average return on a share for a defined period of time.

    Parameters
    ----------
    :param nums: return values for a share for a period of time
    :type nums: list[float]
    :returns: float
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

    Iterating through the prices in a given list a rate of return is calculated
    for every single period.

    Parameters
    ----------
    :param prices: historical share prices for a certain period of time
    :type prices: list[float]
    :returns: list[float]

    :Example:

    list of share prices [1, 1.2, 0.9]
    returned list [0.2, -0.25]

    """
    result = []
    position = 0

    while position < len(prices) - 1:
        r = float(
            (prices[position + 1] / prices[position]) - 1
        )
        result.append(r)
        position += 1

    return result


def stdvt(prices):
    r"""
    Calculates Standard Deviation of a list of data values

    The primary use is to calculate Standard Deviation of returns
    (rates of return)on a share's prices. The function accepts a list of
    historical share prices, then calculates rates of return for every single
    period and finally calculates std for the return values.

    The statistics package method stdev is ised to calculate std. It corresponds
    to Excel's stdev.p function, which calculates std for a population.

    Parameters
    ----------
    :param prices: historical share prices for a period
    :type prices: list[float]
    :return: float
    """
    sd = statistics.stdev(
        [item for item in returns(prices)])

    return annualise(sd)


def annualise(num):
    r"""
    Annualises a values per percentage.

    Use cases: annualising the average monthly return on a share as percentage
               annualising Standard Deviation of monthly returns as percentage

    Returns
    -------
    float: annualised (percent)

    Parameters
    ---------
    :param num: avg monthly return or standard deviation of a share's prices
    :type num: float
    :return: float
    """
    anld = float(num) * 12 * 100
    return anld


def correlation(prices):
    r"""
    Calculates a correlation coefficient between each pair of shares

    Parameters
    ----------
    :param prices: list containing arrays of prices or rates of return
    :type prices: list[list[float]]
    :return: the N-dimentional array with correlation coefficients for each pair
    :return type: array(array(float))

    :Example:

    produced results for correlated Share A and Share B
              A              B
    A   [[ 1.          0.31029782]
    B   [ 0.31029782  1.        ]]
    """
    if len(prices) > 1:

        correlations = np.corrcoef(prices)
        return correlations

    else:
        print("Insufficient number of shares to calculate correlations.  " +
              " (Minimum 2 required, but %(num)d were provided)" % {
                  "num": len(prices)})



            # lists_of_prices_to_correlate = []
            #
            # if len(shares) > 1:
            #
            #     for share in shares:
            #         lists_of_prices_to_correlate.append(
            #             share.get_historical_prices())
            #     correlations = np.corrcoef(lists_of_prices_to_correlate)
            #     return correlations
            #
            # else:
            #     print("Insufficient number of shares to perform correlation " +
            #           " (minimum 2 required, but %(num)d were provided)" % {
            #               "num": len(shares)})
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
