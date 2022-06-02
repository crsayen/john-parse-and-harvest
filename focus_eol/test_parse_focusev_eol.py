# import pandas as pd
from parse_focusev_flash_report import parse_focusev_flash
from pytest import approx

folder = 'doc/examples/'
file = '7GB372632A9435_9456_2022-05-18-1426.dat'

def test_parse_date():
    df = parse_focusev_flash(folder,file)
    print(df)
    assert df.DateTimeStamp == "05/18/2022 14:26:27"

def test_parse_file():
    print("start test")
    df = parse_focusev_flash(folder,file)
    assert df.FILE_NAME == file
   
def test_parse_serial():
    df = parse_focusev_flash(folder,file)
    assert df.SERIAL_NUMBER == '7GB372632A9435'

def test_parse_average_speed():
    df = parse_focusev_flash(folder,file)
    assert df.AVERAGE_SPEED == approx(3500,5)  

def test_parse_average_torque():
    df = parse_focusev_flash(folder,file)
    assert df.AVERAGE_TORQUE == approx(255,5)  
        
def test_parse_vibration():
    df = parse_focusev_flash(folder,file)
    assert df.VIBRATION == approx(3,1)      

