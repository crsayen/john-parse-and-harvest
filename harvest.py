import pandas
import os
import shutil
from test_db_connect import read_table,connect_to_db
from parse_merlin_report import parse_merlin


def harvest_merlin():
    server = 'JOHNLAPTOP\SQLEXPRESS'
    db = 'batterylab_finaltest'
    conn = connect_to_db(server,db)
    table = "MERLIN"
    df = read_table(table,conn)
    # f_locs = ['C:\\work\\pyHarvest\\reports\\'
    # f_locs = ['C:\\PTM820eSystem\\Runtime\\Toyota Prius Battery_Gen2\\Test Sequence Logs\\',
            #   'C:\\PTM820eSystem\\Runtime\\Toyota Prius Battery_Gen3\\Test Sequence Logs\\']
    f_locs = ['C:\\work\\pyHarvest\\reports\\']
    for f_loc in f_locs:
        directs = os.listdir(f_loc)  # 
        directs = [f for f in directs if os.path.isdir(f_loc + f)]
        print(f'{directs=}')
        for direct in directs:
            files = os.listdir(f_loc + "\\" + direct)
            for file in files:
                already_in_db = (file in df.FILE_NAME.values)
                with open(f_loc + "\\" + direct + "\\" + file, encoding='latin-1') as f:
                    s = f.read(600)
                is_report_file = s.find('START OF TEST') > 0
                print(f'{file=},{already_in_db=},{is_report_file=}')
                if already_in_db and is_report_file:
                    #mark so we don't try next time?
                    pass
                elif is_report_file:
                    data_to_db = parse_merlin(f_loc + direct + "\\",file)
                    print(f"{data_to_db=}")
                    cursor = conn.cursor()
                    # Insert Dataframe into SQL Server:
                    for index, row in data_to_db.iterrows():
                        sql=f"""
                        INSERT INTO {table}
                        (time,FILE_NAME,PART_NUMBER,SERIAL_NUMBER,OVERALL_RESULT)
                        VALUES (?,?,?,?,?)
                        """
                        cursor.execute(sql, row.time,row.FILE_NAME, row.PART_NUMBER, row.SERIAL_NUMBER,row.OVERALL_RESULT)
                    conn.commit()            
                    cursor.close()
    conn.close()
           

if __name__ == "__main__":
    print('start')
    harvest_merlin()