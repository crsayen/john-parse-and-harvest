
# import pytest
from parse_merlin_report import parse_merlin


def test_parse_merlin_file():
    print("start test")
    df = parse_merlin('doc/examples/','BP22091002_-220331-125402.rtf')
    assert df['FILE_NAME'][0] == 'BP22091002_-220331-125402.rtf'

def test_parse_merlin_part():
    df = parse_merlin('doc/examples/','BP22091002_-220331-125402.rtf')
    assert df['PART_NUMBER'][0] == 'W600-TP204NR'
    
def test_parse_merlin_serial():
    df = parse_merlin('doc/examples/','BP22091002_-220331-125402.rtf')
    assert df['SERIAL_NUMBER'][0] == 'bp22090001'

def test_parse_merlin_result():
    df = parse_merlin('doc/examples/','BP22091002_-220331-125402.rtf')
    assert df['OVERALL_RESULT'][0] == "Pass"        
    
