# import pytest
from merlin.parse import parse_merlin


class TestParseMerlin:
    pm = parse_merlin("doc/examples/", "BP22091002_-220331-125402.rtf")

    def test_parse_merlin_file(self):
        assert self.pm.FILE_NAME == "BP22091002_-220331-125402.rtf"

    def test_parse_merlin_part(self):
        assert self.pm.PART_NUMBER == "W600-TP204NR"

    def test_parse_merlin_serial(self):
        assert self.pm.SERIAL_NUMBER == "bp22090001"

    def test_parse_merlin_result(self):
        assert self.pm.OVERALL_RESULT == "Pass"
