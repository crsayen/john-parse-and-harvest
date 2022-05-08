import pandas as pd
import os
import shutil
from db_connect import read_table,connect_to_db
from parse_batterylab_report import parse_batterylab
import CONFIG_batterylab as CONFIG
import time
import itertools
import logging

def files_in_csv():
    try:
        file_list = pd.read_csv('file_list.csv')
    except:
        print('read csv error')  #start with blank list
        file_list = pd.DataFrame([],columns=['file','isReport','inDb'])
    return file_list

def files_in_folder(root_dir):
    walk_files = []
    count=0
    for root, dirs, files in os.walk(root_dir, topdown=False):
        walk_files.append(files)
        for name in files:
            count += 1
    flat = list(itertools.chain.from_iterable(walk_files))
    print(f'{len(flat)=}')
    return flat

def harvest_batterylab():
    logging.info("harvest_batterylab started")
    conn = connect_to_db(CONFIG)
    data_from_db = read_table(CONFIG.table,conn)
    files_in_db = data_from_db.FILE_NAME.values
    df_files_csv = files_in_csv() 
    list_files_csv = df_files_csv.file.values
    list_files_dir = files_in_folder(CONFIG.report_folder_roots[0])
    not_in_csv = [f for f in list_files_dir if f not in list_files_csv]
    logging.info(f"{len(not_in_csv)=}")
    for f in not_in_csv:
        if f in files_in_db:
            # not in csv, but in db, so add to csv
            logging.info(f'add file to csv {f}')
            new_to_file_list = pd.DataFrame([[f,True,True]],columns=['file','isReport','inDb'])
            df_files_csv = pd.concat([df_files_csv,new_to_file_list])
            df_files_csv.to_csv('file_list.csv',index=False)
        else:
            #file not in csv, nor db, add to db
            logging.info(f'add record to db {f}')
            data_to_db = parse_batterylab(CONFIG.report_folder_roots[0] + "\\",f) 
            print(f'{data_to_db=}') 
            cursor = conn.cursor()
            # Insert Dataframe into SQL Server:
            for _, row in data_to_db.iterrows():
                sql=f"""
                INSERT INTO {CONFIG.table}
                (DateTimeStamp,FILE_NAME,PART_NUMBER,SERIAL_NUMBER,OVERALL_RESULT,CAPACITY)
                VALUES (?,?,?,?,?,?)
                """
                cursor = cursor.execute(sql, row.DateTimeStamp,row.FILE_NAME, row.PART_NUMBER, row.SERIAL_NUMBER,row.OVERALL_RESULT,row.CAPACITY)
                print(cursor.rowcount)
            conn.commit()            
            cursor.close() 
    conn.close()
    logging.info("harvest_batterylab finished")  

if __name__ == "__main__":
    starttime = time.perf_counter()
    print('start harvest')
    try:
        harvest_batterylab()
    except BaseException as err:
        logging.critical(f"Unexpected {err=}, {type(err)=}")
        raise
    print('end harvest', time.perf_counter()-starttime)