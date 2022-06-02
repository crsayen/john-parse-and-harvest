# from cmath import nan
import pandas as pd
from dataclasses import dataclass,field

from sqlalchemy import false
from dateParsing import parse_date
import datetime

@dataclass
class parse_focusev_eol:
    folder: str
    FILE_NAME: str
    AVERAGE_SPEED: float = field(init=False)
    AVERAGE_TORQUE: float = field(init=False)
    SERIAL_NUMBER : str = field(init = False)
    VIBRATION : float = field(init=False)
    DateTimeStamp :str = field(init=False) #datetime.datetime(1900,1,1,1,1,1,1).__str__()

    def __post_init__(self):
        df = pd.read_csv(self.folder + self.FILE_NAME,sep='\t')

        # print(df)
        # pass
        
        mask = 3495 < df['Average Speed'].astype(float) < 3505
        df['cumsum'] = df[mask].cumsum
        print(df['cumsum','Average Speed'])
        
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
    df = parse_focusev_eol('doc/examples/','7GB372632A9435_9456_2022-05-18-1426.dat')
    print(df)
    pass