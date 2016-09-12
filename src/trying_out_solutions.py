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

# #print(x)
#
# cnxn = pyodbc.connect(
#     'driver={SQL Server};server=localhost;database=PRM;'
#     'Integrated Security=True')
#
# cursor = cnxn.cursor()
#
# cursor.execute("SELECT PRICE "
#                "FROM [dbo].[SHARE_CALENDAR]"
#                "where epic = 'VOD' and CALENDAR_DATE between '2016-05-11' and "
#                "'2016-05-31'")
#
# p = cursor.fetchall()
#
# x = [(float(item[0])) for item in p]
#
# print(x)


# s = Share('VOD.L')
#
# z = s.get_historical('2016-05-11', '2016-05-31')
#
# pcs = [float(item['Close']) for item in z]
#
# print(pcs)
#
#
# x.reverse() == pcs

"""
  s = self.filtered()
        w = self.adjusted_percent()

        self.final = dict(zip(map(s, w))

"""