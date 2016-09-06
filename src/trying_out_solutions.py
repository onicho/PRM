from logic.sharefactory import *
from logic.test_portf import *
from logic.calculator import *

list_of_epic_strings = ['ERM','CGL', 'NG']

shares = []

for epic in list_of_epic_strings:
    shares.append(ShareFactory.create(epic, '2009-01-01', '2014-12-31'))

market = ShareFactory.create('^FTSE', '2009-01-01', '2014-12-31')

p = TreynorBlackPortfolio(shares, market, 1.5)

print(p.final_active_portfolio)

print(p.active_proportion_tb)

