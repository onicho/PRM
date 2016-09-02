# create class share

class Share(object):   # look up new-style classes
    ## Constructs a share
    #
    def __init__(self, name):
        self.name = str(name)
        self.historical_prices = []
        self.hist_price_period = {'START_DATE': 0, 'END_DATE': 0, 'PRICE_FREQUENCY': ''}

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def getName(self):
        return self.name

    def set_historical_prices(self, historical_prices):
        self.historical_prices = historical_prices

    def get_historical_prices(self):
        return self.historical_prices

    def update_hist_price_period(self, start_date_str, end_date_str, frequency_str = 'monthly'):
        self.hist_price_period['START_DATE'] = start_date_str
        self.hist_price_period['END_DATE'] = end_date_str
        self.hist_price_period['PRICE_FREQUENCY'] = frequency_str

    def get_hist_price_period(self):
        return self.hist_price_period


# s1 = Share("LLOY")
# hist_pr = [30,35,40,80]
# s1.set_historical_prices(hist_pr)
#
# s1.update_hist_price_period('2010-01-01', '2015-01-01', 'yearly')
#
# print(s1.getName(),
#       type(s1.get_historical_prices())
#       )


