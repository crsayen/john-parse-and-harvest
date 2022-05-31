
# import pytest
from parse_merlin_report import parse_merlin


def test_parse_merlin_file():
    print("start test")
    pm = parse_merlin('doc/examples/','BP22091002_-220331-125402.rtf')
    # assert df['FILE_NAME'][0] == 'BP22091002_-220331-125402.rtf'
    assert pm.FILE_NAME == 'BP22091002_-220331-125402.rtf'

def test_parse_merlin_part():
    pm = parse_merlin('doc/examples/','BP22091002_-220331-125402.rtf')
    assert pm.PART_NUMBER == 'W600-TP204NR'
    
def test_parse_merlin_serial():
    pm = parse_merlin('doc/examples/','BP22091002_-220331-125402.rtf')
    assert pm.SERIAL_NUMBER == 'bp22090001'

def test_parse_merlin_result():
    pm = parse_merlin('doc/examples/','BP22091002_-220331-125402.rtf')
    assert pm.OVERALL_RESULT == "Pass"        
    
