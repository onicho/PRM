"""
This module bla bla
"""
from colorama import *
import textwrap


def header():
    topline = '\n' + Fore.YELLOW + '*' * 14 + \
              "  Portfolio Risk Management (PRM), version 1.0  2016 " + \
              '*' * 14 + '\n' + '\033[30m'

    bottomline  = Fore.YELLOW + '*' * 80 + '\n' + '\033[30m'

    text = """
    The PRM tool facilitates accurate statistical analysis for a number of sha -
    res. Its primary use is to assess performance and key risk indicators for a
    set of securities, as well as construct optimised investment portfolios with
    Elton and Gruber or Treynor-Black operational procedures.

    """
    print(topline)
    print(text)
    print(bottomline)


header()
