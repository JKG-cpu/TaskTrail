from textual.app import ComposeResult
from textual.widgets import Static, Button
from textual.containers import Grid, Vertical

class HomePage(Static):
    def compose(self) -> ComposeResult:
        with Grid():
            for item in ["Assignments", "Calendar", "Classes"]:
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
