from textual.app import ComposeResult
from textual.screen import ModalScreen
from textual.widgets import Input, Button, Label
from textual.containers import Vertical, Horizontal, Grid

__all__ = [
    "EditClassForm"
]

class EditClassForm(ModalScreen):
    def __init__(self, class_name: str, assignment_weight: float, test_weight: float) -> None:
        super().__init__()
        self.class_name = class_name
        self.assignment_weight = assignment_weight
        self.test_weight = test_weight

        self.assignments = []
        self.tests = []

    def compose(self) -> ComposeResult:
        with Vertical(classes = "main-container") as vertical:
            vertical.border_title = f"Edit class: {self.class_name}"
            vertical.styles.height = "auto"
            vertical.styles.border_title_align = "center"

            with Horizontal(classes = "class-edit") as h:
                h.border_title = "Change class Name"

                ipt = Input(placeholder = "Change class name")
                ipt.styles.width = "50%"
                yield ipt

                label = Label(f"Current Class Name: {self.class_name}")
                label.styles.width = "50%"
                yield label
            
            with Grid(classes = "class-edit") as g:
                g.border_title = "Grade Weights"
                g.styles.grid_size_columns = 2
                g.styles.grid_size_rows = 2

                ipt = Input(placeholder = "Change Assignment Weight (integer)", type = "number")
                yield ipt

                label = Label(f"Current Assignment Weight: {self.assignment_weight}")
                yield label

                ipt = Input(placeholder = "Change Assignment Weight (integer)", type = "number")
                yield ipt

                label = Label(f"Current Test Weight: {self.test_weight}")
                yield label

            with Horizontal(classes = "class-edit") as h:
                save = Button("Save and exit", id = "save")
                save.styles.width = "50%"
                yield save

                cancel = Button("Cancel", id = "cancel")
                cancel.styles.width = "50%"
                yield cancel

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "save":
            self._handle_submission()

        if event.button.id == "cancel":
            self.dismiss(None)

    def _handle_item(self, data: dict) -> None:
        pass

    def _handle_submission(self) -> None:
        pass

class AddGrade(ModalScreen):
    pass
