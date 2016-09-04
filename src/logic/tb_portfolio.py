from logic.calculator import Calculator

c = Calculator()


def shares_alphas(lst_shares, mkt_prices, rf):
    alphas_lst = [c.alpha(i, mkt_prices, rf) for i in lst_shares]
    return alphas_lst


def shares_specific_risk(lst_shares, mkt_prices):
    risk_nums = [c.specific_risk(i, mkt_prices) for i in lst_shares]

    return risk_nums


def shares_betas(lst_shares, mkt_prices):
    betas_lst = [c.beta(i, mkt_prices) for i in lst_shares]
    return betas_lst


def mkt_return(mkt_prices):
    retmkt = c.annualise_as_percentage(c.average_return(c.return_on_share_prices(mkt_prices)))
    return retmkt


def mkt_risk(mkt_prices):
    riskmkt = c.total_risk(mkt_prices)
    return riskmkt


##################################################################################

def non_zero_alpha(alphas_lst):
    return all(alpha != 0 for alpha in alphas_lst)


def unadjust_weights(alphas, specific_risk, bool):
    if bool:

        index = 0
        unadj_w = []

        while index < len(alphas):
            w = alphas[index] / specific_risk[index]
            unadj_w.append(w)
            index += 1

        return unadj_w

    else:
        pass


def adjust_weights(unadj_weights):
    adj_w = [float(i / sum(unadj_weights)) for i in unadj_weights]

    return adj_w


def adj_weight_percent(adjusted_weights):
    weights_percent = [round((i * 100), 2) for i in adjusted_weights]

    return weights_percent


def portfolio_alpha(adjusted_weights, alphas):
    if len(adjusted_weights) == len(alphas):

        position = 0
        a = []
        while position < len(alphas):
            a.append(adjusted_weights[position] * alphas[position])
            position += 1

        return round(sum(a), 2)


def portfolio_beta(adjusted_weights, betas):
    if len(adjusted_weights) == len(betas):

        position = 0
        b = []
        while position < len(betas):
            b.append(adjusted_weights[position] * betas[position])
            position += 1

        return round(sum(b), 2)


def portfolio_specific_risk(adjusted_weights, shares_spec_risk):
    if len(adjusted_weights) == len(shares_spec_risk):

        position = 0
        sr = []
        while position < len(shares_spec_risk):
            sr.append(round(pow(adjusted_weights[position], 2), 4) * round(shares_spec_risk[position], 2))
            position += 1

        return round(sum(sr), 2)


def active_port(port_alpha, port_sp, return_mkt, rf, totrisk_mkt):
    w = (float(port_alpha) / float(port_sp)) / ((float(return_mkt) - float(rf)) / float(totrisk_mkt))

    return round(w, 2)


def tb_active_port(weight_act_port, beta_port):
    w_tb = float(weight_act_port) / (1 + (1 - float(beta_port)) * float(weight_act_port))

    return round(w_tb, 2)


