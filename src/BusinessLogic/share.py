# create class share

class Share:
    ## Constructs a share
    #
    def __init__(self, name):
        self.__name = str(name)
        self.__historical_prices = {}

    def __repr__(self):
        return self.__name

    def __str__(self):
        return self.__name

    def getName(self):
        return self.__name

    def set_historical_prices(self, historical_prices):
        self.__historical_prices = historical_prices

    def get_historical_prices(self):
        return self.__historical_prices


# s1 = Share("LLOY")
# hist_pr = {'2009-01-01': 30, '2010-01-01': 35, '2011-01-01': 40}
# s1.set_historical_prices(hist_pr)
#
# print(s1.getName(),
#       s1.get_historical_prices()
#       )
#
# print(s1)
# print(type(s1))