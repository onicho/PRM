# create class share

class Share:
    ## Constructs a share
    #
    def __init__(self, name):
        self.__name = str(name)
        self.__historical_prices = {}

    def getName(self):
        return self.__name

    def set_historical_prices(self, historical_prices):
        self.__historical_prices = historical_prices

    def get_historical_prices(self):
        return self.__historical_prices



