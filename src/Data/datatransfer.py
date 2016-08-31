from yahoo_finance import Share
from pprint import pprint

lonExt = '.L'

from sqlalchemy import *
URL = 'mssql+pyodbc://GMT04999:1433/PRM_Lite?driver=SQL+Server'

engine = create_engine(URL, echo = True)

conn = engine.connect()

sharesQuery = text(
        "SELECT distinct epic "
        "FROM [dbo].[SHARE]"
)

metadata = MetaData()

orders = Table('SHARE_CALENDAR', metadata,
    Column('EPIC', String),
    Column('CALENDAR_DATE', Date),
    Column('PRICE', Integer)
)

po = conn.execute(sharesQuery)

for epicCode in po:
    ShareObject = Share(epicCode['epic'] + lonExt)

    print(ShareObject.get_price())

    prices = [{p['Date']:p['Close']} for p in ShareObject.get_historical('2009-01-01', '2009-01-15')]
    for priceDict in prices:
        price = list(priceDict.items())
        # update_blah = (
        # orders.update.\
        #     where(and_(orders.c.CALENDAR_DATE == price[0],
        #                orders.c.EPIC == epicCode['epic'])).
        #     values(PRICE=price[1])
        # )

        updateQuery = "update [dbo].[SHARE_CALENDAR] set price = " + price[1] + " where CALENDAR_DATE = '" + price[0] + "' AND epic = '" + epicCode['epic'] +"'"

        print(updateQuery)

        print(conn.execute(updateQuery))