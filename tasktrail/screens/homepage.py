from textual.app import ComposeResult
from textual.screen import Screen
from textual.containers import Grid, Vertical
from textual.widgets import Static, Header, Footer, Button, Label, Tabs

class HomePage(Screen):
    CSS_PATH = ["../styles/homepage.tcss", "../styles/base.tcss"]

    def compose(self) -> ComposeResult:
        header = Header("TaskTrail")
        header.styles.height = 3
        header.styles.content_align = ("center", "middle")
        header.styles.align = ("center", "middle")
        yield header

        yield Tabs("Home Page", "First tab", "Second tab", "Thirdtab", classes = "navbar")

        with Grid():
            for item in ["Assignments", "Profiles", "Classes"]:
                with Vertical(classes = "grid-section"):
                    static = Static(item, classes = "grid-title")
                    static.styles.text_align = "center"
                    yield static
                    static = Static(item, classes = "grid-item")
                    static.styles.text_align = "center"
                    yield static

            with Vertical(classes = "grid-section"):
                static = Static("Today's Date", classes = "grid-item", id = "todays-data-btn")
                static.styles.text_align = "center"
                yield static
        
                static = Button("Settings", classes = "grid-item", id = f"settings-btn")
                static.styles.text_align = "center"
                yield static

        footer = Footer()
        yield footer

