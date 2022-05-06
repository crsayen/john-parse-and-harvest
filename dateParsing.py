from dateutil.parser import parse
from datetime import datetime
import re

def battlab_date_from_filename(name):
    s = name[-17:-4]
    d = datetime.strptime(s,"%y%m%d-%H%M%S")   
    return d 

def parse_date_string(s):
    p = re.compile(r"\d{1,2}[\/]\d{1,2}[\/]\d{4}[ ]\d{1,2}[:]\d{1,2}")
    m = p.search(s)
    if m is None:
        return datetime(1900,1,1,1,1,1,1)
    
    dt = parse(s, dayfirst=False, ignoretz=True, fuzzy=True)
    return dt

if __name__ == "__main__":
    dt = parse_date_string('<TH ALIGN="LEFT"><H3>4/26/2022 2:28 PM</H3></TH>')
    dt = parse_date_string('<TH ALIGN="CENTER"><H3>Battery Module : Prius NiMH</H3></TH>')