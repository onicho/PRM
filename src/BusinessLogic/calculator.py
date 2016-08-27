from numpy import *
import statistics


class Calculator(object):

    def __init__(self):
        self.name = "Share evaluation calculator"

    def __repr__(self):
        self.repr_name = "Calculator"


    @staticmethod
    def average_return(list_of_nums):
        ar_result = float(sum(list_of_nums) / len(list_of_nums))
        return ar_result

    @staticmethod
    def return_on_share_prices(list_of_prices):
        rs_result = []
        position = 0

        while position < len(list_of_prices) - 1:
            r = float(
                (list_of_prices[position + 1] / list_of_prices[position]) - 1)  # format(..., '.5f')  # !!!!! check
            rs_result.append(r)
            position += 1

        return rs_result

    @staticmethod
    def standard_deviation(list_of_num):
        # NB: stdev  == excel stdev.p!!! numpy gives you stdev.s!!
        sd_result = statistics.stdev(list_of_num)
        return sd_result

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

        return beta_result#round(beta_result, 2)

    def alpha(self, lst_hist_prices_share, lst_hist_prices_market, rf):
        # Alpha %  --> α = Rs – [Rf + (Rm – Rf) β]

        returns_share = [float(round(item, 9)) for item in self.return_on_share_prices(lst_hist_prices_share)]
        rs = self.annualise_as_percentage(self.average_return(returns_share))

        returns_market = [float(round(item, 9)) for item in self.return_on_share_prices(lst_hist_prices_market)]
        rm = self.annualise_as_percentage(self.average_return(returns_market))

        beta_s = self.beta(returns_share, returns_market)

        alpha_s = rs - (rf + (rm - rf) * beta_s)

        return round(alpha_s, 2)

    def erb(self, lst_share_prices, lst_market_prices, rf):
        # ERB --> Treynor ratio = (Rs – Rf) ÷ β

        rs = self.annualise_as_percentage(
            self.average_return([float(round(item, 9)) for item in self.return_on_share_prices(lst_share_prices)]))

        erb_result = float((rs - rf) / self.beta(lst_share_prices, lst_market_prices))

        return round(erb_result, 2)

    def total_risk(self):




