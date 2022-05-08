import pandas as pd
import os
import shutil
from db_connect import read_table,connect_to_db
from parse_merlin_report import parse_merlin
import CONFIG_batterylab
import time
import itertools

if __name__ == "__main__":
    starttime = time.perf_counter()
    print('start harvest')
    # harvest_merlin()
    count = 0
    try:
        file_list = pd.read_csv('file_list.csv')
    except:
        print('read csv error')  #start with blank list
        file_list = pd.DataFrame([],columns=['dir','file','isReport','inDb'])
    print('end harvest', count, time.perf_counter()-starttime)    
    to_file_list = []    
    walk_files = []
    for root, dirs, files in os.walk('c:\\work\\pyHarvest', topdown=False):
        walk_files.append(files)
        for name in files:
            count += 1
            # print(root,name)
            # print(os.path.join(root, name))
            # if not (name in file_list.file.values):
            #     print(f'{name=}')
            #     print([root,name])
            #     d = {'dir': [root], 'file': [name]}
            #     print(d)
            #     one_file = pd.DataFrame(d)
            #     print(one_file)
            #     to_file_list.append([root, name, False, False])
            
        for name in dirs:
            pass
            # count += 1
            # print(root,name)
            # print(os.path.join(root, name))
    # to_file_list.to_csv('file_list.csv')
    print(f'{len(walk_files)=}')
    flat = list(itertools.chain.from_iterable(walk_files))
    print(f'{len(flat)=}')
    f_list = file_list.file.values
    x = [f for f in flat if f not in f_list ]
    print(f'{len(x)=}')
    print(f'{len(file_list)=}')
    print(f'{x=}')
    print(f'{f_list=}')
    
 
    print('end harvest', count, time.perf_counter()-starttime)
    print(to_file_list)
    new_to_file_list = pd.DataFrame(to_file_list,columns=['dir','file','isReport','inDb'])
    print(f'{new_to_file_list=}')
    df = pd.concat([file_list,new_to_file_list])
    df.to_csv('file_list.csv',index=False)
    print('end harvest', count, time.perf_counter()-starttime)