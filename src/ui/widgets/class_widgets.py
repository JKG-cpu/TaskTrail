from textual.app import ComposeResult
from textual.widgets import Static, Label
from textual.containers import VerticalScroll, Vertical

__all__ = [
    "ClassWidgetHandler"
]

class ClassWidgets(Static):
    def __init__(self, class_name: str, percent: int | None, assignment_weight: float, test_weight: float) -> None:
        super().__init__()
        self.class_name = class_name
        self.percent = percent
        self.assignment_weight = assignment_weight
        self.test_weight = test_weight

    def compose(self):
        with Vertical(classes = "sub-container") as vertical:
            vertical.border_title = self.class_name
            vertical.styles.border_title_align = "center"
            vertical.styles.height = "auto"

            static = Static(str(self.percent) if self.percent else "100" + "% Overall")
            static.styles.content_align = ("center", "middle")
            yield static

            static = Static(f"Assignments: {self.assignment_weight} percent of overall grade.")
            static.styles.content_align = ("center", "middle")
            yield static

            static = Static(f"Tests: {self.test_weight} percent of overall grade.")
            static.styles.content_align = ("center", "middle")
            yield static
    
class ClassWidgetHandler(Static):
    def __init__(self, logged_in: bool, class_data: dict[str, dict]) -> None:
        super().__init__()
        self.styles.height = "1fr"
        self.logged_in = logged_in
        self.class_data = class_data
        self.class_names: list[str] = list(self.class_data.keys())

    def compose(self) -> ComposeResult:
        if self.logged_in:
            with VerticalScroll(classes = "main-container") as vertical:
                vertical.border_title = "Classes"
                vertical.styles.scrollbar_visibility = "hidden"
                
                if self.class_data:
                    for class_name in self.class_names:
                        class_data = self.class_data[class_name]
                        yield ClassWidgets(
                            class_name = class_name, 
                            percent = class_data["percent"],
                            assignment_weight = class_data["assignment_weight"],
                            test_weight = class_data["test_weight"]
                        )

                else:
                    yield Label("No classes created.")

        else:
            with Vertical(classes = "sub-container") as vertical:
                vertical.border_title = "Classes"
                static = Static("Can't view classes, not logged in!")
                static.styles.content_align = ("center", "middle")
                static.styles.height = "1fr"
                yield static
