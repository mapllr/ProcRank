from scripts.extract_process_data import Extract
from scripts.save_process_data import Save
from scripts.convert_set_data import Convert
from scripts.make_plot import Plot


class Main:
    def __init__(self):
        self.extract  = Extract()
        self.save     = Save()
        self.convert  = Convert()
        self.plot    = Plot()

        self.raw_data = self.extract.get_raw_data()
        self.file_name_csv = self.save.save_csv(self.raw_data)
        self.df = self.extract.open_csv(self.file_name_csv)

        self.mem, self.comm = self.convert.nparr(self.df["%MEM"], self.df["COMMAND"])

    def main(self):
        pass


if __name__ == "__main__":
    Main().main()
