import pandas as pd
# import pyodbc 
from db_connect import connect_to_db,read_table
import CONFIG_batterylab

def test_read_from_batt_db():
    # server = 'dt-sql03'

    # db = 'sievt_finaltest'
    CONFIG_batterylab.server = 'JOHNLAPTOP\SQLEXPRESS'
    CONFIG_batterylab.db = 'batterylab_finaltest'
    CONFIG_batterylab.Trusted_ConnectionStr = 'Trusted_Connection=yes;'
    conn = connect_to_db(CONFIG_batterylab)
    table = "BATTERYLAB"
    df = read_table(table,conn)
    conn.close
    cols_expected = ['DateTimeStamp', 'FILE_NAME', 'PART_NUMBER', 'SERIAL_NUMBER', 'OVERALL_RESULT', 'CAPACITY']
    cols = list(df.columns)
    for col in cols_expected:
        print(col,col in cols)
        assert col in cols
    

def test_read_from_batt_db_merlin():
    # server = 'dt-sql03'
    CONFIG_batterylab.server = 'JOHNLAPTOP\SQLEXPRESS'
    CONFIG_batterylab.db = 'batterylab_finaltest'
    CONFIG_batterylab.Trusted_ConnectionStr = 'Trusted_Connection=yes;'
    # db = 'sievt_finaltest'
    conn = connect_to_db(CONFIG_batterylab)
    table = "MERLIN"
    df = read_table(table,conn)
    conn.close
    cols_expected = ['DateTimeStamp', 'FILE_NAME', 'PART_NUMBER', 'SERIAL_NUMBER', 'OVERALL_RESULT']
    cols = list(df.columns)
    for col in cols_expected:
        print(col,col in cols)
        assert col in cols
    
if __name__ == "__main__":
    print('start')
    test_read_from_batt_db()
    test_read_from_batt_db_merlin()
  