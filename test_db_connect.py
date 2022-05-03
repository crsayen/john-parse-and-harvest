import pandas as pd
import pyodbc 

def read_table(table,connection,datefield=None):
    sql = f'SELECT * FROM {table}'
    return pd.read_sql(sql,connection,parse_dates=datefield)

def connect_to_db(server,db):
    driver = '{SQL Server}'
    conn_str = (f'Driver={driver};'
            f'Server={server};' 
            f'Uid=teststand;Pwd=teststand;'
            'Trusted_Connection=yes;'
           f'Database={db};')
    print(conn_str)
    conn = pyodbc.connect(conn_str)
    return conn




def test_read_from_batt_db():
    # server = 'dt-sql03'
    server = 'JOHNLAPTOP\SQLEXPRESS'
    db = 'batterylab_finaltest'
    # db = 'sievt_finaltest'
    conn = connect_to_db(server,db)
    table = "BATTERYLAB"
    df = read_table(table,conn)
    conn.close
    cols_expected = ['time', 'FILE_NAME', 'PART_NUMBER', 'SERIAL_NUMBER', 'OVERALL_RESULT', 'CAPACITY']
    cols = list(df.columns)
    for col in cols_expected:
        print(col,col in cols)
        assert col in cols
    

def test_read_from_batt_db_merlin():
    # server = 'dt-sql03'
    server = 'JOHNLAPTOP\SQLEXPRESS'
    db = 'batterylab_finaltest'
    # db = 'sievt_finaltest'
    conn = connect_to_db(server,db)
    table = "MERLIN"
    df = read_table(table,conn)
    conn.close
    cols_expected = ['time', 'FILE_NAME', 'PART_NUMBER', 'SERIAL_NUMBER', 'OVERALL_RESULT']
    cols = list(df.columns)
    for col in cols_expected:
        print(col,col in cols)
        assert col in cols
    
if __name__ == "__main__":
    print('start')
    test_read_from_batt_db()
    test_read_from_batt_db_merlin()
  