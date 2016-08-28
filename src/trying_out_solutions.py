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
                float(pow(c.beta(lst_shares[count], mkt_prices),2)) / \
                float(c.specific_risk(lst_shares[count], mkt_prices))
            )

            count += 1


    return num_components, denom_components















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

testlist = order_by_erb([NGprices, AMLprices, CGLprices, ERMprices], 1.5, MKTprices)


test = cut_off_rate(testlist, 1.5, MKTprices)

# for i in test:
#     print(i)

print(test)


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
