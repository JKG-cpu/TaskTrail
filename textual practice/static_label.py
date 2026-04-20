from textual.app import App
from textual.widgets import Static, Label

class TextualApp(App):
    def compose(self):
        self.static = Static(
            "I am a [bold red]Static[/bold red] widget!"
        )
        yield self.static

        self.label = Label(
            "I am a [yellow italic]Lable[/] widget!"
        )
        yield self.label
    
    def on_mount(self):
        # Styling the static
        self.static.styles.background = "blue"
        self.static.styles.border = ("solid", "white")
        self.static.styles.text_align = "center"
        self.static.styles.padding = 1, 1
        self.static.styles.margin = 4, 4
        self.static.styles.width = "auto"
        # Styling the label
        self.label.styles.background = "darkgreen"
        self.label.styles.border = ("double", "red")
        self.label.styles.padding = 1, 1
        self.label.styles.margin = 2, 4
        self.label.styles.width = "100%"

if __name__ == "__main__":
    t = TextualApp()
    t.run()