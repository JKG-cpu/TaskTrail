from textual.app import ComposeResult
from textual.widgets import Label, ListView, ListItem, Button
from textual.containers import Vertical, VerticalScroll, Horizontal
from textual.messages import Message

from ...logic import ClassHandler
from ..forms import AddGrade

__all__ = ["AssignmentWidget"]

class AssignmentBox(Vertical):
    def __init__(self, assignment: dict) -> None:
        super().__init__()
        self.assignment = assignment

    def compose(self) -> ComposeResult:
        yield Label(str(self.assignment))

class AssignmentWidget(VerticalScroll):
    class Refresh(Message):
        pass

    def __init__(self, class_handler: ClassHandler, selected_class: str) -> None:
        super().__init__()
        self.classes = "sub-container"
        self.class_handler = class_handler
        self.selected_class = selected_class

    def compose(self) -> ComposeResult:
        if not self.selected_class:
            yield Label("No class selected")
            return

        yield Label(self.selected_class)

        assignments = self.class_handler.get_assignments(self.selected_class)
        with Vertical(classes="sub-container") as v:
            v.border_title = "Assignments"
            v.styles.border_title_align = "center"
            v.styles.height = "auto"
            yield ListView(
                *[ListItem(AssignmentBox(a)) for a in assignments]
                if assignments else
                [ListItem(Label("No Assignments created"), disabled = True)],
                id="assignment-list"
            )

        with Horizontal(classes="sub-container"):
            yield Button("Add Assignment", id = "add-assignment")
            yield Button("Remove Assignment", id = "remove-assignment")
            yield Button("Complete Assignment", id = "complete-assignment")

        tests = self.class_handler.get_tests(self.selected_class)
        with Vertical(classes = "sub-container") as v:
            v.border_title = "Tests"
            v.styles.border_title_align = "center"
            v.styles.height = "auto"
            yield ListView(
                *[ListItem(AssignmentBox(t)) for t in tests]
                if tests else
                [ListItem(Label("No tests created"), disabled = True)],
                id = "test-list"
            )

        with Horizontal(classes="sub-container"):
            yield Button("Add Test", id = "add-test")
            yield Button("Remove Test", id = "remove-test")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "add-assignment":
            self.app.push_screen(AddGrade(), callback = self._add_grade_callback)

        if event.button.id == "remove-assignment":
            pass

        if event.button.id == "add-test":
            self.app.push_screen(AddGrade(True), callback = self._add_grade_callback)

        if event.button.id == "remove-test":
            pass

    def _add_grade_callback(self, data: dict | None) -> None:
        if data is None:
            return
        
        if data["is_test"]:
            valid = self.class_handler.add_test(
                class_name = self.selected_class,
                name = data["name"],
                grade = data["score"]
            )

            if valid:
                self.post_message(self.Refresh())

            else:
                self.notify("Invalid Test Name (ALREADY USED)")

        else:
            valid = self.class_handler.add_assignment(
                class_name = self.selected_class,
                name = data["name"]
            )

            if valid:
                self.post_message(self.Refresh())
            
            else:
                self.notfiy("Invalid Assignment Name (ALREADY USED)")
    
