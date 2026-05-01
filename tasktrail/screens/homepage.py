from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer, TabPane, TabbedContent
from os.path import join

from ..widgets import Tabs
from ..logic import Services

class HomePage(Screen):
    CSS_PATH = [join("..", "styles", "base.tcss")]

    def __init__(self) -> None:
        super().__init__()
        self.services = Services()
        self.tabs = self.services.get_tabs()

    def compose(self) -> ComposeResult:
        yield Header("TaskTrail")

        with TabbedContent():
            for tab in self.tabs:
                with TabPane(tab["name"], id = tab["name"]):
                    yield Tabs(tab["type"], tab["name"], tab["static"])

        yield Footer()

