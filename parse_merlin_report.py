from cmath import nan
import pandas as pd

def parse_merlin(dName='doc/examples/',fName='BP22091002_-220331-125402.rtf'):
    print("parse_merlin", dName,fName)
    # d = {'time':[nan],'file':["None"],'PART_NUMBER':['None'],'SERIAL_NUMBER':['None'],'OVERALL_RESULT':['None']}
    df = pd.DataFrame(columns=['time','FILE_NAME','PART_NUMBER','SERIAL_NUMBER','OVERALL_RESULT'])
    df.loc[0]=['',fName,'','','']
    with open(dName + fName) as f:
        lines = f.readlines()
    
    for line in lines:
        line = line.strip()
        s = 'PART NUMBER:'

        if (loc:=line.find(s)) >=0:
            pn = line[loc + len(s) + 1:]
            print(f'{pn=}')
            df['PART_NUMBER'][0] = pn
            
        s = 'SERIAL NUMBER:'
        if (loc:=line.find(s)) >=0:
            pn = line[loc + len(s) + 1:]
            print(f'{pn=}')
            df['SERIAL_NUMBER'][0] = pn

        s = 'Overal Result ='
        if (loc:=line.find(s)) >=0:
            pn = line[loc + len(s) + 1:]
            print(f'{pn=}')
            df['OVERALL_RESULT'][0] = pn
            
        s = 'Overall Result ='
        if (loc:=line.find(s)) >=0:
            pn = line[loc + len(s) + 1:]
            print(f'{pn=}')
            df['OVERALL_RESULT'][0] = pn            
    # print(df)
    return df

if __name__ == "__main__":
    print('start')
    df = parse_merlin()
    print(df)