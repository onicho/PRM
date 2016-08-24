

def find_correlation(list_of_shares):
    lists_of_prices_to_correlate = []
    if len(list_of_shares) > 1:
        for share in list_of_shares:
            lists_of_prices_to_correlate.append(share.get_historical_prices())
        return lists_of_prices_to_correlate



