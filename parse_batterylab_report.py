from cmath import nan
import pandas as pd
from dateParsing import parse_date_string
import datetime
def parse_batterylab(dName='doc/examples/',fName='141MIM04162G_4_26_20222_28_48 PM.html'):
    # d = {'time':[nan],'file':["None"],'PART_NUMBER':['None'],'SERIAL_NUMBER':['None'],'OVERALL_RESULT':['None']}
    df = pd.DataFrame(columns=['DateTimeStamp','FILE_NAME','PART_NUMBER','SERIAL_NUMBER','OVERALL_RESULT','CAPACITY'])
    df.loc[0]=[datetime.datetime(1900,1,1,1,1,1,1),fName,'','','','']
    with open(dName + fName) as f:
        lines = f.readlines()
    
    for idx, line in enumerate(lines):
        line = line.strip()
        line = line.replace('<BR>', '')
        print(f'{line=}')

        if 12 < idx < 18:
            dt = parse_date_string(line)
            if dt.year > 2000:
                df.at[0,'DateTimeStamp'] = dt
                print(df)
                  
        s = 'PART NUMBER:'
        if (loc:=line.find(s)) >=0:
            pn = line[loc + len(s) + 1:]
            print(f'{pn=}')
            df.at[0,'PART_NUMBER'] = pn
            
        s = 'Serial Number :'
        if (loc:=line.find(s)) >=0:
            print('serial number line', line)
            pn = line[loc + len(s) + 1:]
            print(f'{pn=}')
            df.at[0,'SERIAL_NUMBER'] = pn

        s = 'Test Result :'
        if (loc:=line.find(s)) >=0:
            pn = line[loc + len(s) + 1:]
            print(f'{pn=}')
            df.at[0,'OVERALL_RESULT'] = pn
            
        s = 'Capacity (%) : '
        if (loc:=line.find(s)) >=0:
            pn = line[loc + len(s) + 1:]
            print(f'{pn=}')
            df.at[0,'CAPACITY'] = pn            
    # print(df)
    return df

if __name__ == "__main__":
    print('start')
    df = parse_batterylab()
    print(df)