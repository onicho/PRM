from logic.share import ShareFactory
from logic.portfolio import *
import pyodbc
from yahoo_finance import *

# cnxn = pyodbc.connect(
#     'driver={SQL Server};server=localhost;database=PRM;Integrated '
#     'Security=True'
# )
# cursor = cnxn.cursor()
#
# db_tickers = [ticker[0] for ticker in
#               cursor.execute(
#                   "SELECT distinct epic FROM [dbo].[SHARE]").fetchall()
#               ]

#print(db_tickers)

#
# s = Share('BP.L')
#
# x = s.get_price()
#
#
# prices = [{p['Date']: p['Close']} for p in
#           s.get_historical('2016-08-31', '2016-08-31')]
#
# print(x)

# cnxn = pyodbc.connect(
#     'driver={SQL Server};server=localhost;database=PRM_Lite;'
#     'Integrated Security=True')
#
# cursor = cnxn.cursor()
#
# cursor.execute("SELECT distinct epic, CALENDAR_DATE, PRICE "
#                "FROM [dbo].[SHARE_CALENDAR]")
#
# po = cursor.fetchall()
#
# x = [(item[1],float(item[2])) for item in po]
#
# print(x)



"""
  s = self.filtered()
        w = self.adjusted_percent()

        self.final = dict(zip(map(s, w))

"""