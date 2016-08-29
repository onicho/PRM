from yahoo_finance import Share
from pprint import pprint

ShareObject = Share('^FTSE')


print(ShareObject.get_price())
print


#pprint(ShareObject.get_historical('2016-05-23', '2016-05-29'))

closes = [c['Close'] for c in ShareObject.get_historical('2009-01-01', '2009-01-15')]

print(closes)

