from BusinessLogic.calculator import *
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
                float((c.annualise_as_percentage(c.average_return(c.return_on_share_prices(lst_shares[index])))) - rf) * \
                float(c.beta(lst_shares[index], mkt_prices)) / \
                float(c.specific_risk(lst_shares[index], mkt_prices))
            )
            index += 1

    count = 0
    denom_components = []

    for item in lst_shares:

        while count <= lst_shares.index(item):
            denom_components.append(
                float(pow(c.beta(lst_shares[count], mkt_prices), 2)) / \
                float(c.specific_risk(lst_shares[count], mkt_prices))
            )
            count += 1

    co_rates = []

    for share in lst_shares:
        n = len(lst_shares) - (lst_shares.index(share) + 1)

        num_element = num_components[:-n or None]  # to remove the last N elements of a list.

        den_element = denom_components[:-n or None]

        var_mkt = c.total_risk(mkt_prices)

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
              float((c.beta(i, mkt_prices) / c.specific_risk(i, mkt_prices))) *

              (float(c.erb(i,mkt_prices,rf)) - float(cof))
        )
        unadj_weights.append(w)


    return unadj_weights


def normalised_weights(unadj_weights):

    sum_of_weights = sum(unadj_weights).round(6)

    norm_weights = []

    for i in unadj_weights:
        norm_weights.append(i/sum_of_weights)


    return norm_weights





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

testlist = order_by_erb([NGprices, AMLprices, ERMprices, CGLprices], 1.5, MKTprices)

test = cut_off_rate(testlist, 1.5, MKTprices)

for i in test:
    print(i)

# print(test)



test2 = cor_filter_shares_portf(testlist, {7.35: 2})

for i in test2:
    print(i)

test3 = unadjusted_weights(test2,MKTprices,{7.35: 2},1.5)
print(test3)


test4 = normalised_weights(test3)

print(test4)


#############################################









































"""

#tests

array1 = []

with open("values1.txt", "r") as ins:
    for line in ins:
        array1.append(line.rstrip('\n').rstrip('\r'))
array2 = []

with open("values2.txt", "r") as ins:
    for line in ins:
        array2.append(line.rstrip('\n').rstrip('\r'))
array3 = []

with open("values3.txt", "r") as ins:
    for line in ins:
        array3.append(line.rstrip('\n').rstrip('\r'))
arrayMKT = []

with open("MKTvalues.txt", "r") as ins:
    for line in ins:
        arrayMKT.append(line.rstrip('\n').rstrip('\r'))

values3 = [float(i) for i in array3]
values1 = [float(i) for i in array1]
values2 = [float(i) for i in array2]
MKTvalues = [float(i) for i in arrayMKT]

print(beta(MKTvalues, MKTvalues))


#########################

 erbs = []

 for i in lst2d_shareprices:
     erbs.append(c.erb(i,mkt_prices, rf))

 erbs.sort(reverse=True)

 sorted_erb_shares = []

 for i in lst2d_shareprices:

     position = 0
     matched = False


"""
