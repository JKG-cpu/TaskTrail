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

BASE_ACCOUNT = {
    "password": "",
    "profiles": {
        "Profile 1": {
            "tabs": BASE_TABS,
            "settings": {
                "auto_delete_todo_lists": True,
                "school_mode": True
            },
            "last_used": True
        }
    }
}

class ProfileHandler:
    def __init__(self, file_handler: FileHandler, data: dict) -> None:
        self.file_handler = file_handler
        self.data: dict[str, dict] = data

        self.current_user: str | None = None
        self.current_profile: str | None = None
        self.current_data: dict[str, str | dict] | None = None

    # Helpers
    def _construct_variables(self, username: str) -> None:
        self.current_user = username
        self.current_data = self.data.get(username)
        
        profiles = self.current_data["profiles"]
        for profile in profiles:
            if profiles[profile]["last_used"]:
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

    def create_account(self, username: str, password: str) -> bool:
        new_account = BASE_ACCOUNT.copy()
        new_account["password"] = password

        user = self.data.get(username)

        if user:
            return False

        self.data[username] = new_account
        self.file_handler.save(self.data)
        return True

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

    def is_loggedin(self) -> bool: return self.current_user != None and self.current_profile != None
    def get_username(self) -> str | None: return self.current_user
    def get_profile(self) -> str | None: return self.current_profile

class SettingsHandler:
    def __init__(self, file_handler: FileHandler, data: dict):
        self.file_handler = file_handler
        self.data = data

        self.user: str | None = None
        self.user_data: dict | None = None

    # Change
    def reset(self) -> None: 
        self.user = None
        self.user_data = None

    def select_user(self, user: str) -> None: 
        self.user = user
        self.user_data = self.data.get(self.user)

    def update_settings(self, selected_settings: list, profile_name: str) -> None:
        profile_settings = self.user_data.get("profiles").get(profile_name).get("settings")
        for setting in profile_settings:
            if setting in selected_settings:
                profile_settings[setting] = True
            
            else:
                profile_settings[setting] = False

        self.file_handler.save(self.data)

    def get_settings(self, profile_name: str) -> list[tuple[str, str, bool]]:
        profile = self.user_data.get("profiles").get(profile_name)
        settings: dict[str, bool] = profile.get("settings")
        return [
            (setting.replace("_", " ").title(), setting, settings[setting]) for setting in settings
        ]

class PageHandler:
    def __init__(self, file_handler: FileHandler, data: dict):
        self.file_handler = file_handler
        self.data = data

        self.user: str | None = None
        self.profile: str | None = None
        self.profile_data: dict[str, list | dict | bool] | None = None

    def reset(self) -> None: self.user, self.profile, self.profile_data = None, None, None

    def set_variables(self, user: str, profile: str) -> None:
        self.user = user
        self.profile = profile
        self.profile_data = self.data.get(user).get("profiles").get(profile)

    def get_data(self, page_id: str) -> dict | None:
        tabs = self.profile_data.get("tabs")

        if not tabs:
            return None

        for tab in tabs:
            if str(tab["order"]) == page_id:
                return tab["data"]
        
        else:
            raise ValueError(f"Improper id for {page_id}")

class Services:
    def __init__(self) -> None:
        self.file_handler = FileHandler()
        self.data = self.file_handler.load_data()

        self.profile_handler = ProfileHandler(self.file_handler, self.data)
        self.settings_handler = SettingsHandler(self.file_handler, self.data)
        self.page_handler = PageHandler(self.file_handler, self.data)
    
    # Select / Change
    def login(self, username: str, password: str) -> bool:
        output = self.profile_handler.login(username, password)

        if output:
            self.settings_handler.select_user(username)
            self.page_handler.set_variables(username, self.profile_handler.get_profile())
            
        return output

    def create_account(self, username: str, password: str) -> bool:
        return self.profile_handler.create_account(username, password)

    def signout(self) -> None:
        self.profile_handler.signout()
        self.settings_handler.reset()

    def select_profile(self, profile: str) -> bool | int:
        return self.profile_handler.select_profile(profile)

    def update_settings(self, selected_settings: list, profile: str) -> None:
        return self.settings_handler.update_settings(selected_settings, profile) 

    # Get
    def get_tabs(self) -> list[dict]:
        return self.profile_handler.get_tabs()
    
    def get_username(self) -> str | None:
        return self.profile_handler.get_username()

    def get_profile(self) -> str | None:
        return self.profile_handler.get_profile()

    def get_settings(self, profile_name: str) -> list[tuple[str, str, bool]] | None:
        return self.settings_handler.get_settings(profile_name = profile_name)

    def get_page_data(self, page_id: str) -> dict | None:
        return self.page_handler.get_data(page_id)

    def is_loggedin(self) -> bool:
        return self.profile_handler.is_loggedin()
