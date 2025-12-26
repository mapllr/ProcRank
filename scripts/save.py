import datetime
import os 


class Save:
    def __init__(self):
        self.save_path = "garbage/" 
        self.file_name = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M:%S")

    def save_csv(self, raw_data):
        if not os.path.exists(self.save_path): 
            os.mkdir(self.save_path)

        with open(f"{self.save_path}{self.file_name}.csv", "w") as file:
            for sen in raw_data:
                parts = sen.split()
                data = f"{parts[0]},{parts[1]},{parts[2]}"
                file.write(f"{data}\n")
        return f"{self.save_path}{self.file_name}.csv"
