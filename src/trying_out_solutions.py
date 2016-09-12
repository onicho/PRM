from logic.share import ShareFactory
from logic.portfolio import *
import pyodbc
#
# list_of_epic_strings = ['ERM','CGL', 'NG']
#
# shares = []
#
# for epic in list_of_epic_strings:
#     shares.append(ShareFactory.create(epic, '2009-01-01', '2014-12-31'))
#
# market = ShareFactory.create('^FTSE', '2009-01-01', '2014-12-31')
#
# p = TreynorBlackPortfolio(shares, market, 1.5)
#
# print(p.final_active_portfolio)
#
# print(p.active_proportion_tb)


cnxn = pyodbc.connect(
    'driver={SQL Server};server=localhost;database=PRM;Integrated '
    'Security=True'
)
cursor = cnxn.cursor()

db_tickers = [ticker[0] for ticker in
              cursor.execute(
                  "SELECT distinct epic FROM [dbo].[SHARE]").fetchall()
              ]

print(db_tickers)