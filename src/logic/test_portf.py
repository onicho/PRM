"""
This module contains classes that can be used to create Portfolio objects, which
represent a portfolio of stock market shares.
"""
from abc import abstractmethod, ABCMeta
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

    __metaclass__ = ABCMeta

    def __init__(self, shares, market, rfr):
        super().__init__(shares, market, rfr)
        self.final = {}

    @abstractmethod
    def unadjusted(self):
        raise NotImplementedError

    @abstractmethod
    def adjusted(self):
        raise NotImplementedError

    @abstractmethod
    def adjusted_percent(self):
        raise NotImplementedError
        # percents = [round((i * 100), 2) for i in self.adjusted()]
        # return percents

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
        #self.shs_zip_props()


# # START HERE!
#     def ordered(self):
#         """
#
#         :return:
#         """
#
#         erbs_shares = {}
#
#         for share in self.candidate_shares:
#             erbs_shares[c.erb(share.historical_prices, self.mkt_ticker.historical_prices, self.risk_free_rate)] = share
#
#         ordered_shares = [item[1] for item in sorted(erbs_shares.items(), reverse=True)]
#         return ordered_shares
#
#
#
#
#
#
#
#
#
#     def cut_off_rate(self):
#
#         index = 0
#         num_components = []
#         shares = self.ordered()
#
#         for item in shares:
#
#             while index <= shares.index(item):
#                 # annualised(returns - rfr * beta / specific_risk)
#                 rets = c.returns(...)
#                 beta = c.beta(...)
#                 risk = c.s_risk(...)
#                 value = annualise(average(rets - rfr) * beta / risk)
#                 num_components.append(
#                     float((c.annualise(
#                         c.average(
#                             c.returns(shares[index].historical_prices)))) - self.risk_free_rate) * \
#                     float(c.beta(shares[index].historical_prices, self.mkt_ticker.historical_prices)) / \
#                     float(c.s_risk(shares[index].historical_prices, self.mkt_ticker.historical_prices))
#                 )
#                 index += 1
#
#         count = 0
#         denom_components = []
#
#         for item in shares:
#
#             while count <= shares.index(item):
#                 denom_components.append(
#                     float(pow(c.beta(shares[count].historical_prices, self.mkt_ticker.historical_prices), 2)) / \
#                     float(c.s_risk(shares[count].historical_prices, self.mkt_ticker.historical_prices))
#                 )
#                 count += 1
#
#         co_rates = []
#
#         for share in shares:
#             n = len(shares) - (shares.index(share) + 1)
#
#             num_element = num_components[
#                           :-n or None]  # to remove the last N elements of a list.
#
#             den_element = denom_components[:-n or None]
#
#             var_mkt = c.t_risk(self.mkt_ticker.historical_prices)
#
#             cof = round(float((var_mkt * sum(num_element)) / \
#                               (1 + var_mkt * (sum(den_element)))), 2)
#
#             co_rates.append(cof)
#
#         erbs_shares = []
#
#         for one_share in shares:
#             erbs_shares.append(
#                 c.erb(one_share.historical_prices, self.mkt_ticker.historical_prices, self.risk_free_rate))
#
#         cof_rate = {}
#         item_index = 0
#         found = False
#
#         while not found and item_index < len(co_rates):
#             if co_rates[item_index] <= erbs_shares[item_index + 1]:
#                 item_index += 1
#             else:
#                 cof_rate = {co_rates[item_index]: item_index}
#                 found = True
#
#         return cof_rate  # co_rates, len(ordered_shares)
#
#     def shares_filter(self):
#
#         rate = self.cut_off_rate()
#         n = (list(rate.values()))[0] + 1
#
#         shares = self.ordered()
#         filtered_shares = shares[: n]
#
#         return filtered_shares
#
#
#
#
#     def unadjusted(self):
#
#         rate = self.cut_off_rate()
#         cof = list(rate.keys())[0]
#
#         unadj_weights = []
#         filtered_shares = self.shares_filter()
#
#         for item in filtered_shares:
#             w = (
#                 float((c.beta(item.historical_prices, self.mkt_ticker.historical_prices) / c.s_risk(
#                     item.historical_prices, self.mkt_ticker.historical_prices))) *
#
#                 (float(c.erb(item.historical_prices, self.mkt_ticker.historical_prices, self.risk_free_rate)) - float(
#                     cof))
#             )
#             unadj_weights.append(w)
#
#         return unadj_weights
#
#
#
#
#
#     def adjusted(self):
#
#         weights = self.unadjusted()
#         sum_of_weights = sum(weights)
#
#         norm_weights = []
#
#         for i in weights:
#             norm_weights.append(i / sum_of_weights)
#
#         return norm_weights
#
#
#
#     def adjusted_percent(self):
#         weights_percent = [round((i * 100), 2) for i in self.adjusted()]
#
#         return weights_percent
#
#
#
#     def shs_zip_props(self):
#         shares = self.shares_filter()
#         weights = self.adjusted_percent()
#         self.final = dict(zip(map(Share, shares), weights))
#
#











s1 = ShareFactory.create('ERM', '2009-01-01', '2014-12-31')
s2 = ShareFactory.create('AML', '2009-01-01', '2014-12-31')
s3 = ShareFactory.create('CGL', '2009-01-01', '2014-12-31')
s4 = ShareFactory.create('NG', '2009-01-01', '2014-12-31')
mkt = ShareFactory.create('^FTSE', '2009-01-01', '2014-12-31')
rf = 1.5
shares = [s1, s2, s3, s4]

p = EltonGruberPortfolio(shares,mkt, rf)

print(p.mkt_return)

#print(p.adjusted())








#
#
# class TreynorBlackPortfolio(Portfolio):
#     def __init__(self, lst_of_shares, market_ticker, rfr):
#
#         super().__init__(lst_of_shares, market_ticker, rfr)
#         self.final_active_portfolio = {}
#         self.active_proportion_tb = 0
#         self.zip_shares_proportions()
#         self.active_port()
#
#     def non_zero_alpha(self):
#         return all(alpha != 0 for alpha in self.shares_alphas())
#
#     def unadjusted_weights(self):
#
#         alphas = self.shares_alphas()
#         non_zero = self.non_zero_alpha()
#         sp_risk = self.shares_specific_risk()
#
#         if non_zero:
#
#             index = 0
#             unadj_w = []
#
#             while index < len(alphas):
#                 w = alphas[index] / sp_risk[index]
#                 unadj_w.append(w)
#                 index += 1
#             return unadj_w
#         else:
#             print("Some of the candidate securities' alphas are equal to zero.")
#
#     def adjusted_weights(self):
#
#         weights = self.unadjusted_weights()
#         adj_w = [float(w / sum(weights)) for w in weights]
#         return adj_w
#
#     def adj_weight_percent(self):
#
#         weights_percent = [round((i * 100), 2) for i in self.adjusted_weights()]
#         return weights_percent
#
#     def zip_shares_proportions(self):
#         weights = self.adj_weight_percent()
#         self.final_active_portfolio = dict(zip(map(Share, self.candidate_shares), weights))
#
#     def portfolio_alpha(self):
#
#         weights = self.adjusted_weights()
#         alphas = self.shares_alphas()
#
#         if len(weights) == len(alphas):
#
#             position = 0
#             a = []
#             while position < len(alphas):
#                 a.append(weights[position] * alphas[position])
#                 position += 1
#
#             return sum(a)
#
#     def portfolio_beta(self):
#
#         betas = self.shares_betas()
#         weights = self.adjusted_weights()
#
#         if len(weights) == len(betas):
#
#             position = 0
#             b = []
#             while position < len(betas):
#                 b.append(weights[position] * betas[position])
#                 position += 1
#
#             return sum(b)
#
#     def portfolio_specific_risk(self):
#
#         sr_shares = self.shares_specific_risk()
#         weights = self.adjusted_weights()
#
#         if len(weights) == len(sr_shares):
#
#             position = 0
#             sr = []
#             while position < len(sr_shares):
#                 sr.append(round(pow(weights[position], 2), 4) * round(sr_shares[position], 2))
#                 position += 1
#
#             return sum(sr)
#
#     def active_port(self):
#
#         port_alpha = self.portfolio_alpha()
#         port_beta = self.portfolio_beta()
#         port_sp = self.portfolio_specific_risk()
#         return_mkt = self.mkt_return()
#         totrisk_mkt = self.mkt_risk()
#
#         w = (float(port_alpha) / float(port_sp)) / ((float(return_mkt) - float(self.risk_free_rate)) / float(totrisk_mkt))
#
#         w_tb = float(w) / (1 + (1 - float(port_beta)) * float(w))
#
#         self.active_proportion_tb = w_tb
