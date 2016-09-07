r"""
This module contains classes that can be used to create Share objects
"""

import pyodbc


class Share(object):
    r"""
    The Share object represents a stock exchange share.

    The class encapsulates share information. A Share has a unique name
    and a range of historical prices for a particular period of time.
    """

    def __init__(self, name):
        r"""
        Constructs instance variables for class Share.

        Instance variables are the Share name and a list of historical share
        prices, where each price in the list is a Clothing price of a Share
        for a day, month or a year.

        :param name: name of a share that corresponds to a market stock ticker
        :type name: str

        :Example:

        'RBS' or 'BP' or 'TSCO'
        """
        self.name = str(name)
        self.prices = []  # list of historical share prices for a certain period

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class ShareFactory(object):
    r"""
    Class that has mechanisms to create Share objects.

    This is an object factory class that encapsulates the Share instantiation
    process.
    """

    @staticmethod
    def create(ticker, start_date, end_date):
        r"""
        Creates an object of class Share.

        A new Share object is created, which is given a name that corresponds to
        a stock market ticker (epic code). A connection with a database is
        established to retrieve historical prices data for the given period of
        time. The prices get assigned to the share object.

        :param ticker: an epic code of a stock market share
        :param start_date: start of the historical prices data period
        :param end_date: end of the historical prices data period
        :type ticker: str
        :type start_date: str
        :type: end_date: str
        :return: a new object Share with a name and a list of historical prices

        :Example:

        ticker can be 'AML', 'NG' or any other epic code of FTSE100 shares
        ..note:: start and end dates must be in the 'yyyy-mm-dd' format
        """
        s = Share(ticker)
        # connection to the PRM database is established
        cnxn = pyodbc.connect(
            'driver={SQL Server};server=localhost;database=PRM;Integrated Security=True'
        )
        cursor = cnxn.cursor()
        cursor.execute(
            "SELECT price FROM [dbo].[vw_LastDayOfMonthPricesWithStringDate]"
            "where epic = '" + ticker + "' and (CALENDAR_DATE between '" +
            start_date + "' and '" + end_date + "')"
            "order by CALENDAR_DATE asc "
        )
        # a list of historical share prices is created and assigned to the share
        share_prices = [float(p[0]) for p in cursor.fetchall()]
        s.prices = share_prices

        return s