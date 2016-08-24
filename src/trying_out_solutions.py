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
