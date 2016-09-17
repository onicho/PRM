"""
This module bla bla
"""

from data.share import *
from logic.calculator import *
from presentation.input import *
from tabulate import *

def header():
    topline = '\n' + Fore.LIGHTCYAN_EX + '*' * 14 + \
              "  Portfolio Risk Management (PRM), version 1.0  2016 " + \
              '*' * 14 + '\n' + '\033[30m'

    bottomline = Fore.LIGHTCYAN_EX + '*' * 80 + '\n' + '\033[30m'

    text = """
    The PRM tool facilitates accurate statistical analysis for a number of sha -
    res. Its primary use is to assess performance and key risk indicators for a
    set of securities, as well as construct optimised investment portfolios with
    Elton and Gruber or Treynor-Black operational procedures.

    """
    print(topline)
    print(text)
    print(bottomline)


def sharenotes():
    nb = """
    NB:maximum of 10 shares can be processed at the time. PRM works with FTSE100
    securities only and uses their MONTHLY closing prices for calculations.
    """
    print(nb)


def datenotes():
    dt = """
    NB: start and end dates of the time period must be in the following format:
    yyyy-mm-dd. The earliest start date can be 1 January 2009. There must be at
    least 31 days difference between the start and end dates because PRM works
    with MONTHLY closing share price.
    """
    print(dt)


def risknotes():
    r = """
    NB: risk free rate should be a number more than zero and less than 100. It
    can be expressed as a decimal point number.
    """
    print(r)


def share_maker(strings, dates):
    shares = [ShareFactory.create(s, dates[0], dates[1]) for s in strings]
    return shares


def market_maker(dates):
    market = ShareFactory.create('^FTSE', dates[0], dates[1])
    return market


def main():
    header()

    sharenotes()
    strings = get_tickers()

    datenotes()
    dates = get_period()

    risknotes()
    rate = get_rfr()

    shares = share_maker(strings, dates)
    market = market_maker(dates)

    print()
    print('*' * 80)
    print('\n' * 5)

    #returns = returns(s.price)

# main()

d = ['2009-01-01', '2014-12-31']

l = ['ERM', 'AML', 'CGL', 'NG', '^FTSE']

myshares = share_maker(l,d)


def risk_indicators(stocks):

    names = [s.name for s in stocks]

    #  returns
    print()
    print(Fore.BLUE +"Average Annualised Return R as percentage %" + '\033[30m')
    print()
    rts = [annualise(np.average(returns(s.prices))) for s in stocks]
    rts_tab = [[s,r] for s,r in zip(names, rts)]
    print(tabulate(rts_tab, headers=['Share', 'Return'], tablefmt='orgtbl'))
    print()

    #  standard deviation
    print()
    print(
        Fore.BLUE + "Average Annualised Return R as percentage %" + '\033[30m')
    print()
    rts = [annualise(np.average(returns(s.prices))) for s in stocks]
    rts_tab = [[s, r] for s, r in zip(names, rts)]
    print(tabulate(rts_tab, headers=['Share', 'Return'], tablefmt='orgtbl'))
    print()



risk_indicators(myshares)



