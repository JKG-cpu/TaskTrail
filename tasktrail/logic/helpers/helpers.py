from json import load, dump
from os.path import join
from os import system, name

__all__ = [
    "cc", "FileHandler"
]

def cc():
    system("cls" if name == "nt" else "clear")

class FileHandler:
    def __init__(self):
        self.file_path = join("tasktrail", "data", "data.json")
    
    def load_data(self) -> dict:
        try:
            with open(self.file_path, "r") as f:
                return load(f)
        
        except FileNotFoundError as f:
            raise FileNotFoundError(f"Filepath {self.file_path} has not been found: {f}")
    
        except Exception as e:
            raise Exception(f"Error loading data from {self.file_path}: {e}")
    
    def save(self, data: dict) -> None:
        try:
            with open(self.file_path, "w") as f:
                dump(data, f)
        
        except FileNotFoundError as f:
            raise FileNotFoundError(f"Filepath {self.file_path} has not been found: {f}")
    
        except Exception as e:
            raise Exception(f"Error saving data to {self.file_path}: {e}")
    

