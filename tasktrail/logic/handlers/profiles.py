from ..helpers import *

class ProfileHandler:
    def __init__(self, data: dict) -> None:
        self.data = data

        self.current_user = None
        self.user_data = None

    # Helpers
    def _grab_data(self, username: str) -> dict: return self.data.get(username)
    def _construct_variables(self) -> None: self.user_data = self._grab_data(self.current_user)

    # Callables
    def sign_out(self) -> None: self.current_user, self.user_data = None, None
    def get_user(self) -> str: return self.current_user if self.current_user != None else "Guest"
    
    def log_in(self, username: str, password: str) -> int: 
        data = self.data.get(username, None)

        if data is None:
            return 0
    
        # Add Encryption later?
        pswd = data["password"]

        if password == pswd:
            self.current_user = username
            self._construct_variables()
            return 1

        else:
            return 0

