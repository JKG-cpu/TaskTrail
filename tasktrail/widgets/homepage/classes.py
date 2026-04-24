from textual.app import ComposeResult
from textual.widgets import Button, Static
from textual.containers import Vertical, VerticalScroll, Horizontal

class Classes(Static):
    def compose(self) -> ComposeResult:
        with Vertical():
            with VerticalScroll(classes = "grid-section"):
                yield Static("Classes")

            self.buttons = Vertical()
            self.buttons.styles.dock = "bottom"
            self.buttons.styles.height = "auto"
            with self.buttons:
                self.add_section = Horizontal()
                self.add_section.styles.height = "auto"
                with self.add_section:
                    self.add_class_button = Button("Add Class")
                    self.add_class_button.styles.max_width = "50%"
                    yield self.add_class_button

                self.remove_section = Horizontal()
                self.remove_section.styles.height = "auto"
                with self.remove_section:
                    self.remove_class_button = Button("Remove Class")
                    self.remove_class_button.styles.max_width = "50%"
                    yield self.remove_class_button