from textual.widget import Widget
from textual.widgets import Static
from textual.containers import Grid

class HomePage(Widget):
    CSS_PATH = "../styles/homepage.tcss"

    def compose(self):
        with Grid(id = "homepage-grid"):
            for item in ["Profile", "Calendar", "Upcoming Due Dates", "Today's Date"]:
                yield Static(item, id = item.lower().replace(" ", "-").replace("'", ""))
