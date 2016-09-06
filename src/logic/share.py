import pyodbc


class Share(object):

    def __init__(self, name):
        r"""
        Class that encapsulates share information
        :param name:
        """
        self.name = str(name)
        self.historical_prices = []

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name



class ShareFactory(object):

    @staticmethod
    def create(ticker, start_date, end_date):
        s = Share(ticker)
        cnxn = pyodbc.connect('driver={SQL Server};server=localhost;database=PRM;Integrated Security=True')
        cursor = cnxn.cursor()
        cursor.execute("SELECT price FROM [dbo].[vw_LastDayOfMonthPricesWithStringDate]"
                       "where epic = '" + ticker + "' and (CALENDAR_DATE between '" + start_date + "' and '" + end_date +"')"
                       "order by CALENDAR_DATE asc ")
        share_prices = [float(p[0]) for p in cursor.fetchall()]
        s.historical_prices = share_prices
        return s

