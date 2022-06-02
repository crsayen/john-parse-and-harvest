# from cmath import nan
# import pandas as pd
from dataclasses import dataclass,field

from sqlalchemy import false
from dateParsing import parse_date
import datetime

@dataclass
class parse_focusev_flash:
    folder: str
    FILE_NAME: str
    SERIAL_NUMBER: str = field(init=False)
    SERVICE_FLASH_PASS: str = field(init=False)
    RESOLVER_OFFSET : float = field(init = False)
    DateTimeStamp :str = field(init=False) #datetime.datetime(1900,1,1,1,1,1,1).__str__()

    def __post_init__(self):

        # self.DateTimeStamp = datetime.datetime(1900,1,1,1,1,1,1).__str__()
        # self.FILE_NAME = fName
        # self.SERIAL_NUMBER = fName.split('_')[0]
        # self.Average_Speed = ''
        # self.Average_Torque = ''
        # self.Vibration = ''
        foundC1A1 = False
        with open(self.folder + self.FILE_NAME) as f:
            lines = f.readlines()
        
        for idx, line in enumerate(lines):
            line = line.strip()
            line = line.replace('<BR>', '')
            # print(f'{line=}')
               
            s = " Date: "
            if (loc:=line.find(s)) >=0:
                start = loc + len(s)
                file_date = line[start:start + 10]
                s = "Time: "
                if (loc:=line.find(s)) >=0:
                    start = loc + len(s)
                    file_time = line[start:start+11]
                dt = file_date + " " + file_time
                self.DateTimeStamp = parse_date(dt).__str__()
               
            s = 'ECU Serial Number (GDX): '
            if (loc:=line.find(s)) >=0:
                print('serial number line', line)
                start = loc + len(s)
                SERIAL_NUMBER = line[start:start+14]
                print(f'{SERIAL_NUMBER=}')
                self.SERIAL_NUMBER = SERIAL_NUMBER

            s = 'Position Sensor Offset Value (GDX):'
            if (loc:=line.find(s)) >=0:
                rest = line[loc + len(s) + 1:]
                resolver_offset = rest.split(" ")[0]
                print(f'{resolver_offset=}')
                self.RESOLVER_OFFSET = resolver_offset
            
            if foundC1A1:
                foundC1A1 = False
                print(f'line after C1A1 {line=}')
                self.SERVICE_FLASH_PASS = "00 02 00 00 00 00 00" not in line
            
            s = 'DataIdentifier:  0xC1A1     Data Size: 7'
            if (loc:=line.find(s)) >=0:
                foundC1A1 = True
            
            
                
  

if __name__ == "__main__":
    print('start')
    df = parse_focusev_flash('doc/examples/','7GA370342A7724_2022-05-25_DETMainLog.rtf')
    print(df)
    pass