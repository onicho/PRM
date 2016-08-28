from BusinessLogic.calculator import *
from collections import *

c = Calculator()





def cut_off_rate(lst2d_shareprices, rf, mkt_prices):

    erbs = {}

    for i in lst2d_shareprices:
        erbs[c.erb(i,mkt_prices, rf)] = i

    ordered_erbs = sorted(erbs.items(), reverse = True)


    numer_components = []

    for item in lst2d_shareprices:
        numer_components.append(
            float((c.annualise_as_percentage(c.average_return(c.return_on_share_prices(item)))) - rf) * \
            float(c.beta(item, mkt_prices)) / \
            float(c.specific_risk(item, mkt_prices))
        )

    return ordered_erbs





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

test = cut_off_rate([CGLprices, AMLprices, NGprices,ERMprices], 1.5, MKTprices)

for i in test:
    print(i)


#print(test)

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