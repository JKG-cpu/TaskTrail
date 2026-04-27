from .helpers import *
from .handlers import *

class Services:
    def __init__(self) -> None:
        self.data_loader = DataLoader()
        self.data = self.data_loader.load_data()
    
        self.profile_handler = ProfileHandler(self.data)