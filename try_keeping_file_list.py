import pandas as pd
import os
import shutil
from db_connect import read_table,connect_to_db
from parse_merlin_report import parse_merlin
import CONFIG
import time

if __name__ == "__main__":
    starttime = time.perf_counter()
    print('start harvest')
    # harvest_merlin()
    count = 0
    file_list = pd.read_csv('file_list.csv')
    to_file_list = []    
    for root, dirs, files in os.walk('c:\\work\\NI dyno code', topdown=False):
        for name in files:
            count += 1
            # print(root,name)
            # print(os.path.join(root, name))
            if not (name in file_list.file.values):
                print(f'{name=}')
                print([root,name])
                d = {'dir': [root], 'file': [name]}
                print(d)
                one_file = pd.DataFrame(d)
                print(one_file)
                to_file_list.append([root, name])
            
        for name in dirs:
            pass
            # count += 1
            # print(root,name)
            # print(os.path.join(root, name))
    # to_file_list.to_csv('file_list.csv')
    print(to_file_list)
    df = pd.DataFrame(to_file_list,columns=['dir','file'])
    print(df)
    df = pd.concat([file_list,df])
    df.to_csv('file_list.csv',index=False)
    print('end harvest', count, time.perf_counter()-starttime)