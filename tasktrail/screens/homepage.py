from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer, TabPane, TabbedContent

from ..widgets import *

class HomePageScreen(Screen):
    CSS_PATH = ["../styles/homepage.tcss", "../styles/base.tcss"]

    def compose(self) -> ComposeResult:
        header = Header("TaskTrail")
        header.styles.height = 3
        header.styles.content_align = ("center", "middle")
        header.styles.align = ("center", "middle")
        yield header

        with TabbedContent(initial="classesTab"):
            with TabPane("Home Page", id = "homePageTab"):
                yield HomePage()
            
            with TabPane("Assignments", id="assignmentsTab"):
                yield Assignments()

            with TabPane("Classes", id = "classesTab"):
                yield Classes()

        footer = Footer()
        yield footer

