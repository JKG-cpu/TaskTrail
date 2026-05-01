from .helpers import FileHandler

__all__ = [
    "Services"
]

BASE_TABS = [
    {
        "type": "home",
        "name": "HomePage",
        "static": True,
        "order": 1
    },
    {
        "type": "settings",
        "name": "Settings",
        "static": True,
        "order": 2
    }
]

class ProfileHandler:
    def __init__(self) -> None:
        self.file_handler = FileHandler()
        self.data = self.file_handler.load_data()

        self.current_user = None
        self.current_profile = None
        self.current_data = None

    # Helpers
    def _construct_variables(self, username: str) -> None:
        self.current_user = username
        self.current_data = self.data.get(username)
        
        profiles = self.current_data["profiles"]
        for profile in profiles:
            if profiles[profile]["settings"]["last_used"]:
                self.current_profile = profile
                break
        else:
            raise ValueError("No profile was set with a last_used in settings!")

    def _set_last_used(self) -> None:
        for profile in self.current_data["profiles"].values():
            profile["settings"]["last_used"] = False
        self.current_data["profiles"][self.current_profile]["settings"]["last_used"] = True

    # Selecting Data
    def login(self, username: str, password: str) -> bool:
        data = self.data.get(username)

        if data is None:
            return False

        pswd = data["password"]

        if password == pswd:
            self._construct_variables(username)
            return True
    
        else:
            return False

    def signout(self) -> None:
        self.current_user = None
        self.current_profile = None
        self.current_data = None

    def select_profile(self, new_profile: str) -> bool | int:
        if self.current_data is None:
            return 0
    
        profile = self.current_data["profiles"].get(new_profile)

        if profile is None:
            return False
    
        self.current_profile = new_profile
        self._set_last_used()

    # Getting Data
    def get_tabs(self) -> list[dict]:
        if self.current_data is None:
            return BASE_TABS

        tabs = self.current_data["profiles"][self.current_profile]["tabs"]

        return sorted(tabs, key=lambda tab: tab["order"])

class Services:
    def __init__(self) -> None:
        self.profile_handler = ProfileHandler()
    
    def login(self, username: str, password: str) -> bool:
        return self.profile_handler.login(username, password)

    def signout(self) -> None:
        self.profile_handler.signout()
    
    def select_profile(self, profile: str) -> bool | int:
        return self.profile_handler.select_profile(profile)

    def get_tabs(self) -> list[dict]:
        return self.profile_handler.get_tabs()
    