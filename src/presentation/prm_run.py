"""
This module bla bla
"""

from data.share import *
from logic.calculator import *
from presentation.input import *
from tabulate import *
import pandas

def header():
    topline = '\n' + Fore.BLUE + '*' * 14 + \
              "  Portfolio Risk Management (PRM), version 1.0  2016 " + \
              '*' * 14 + '\n' + '\033[30m'

    bottomline = Fore.BLUE + '*' * 80 + '\n' + '\033[30m'

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


def risk_indicators(stocks, mkt, rfr):

    names = [s.name for s in stocks]

    #  returns
    print()
    print(Fore.BLUE + "Average Annualised Return R as percentage %" +'\033[30m')
    print()
    rts = [annualise(np.average(returns(s.prices))) for s in stocks]
    rts_tab = [[s, r] for s, r in zip(names, rts)]
    print(tabulate(rts_tab, headers=['Share', 'Return'], tablefmt='orgtbl',
                   floatfmt=".4f", numalign="right"))
    print()

    #  standard deviation
    print()
    print(
        Fore.BLUE + "Annualised Standard Deviation as percentage %" +'\033[30m')
    print()
    sdev = [stdvt(returns(s.prices)) for s in stocks]
    sdev_tab = [[s, sd] for s, sd in zip(names, sdev)]
    print(tabulate(sdev_tab, headers=['Share', 'StDev'], tablefmt='orgtbl',
                   floatfmt=".4f", numalign="right"))
    print()

    #  Beta
    print()
    print(
        Fore.BLUE + "Beta value of a share" + '\033[30m')
    print()
    b = [beta(s, mkt) for s in stocks]
    b_tab = [[s, bv] for s, bv in zip(names, b)]
    print(tabulate(b_tab, headers=['Share', 'Beta'], tablefmt='orgtbl',
                   floatfmt=".4f", numalign="right"))
    print()

    #  Alpha
    print()
    print(
        Fore.BLUE + "Alpha value of a share" + '\033[30m')
    print()
    a = [alpha(s, mkt,rfr) for s in stocks]
    a_tab = [[s, av] for s, av in zip(names, a)]
    print(tabulate(a_tab, headers=['Share', 'Alpha'], tablefmt='orgtbl',
                   floatfmt=".4f", numalign="right"))
    print()

    #  ERB
    print()
    print(
        Fore.BLUE + "ERB value of a share expressed as %" + '\033[30m')
    print()
    e = [erb(s, mkt, rfr) for s in stocks]
    e_tab = [[s, ev] for s, ev in zip(names, e)]
    print(tabulate(e_tab, headers=['Share', 'ERB'], tablefmt='orgtbl',
                   floatfmt=".4f", numalign="right"))
    print()

    #  Total risk
    print()
    print(
        Fore.BLUE + "Total risk value of a share expressed as %^2" + '\033[30m')
    print()
    tr = [total_risk(s) for s in stocks]
    tr_tab = [[s, tr] for s, tr in zip(names, tr)]
    print(tabulate(tr_tab, headers=['Share', 'Total Risk'], tablefmt='orgtbl',
                   floatfmt=".4f", numalign="right"))
    print()

    #  Specific risk
    print()
    print(
        Fore.BLUE + "Specific risk value of a share expressed as %^2" +
        '\033[30m')
    print()
    sr = [specific_risk(s, mkt) for s in stocks]
    sr_tab = [[s, sr] for s, sr in zip(names, sr)]
    print(tabulate(sr_tab, headers=['Share', 'Specific Risk'],tablefmt='orgtbl',
                   floatfmt=".4f", numalign="right"))
    print()

    #  Correlations
    print()
    print(
        Fore.BLUE + "Correlation coefficients between each pair of shares" +
        '\033[30m')
    print()
    cor = correlation([returns(s.prices) for s in stocks])

    print(pandas.DataFrame(cor, names, names))
    print()




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
    print('\n' * 3)

    risk_indicators(shares, market, rate)



main()

# d = ['2009-01-01', '2014-12-31']
#
# l = ['ERM', 'AML', 'CGL', 'NG', '^FTSE']
#
# myshares = share_maker(l,d)
# mkt = market_maker(d)











#risk_indicators(myshares, mkt, 1.5)



