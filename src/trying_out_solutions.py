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

from BusinessLogic.calculator import *

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