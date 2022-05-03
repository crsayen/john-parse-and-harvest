
# import pytest
from parse_batterylab_report import parse_batterylab


def test_parse_batterylab_file():
    print("start test")
    df = parse_batterylab('doc/examples/','141MIM04162G_4_26_20222_28_48 PM.html')
    assert df['FILE_NAME'][0] == '141MIM04162G_4_26_20222_28_48 PM.html'

def test_parse_batterylab_part():
    df = parse_batterylab('doc/examples/','141MIM04162G_4_26_20222_28_48 PM.html')
    assert df['PART_NUMBER'][0] == ''
    
def test_parse_batterylab_serial():
    df = parse_batterylab('doc/examples/','141MIM04162G_4_26_20222_28_48 PM.html')
    assert df['SERIAL_NUMBER'][0] == '141MIM04162G'

def test_parse_batterylab_result():
    df = parse_batterylab('doc/examples/','141MIM04162G_4_26_20222_28_48 PM.html')
    assert df['OVERALL_RESULT'][0] == "Pass - Good"  
    
def test_parse_batterylab_capacity():
    df = parse_batterylab('doc/examples/','141MIM04162G_4_26_20222_28_48 PM.html')
    assert df['CAPACITY'][0] == "71.909263"          
    
