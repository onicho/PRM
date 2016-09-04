from logic.calculator import Calculator

c = Calculator()

def shares_alphas(lst_shares,mkt_prices, rf):
    alphas_lst = [c.alpha(i, mkt_prices, rf) for i in lst_shares]

    return alphas_lst


def shares_specific_risk(lst_shares,mkt_prices):
    risk_nums = [c.specific_risk(i, mkt_prices) for i in lst_shares]

    return risk_nums

def shares_betas(lst_shares,mkt_prices):
    betas_lst = [c.beta(i, mkt_prices) for i in lst_shares]
    return betas_lst

def mkt_return(mkt_prices):
    retmkt = c.annualise_as_percentage(c.average_return(c.return_on_share_prices(mkt_prices)))
    return retmkt


def mkt_risk(mkt_prices):
    riskmkt = c.total_risk(mkt_prices)
    return riskmkt

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
            sr.append(round(pow(adjusted_weights[position],2),4) * round(shares_spec_risk[position],2))
            position += 1

        return round(sum(sr), 2)


def active_port(port_alpha,port_sp,return_mkt,rf, totrisk_mkt):

    w = (float(port_alpha) / float(port_sp)) / ((float(return_mkt) - float(rf)) / float(totrisk_mkt))

    return round(w, 2)


def tb_active_port(weight_act_port,beta_port):

    w_tb = float(weight_act_port) / (1 + (1 - float(beta_port)) * float(weight_act_port))

    return round(w_tb, 2)







##########################################
array1 = []

with open("ERMprices.txt", "r") as ins:
    for line in ins:
        array1.append(line.rstrip('\n').rstrip('\r'))

ERMprices = [float(i) for i in array1]

arrayMKT = []

with open("MKTprices.txt", "r") as ins:
    for line in ins:
        arrayMKT.append(line.rstrip('\n').rstrip('\r'))

MKTprices = [float(i) for i in arrayMKT]

array2 = []

with open("CGLprices.txt", "r") as ins:
    for line in ins:
        array2.append(line.rstrip('\n').rstrip('\r'))

CGLprices = [float(i) for i in array2]

array3 = []

with open("AMLprices.txt", "r") as ins:
    for line in ins:
        array3.append(line.rstrip('\n').rstrip('\r'))

AMLprices = [float(i) for i in array3]

array4 = []

with open("NGprices.txt", "r") as ins:
    for line in ins:
        array4.append(line.rstrip('\n').rstrip('\r'))

NGprices = [float(i) for i in array4]

###########################################

test = shares_alphas([ERMprices, CGLprices, NGprices], MKTprices, 1.5)

print(test)
print()

test1 = shares_specific_risk([ERMprices, CGLprices, NGprices], MKTprices)

print(test1)
print()

test2 = shares_betas([ERMprices, CGLprices, NGprices], MKTprices)

print(test2)
print()

test3 = non_zero_alpha(test)

print(test3)
print()

test4 = unadjust_weights(test,test1,test3)
print(test4)
print()

test5 = adjust_weights(test4)
print(test5)
print()

test6 = adj_weight_percent(test5)
print(test6)
print()

test7 = portfolio_alpha(test5, test)
print(test7)
print()

test8 = portfolio_beta(test5, test2)
print(test8)
print()

test9 = portfolio_specific_risk(test5, test1)
print(test9)
print()

test10 = mkt_return(MKTprices)
print(test10)
print()

test11 = mkt_risk(MKTprices)
print(test11)
print()

test12 = active_port(test7,test9,test10,1.5,test11)
print(test12)

test13 = tb_active_port(test12, test8)
print(test13)