from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Button

class SettingsPage(Screen):
    CSS_PATH = ["../styles/base.tcss"]

    def compose(self) -> ComposeResult:
        yield Button("Go Back", classes = "toHome")