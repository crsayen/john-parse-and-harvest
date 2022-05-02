import pandas as pd
import pyodbc 

def read_table(table,connection,datefield=None):
    sql = f'SELECT * FROM {table}'
    return pd.read_sql(sql,connection,parse_dates=datefield)
dlist = pyodbc.drivers()
for d in dlist:
    print(d)
# driver = '{ODBC Driver 17 for SQL Server}'
# driver = '{SQL Server Native Client 11.0}'
driver = '{SQL Server}'
server = 'dt-sql03'
# db = 'sievt_finaltest'
db = 'sievt_finaltest'

# conn_str = ('Driver=Microsoft Access Driver (*.mdb, *.accdb);' + 
#            'DBQ=C:/Users/Public/Documents/National Instruments/TestStand 2020 (32-bit)/Components/Models/TestStand Results.mdb;')

conn_str = (f'Driver={driver};'
            f'Server={server};' 
            f'Uid=teststand;Pwd=teststand;'
           f'Database={db};')
print(conn_str)
conn = pyodbc.connect(conn_str)
# sql="""
# INSERT INTO UUT_RESULT (UUT_SERIAL_NUMBER,UUT_STATUS,PART_NUMBER)
# VALUES ('bob','grand','type_bob')
# """
# cursor = conn.cursor()
# cursor.execute(sql)
# conn.commit()
uut_result = read_table("UUT_RESULT",conn)
print(uut_result.columns)
print(uut_result.describe())
print(uut_result)