from textual.app import App
from textual.widgets import Button

from screens import *
from logic import *

class TaskTrail(App):
    BINDINGS = [("q", "quit", "Quit TaskTrail")]

    def on_mount(self) -> None:
        self.push_screen(HomePage())

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "settings-btn":
            # Open Settings Screen
            pass

if __name__ == "__main__":
    TaskTrail().run()
    cc()