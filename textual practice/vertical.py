from textual.app import App
from textual.containers import VerticalScroll
from textual.widgets import Static

NUM_BOXES = 20

class TextualApp(App):
    def compose(self):
        with VerticalScroll():
            for i in range(NUM_BOXES):
                static = Static(f"Static {i}")
                static.styles.border = ("solid", "green")
                yield static

if __name__ == "__main__":
    t = TextualApp()
    t.run()
