from numpy import *


def beta(lst_returns_on_share, lst_returns_on_market):
    # cov(x,y)/ var(y)
    #ddof=0`` provides a maximum likelihood estimate of the variance for normally distributed variables(ref!!!)
    covariance = cov(lst_returns_on_share, lst_returns_on_market, ddof=0)[0][1]
    variance = var(lst_returns_on_market)
    beta_result = float(covariance / variance)
    return beta_result

"""
In standard statistical practice, ``ddof=1`` provides an
unbiased estimator of the variance of a hypothetical infinite population.
``ddof=0`` provides a maximum likelihood estimate of the variance for
normally distributed variables.
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

print(beta(values3, MKTvalues))