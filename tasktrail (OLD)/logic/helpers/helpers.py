from json import load, dump
from os import system, name
from os.path import join

def cc():
    system("cls" if name == "nt" else "clear")

class DataLoader:
    def __init__(self) -> None:
        self.data_filepath = join("tasktrail", "data", "data.json")

    def load_data(self) -> dict:
        try:
            with open(self.data_filepath) as f:
                return load(f)

        except FileNotFoundError:
            raise FileNotFoundError(f"File {self.data_filepath} not found.")
        
        except Exception as e:
            raise Exception(f"Error Loading data: {e}")
        
    def save_data(self, data: dict) -> None:
        try:
            with open(self.data_filepath) as f:
                dump(data, f)
        
        except FileNotFoundError:
            raise FileNotFoundError(f"file {self.data_filepath} not found.")
    
        except Exception as e:
            raise Exception(f"Error loading data: {e}")
        