# import pandas as pd
from parse_focusev_flash_report import parse_focusev_flash


def test_parse_date():
    df = parse_focusev_flash('doc/examples/','7GA370342A7724_2022-05-25_DETMainLog.rtf')
    print(df)
    #\viewkind4\uc1\pard\cf1\f0\fs17 Date: 2022-05-25     Time: 12:22:29 PM  (v9.0.1)\par
    assert df.DateTimeStamp == "2022-05-25 12:22:29"

def test_parse_file():
    print("start test")
    df = parse_focusev_flash('doc/examples/','7GA370342A7724_2022-05-25_DETMainLog.rtf')
    assert df.FILE_NAME == '7GA370342A7724_2022-05-25_DETMainLog.rtf'
   
def test_parse_serial():
    df = parse_focusev_flash('doc/examples/','7GA370342A7724_2022-05-25_DETMainLog.rtf')
    assert df.SERIAL_NUMBER == '7GA370342A7724'

def test_parse_flash_pass():
    df = parse_focusev_flash('doc/examples/','7GA370342A7724_2022-05-25_DETMainLog.rtf')
    assert df.SERVICE_FLASH_PASS == True  
    
def test_parse_resolver_offset():
    df = parse_focusev_flash('doc/examples/','7GA370342A7724_2022-05-25_DETMainLog.rtf')
    assert df.RESOLVER_OFFSET == "4.5715625"          

