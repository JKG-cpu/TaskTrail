from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Static

from logic import *
from screens import *

class TaskTrail(App):
    BINDINGS = [
        ("Q", "quit", "Quit"), 
        ("D", "toggle_dark", "Toggle Dark / Light Mode")
    ]

    def compose(self) -> ComposeResult:
        header = Header(name = "TaskTrail")
        footer = Footer()

        yield header
        yield HomePage()
        yield footer

if __name__ == "__main__":
    task_trail = TaskTrail()
    task_trail.run()
    
    cc()