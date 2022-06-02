from typing import Callable
from util.dateParsing import parse_date_string
import datetime


class parse_batterylab:
    def __init__(
        self, dName="doc/examples/", fName="141MIM04162G_4_26_20222_28_48 PM.html"
    ):
        self.DateTimeStamp = datetime.datetime(1900, 1, 1, 1, 1, 1, 1)
        self.FILE_NAME = fName
        self.PART_NUMBER = ""
        self.SERIAL_NUMBER = ""
        self.OVERALL_RESULT = ""
        self.CAPACITY = ""
        self.label_map: dict[str, tuple[str, list[Callable[[str], str]]]] = {
            "Battery Module :": ("PART_NUMBER", [self.rm_h_tags]),
            "Serial Number :": ("SERIAL_NUMBER", []),
            "Test Result :": ("OVERALL_RESULT", []),
            "Capacity (%) : ": ("CAPACITY", []),
        }

        with open(dName + fName) as f:
            lines = f.readlines()

        for idx, line in enumerate(lines):
            line = line.strip().replace("<BR>", "")
            self.handle_date(idx, line)
            for label, (prop, fns) in self.label_map.items():
                if (loc := line.find(label)) >= 0:
                    pn = self.extract_pn(line, label, loc)
                    for fn in fns:
                        pn = fn(pn)
                    setattr(self, prop, pn)

    def extract_pn(self, line: str, label: str, loc: int) -> str:
        return line[loc + len(label) + 1 :]

    def rm_h_tags(self, pn: str) -> str:
        return pn.replace("</H3>", "").replace("</TH>", "")

    def handle_date(self, idx: str, line: str) -> None:
        if 12 < idx < 18 and (dt := parse_date_string(line)).year > 2000:
            self.DateTimeStamp = dt


if __name__ == "__main__":
    print("start")
    df = parse_batterylab()
    print(df.CAPACITY)
