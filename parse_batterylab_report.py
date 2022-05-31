from cmath import nan
import pandas as pd
from dateParsing import parse_date_string
import datetime

class parse_batterylab:
    def __init__(self,dName='doc/examples/',fName='141MIM04162G_4_26_20222_28_48 PM.html'):
        self.DateTimeStamp = datetime.datetime(1900,1,1,1,1,1,1)
        self.FILE_NAME = fName
        self.PART_NUMBER = ''
        self.SERIAL_NUMBER = ''
        self.OVERALL_RESULT = ''
        self.CAPACITY = ''

        with open(dName + fName) as f:
            lines = f.readlines()
        
        for idx, line in enumerate(lines):
            line = line.strip()
            line = line.replace('<BR>', '')
            print(f'{line=}')

            if 12 < idx < 18:
                dt = parse_date_string(line)
                if dt.year > 2000:
                    self.DateTimeStamp = dt
                    print(dt)
                    
            s = 'Battery Module :'
            if (loc:=line.find(s)) >=0:
                pn = line[loc + len(s) + 1:]
                pn = pn.replace("</H3>","").replace("</TH>","")
                print(f'{pn=}')
                self.PART_NUMBER = pn
                
            s = 'Serial Number :'
            if (loc:=line.find(s)) >=0:
                print('serial number line', line)
                pn = line[loc + len(s) + 1:]
                print(f'{pn=}')
                self.SERIAL_NUMBER = pn

            s = 'Test Result :'
            if (loc:=line.find(s)) >=0:
                pn = line[loc + len(s) + 1:]
                print(f'{pn=}')
                self.OVERALL_RESULT = pn
                
            s = 'Capacity (%) : '
            if (loc:=line.find(s)) >=0:
                pn = line[loc + len(s) + 1:]
                print(f'{pn=}')
                self.CAPACITY = pn            

if __name__ == "__main__":
    print('start')
    df = parse_batterylab()
    print(df.CAPACITY)