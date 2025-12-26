from scripts.extract import Extract
from scripts.save import Save
from scripts.convert import Convert
from scripts.chart import Chart


class Main:
    def __init__(self):
        self.extract  = Extract()
        self.save     = Save()
        self.convert  = Convert()
        self.chart    = Chart()

        self.raw_data = self.extract.get_raw_data()
        self.file_name_csv = self.save.save_csv(self.raw_data)
        self.df = self.extract.open_csv(self.file_name_csv)

        self.mem, self.comm = self.convert.nparr_sort(self.df["%MEM"], self.df["COMMAND"])

    def main(self):
        self.chart.bar(self.comm[-20:], self.mem[-20:])

if __name__ == "__main__":
    Main().main()
