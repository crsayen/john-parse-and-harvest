from cmath import nan
import pandas as pd
import time
import datetime
import os
from test_datetime import battlab_date_from_filename
def parse_merlin(dName='doc/examples/',fName='BP22091002_-220331-125402.rtf'):
    print("parse_merlin", dName,fName)
    # d = {'time':[nan],'file':["None"],'PART_NUMBER':['None'],'SERIAL_NUMBER':['None'],'OVERALL_RESULT':['None']}
    df = pd.DataFrame(columns=['DateTimeStamp','FILE_NAME','PART_NUMBER','SERIAL_NUMBER','OVERALL_RESULT'])
    if fName[-11] == '-':
        ftime = battlab_date_from_filename(fName)
    df.loc[0]=[ftime,fName,'','','']
    with open(dName + fName) as f:
        lines = f.readlines()
    
    for line in lines:
        line = line.strip()
        s = 'PART NUMBER:'

        if (loc:=line.find(s)) >=0:
            pn = line[loc + len(s) + 1:]
            print(f'{pn=}')
            df.loc[0,'PART_NUMBER'] = pn
            
        s = 'SERIAL NUMBER:'
        if (loc:=line.find(s)) >=0:
            pn = line[loc + len(s) + 1:]
            print(f'{pn=}')
            df.loc[0, 'SERIAL_NUMBER'] = pn

        s = 'Overal Result ='
        if (loc:=line.find(s)) >=0:
            pn = line[loc + len(s) + 1:]
            print(f'{pn=}')
            df.loc[0,'OVERALL_RESULT'] = pn
            
        s = 'Overall Result ='
        if (loc:=line.find(s)) >=0:
            pn = line[loc + len(s) + 1:]
            print(f'{pn=}')
            df.loc[0,'OVERALL_RESULT'] = pn            
    # print(df)
    return df

if __name__ == "__main__":
    print('start')
    df = parse_merlin()
    print(df)