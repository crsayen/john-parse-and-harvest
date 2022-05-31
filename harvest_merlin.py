from cmath import log
import pandas as pd
import os
import shutil
from db_connect import read_table,connect_to_db
from parse_merlin_report import parse_merlin
from parse_batterylab_report import parse_batterylab
import CONFIG_merlin as CONFIG
import time
import itertools
import logging



def harvest_merlin():
    logging.info("start harvest_merlin")
    conn = connect_to_db(CONFIG)
    data_from_db = read_table(CONFIG.table,conn)
    data_from_db.to_csv("merlin.csv")
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
                # print(f'{file=},{already_in_db=},{is_report_file=}')
                if already_in_db and is_report_file:
                    #move or mark so we don't try next time?
                    pass
                elif is_report_file:
                    merlin_report = parse_merlin(report_folder_root + report_folder + "\\",file)
                    # print(f"{data_to_db=}")
                    logging.info(f'write to db {merlin_report.FILE_NAME}')
                    cursor = conn.cursor()
                    # Insert Dataframe into SQL Server:
                    # for _, row in merlin_report.iterrows():
                    sql=f"""
                        INSERT INTO {CONFIG.table}
                        (DateTimeStamp,FILE_NAME,PART_NUMBER,SERIAL_NUMBER,OVERALL_RESULT)
                        VALUES (?,?,?,?,?)
                        """
                    cursor = cursor.execute(sql, 
                                            merlin_report.DateTimeStamp,
                                            merlin_report.FILE_NAME,
                                            merlin_report.PART_NUMBER,
                                            merlin_report.SERIAL_NUMBER,
                                            merlin_report.OVERALL_RESULT)
                    # print(cursor.rowcount)
                    logging.info(f'{sql=}')
                    logging.info(f'{merlin_report=}')
                    # cursor = cursor.execute(sql, row.DateTimeStamp,row.FILE_NAME, row.PART_NUMBER, row.SERIAL_NUMBER,row.OVERALL_RESULT)
                    logging.info(f'{cursor.rowcount=}')                   
                    conn.commit()            
                    cursor.close()
    conn.close()
    logging.info('finish harvest_merlin')       

if __name__ == "__main__":
    starttime = time.perf_counter()
    print(f'start harvest report data to {CONFIG.server}')
    harvest_merlin()

    print('end harvest', time.perf_counter()-starttime)
    
    