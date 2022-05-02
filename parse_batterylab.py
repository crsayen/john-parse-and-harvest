from cmath import nan
import pandas as pd

def parse_batterylab(dName='doc/examples/',fName='141MIM04162G_4_26_20222_28_48 PM.html'):
    # d = {'time':[nan],'file':["None"],'PART_NUMBER':['None'],'SERIAL_NUMBER':['None'],'OVERALL_RESULT':['None']}
    df = pd.DataFrame(columns=['time','FILE_NAME','PART_NUMBER','SERIAL_NUMBER','OVERALL_RESULT','CAPACITY'])
    df.loc[0]=['',fName,'','','','']
    with open(dName + fName) as f:
        lines = f.readlines()
    
    for line in lines:
        line = line.strip()
        line = line.replace('<BR>', '')
        print(f'{line=}')
        
        s = 'PART NUMBER:'

        if (loc:=line.find(s)) >=0:
            pn = line[loc + len(s) + 1:]
            print(f'{pn=}')
            df['PART_NUMBER'][0] = pn
            
        s = 'Serial Number :'
        if (loc:=line.find(s)) >=0:
            print('serial number line', line)
            pn = line[loc + len(s) + 1:]
            print(f'{pn=}')
            df['SERIAL_NUMBER'][0] = pn

        s = 'Test Result :'
        if (loc:=line.find(s)) >=0:
            pn = line[loc + len(s) + 1:]
            print(f'{pn=}')
            df['OVERALL_RESULT'][0] = pn
            
        s = 'Capacity (%) : '
        if (loc:=line.find(s)) >=0:
            pn = line[loc + len(s) + 1:]
            print(f'{pn=}')
            df['CAPACITY'][0] = pn            
    # print(df)
    return df

if __name__ == "__main__":
    print('start')
    df = parse_batterylab()
    print(df)