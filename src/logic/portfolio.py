from logic.calculator import Calculator
from logic.share import Share

c = Calculator()


class Portfolio(object):
    def __init__(self, lst_of_shares, market_ticker, rfr):
        self.candidate_shares = lst_of_shares
        self.risk_free_rate = rfr
        self.mkt_ticker = market_ticker

    @staticmethod
    def shares_alphas(candidate_shares, mkt_ticker, rfr):
        alphas_lst = [c.alpha(share.historical_prices, mkt_ticker.historical_prices, rfr) for share in
                      candidate_shares]

        return alphas_lst

    @staticmethod
    def shares_specific_risk(candidate_shares, mkt_ticker):
        risk_nums = [c.specific_risk(share.historical_prices, mkt_ticker.historical_prices) for share in
                     candidate_shares]

        return risk_nums

    @staticmethod
    def shares_betas(candidate_shares, mkt_ticker):
        betas_lst = [c.beta(share.historical_prices, mkt_ticker.historical_prices) for share in candidate_shares]

        return betas_lst

    @staticmethod
    def mkt_return(mkt_ticker):
        retmkt = c.annualise_as_percentage(c.average_return(c.return_on_share_prices(mkt_ticker.historical_prices)))
        return retmkt

    @staticmethod
    def mkt_risk(mkt_ticker):
        riskmkt = c.total_risk(mkt_ticker.historical_prices)
        return riskmkt


class EltonGruberPortfolio(Portfolio):

    def __init__(self, lst_of_shares, market_ticker, rfr):

        super().__init__(lst_of_shares, market_ticker, rfr)
        self.final_active_portfolio = {}

    @staticmethod
    def order_by_erb(candidate_shares, risk_free_rate, mkt_ticker):
        erbs_shares = {}

        for i in candidate_shares:
            erbs_shares[c.erb(i.historical_prices, mkt_ticker.historical_prices, risk_free_rate)] = i

        ordered_shares = [item[1] for item in sorted(erbs_shares.items(), reverse=True)]
        return ordered_shares

    @staticmethod
    def cut_off_rate(ordered_shares, rf, mkt_ticker):
        index = 0
        num_components = []

        for item in ordered_shares:

            while index <= ordered_shares.index(item):
                num_components.append(
                    float((c.annualise_as_percentage(
                        c.average_return(c.return_on_share_prices(ordered_shares[index].historical_prices)))) - rf) * \
                    float(c.beta(ordered_shares[index].historical_prices, mkt_ticker.historical_prices)) / \
                    float(c.specific_risk(ordered_shares[index].historical_prices, mkt_ticker.historical_prices))
                )
                index += 1

        count = 0
        denom_components = []

        for item in ordered_shares:

            while count <= ordered_shares.index(item):
                denom_components.append(
                    float(pow(c.beta(ordered_shares[count].historical_prices, mkt_ticker.historical_prices), 2)) / \
                    float(c.specific_risk(ordered_shares[count].historical_prices, mkt_ticker.historical_prices))
                )
                count += 1

        co_rates = []

        for share in ordered_shares:
            n = len(ordered_shares) - (ordered_shares.index(share) + 1)

            num_element = num_components[
                          :-n or None]  # to remove the last N elements of a list.

            den_element = denom_components[:-n or None]

            var_mkt = c.total_risk(mkt_ticker.historical_prices)

            cof = round(float((var_mkt * sum(num_element)) / \
                              (1 + var_mkt * (sum(den_element)))), 2)

            co_rates.append(cof)

        erbs_shares = []

        for one_share in ordered_shares:
            erbs_shares.append(c.erb(one_share.historical_prices, mkt_ticker.historical_prices, rf))

        cof_rate = {}
        item_index = 0
        found = False

        while not found and item_index < len(co_rates):
            if co_rates[item_index] <= erbs_shares[item_index + 1]:
                item_index += 1
            else:
                cof_rate = {co_rates[item_index]: item_index}
                found = True

        return cof_rate  # co_rates, len(ordered_shares)

    @staticmethod
    def cor_filter_shares_portf(ordered_shares, cof_index):
        n = (list(cof_index.values()))[0] + 1

        filtered_shares = ordered_shares[: n]

        return filtered_shares

    @staticmethod
    def unadjusted_weights(filtered_shares, mkt_ticker, cof_index, rf):
        cof = list(cof_index.keys())[0]

        unadj_weights = []

        for item in filtered_shares:
            w = (
                float((c.beta(item.historical_prices, mkt_ticker.historical_prices) / c.specific_risk(
                    item.historical_prices, mkt_ticker.historical_prices))) *

                (float(c.erb(item.historical_prices, mkt_ticker.historical_prices, rf)) - float(cof))
            )
            unadj_weights.append(w)

        return unadj_weights

    @staticmethod
    def normalised_weights(unadj_weights):
        sum_of_weights = sum(unadj_weights)

        norm_weights = []

        for i in unadj_weights:
            norm_weights.append(i / sum_of_weights)

        return norm_weights

    @staticmethod
    def norm_weight_percent(norm_weights):
        weights_percent = [round((i * 100), 2) for i in norm_weights]

        return weights_percent

    def zip_shares_proportions(self, filtered_shares, norm_weight_percent):
        self.final_active_portfolio = dict(zip(map(Share, filtered_shares), norm_weight_percent))


class TreynorBlackPortfolio(Portfolio):

    def __init__(self, lst_of_shares, market_ticker, rfr):

        super().__init__(lst_of_shares, market_ticker, rfr)
        self.final_active_portfolio = []


