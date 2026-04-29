from textual.app import ComposeResult
from textual.widgets import Static

class Assignments(Static):
    def compose(self) -> ComposeResult:
        yield Static("Assignments")