from tests.test_datetime import battlab_date_from_filename


class parse_merlin:
    def __init__(self, dName="doc/examples/", fName="BP22091002_-220331-125402.rtf"):
        self.DateTimeStamp = ""
        self.FILE_NAME = ""
        self.PART_NUMBER = ""
        self.SERIAL_NUMBER = ""
        self.OVERALL_RESULT = ""
        # # print("parse_merlin", dName,fName)
        # # d = {'time':[nan],'file':["None"],'PART_NUMBER':['None'],'SERIAL_NUMBER':['None'],'OVERALL_RESULT':['None']}
        # df = pd.DataFrame(columns=['DateTimeStamp','FILE_NAME','PART_NUMBER','SERIAL_NUMBER','OVERALL_RESULT'])
        if fName[-11] == "-":
            ftime = battlab_date_from_filename(fName)
        self.DateTimeStamp = ftime
        self.FILE_NAME = fName
        with open(dName + fName) as f:
            lines = f.readlines()

        for line in lines:
            line = line.strip()
            s = "PART NUMBER:"

            if (loc := line.find(s)) >= 0:
                pn = line[loc + len(s) + 1 :]
                # print(f'{pn=}')
                self.PART_NUMBER = pn

            s = "SERIAL NUMBER:"
            if (loc := line.find(s)) >= 0:
                pn = line[loc + len(s) + 1 :]
                # print(f'{pn=}')
                self.SERIAL_NUMBER = pn

            s = "Overal Result ="
            if (loc := line.find(s)) >= 0:
                pn = line[loc + len(s) + 1 :]
                # print(f'{pn=}')
                self.OVERALL_RESULT = pn

            s = "Overall Result ="
            if (loc := line.find(s)) >= 0:
                pn = line[loc + len(s) + 1 :]
                # print(f'{pn=}')
                self.OVERALL_RESULT = pn


if __name__ == "__main__":
    print("start")
    for _ in range(1):
        df = parse_merlin()
        print(df.OVERALL_RESULT)
        if df.OVERALL_RESULT != "Pass":
            print(df)
