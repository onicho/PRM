"""
This module contains a function that allows to update the PRM database
"""

from datetime import *
import pyodbc
from yahoo_finance import Share
from logic.exceptions import *


def update_db(start, end):
    """
    Updates the PRM database with closing daily prices from Yahoo Finance.

    It establishes connection with the PRM db to retrieve all epic codes that
    need to be updated. Then a call to Yahoo Finance API is made to retrieve
    prices for the specified range of dates. The epic codes, dates and prices
    get passed to the stored procedure Update_Prices in the db, which updates
    prices or inserts new rows in the price table.

    :param start: start date of the historical prices range
    :param end: end date of the historical prices range
    :type start: str "yyy-mm-dd"
    :type end: str "yyy-mm-dd"
    """

    if (type(start) is str and datetime.strptime(start, "%Y-%m-%d").date()) and\
            (type(end) is str and datetime.strptime(end, "%Y-%m-%d").date()):

        cnxn = pyodbc.connect(
            'driver={SQL Server};server=localhost;database=PRM;'
            'Integrated Security=True')

        cursor = cnxn.cursor()

        cursor.execute("SELECT distinct epic FROM [dbo].[SHARE]")

        po = cursor.fetchall()

        lonext = '.L'

        for epicCode in po:

            if epicCode[0] == "^FTSE":
                shareobject = Share(epicCode[0])

            else:
                shareobject = Share(epicCode[0] + lonext)

            prices = [{p['Date']: p['Close']} for p in
                      shareobject.get_historical(start, end)]

            for priceDict in prices:
                cnxn.cursor()
                price = list(priceDict.items())
                cursor.execute("[dbo].[Update_Prices] '" + epicCode[0] + "', '" +
                               price[0][0] + "', " + price[0][1] + "")
                cnxn.commit()

    else:
        raise InputError("start, end", "incorrect argument type or format  " +
                         "check that your dates are str in yyy-mm-dd format")


