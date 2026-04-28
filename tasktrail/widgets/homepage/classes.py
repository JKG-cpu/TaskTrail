from textual.app import ComposeResult
from textual.widgets import Button, Static
from textual.containers import Vertical, VerticalScroll, Horizontal

class ClassCard(Static):
    def __init__(self, class_name: str, class_assignments: list[dict]) -> None:
        super().__init__()
        self.class_name = class_name
        self.class_assignments = class_assignments

    def compose(self) -> ComposeResult:
        yield Static(self.class_name)
        for assignment in self.class_assignments:
            yield Static(str(self.class_assignments[assignment]))

class Classes(Static):
    def __init__(self, classes: dict) -> None:
        super().__init__()
        self.class_data = classes

    def compose(self) -> ComposeResult:
        with Vertical():
            with VerticalScroll(classes = "grid-section"):
                for key in self.class_data.keys():
                    yield ClassCard(str(key), self.class_data[key])

            self.buttons = Vertical(classes = "grid-section")
            self.buttons.styles.dock = "bottom"
            self.buttons.styles.height = "auto"
            with self.buttons:
                self.add_section = Horizontal()
                self.add_section.styles.height = "auto"
                with self.add_section:
                    self.add_class_button = Button("Add Class", id = "addClass")
                    yield self.add_class_button

                self.remove_section = Horizontal()
                self.remove_section.styles.height = "auto"
                with self.remove_section:
                    self.remove_class_button = Button("Remove Class", id = "removeClass")
                    yield self.remove_class_button
    