import pandas
import os
import shutil
from test_db_connect import read_table,connect_to_db
import parse_merlin


def harvest_merlin():
    server = 'JOHNLAPTOP\SQLEXPRESS'
    db = 'batterylab_finaltest'
    conn = connect_to_db(server,db)
    table = "MERLIN"
    df = read_table(table,conn)
    conn.close
    f_loc = 'C:\\work\\pyHarvest\\reports\\'
    files = os.listdir(f_loc)
    files = [f for f in files if os.path.isfile(f_loc + f)]
    print(f'{files=}')
    for file in files:
        print(df['FILE_NAME'].values)
        already_in_db = (file in df.FILE_NAME.values)
        print(f'{already_in_db=}')
        if already_in_db:
            source = f_loc + file
            dest = f_loc + "processed\\" + file
            shutil.move(source,dest)
        else:
            #copy to db
            print(f_loc,'+',file)
            df = parse_merlin.parse_merlin(f_loc,file)
            print("data to db", df)
            cursor = conn.cursor()
            # Insert Dataframe into SQL Server:
            for index, row in df.iterrows():
                sql=f"""
                INSERT INTO {table} (time,FILE_NAME,PART_NUMBER,SERIAL_NUMBER,OVERALL_RESULT)
                VALUES (?,?,?,?,?)
            """
                cursor.execute(sql, row.time,row.FILE_NAME, row.PART_NUMBER, row.SERIAL_NUMBER,row.OVERALL_RESULT)
            conn.commit()            
            cursor.close()
            conn.commit()
           

if __name__ == "__main__":
    print('start')
    harvest_merlin()