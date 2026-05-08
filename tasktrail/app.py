from textual.app import App
from textual.widgets import Static

from .screens import *

class TaskTrail(App):
    BINDINGS = [("q", "quit", "Quit TaskTrail")]
    SCREENS = {
        "Home": HomePage
    }

    def on_mount(self) -> None:
        self.push_screen("Home")

