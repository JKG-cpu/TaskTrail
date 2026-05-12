from textual.app import App

from .screens import *

class TaskTrail(App):
    BINDINGS = [("q", "quit", "Quit TaskTrail")]
    SCREENS = {
        "Home": HomePage
    }

    def on_mount(self) -> None:
        self.push_screen("Home")

    def action_quit(self) -> None:
        self._quit_properly = True
        return super().action_quit()
