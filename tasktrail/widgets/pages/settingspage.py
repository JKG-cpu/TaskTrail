from textual.app import ComposeResult
from textual.widgets import Button, Static, Label

class SettingsPage(Static):
    CSS_PATH = ["../styles/base.tcss", "../styles/settings.tcss"]

    def __init__(self, username: str) -> None:
        super().__init__()
        self.username = username

    def compose(self) -> ComposeResult:
        if self.username:
            yield Label(f"Hello, {self.username}")
            yield Button("Sign out", classes = "signOut")

        else:
            yield Label("You are not logged in!")
            yield Button("Login", classes = "login")
