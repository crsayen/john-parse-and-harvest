import pandas as pd

import pyodbc


def read_table(table, connection, datefield="DateTimeStamp"):
    sql = f"SELECT * FROM {table}"
    return pd.read_sql(sql, connection, parse_dates=datefield)


def connect_to_db(CONFIG):
    driver = "{SQL Server}"
    conn_str = (
        f"Driver={driver};"
        f"Server={CONFIG.server};"
        f"Uid=teststand;Pwd=teststand;"
        f"{CONFIG.Trusted_ConnectionStr}"
        f"Database={CONFIG.db};"
    )
    # print(conn_str)
    conn = pyodbc.connect(conn_str)
