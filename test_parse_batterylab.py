# import pandas as pd
from parse_batterylab_report import parse_batterylab


def test_parse_batterylab_time():
    df = parse_batterylab('doc/examples/','141MIM04162G_4_26_20222_28_48 PM.html')
    print(df)
    d = df.at[0, 'DateTimeStamp']     #4/26/2022 2:28 PM
    assert d.year == 2022
    assert d.month == 4
    assert d.day == 26
    assert d.hour == 14    

def test_parse_batterylab_file():
    print("start test")
    df = parse_batterylab('doc/examples/','141MIM04162G_4_26_20222_28_48 PM.html')
    assert df.at[0,'FILE_NAME'] == '141MIM04162G_4_26_20222_28_48 PM.html'

def test_parse_batterylab_part():
    df = parse_batterylab('doc/examples/','141MIM04162G_4_26_20222_28_48 PM.html')
    assert df.at[0,'PART_NUMBER'] == ''
    
def test_parse_batterylab_serial():
    df = parse_batterylab('doc/examples/','141MIM04162G_4_26_20222_28_48 PM.html')
    assert df.at[0,'SERIAL_NUMBER'] == '141MIM04162G'

def test_parse_batterylab_result():
    df = parse_batterylab('doc/examples/','141MIM04162G_4_26_20222_28_48 PM.html')
    assert df.at[0,'OVERALL_RESULT'] == "Pass - Good"  
    
def test_parse_batterylab_capacity():
    df = parse_batterylab('doc/examples/','141MIM04162G_4_26_20222_28_48 PM.html')
    assert df.at[0,'CAPACITY'] == "71.909263"          

if __name__ == "__main__":    
    test_parse_batterylab_time()