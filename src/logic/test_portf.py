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

    def unadjusted_weights(self):
        pass

    def adjusted_weights(self):
        pass


class EltonGruberPortfolio(Portfolio):

    def __init__(self, lst_of_shares, market_ticker, rfr):

        super().__init__(lst_of_shares, market_ticker, rfr)

        """
        self.candidate_shares = lst_of_shares
        self.risk_free_rate = rfr
        self.mkt_ticker = market_ticker

        """
        self.final_active_portfolio = {}
        self.zip_shares_proportions()

    def order_by_erb(self):

        erbs_shares = {}

        for share in self.candidate_shares:
            erbs_shares[c.erb(share.historical_prices, self.mkt_ticker.historical_prices, self.risk_free_rate)] = share

        ordered_shares = [item[1] for item in sorted(erbs_shares.items(), reverse=True)]
        return ordered_shares

    def cut_off_rate(self):

        index = 0
        num_components = []
        shares = self.order_by_erb()

        for item in shares:

            while index <= shares.index(item):
                num_components.append(
                    float((c.annualise_as_percentage(
                        c.average_return(
                            c.return_on_share_prices(shares[index].historical_prices)))) - self.risk_free_rate) * \
                    float(c.beta(shares[index].historical_prices, self.mkt_ticker.historical_prices)) / \
                    float(c.specific_risk(shares[index].historical_prices, self.mkt_ticker.historical_prices))
                )
                index += 1

        count = 0
        denom_components = []

        for item in shares:

            while count <= shares.index(item):
                denom_components.append(
                    float(pow(c.beta(shares[count].historical_prices, self.mkt_ticker.historical_prices), 2)) / \
                    float(c.specific_risk(shares[count].historical_prices, self.mkt_ticker.historical_prices))
                )
                count += 1

        co_rates = []

        for share in shares:
            n = len(shares) - (shares.index(share) + 1)

            num_element = num_components[
                          :-n or None]  # to remove the last N elements of a list.

            den_element = denom_components[:-n or None]

            var_mkt = c.total_risk(self.mkt_ticker.historical_prices)

            cof = round(float((var_mkt * sum(num_element)) / \
                              (1 + var_mkt * (sum(den_element)))), 2)

            co_rates.append(cof)

        erbs_shares = []

        for one_share in shares:
            erbs_shares.append(
                c.erb(one_share.historical_prices, self.mkt_ticker.historical_prices, self.risk_free_rate))

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

    def shares_filter(self):

        rate = self.cut_off_rate()
        n = (list(rate.values()))[0] + 1

        shares = self.order_by_erb()
        filtered_shares = shares[: n]

        return filtered_shares

    def unadjusted_weights(self):

        rate = self.cut_off_rate()
        cof = list(rate.keys())[0]

        unadj_weights = []
        filtered_shares = self.shares_filter()

        for item in filtered_shares:
            w = (
                float((c.beta(item.historical_prices, self.mkt_ticker.historical_prices) / c.specific_risk(
                    item.historical_prices, self.mkt_ticker.historical_prices))) *

                (float(c.erb(item.historical_prices, self.mkt_ticker.historical_prices, self.risk_free_rate)) - float(
                    cof))
            )
            unadj_weights.append(w)

        return unadj_weights

    def adjusted_weights(self):

        weights = self.unadjusted_weights()
        sum_of_weights = sum(weights)

        norm_weights = []

        for i in weights:
            norm_weights.append(i / sum_of_weights)

        return norm_weights

    def weights_percent(self):
        weights_percent = [round((i * 100), 2) for i in self.adjusted_weights()]

        return weights_percent

    def zip_shares_proportions(self):
        shares = self.shares_filter()
        weights = self.weights_percent()
        self.final_active_portfolio = dict(zip(map(Share, shares), weights))
























class TreynorBlackPortfolio(Portfolio):
    def __init__(self, lst_of_shares, market_ticker, rfr):

        super().__init__(lst_of_shares, market_ticker, rfr)
        self.final_active_portfolio = []
        self.active_proportion_tb = 0

    @staticmethod
    def non_zero_alpha(alphas_lst):
        return all(alpha != 0 for alpha in alphas_lst)

    @staticmethod
    def unadjusted_weights(alphas, specific_risk, bool):
        if bool:

            index = 0
            unadj_w = []

            while index < len(alphas):
                w = alphas[index] / specific_risk[index]
                unadj_w.append(w)
                index += 1

            return unadj_w

        else:
            print("Some of the candidate securities' alphas are equal to zero.")

    @staticmethod
    def adjusted_weights(unadj_weights):
        adj_w = [float(i / sum(unadj_weights)) for i in unadj_weights]

        return adj_w

    @staticmethod
    def adj_weight_percent(adjusted_weights):
        weights_percent = [round((i * 100), 2) for i in adjusted_weights]

        return weights_percent

    def zip_shares_proportions(self, candidate_shares, adj_weight_percent):
        self.final_active_portfolio = dict(zip(map(Share, candidate_shares), adj_weight_percent))

    @staticmethod
    def portfolio_alpha(adjusted_weights, alphas):
        if len(adjusted_weights) == len(alphas):

            position = 0
            a = []
            while position < len(alphas):
                a.append(adjusted_weights[position] * alphas[position])
                position += 1

            return sum(a)

    @staticmethod
    def portfolio_beta(adjusted_weights, betas):
        if len(adjusted_weights) == len(betas):

            position = 0
            b = []
            while position < len(betas):
                b.append(adjusted_weights[position] * betas[position])
                position += 1

            return sum(b)

    @staticmethod
    def portfolio_specific_risk(adjusted_weights, shares_spec_risk):
        if len(adjusted_weights) == len(shares_spec_risk):

            position = 0
            sr = []
            while position < len(shares_spec_risk):
                sr.append(round(pow(adjusted_weights[position], 2), 4) * round(shares_spec_risk[position], 2))
                position += 1

            return sum(sr)

    def active_port(self, port_alpha, port_beta, port_sp, return_mkt, rf, totrisk_mkt):

        w = (float(port_alpha) / float(port_sp)) / ((float(return_mkt) - float(rf)) / float(totrisk_mkt))

        w_tb = float(w) / (1 + (1 - float(port_beta)) * float(w))

        self.active_proportion_tb = w_tb
