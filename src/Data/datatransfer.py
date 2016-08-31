import pyodbc
from yahoo_finance import Share
from pyodbc import *

from pprint import pprint

lonExt = '.L'

# from sqlalchemy import *
#
# URL = 'mssql+pyodbc://GMT04999:1433/PRM_Lite?driver=SQL+Server'
#
# engine = create_engine(URL, echo=True)

cnxn = pyodbc.connect('driver={SQL Server};server=localhost;database=PRM_Lite;Integrated Security=True')
cursor = cnxn.cursor()

# sharesQuery = text(
#     "SELECT distinct epic "
#     "FROM [dbo].[SHARE]"
# )
cursor.execute("SELECT distinct epic FROM [dbo].[SHARE]")
#po = conn1.execute(sharesQuery)

po = cursor.fetchall()

for epicCode in po:
    print("Next Ticker is " + epicCode[0])

    ShareObject = Share(epicCode[0] + lonExt)

    prices = [{p['Date']: p['Close']} for p in ShareObject.get_historical('2009-01-01', '2009-01-15')]

    for priceDict in prices:
        cnxn.cursor()
        price = list(priceDict.items())
        cursor.execute("[dbo].[Update_Prices] '" + epicCode[0] + "', '" + price[0][0] + "', " + price[0][1] + "")
        cnxn.commit()

    #         connection = engine.raw_connection()
#         try:
#             price = list(priceDict.items())
#             cursor = connection.cursor()
#             cursor.callproc("[dbo].[Update_Prices] ?, ?, ?", [epicCode['epic'], price[0][0], price[0][1]])
#             results = list(cursor.fetchall())
#             cursor.close()
#             connection.commit()
#         finally:
#             connection.close()


        # conn = engine.connect()
        # #cursor = conn.cursor()

        #
        # #cursor.callproc("[dbo].[Update_Prices] ?, ?, ?", [epicCode['epic'], price[0][0], price[0][1]])
        #
        # updateQuery = "[dbo].[Update_Prices] '" + epicCode['epic'] + "', '" + price[0][0] + "', " + price[0][1] + ""
        #
        # # updateQuery = "update [dbo].[SHARE_CALENDAR] set price = " + price[0][1] + " where CALENDAR_DATE = '" + \
        # #               price[0][0] + "' AND epic = '" + epicCode['epic'] + "'"
        #
        # #conn.execute("[dbo].[Update_Prices] ?, ?, ?", [epicCode['epic'], price[0][0], price[0][1]])
        # conn.(updateQuery)




