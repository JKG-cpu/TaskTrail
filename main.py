from textual.app import App
from os.path import join

from ui import *
from logic import *

class TaskTrail(App):
    theme = "tokyo-night"
    BINDINGS = [("q", "quit", "Quit TaskTrail")]
    SCREENS = {
        "Home": HomePage
    }
    CSS_PATH = [join("styles", "base.tcss")]

    def on_mount(self) -> None:
        self.push_screen("Home")

    def action_quit(self):
        self._clear_on_quit = True
        return super().action_quit()

if __name__ == "__main__":
    tasktrail = TaskTrail()
    tasktrail.run()

    if getattr(tasktrail, "_clear_on_quit", False):
        cc()