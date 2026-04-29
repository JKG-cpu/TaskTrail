from textual.app import App
from textual.widgets import Button

from .screens import *
from .logic import *

class TaskTrail(App):
    BINDINGS = [("q", "quit", "Quit TaskTrail")]
    SCREENS = {
        "Home": HomePageScreen,
        "Settings": SettingsPage
    }

    def on_mount(self) -> None:
        self.push_screen("Home")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        # Homepage Tab
        if event.button.id == "settings-btn":
            self.push_screen("Settings")
            return

        # Classes Tab
        if event.button.id == "addClass":
            pass

        if event.button.id == "removeClass":
            pass

        # General buttons
        if event.button.has_class("toHome"):
            self.push_screen("Home")
            return

        if event.button.has_class("goBack"):
            self.pop_screen()
            return