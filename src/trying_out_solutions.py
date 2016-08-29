
from sqlalchemy import *
from sqlalchemy.engine import reflection

URL = 'mssql+pyodbc://GMT04999:1433/PRM_Lite?driver=SQL+Server'

engine = create_engine(URL, echo = True)

#inspection = reflection.Inspector.from_engine(engine)
#print(inspection.get_table_names())

conn = engine.connect()


s = text(
        "SELECT EPIC"
        " FROM SHARE_CALENDAR"
        " WHERE SHARE_CALENDAR.CALENDAR_DATE = '2009-01-01' "
    )

result = [dict(r) for r in conn.execute(s)]

#myresult = result.fetchone()

# a = []
# for row in myresult:
#     d = dict(row.items())
#     a.append(d)
print(result)

for i in result:
    print(i)

"""
In[2]: l = [{'EPIC': '^FTSE'}, {'EPIC': 'BP'}, {'EPIC': 'LLOY'}, {'EPIC': 'RBS'}, {'EPIC': 'TSCO'}]
In[3]: x = [d['value'] for d in l if 'value' in d]
In[4]: x
Out[4]: []
In[5]: x = [d['EPIC'] for d in l if 'EPIC' in d]
In[6]: x
Out[6]: ['^FTSE', 'BP', 'LLOY', 'RBS', 'TSCO']
In[7]: x[1]
Out[7]: 'BP'
In[8]: type(x[0])
Out[8]: str




"""