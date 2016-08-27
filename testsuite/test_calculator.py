"""
#
# #lst = [30,33,50,40,20]
#
#
# lst = [ 228.75,
# 180,
# 204,
# 252,
# 207.5,
# 204,
# 228,
# 269.7,
# 373.3,
# 380]
#
#
# position = 0
# price_returns = []
#
# while position < len(lst)-1:
#     r = format(float((lst[position + 1] / lst[position]) - 1),'.5f') #!!!!! check
#     price_returns.append(r)
#     position += 1
#
# print(*price_returns, sep='\n')
#
# print(len(price_returns))



test_lst = [
228.75,
180,
204,
252,
207.5,
204,
228,
269.7,
373.3,
380,
393,
435.7,
470.3,
470.2,
520,
516,
588.5,
599.5,
605,
588.5,
611,
649,
695,
692,
693,
698,
697,
713,
663,
653,
682,
571,
615,
678,
696,
625,
690,
717,
760,
785,
801,
746.5,
714,
770,
770,
800,
783,
870.5,
890,
921,
966.5,
980,
942,
1023,
1065,
1202,
1160,
1075,
1243,
1350,
1326,
1319,
1198,
1070,
1189,
1110,
1084,
1082,
1015,
1051,
1019,
1047
]

rs = Calculator.return_on_share_prices(test_lst)
avg = Calculator.average_return(rs)
#print(avg)

avg_annualised  = Calculator.annualise_as_percentage(avg)

#print(avg_annualised)

import numpy

std = std(rs)
a_std = Calculator.annualise_as_percentage(std)
print(std)

import statistics

std1 = statistics.stdev(rs)
a_std1 = Calculator.annualise_as_percentage(std1)
print(a_std1)


"""


#CORRELATION

"""
from numpy import corrcoef
from BusinessLogic.share import Share

def find_correlation(list_of_shares):
    lists_of_prices_to_correlate = []

    if len(list_of_shares) > 1:
        for share in list_of_shares:
            lists_of_prices_to_correlate.append(share.get_historical_prices())
        correlations = corrcoef(lists_of_prices_to_correlate)
        return correlations
    else:
        print("Insufficient number of shares to perform correlation " +
              " (minimum 2 required, but %(num)d were provided)" % {"num": len(list_of_shares)})




s1 = Share('BP')
s2 = Share('RBS')
s3 = Share('LLOY')

s1.set_historical_prices([30,35,41])
s2.set_historical_prices([25,11,50])
s3.set_historical_prices([10,16,20])


#print(s3.getName(), s3.get_historical_prices())

mylst = [s1, s2, s3]

other_list = [s1]

print(find_correlation(mylst))

"""

#BETA

"""
def beta(lst_returns_on_share, lst_returns_on_market):
    # cov(x,y)/ var(y)
    #ddof=0`` provides a maximum likelihood estimate of the variance for normally distributed variables(ref!!!)
    covariance = cov(lst_returns_on_share, lst_returns_on_market, ddof=0)[0][1]
    variance = var(lst_returns_on_market)
    beta_result = float(covariance / variance)
    return round(beta_result, 2)


In standard statistical practice, ``ddof=1`` provides an
unbiased estimator of the variance of a hypothetical infinite population.
``ddof=0`` provides a maximum likelihood estimate of the variance for
normally distributed variables.
"""

#ALPHA

"""
def alpha(lst_hist_prices_share, lst_hist_prices_market, rf):
    # Alpha %  --> α = Rs – [Rf + (Rm – Rf) β]
    returns_share = [float(round(item, 9)) for item in calc.return_on_share_prices(lst_hist_prices_share)]
    rs = calc.annualise_as_percentage(calc.average_return(returns_share))

    returns_market = [float(round(item, 9)) for item in calc.return_on_share_prices(lst_hist_prices_market)]
    rm = calc.annualise_as_percentage(calc.average_return(returns_market))

    beta_s = calc.beta(returns_share, returns_market)

    alpha_s = rs - (rf + (rm - rf) * beta_s)

    return round(alpha_s, 2)

"""
