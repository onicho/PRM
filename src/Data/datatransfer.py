from yahoo_finance import Share
from pprint import pprint

ShareObject = Share('BP.L')


print(ShareObject.get_price())
print


#pprint(ShareObject.get_historical('2016-05-23', '2016-05-29'))

prices = [{p['Date']:p['Close']} for p in ShareObject.get_historical('2009-01-01', '2009-01-15')]

for i in prices:
    print(i)


