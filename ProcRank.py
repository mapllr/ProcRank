from scripts.extract_process_data import Extract
from scripts.save_process_data import Save


class Main:
    def __init__(self):
        self.extract  = Extract()
        self.save     = Save()
        self.raw_data = self.extract.get_raw_data()

    def main(self):
        self.save.save_csv(self.raw_data)

        

if __name__ == "__main__":
    Main().main()
