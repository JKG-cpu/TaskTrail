from textual.app import App, ComposeResult
from textual.containers import Grid
from textual.widgets import Static

class GridApp(App):
    CSS_PATH = "tcss/grid.tcss"  # Link to CSS file

    def compose(self) -> ComposeResult:
        yield Grid(*[Static(f"Cell {i}", classes="box") for i in range(1, 8)])

if __name__ == "__main__":
    app = GridApp()
    app.run()
