from batterylab.parse import parse_batterylab


class TestParseBatterylab:
    df = parse_batterylab("doc/examples/", "141MIM04162G_4_26_20222_28_48 PM.html")

    def test_parse_batterylab_time(self):
        print(self.df)
        d = self.df.DateTimeStamp  # 4/26/2022 2:28 PM
        assert d.year == 2022
        assert d.month == 4
        assert d.day == 26
        assert d.hour == 14

    def test_parse_batterylab_file(self):
        assert self.df.FILE_NAME == "141MIM04162G_4_26_20222_28_48 PM.html"

    def test_parse_batterylab_part(self):
        assert self.df.PART_NUMBER == "Prius NiMH"

    def test_parse_batterylab_serial(self):
        assert self.df.SERIAL_NUMBER == "141MIM04162G"

    def test_parse_batterylab_result(self):
        assert self.df.OVERALL_RESULT == "Pass - Good"

    def test_parse_batterylab_capacity(self):
        assert self.df.CAPACITY == "71.909263"
