import pytest
from datetime import datetime

def battlab_date_from_filename(name):
    s = name[-17:-4]
    d = datetime.strptime(s,"%y%m%d-%H%M%S")   
    return d 

def test_filetime():
    name = "BP22091002_-220331-125402.rtf"
    d = battlab_date_from_filename(name)
    assert d.year == 2022
    assert d.month == 3
    assert d.day == 31
    assert d.hour == 12
    