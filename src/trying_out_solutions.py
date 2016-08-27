from numpy import *
from BusinessLogic.calculator import *
from  scipy.stats import beta

calc = Calculator()


def testbeta(lst_share_prices, lst_market_prices):
    # cov(x,y)/ var(y)
    # ddof=0`` provides a maximum likelihood estimate of the variance for normally distributed variables(ref!!!)

    returns_share = [float(round(item, 9)) for item in calc.return_on_share_prices(lst_share_prices)]
    returns_market = [float(round(item, 9)) for item in calc.return_on_share_prices(lst_market_prices)]

    beta_result = float((cov(returns_share, returns_market, ddof=0)[0][1]) /
                        (var(returns_market)))

    return round(beta_result, 2)





##########################################
array1 = []

with open("AMLprices.txt", "r") as ins:
    for line in ins:
        array1.append(line.rstrip('\n').rstrip('\r'))

AMLprices = [float(i) for i in array1]

arrayMKT = []

with open("MKTprices.txt", "r") as ins:
    for line in ins:
        arrayMKT.append(line.rstrip('\n').rstrip('\r'))

MKTprices = [float(i) for i in arrayMKT]

###########################################

test = testbeta(AMLprices, MKTprices)

print(test)

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

"""
