
class Portfolio:

    def __init__(self, lst_of_shares):
        self.candidate_shares = lst_of_shares
        self.optimal_active_portf = []

from logic.calculator import *
from collections import *

c = Calculator()


def order_by_erb(lst2d_shareprices, rf, mkt_prices):
    erbs_shares = {}

    for i in lst2d_shareprices:
        erbs_shares[c.erb(i, mkt_prices, rf)] = i

    ordered_shares = [item[1] for item in sorted(erbs_shares.items(), reverse=True)]

    return ordered_shares


def cut_off_rate(lst_shares, rf, mkt_prices):
    index = 0
    num_components = []

    for item in lst_shares:

        while index <= lst_shares.index(item):
            num_components.append(
                float((c.annualise(c.average(c.returns(lst_shares[index])))) - rf) * \
                float(c.beta(lst_shares[index], mkt_prices)) / \
                float(c.s_risk(lst_shares[index], mkt_prices))
            )
            index += 1

    count = 0
    denom_components = []

    for item in lst_shares:

        while count <= lst_shares.index(item):
            denom_components.append(
                float(pow(c.beta(lst_shares[count], mkt_prices), 2)) / \
                float(c.s_risk(lst_shares[count], mkt_prices))
            )
            count += 1

    co_rates = []

    for share in lst_shares:
        n = len(lst_shares) - (lst_shares.index(share) + 1)

        num_element = num_components[
                      :-n or None]  # to remove the last N elements of a list.

        den_element = denom_components[:-n or None]

        var_mkt = c.t_risk(mkt_prices)

        cof = round(float((var_mkt * sum(num_element)) / \
                          (1 + var_mkt * (sum(den_element)))), 2)

        co_rates.append(cof)

    erbs_shares = []

    for i in lst_shares:
        erbs_shares.append(c.erb(i, mkt_prices, rf))

    cof_rate = {}
    item_index = 0
    found = False

    while not found and item_index < len(co_rates):
        if co_rates[item_index] <= erbs_shares[item_index + 1]:
            item_index += 1
        else:
            cof_rate = {co_rates[item_index]: item_index}
            found = True

    return cof_rate, co_rates, len(lst_shares)


def cor_filter_shares_portf(lst_shares, cof_index):
    n = (list(cof_index.values()))[0] + 1

    filtered_shares = lst_shares[: n]

    return filtered_shares


def unadjusted_weights(lst_shares, mkt_prices, cof_index, rf):
    cof = list(cof_index.keys())[0]

    unadj_weights = []

    for i in lst_shares:
        w = (
            float((c.beta(i, mkt_prices) / c.s_risk(i, mkt_prices))) *

            (float(c.erb(i, mkt_prices, rf)) - float(cof))
        )
        unadj_weights.append(w)

    return unadj_weights


def normalised_weights(unadj_weights):
    sum_of_weights = sum(unadj_weights).round(6)

    norm_weights = []

    for i in unadj_weights:
        norm_weights.append(i / sum_of_weights)

    return norm_weights


def norm_weight_percent(norm_weights):
    weights_percent = [round((i * 100), 2) for i in norm_weights]

    return weights_percent





