"""
This module contains classes that can be used to create Portfolio objects, which
represent a portfolio of stock market shares.
"""
import abc
from logic.calculator import *
from logic.share import Share


class Portfolio(object):
    r"""
    It is a base class for a portfolio object, which can be implemented.
    """
    def __init__(self, shares, mkt, rfr):
        r"""
        The class encapsulates portfolio information, specifically which shares
        the portfolio consists of, the stock exchange market where these shares
        are traded (also acts as a benchmark) and the risk free rate for the
        portfolio.

        Parameters
        ----------
        :param shares: Share objects passed to the class to form a portfolio
        :param mkt: the market ticker (index), e.g. FTSE100
        :param rfr: the risk free rate of the portfolio
        :type shares: list[Share]
        :type mkt: Share
        :type rfr: float
        """
        # checking that Portfolio is instantiated with correct arguments
        if all(type(obj) == Share for obj in shares) and type(mkt) is Share and \
                        type(rfr) is float:

            self.candidates = shares
            self.rfr = rfr
            self.market = mkt

        else:
            raise TypeError("Check that the object Portfolio instantiated with "
                            "the correct types of arguments")

    @property
    def shs_alphas(self):
        """
        Calculates alpha values for the shares in the portfolio. It applies
        the alpha function from the calculator module to every Share object in
        the portfolio to get values.
        :return: alpha values for each share in the portfolio
        :rtype: list[float]
        """
        alf = [alpha(share, self.market, self.rfr) for share in self.candidates]

        return alf

    @property
    def shs_specrisk(self):
        r"""
        Calculates specific risk values for the shares in the portfolio. It
        applies the specific_risk function from the calculator module to every
        Share object in the portfolio to get values.
        :return: specific risk values for each share in the portfolio
        :rtype: list[float]
        """
        srisk = [specific_risk(share, self.market) for share in self.candidates]

        return srisk

    @property
    def shs_betas(self):
        r"""
        Calculates beta values for the shares in the portfolio. It
        applies the beta function from the calculator module to every Share
        object in the portfolio to get values.
        :return: specific risk values for each share in the portfolio
        :rtype: list[float]
        """
        bts = [beta(share, self.market) for share in self.candidates]

        return bts

    @property
    def mkt_return(self):
        r"""
        Calculates the return of the market (e.g. FTSE100) where the portfolio
        shares are traded. The system is set to process monthly clothing prices
        for the shares, so the return rate values get averaged and annualised by
        using respective calculator functions.
        :return: annualised return rate for the market for a specific period
        :rtype: float
        """
        retmkt = annualise(np.average(
                                      returns(self.market.prices)
                                     ))
        return retmkt

    @property
    def mkt_risk(self):
        r"""
        Calculates the total risk the market (e.g. FTSE100) where the portfolio
        shares are traded. The total risk calculator function is used.
        :return: total risk of the market for a specific period
        :rtype: float
        """
        mrisk = total_risk(self.market)

        return mrisk


class WeightedPortfolio(Portfolio):
    """

    """
    __metaclass__ = abc.ABCMeta

    def __init__(self, shares, market, rfr):
        super().__init__(shares, market, rfr)
        self.final = {}

    @abc.abstractmethod
    def unadjusted(self):
        raise NotImplementedError

    def adjusted(self):
        """
        Calculates the normalised weights, i.e. proportion of portfolio invested
        in i share of the portfolio. The sum of adjusted weights should add up
        to 1.
        prop  = wi / SUM[unadjusted weights]
        :return: adjusted proportions of shares for the portfolio
        :rtype: list[float]
        """
        weights = [abs(w) for w in self.unadjusted()]

        adj = [(w/sum(weights))for w in weights]
        return adj

    def adjusted_percent(self):
        percentage = [round((w * 100), 2) for w in self.adjusted()]
        return percentage

    @abc.abstractmethod
    def shs_zip_props(self):
        raise NotImplementedError


class EltonGruberPortfolio(WeightedPortfolio):
    """
    A concrete class for a portfolio object, which constructs an active
    portfolio of stock market shares using the Elton and  Gruber operational
    procedure.
    This class inherits functionality of the WeightedPortfolio abstract class
    and the latter is derived from the base class Portfolio.
    """

    def __init__(self, shares, market, rfr):
        """
        The class encapsulates portfolio information, specifically:
        *candidate shares has passed to the class to form an active portfolio
        *the stock exchange market (market ticker,e.g FTSE100)where these shares
         are traded (it also acts as a benchmark for portfolio calculations)
        *the risk free rate for the portfolio
        *shares that form the final active portfolio and their proportions in it
        Parameters
        ----------
        :param shares: Share objects passed to the class to form a portfolio
        :param mkt: the market ticker (index), e.g. FTSE100
        :param rfr: the risk free rate of the portfolio
        :type shares: list[Share]
        :type mkt: Share
        :type rfr: float
        """
        super().__init__(shares, market, rfr)
        self.shs_zip_props()

    def order(self):
        """
        Ranks all shares according to their Excess Return on Beta. Every share
        is ordered from highest to lowest erb. A list of ordered shares is
        assigned to the class instance variable 'ordered'
        :return: ordered shares with highest erb first and lowest erb last
        :rtype: list[Share]
        """
        stocks = {}

        for share in self.candidates:
            stocks[erb(share, self.market, self.rfr)] = share

        ordered = [item[1] for item in sorted(stocks.items(), reverse=True)]
        return ordered

    def cutoff(self):
        """
        Calculates the unique cut-off rate c* for erb. All securities with erbs
        greater than cut-off rate will be included in the portfolio, but all
        securities with erbs less than cut-off rate will be excluded.
        Cut-off rate Cj for portfolio containing first j securities is given by

        Cj = trm * SUM[(ri - rf)Bi / sri] / 1 + trm * SUM[(Bi^2/sri)]

         trm  - total risk of the market
         ri - return on security i
         rf - risk free rate
         Bi - Beta of a security i
         sri - specific risk of a security i

         Steps
         -----
         1. The numerator has a constant element trm and a number of elements
         that need to be summed up in the numerator. The number of elements
         for each Cj varies, e.g C1 = 2 elem, C2 = 2 elem, etc. First step is to
         calculate variable numerator elements , i.e. the element for each share

         2. Find variable denominator elements (same principal as the
         denominator calculation)

         3. Calculate cut-off rates for shares

         4. Compare cut-rates with erbs of ordered shares and identify the
         unique cut off rate

        :return: the unique cut-off rate and its index in the list
        :rtype: dict{float : int}
        """
        stocks = self.order()

        #  Step1: calculate variable numerator components for each share
        numerator = []
        idx = 0

        for item in stocks:

            while idx <= stocks.index(item):

                r = returns(stocks[idx].prices)
                rets = annualise(np.average(r)) - self.rfr
                b = beta(stocks[idx], self.market)
                sri = specific_risk(stocks[idx], self.market)

                # (ri - rf) * Bi / sri
                numerator.append(rets * b / sri)

                idx += 1

        # Step2:  calculate variable denominator components for each share
        denominator = []
        count = 0

        for item in stocks:

            while count <= stocks.index(item):

                bb = pow(beta(stocks[count], self.market), 2)
                sri = specific_risk(stocks[count], self.market)

                #  bb / sri
                denominator.append(bb / sri)

                count += 1

        # Step3:  calculate cut-off rates for each share
        rates = []

        for share in stocks:

            n = len(stocks) - (stocks.index(share) + 1)

            # to remove the last n elements of a list
            num = numerator[:-n or None]
            denom = denominator[:-n or None]

            trm = total_risk(self.market)

            #  Calculating Cj for each share
            cj = (trm * sum(num)) / (1 + trm * sum(denom))

            rates.append(cj)

        # Step4:  compare rates with erbs of ordered shares and identify the
        # unique cut-off rate

        erbs = [erb(share, self.market, self.rfr) for share in stocks]

        c = {}

        index = 0
        found = False

        while not found:

            if index + 1 == len(rates):
                c = {rates[index]: index}
                break

            if rates[index] <= erbs[index + 1]:
                    index += 1
            else:
                c = {rates[index]: index}
                found = True

        return c

    def filtered(self):
        """
        Filters candidate shares that were ordered by their their erbs
        All ordered securities with the index that is equal or less than the
        index of the cut-off rate will be included in the optimal portfolio.
        :return: shares to be included in the optimal portfolio
        :rtype: list[Share]
        """
        c = self.cutoff()
        n = list(c.values())[0] + 1

        items = self.order()
        filtered = items[: n]

        return filtered

    def unadjusted(self):
        """
        Calculates unadjusted (unnormalised) weights of shares in Elton Gruber
        Portfolio. The formula to find the weight w of a security i is:

        wi = (Bi / sri) * ((ri - rf) / Bi - c* ), which can also be expressed:

        wi = (Bi / sri) * (erbi - c* ), where:

        Bi - is Beta of a share i
        sri - specific risk of a share i
        erbi - excess return to beta of share i
        c* - the unique cut-off rate of the portfolio

        :return: unadjusted proportions of shares for the portfolio
        :rtype: list[float]
        """

        weights = []
        securities = self.filtered()

        for item in securities:

            c = list(self.cutoff().keys())[0]
            rf = self.rfr
            mkt = self.market
            bi = beta(item, mkt)
            sri = specific_risk(item, mkt)
            erbi= erb(item, mkt, rf)

            w = (bi/sri) * (erbi - c)
            weights.append(w)

        return weights

    def shs_zip_props(self):

        s = self.filtered()
        w = self.adjusted_percent()

        self.final = dict(zip(map(Share, s), w))


class TreynorBlackPortfolio(WeightedPortfolio):
    """
    A concrete class for a portfolio object, which constructs an active
    portfolio of stock market shares by applying conthe Treynor-Black method of
    an equity portfolio construction. This is a procedure for constructing a
    portfolio of stocks identified to have non zero alpha.

    This class inherits functionality of the WeightedPortfolio abstract class
    and the latter is derived from the base class Portfolio.
    """

    def __init__(self, shares, mkt, rfr):
        """
        The class encapsulates portfolio information, specifically:
        *candidate shares passed to the class to form an active portfolio
        *the stock exchange market (market ticker,e.g FTSE100)where these shares
         are traded (it also acts as a benchmark for portfolio calculations)
        *the risk free rate for the portfolio
        *shares that form the final active portfolio and their proportions in it
        Parameters
        ----------
        :param shares: Share objects passed to the class to form a portfolio
        :param mkt: the market ticker (index), e.g. FTSE100
        :param rfr: the risk free rate of the portfolio
        :type shares: list[Share]
        :type mkt: Share
        :type rfr: float
        """
        super().__init__(shares, mkt, rfr)
        self.active_proportion_tb = 0

        #self.active_port()
        #shs_zip_props(self)

    @property
    def non_zero_alpha(self):
        """
        Checks that all candidate stocks have non zero alphas
        :return: Boolean
        """
        return all(alpha != 0 for alpha in self.shs_alphas)

    def unadjusted(self):
        """
        Calculates unadjusted (unnormalised) weights of shares in Treynor Black
        Portfolio. The formula to find the weight w of a security i is:

        wi = Ai / sri

        Ai - is Alpha of a share i
        sri - specific risk of a share i

        :return: unadjusted proportions of shares for the portfolio
        :rtype: list[float]
        """
        alf = self.shs_alphas
        risk = self.shs_specrisk

        if self.non_zero_alpha:  # if True
            index = 0
            nonadj = []

            while index < len(alf):

                w = alf[index] / risk[index]
                nonadj.append(w)
                index += 1

            return nonadj

        else:
            print("Some of the candidate securities' alphas are equal to zero.")
            return []







    # def adj_weight_percent(self):
    #
    #     weights_percent = [round((i * 100), 2) for i in self.adjusted()]
    #     return weights_percent
    #
    # def shs_zip_props(self):
    #     weights = self.adj_weight_percent()
    #     self.final_active_portfolio = dict(zip(map(Share, self.candidate_shares), weights))
    #
    #
    # def portfolio_alpha(self):
    #
    #     weights = self.adjusted()
    #     alphas = self.shares_alphas()
    #
    #     if len(weights) == len(alphas):
    #
    #         position = 0
    #         a = []
    #         while position < len(alphas):
    #             a.append(weights[position] * alphas[position])
    #             position += 1
    #
    #         return sum(a)
    #
    # def portfolio_beta(self):
    #
    #     betas = self.shares_betas()
    #     weights = self.adjusted()
    #
    #     if len(weights) == len(betas):
    #
    #         position = 0
    #         b = []
    #         while position < len(betas):
    #             b.append(weights[position] * betas[position])
    #             position += 1
    #
    #         return sum(b)
    #
    # def portfolio_specific_risk(self):
    #
    #     sr_shares = self.shares_specific_risk()
    #     weights = self.adjusted()
    #
    #     if len(weights) == len(sr_shares):
    #
    #         position = 0
    #         sr = []
    #         while position < len(sr_shares):
    #             sr.append(round(pow(weights[position], 2), 4) * round(sr_shares[position], 2))
    #             position += 1
    #
    #         return sum(sr)
    #
    # def active_port(self):
    #
    #     port_alpha = self.portfolio_alpha()
    #     port_beta = self.portfolio_beta()
    #     port_sp = self.portfolio_specific_risk()
    #     return_mkt = self.mkt_return()
    #     totrisk_mkt = self.mkt_risk()
    #
    #     w = (float(port_alpha) / float(port_sp)) / ((float(return_mkt) - float(self.risk_free_rate)) / float(totrisk_mkt))
    #
    #     w_tb = float(w) / (1 + (1 - float(port_beta)) * float(w))
    #
    #     self.active_proportion_tb = w_tb
    #
    #




s1 = ShareFactory.create('BRBY', '2015-09-30', '2016-08-31')
s2 = ShareFactory.create('TSCO', '2015-09-30', '2016-08-31')
s3 = ShareFactory.create('RBS', '2015-09-30', '2016-08-31')
s4 = ShareFactory.create('BP', '2015-09-30', '2016-08-31')


s5 = ShareFactory.create('RBS', '2009-01-01', '2015-07-31')
s6 = ShareFactory.create('AAL', '2009-01-01','2015-07-31')
s7 = ShareFactory.create('BRBY', '2009-01-01', '2015-07-31')
s8 = ShareFactory.create('BP', '2009-01-01', '2015-07-31')
s9 = ShareFactory.create('TSCO', '2009-01-01', '2015-07-31')
s10 = ShareFactory.create('SGE', '2009-01-01', '2015-07-31')


s11 = ShareFactory.create('ERM', '2009-01-01', '2014-12-31')
s12 = ShareFactory.create('AML', '2009-01-01', '2014-12-31')
s13 = ShareFactory.create('NG','2009-01-01', '2014-12-31')
s14 = ShareFactory.create('CGL', '2009-01-01', '2014-12-31')


mkt = ShareFactory.create('^FTSE', '2015-09-30', '2016-08-31')


rf = 1.5

shares = [s1,s2, s3, s4]

shares1 = [s11,s13, s14]

shares2 = [s5,s6, s7, s8]

p = TreynorBlackPortfolio(shares,mkt, rf)

print(p.candidates)
print()
#
#
# print()
#
#
# print(p.filtered())
#
print(p.unadjusted())
print()
print(p.adjusted())
print(sum(p.adjusted()))
#
# print()
#
# print(p.final)


