from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer, Static
from textual.containers import Vertical

__all__ = [
    "HomePage"
]

class HomePage(Screen):
    def compose(self) -> ComposeResult:
        yield Header()

        with Vertical(classes = "main-container"):
            yield Static("HomePage")

        yield Footer()
