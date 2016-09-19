"""
This module bla bla
"""
from logic.portfolio import *
from data.share import *
from logic.calculator import *
from presentation.input import *
from tabulate import *
import pandas
import matplotlib.pyplot as plt


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
    print(
        Fore.BLUE + "Average Annualised Return R as percentage %" + '\033[30m')
    print()
    rts = [annualise(np.average(returns(s.prices))) for s in stocks]
    rts_tab = [[s, r] for s, r in zip(names, rts)]
    print(tabulate(rts_tab, headers=['Share', 'Return'], tablefmt='orgtbl',
                   floatfmt=".4f", numalign="right"))
    print()

    #  standard deviation
    print()
    print(
        Fore.BLUE + "Annualised Standard Deviation as percentage %" + '\033[30m')
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
    print("""
    INVESTOPEDIA EXPLAINS: a beta of less than 1 means that the security is
    theoretically less volatile than the market. A beta of greater than 1
    indicates that the security's price is theoretically more volatile than the
    market. For example, if a stock's beta is 1.2, it's  20% more volatile than
    the market. Negative betas are possible for investments that tend to go down
    when the market goes up, and vice versa.
    """)
    print()

    #  Alpha
    print()
    print(
        Fore.BLUE + "Alpha value of a share" + '\033[30m')
    print()
    a = [alpha(s, mkt, rfr) for s in stocks]
    a_tab = [[s, av] for s, av in zip(names, a)]
    print(tabulate(a_tab, headers=['Share', 'Alpha'], tablefmt='orgtbl',
                   floatfmt=".4f", numalign="right"))
    print()
    print("""
    INVESTOPEDIA EXPLAINS: Alpha measures volatility or risk, and is also often
    referred to as “excess return” or “abnormal rate of return.” A positive alpha
    of 1.0 means the fund or stock has outperformed its benchmark index (e.g.
    FTSE100) by 1 percent. A similar negative alpha of 1.0 would indicate an
    underperformance of 1 percent.
    """)
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
    print(
        tabulate(sr_tab, headers=['Share', 'Specific Risk'], tablefmt='orgtbl',
                 floatfmt=".4f", numalign="right"))
    print()
    print("""
      INVESTOPEDIA EXPLAINS: Specific risk, also known as "unsystematic risk,"
      "diversifiable risk" or "residual risk," is the type of uncertainty that
      comes with the company or industry you invest in. Unsystematic risk can be
      reduced through diversification.
      """)
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


def eg_constructor(shares, mkt, rfr):

    eg = EltonGruberPortfolio(shares, mkt, rfr).final
    eg_tab = [[key.name, value] for key, value in eg.items()]

    #  printing the table
    print(
        Fore.BLUE + "Elton and Gruber Active Investment Portfolio" +
        '\033[30m')
    print()
    print(tabulate(eg_tab, headers=['Share', 'Weight %'], tablefmt='orgtbl',
                   numalign="right"))
    print()

    #  plotting a pie chart

    # REFERENCE:
    # guidance on how to build a chart was taken from the link source below
    # https://www.getdatajoy.com/examples/python-plots/pie-chart

    plt.pie([item[1] for item in eg_tab],
            labels=[item[0] for item in eg_tab],
            colors=['lightblue', 'green', 'cyan', 'yellowgreen', 'mediumpurple',
                    'lightskyblue', 'lightcoral', 'yellow'],
            autopct='%1.2f%%',  # print the values inside the wedges
            )


    plt.title('Elton and Gruber Portfolio' + '\n')
    plt.axis('equal')
    fig1 = plt.gcf()
    plt.draw()
    fig1.savefig(
        'C:\\PycharmProjects\\PRM\\src\\.image_output\\eg_portfolio.png',
        dpi=100)
    plt.close()


def tb_constructor(shares, mkt, rfr):
    p = TreynorBlackPortfolio(shares, mkt, rfr)
    tb = p.final
    tb_tab = [[key.name, value] for key, value in tb.items()]

    #  printing the table
    print(
        Fore.BLUE + "Treynor-Black Active Investment Portfolio" +
        '\033[30m')
    print()
    print(tabulate(tb_tab, headers=['Share', 'Weight %'], tablefmt='orgtbl',
                   numalign="right"))
    print()

    #  plotting a portfolio components pie chart

    plt.pie([item[1] for item in tb_tab],
            labels=[item[0] for item in tb_tab],
            colors=['lightblue', 'green', 'cyan', 'yellowgreen', 'mediumpurple',
                    'lightskyblue', 'lightcoral', 'yellow'],
            autopct='%1.2f%%',
            )

    # REFERENCE:
    # guidance on how to build a chart was taken from the link source below
    # https://www.getdatajoy.com/examples/python-plots/pie-chart

    plt.title('Treynor-Black Portfolio' + '\n')
    plt.axis('equal')
    fig1 = plt.gcf()
    plt.draw()
    fig1.savefig(
        'C:\\PycharmProjects\\PRM\\src\\.image_output\\tb_portfolio.png',
        dpi=100)
    plt.close()

    print()

    #  plotting active/passive weights chart

    plt.pie([p.active, 100 - p.active],
            labels=['Passive', 'Active'],
            colors=['lightblue', 'green', 'cyan', 'yellow'],
            autopct='%1.2f%%',  # print the values inside the wedges
            )

    # REFERENCE:
    # guidance on how to build a chart was taken from the link source below
    # https://www.getdatajoy.com/examples/python-plots/pie-chart

    plt.title('Weights of active and passive portfolios in TB' + '\n')
    plt.axis('equal')
    fig2 = plt.gcf()
    plt.draw()
    fig2.savefig(
        'C:\\PycharmProjects\\PRM\\src\\.image_output\\active_passive.png',
        dpi=100)
    plt.close()


def main():
    try:

        run_prm = True

        while run_prm:

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
            print('\n' * 2)
            print(Fore.YELLOW + '-' * 80)
            print(Fore.BLUE + "Assessment for the period: " + '\033[30m')
            print("FROM " + dates[0] + " TO " + dates[1])
            print()
            print(Fore.BLUE + "Your risk free rate : " + '\033[30m')
            print(str(rate) + '%')
            print(Fore.YELLOW + '-' * 80 + '\033[30m')

            risk_indicators(shares, market, rate)

            print()
            print('\n')

            print(Fore.YELLOW + '-' * 80)
            print(
                Fore.BLUE + "Candidate shares for portfolio construction: " +
                '\033[30m')
            for i in strings:
                print(i, end='  ')
            print()
            print()
            print(Fore.BLUE + "Assessment for the period: " + '\033[30m')
            print("FROM " + dates[0] + " TO " + dates[1])
            print()
            print(Fore.BLUE + "Your risk free rate : " + '\033[30m')
            print(str(rate) + '%')
            print(Fore.YELLOW + '-' * 80 + '\033[30m')
            print()

            eg_constructor(shares, market, rate)

            tb_constructor(shares, market, rate)

            print()
            print(
                Fore.YELLOW + "See portfolios' chart images in the output file"
                + '\033[30m')
            print()

            answer = str(input("Would you like to analyse another batch of "
                               "shares? (enter y to continue): "))

            if answer.lower() != "y":
                run_prm = False
                print()
                print('*' * 22 + "MANY THANKS FOR USING PRM. GOOD BYE" + '*'*22)

            else:
                print('\n' * 5)

    except Exception:
        print("There was an unexpected error during execution.")
        print("Please try to run the system again")
        print()
        text = """
        The most likely reason being that one of the shares you entered was no
        longer traded on LSE, which means that the system could not retrieve its
        prices to compare them to all other shares in the assessment batch.
        """
        print(Fore.LIGHTMAGENTA_EX + text + '\033[30m')


main()




