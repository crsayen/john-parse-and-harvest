import pandas as pd
import os
import shutil
from db_connect import read_table,connect_to_db
from parse_merlin_report import parse_merlin
import CONFIG
import time

def harvest_merlin():

    conn = connect_to_db(CONFIG.server,CONFIG.db)
    data_from_db = read_table(CONFIG.table,conn)
    for report_folder_root in CONFIG.report_folder_roots:
        report_folders = os.listdir(report_folder_root)  # 
        report_folders = [f for f in report_folders if os.path.isdir(report_folder_root + f)]
        print(f'{report_folders=}')
        for report_folder in report_folders:
            files = os.listdir(report_folder_root + "\\" + report_folder)
            for file in files:
                already_in_db = (file in data_from_db.FILE_NAME.values)
                is_report_file = False
                if already_in_db == False:
                    with open(report_folder_root + "\\" + report_folder + "\\" + file, encoding='latin-1') as f:
                       s = f.read(600)
                    is_report_file = s.find('START OF TEST') > 0
                else:
                    is_report_file = True    
                print(f'{file=},{already_in_db=},{is_report_file=}')
                if already_in_db and is_report_file:
                    #move or mark so we don't try next time?
                    pass
                elif is_report_file:
                    data_to_db = parse_merlin(report_folder_root + report_folder + "\\",file)
                    print(f"{data_to_db=}")
                    cursor = conn.cursor()
                    # Insert Dataframe into SQL Server:
                    for _, row in data_to_db.iterrows():
                        sql=f"""
                        INSERT INTO {CONFIG.table}
                        (time,FILE_NAME,PART_NUMBER,SERIAL_NUMBER,OVERALL_RESULT)
                        VALUES (?,?,?,?,?)
                        """
                        cursor.execute(sql, row.time,row.FILE_NAME, row.PART_NUMBER, row.SERIAL_NUMBER,row.OVERALL_RESULT)
                    conn.commit()            
                    cursor.close()
    conn.close()
           

if __name__ == "__main__":
    starttime = time.perf_counter()
    print('start harvest')
    harvest_merlin()

    print('end harvest', time.perf_counter()-starttime)