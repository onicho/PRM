from BusinessLogic.calculator import Calculator

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



#def portfolio_alpha(adjusted_weights, alphas):





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

