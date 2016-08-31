from yahoo_finance import Share
from pprint import pprint

lonExt = '.L'

from sqlalchemy import *

URL = 'mssql+pyodbc://GMT04999:1433/PRM_Lite?driver=SQL+Server'

engine = create_engine(URL, echo=True)

conn1 = engine.connect()

sharesQuery = text(
    "SELECT distinct epic "
    "FROM [dbo].[SHARE]"
)

po = conn1.execute(sharesQuery)

for epicCode in po:
    ShareObject = Share(epicCode['epic'] + lonExt)

    print(ShareObject.get_price())

    prices = [{p['Date']: p['Close']} for p in ShareObject.get_historical('2009-01-01', '2009-01-15')]
    for priceDict in prices:
        conn = engine.connect()
        price = list(priceDict.items())

        updateQuery = "update [dbo].[SHARE_CALENDAR] set price = " + price[0][1] + " where CALENDAR_DATE = '" + \
                      price[0][0] + "' AND epic = '" + epicCode['epic'] + "'"

        conn.execute(updateQuery)
