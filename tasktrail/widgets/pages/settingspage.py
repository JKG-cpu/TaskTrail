from textual.app import ComposeResult
from textual.widgets import Button, Static

class SettingsPage(Static):
    CSS_PATH = ["../styles/base.tcss", "../styles/settings.tcss"]

    def compose(self) -> ComposeResult:
        yield Button("Go Back", classes = "toHome")
        yield Button("Login", classes = "login")
        