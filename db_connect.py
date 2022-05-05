import pandas as pd
import pyodbc 
import CONFIG

def read_table(table,connection,datefield="DateTimeStamp"):
    sql = f'SELECT * FROM {table}'
    return pd.read_sql(sql,connection,parse_dates=datefield)

def connect_to_db(server,db):
    driver = '{SQL Server}'
    conn_str = (f'Driver={driver};'
            f'Server={server};' 
            f'Uid=teststand;Pwd=teststand;'
            f'{CONFIG.Trusted_ConnectionStr}'
            f'Database={db};')
    print(conn_str)
    conn = pyodbc.connect(conn_str)
    return conn