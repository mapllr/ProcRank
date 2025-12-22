import subprocess
import platform
import pandas as pd 


class Extract:
    def __init__(self):
        self.os = ['Linux']

    def get_raw_data(self):
        if platform.system() in self.os:
            res = subprocess.run(
                    ['ps', '-eo', 'pid,%mem,comm'],
                    capture_output = True,
                    text=True
                )
            return res.stdout.splitlines()

        else:
            return "Os Not Supported"

    def open_csv(self, file_name_csv):
        return pd.read_csv(file_name_csv)
