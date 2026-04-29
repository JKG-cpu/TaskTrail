from .helpers import *

class Handler:
    def __init__(self, data: dict) -> None:
        self.data = data

        self.current_user = None
        self.user_data = None

    # Helpers
    def _grab_data(self, username: str) -> dict: return self.data.get(username)
    def _construct_variables(self) -> None: 
        self.user_data = self._grab_data(self.current_user)

    # Login / Sign out
    def sign_out(self) -> None: 
        self.current_user, self.user_data = None, None

    def log_in(self, username: str, password: str) -> bool: 
        data = self.data.get(username, None)

        if data is None:
            return False
    
        # Add Encryption later?
        pswd = data["password"]

        if password == pswd:
            self.current_user = username
            self._construct_variables()
            return True

        else:
            return False

    # Grabbing data
    def get_user(self) -> str: return self.current_user

    def get_class_data(self) -> str | dict:
        if self.user_data is None:
            return "You need an account to have classes!"

        class_data = self.user_data.get("classes")

        if class_data is None:
            raise ValueError(f"Error grabbing class data! Current class data: {class_data}")

        return class_data

class Services:
    def __init__(self) -> None:
        self.data_loader = DataLoader()
        self.data = self.data_loader.load_data()
    
        self.handler = Handler(self.data)
    
    # Login
    def login(self, username: str, password: str) -> bool:
        return self.handler.log_in(username = username, password = password)

    def sign_out(self) -> None:
        self.handler.sign_out()

    # Getting Data
    def get_class_data(self) -> str | dict:
        return self.handler.get_class_data()

    def get_username(self) -> str: 
        return self.handler.get_user()
