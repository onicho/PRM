from BusinessLogic.share import Share
import pyodbc


class ShareGenerator:
    @staticmethod
    def create_share(str_share_name):
        return Share(str_share_name)

    @staticmethod
    def shares_maker(list_of_epic_strings):
        list_of_shares = []
        for epic in list_of_epic_strings:
            list_of_shares.append(ShareGenerator.create_share(epic))
        return list_of_shares


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






# test





x = ShareFactory.create('^FTSE', '2009-01-01','2014-12-31')

for price in x.historical_prices:
    print(price)


print(len(x.historical_prices))








#shares = [Share(x) for x in ["ERM", "AML"]]

####################################################


# @staticmethod
# def create(ticker, start_date, end_date):
#     s = Share(ticker)
#     dbo = Database(connection)
#     # can also look up descriptors
#     s.historical_price = dbo.get_historical_price(ticker)
#     return s