from numpy import *
import statistics


class Calculator(object):

    def __init__(self):
        self.name = "Share evaluation calculator"

    def __repr__(self):
        self.repr_name = "Calculator"

    def __str__(self):
        self.str_name = "Calculator"


    @staticmethod
    def average_return(list_of_prices):
        ar_result = float(sum(list_of_prices) / len(list_of_prices))
        return ar_result

    @staticmethod
    def return_on_share_prices(list_of_hist_prices):
        rs_result = []
        position = 0

        while position < len(list_of_hist_prices) - 1:
            r = float(
                (list_of_hist_prices[position + 1] / list_of_hist_prices[position]) - 1)     # format(..., '.5f')  # !!!!! check
            rs_result.append(r)
            position += 1

        return rs_result

    def standard_deviation(self, list_of_hist_prices):
        # NB: stdev  == excel stdev.p!!! numpy gives you stdev.s!!

        sd = statistics.stdev([float(round(item, 9)) for item in self.return_on_share_prices(list_of_hist_prices)])

        return float(self.annualise_as_percentage(sd))

    @staticmethod
    def annualise_as_percentage(num):
        annualised_num = num * 12 * 100
        return annualised_num

    @staticmethod
    def correlation_coefficent(list_of_shares):
        lists_of_prices_to_correlate = []

        if len(list_of_shares) > 1:

            for share in list_of_shares:
                lists_of_prices_to_correlate.append(share.get_historical_prices())
            correlations = corrcoef(lists_of_prices_to_correlate)
            return correlations

        else:
            print("Insufficient number of shares to perform correlation " +
                  " (minimum 2 required, but %(num)d were provided)" % {"num": len(list_of_shares)})

    def beta(self, lst_share_prices, lst_market_prices):
        # cov(x,y)/ var(y)
        # ddof=0`` provides a maximum likelihood estimate of the variance for normally distributed variables(ref!!!)

        returns_share = [float(round(item, 9)) for item in self.return_on_share_prices(lst_share_prices)]
        returns_market = [float(round(item, 9)) for item in self.return_on_share_prices(lst_market_prices)]

        beta_result = float((cov(returns_share, returns_market, ddof=0)[0][1]) /
                            (var(returns_market)))

        return beta_result #round(beta_result, 2)

    def alpha(self, lst_hist_prices_share, lst_hist_prices_market, rf):
        # Alpha %  --> α = Rs – [Rf + (Rm – Rf) β]

        returns_share = [float(round(item, 9)) for item in self.return_on_share_prices(lst_hist_prices_share)]
        rs = self.annualise_as_percentage(self.average_return(returns_share))

        returns_market = [float(round(item, 9)) for item in self.return_on_share_prices(lst_hist_prices_market)]
        rm = self.annualise_as_percentage(self.average_return(returns_market))

        beta_s = self.beta(lst_hist_prices_share, lst_hist_prices_market)

        alpha_s = rs - (rf + (rm - rf) * beta_s)

        return round(alpha_s, 2)

    def erb(self, lst_share_prices, lst_market_prices, rf):
        # ERB --> Treynor ratio = (Rs – Rf) ÷ β

        rs = self.annualise_as_percentage(
            self.average_return([float(round(item, 9)) for item in self.return_on_share_prices(lst_share_prices)]))

        erb_result = float((rs - rf) / self.beta(lst_share_prices, lst_market_prices))

        return round(erb_result, 2)

    def total_risk(self, lst_hist_prices):
        tr = pow(self.standard_deviation(lst_hist_prices), 2)
        return tr

    def specific_risk(self,share_histprices, market_histprices):

        sr = float(self.total_risk(share_histprices) - (pow(self.beta(share_histprices, market_histprices), 2) *
                                                  self.total_risk(market_histprices)))

        return sr








