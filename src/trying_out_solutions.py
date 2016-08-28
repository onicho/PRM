from BusinessLogic.calculator import Calculator

c = Calculator()


def non_zero_alpha(lst_shares, mkt_prices, rf):
    alphas = [c.alpha(i, mkt_prices, rf) for i in lst_shares]

    return all(alpha != 0 for alpha in alphas)


def unadjust_weights(lst_shares, mkt_prices, rf, bool):
    if bool:
        systematic_risk_nums = [c.specific_risk(i, mkt_prices) for i in lst_shares]

        alphas = [c.alpha(i, mkt_prices, rf) for i in lst_shares]

        index = 0
        unadj_w = []

        while index < len(lst_shares):
            w = alphas[index] / systematic_risk_nums[index]
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

test = non_zero_alpha([ERMprices, CGLprices, NGprices], MKTprices, 1.5)

print(test)
print()

test2 = unadjust_weights([ERMprices, CGLprices, NGprices], MKTprices, 1.5, test)

for i in test2:
    print(i)
print()

test3 = adjust_weights(test2)

for i in test3:
    print(i)

test4 = adj_weight_percent(test3)

print(test4)