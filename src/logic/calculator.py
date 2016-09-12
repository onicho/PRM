"""This module contains methods that perform calculations and statistical
assessments for Share objects by using Shares' historical prices values
"""

import numpy as np
import statistics
from logic.share import *


def returns(prices):
    r"""
    Calculates returns on share's prices

    A return over a single period is calculated for each price. To calculate
    the monthly return on a share's prices, the following financial formula
    is applied:
    Formula
    -------
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

    returns([1, 1.2, 0.9])
    [0.2, -0.25]

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
    sd = statistics.stdev(prices)

    # returns already annualised stdvt value
    return annualise(sd)


def annualise(num):
    r"""
    Annualises a values per percentage.

    Use cases
    ---------
    annualising the average monthly return of a share as percentage
    annualising Standard Deviation of monthly returns as percentage

    Parameters
    ---------
    :param num: avg monthly return or standard deviation of a share's prices
    :type num: float
    :return: annualised value as percent
    :rtype: float
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


def beta(share, market):
    r"""
    Calculates Beta of a stock

    Calculation of beta through regression, i.e. the covariance of the two
    arrays (each contains rates of return for a share) divided by the variance
    of the array of the market index returns. The formula is:
    Formula
    -------
    Beta  =  Covariance (ri,rm )/Variance of Market , where
    ri = returns on share
    rm = returns on market index

    Numpy methods to estimate covariance and variance are used. Degrees of
    Freedom ddof is set to 0, which indicates the number of values that are free
    to vary in the final calculation

    Parameters
    ----------
    :param share: object Share that represents a stock market share
    :param market: object Share that represents the stock market ticker FTSE100
    :type share: Share
    :type market: Share
    :return: beta value of a stock
    :rtype: float
    """

    # a list of rates of return on a share calculated from share's prices
    s = [rate for rate in returns(share.prices)]
    m = [rate for rate in returns(market.prices)]

    b = (
            np.cov(s, m, ddof=0)[0][1] / np.var(m)
        )

    return float(b)


def alpha(share, market, rf):
    r"""
    Calculates Alpha of a stock.

    Alpha value of security is the difference between the actual expected return
    of a share and the equilibrium expected return of a share. The return rates
    of a share for a period of time are calculated, then the average return
    value is found. The avg return value is annualised because the current
    version of the system works monthly returns of a share or market.
    Formula
    -------
    alpha = r - [rf + (rm - rf) * Beta]

    r =  actual avg return of a share
    rf = risk free rate
    rm actual avg return of the market
    Beta = beta value of a share

    Parameters
    ----------
    :param share: object Share that represents a stock market share
    :param market: object Share that represents the stock market ticker FTSE100
    :param rf: risk free rate
    :type share: Share
    :type market: Share
    :type rf: float
    :return: alpha value of a stock
    :rtype: float
    """

    rshare = [rate for rate in returns(share.prices)]
    r = annualise(np.average(rshare))

    rmarket = [rate for rate in returns(market.prices)]
    rm = annualise(np.average(rmarket))

    b = beta(share, market)

    av = r - (rf + (rm - rf) * b)
    return float(av)


def erb(share, market, rf):
    r"""
    Excess-Return-to-Beta of a stock

    Calculates risk-adjusted return, which is the average return earned in
    excess of the risk-free rate per unit of volatility or total risk.

    Formula
    -------
    erb = (r - rf) / Beta

    r = the share's return
    rf  = the risk-free rate of return
    Beta = the security's Beta, i.e. price volatility relative to
     the overall market

    Parameters
    ----------
    :param share: object Share that represents a stock market share
    :param market: object Share that represents the stock market ticker FTSE100
    :param rf: risk free rate
    :type share: Share
    :type market: Share
    :type rf: float
    :return: erb value of a stock
    :rtype: float
    """

    rshare = [rate for rate in returns(share.prices)]
    r = annualise(np.average(rshare))

    result = (r - rf) / beta(share, market)

    return result


def total_risk(share):
    r"""
    Measures Total Risk of each stock.

    Calculating the Total Risk by squaring annualised standard deviation of the
    share's return rate values.
    Formula
    -------
    tr = sd ^ 2 (std raised to the power of 2)

    Parameters
    ----------
    :param share: object Share that represents a stock market share
    :type share: Share
    :return: total risk measure of a stock (variance) as percent ^ 2
    :rtype: float
    """
    sreturn = returns(share.prices)
    tr = pow(stdvt(sreturn), 2)

    return tr


def specific_risk(share, market):
    r"""
    Specific Risk of a share (also known as unsystematic or diversifiable risk)

    The calculation is derived from the Total Risk formula, which is the sum of
    systematic and non-systematic risks.

    Formula
    -------
    sr^2 = trs^2 - [Beta^2 * trm^2]
    trs = total risk of a share
    Beta  = beta of a share
    trm = total risk of a market

    Parameters
    ----------
    :param share:
    :param market:
    :return:
    """
    trs = total_risk(share)  # the value is already squared
    b = pow(beta(share, market), 2)
    trm = total_risk(market)  # the value is already squared

    sr = trs - b * trm
    return sr



