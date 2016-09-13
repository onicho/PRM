from logic.share import ShareFactory
from logic.portfolio import *
import pyodbc
from yahoo_finance import *

cnxn = pyodbc.connect(
    'driver={SQL Server};server=localhost;database=PRM;'
    'Integrated Security=True')
cursor = cnxn.cursor()

cursor.execute("SELECT distinct CALENDAR_DATE FROM [dbo].[CALENDAR]")

x = [str(d[0]) for d in cursor.fetchall()]


print('2016-05-12' in x)
