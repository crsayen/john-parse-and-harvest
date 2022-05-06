import pytest
from datetime import datetime
import time
from dateParsing import parse_date_string
from dateParsing import battlab_date_from_filename


def test_filetime():
    name = "BP22091002_-220331-125402.rtf"
    d = battlab_date_from_filename(name)
    assert d.year == 2022
    assert d.month == 3
    assert d.day == 31
    assert d.hour == 12

def test_date_from_batt_record_good():  
    dt = parse_date_string('<TH ALIGN="LEFT"><H3>4/26/2022 2:28 PM</H3></TH>')
    assert dt.year == 2022
    assert dt.month == 4
    assert dt.day == 26
    assert dt.hour == 14

def test_date_from_batt_record_bogus():  
    dt = parse_date_string('<TH ALIGN="CENTER"><H3>Battery Module : Prius NiMH</H3></TH>')
    assert dt.year == 1
    assert dt.month == 1
    assert dt.day == 1
    assert dt.hour == 1
    
if __name__ == "__main__":
    starttime = time.perf_counter()
    test_date_from_batt_record()

    print('end harvest', time.perf_counter()-starttime)