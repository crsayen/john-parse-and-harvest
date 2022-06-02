import pandas as pd
from pandas import DataFrame
import os
from util.db_connect import read_table, connect_to_db
from batterylab.parse import parse_batterylab
import config.batterylab as CONFIG
import time
import logging


def files_in_csv() -> DataFrame:
    try:
        file_list = pd.read_csv("file_list.csv")
    except:
        print("read csv error")  # start with blank list
        file_list = pd.DataFrame([], columns=["file", "isReport", "inDb"])
    return file_list


def files_in_folder(root_dir: str) -> list[str]:
    return [
        file
        for (root, dirs, files) in os.walk(root_dir, topdown=False)
        for file in files
    ]


def harvest_batterylab():
    logging.info("harvest_batterylab started")
    conn = connect_to_db(CONFIG)
    data_from_db = read_table(CONFIG.table, conn)
    data_from_db.to_csv("batterylab.csv")
    files_in_db = data_from_db.FILE_NAME.values
    df_files_csv = files_in_csv()
    list_files_csv = df_files_csv.file.values
    list_files_dir = files_in_folder(CONFIG.report_folder_roots[0])
    not_in_csv = [f for f in list_files_dir if f not in list_files_csv]
    logging.info(f"{len(not_in_csv)=}")
    for f in not_in_csv:
        if f in files_in_db:
            # not in csv, but in db, so add to csv
            logging.info(f"add file to csv {f}")
            new_to_file_list = pd.DataFrame(
                [[f, True, True]], columns=["file", "isReport", "inDb"]
            )
            df_files_csv = pd.concat([df_files_csv, new_to_file_list])
            df_files_csv.to_csv("file_list.csv", index=False)
        else:
            # file not in csv, nor db, add to db
            logging.info(f"add record to db {f}")
            bl_report = parse_batterylab(CONFIG.report_folder_roots[0] + "\\", f)
            # print(f'{bl_report=}')
            cursor = conn.cursor()
            # Insert into SQL Server:
            sql = f"""
                INSERT INTO {CONFIG.table}
                (DateTimeStamp,FILE_NAME,PART_NUMBER,SERIAL_NUMBER,OVERALL_RESULT,CAPACITY)
                VALUES (?,?,?,?,?,?)
                """
            cursor = cursor.execute(
                sql,
                bl_report.DateTimeStamp,
                bl_report.FILE_NAME,
                bl_report.PART_NUMBER,
                bl_report.SERIAL_NUMBER,
                bl_report.OVERALL_RESULT,
                bl_report.CAPACITY,
            )
            print(cursor.rowcount)
            conn.commit()
            cursor.close()
    conn.close()
    logging.info("harvest_batterylab finished")


if __name__ == "__main__":
    starttime = time.perf_counter()
    print(f"start harvest of report data to {CONFIG.server}")
    try:
        harvest_batterylab()
    except BaseException as err:
        logging.critical(f"Unexpected {err=}, {type(err)=}")
        raise
    print("end harvest", time.perf_counter() - starttime)
