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

    # Display
    #region
    def compose(self) -> ComposeResult:
        with Vertical(classes = "main-container") as vertical:
            vertical.border_title = f"Edit class: {self.class_name}"
            vertical.styles.height = "auto"
            vertical.styles.border_title_align = "center"

            # Change class name
            with Horizontal(classes = "class-edit") as h:
                h.border_title = "Change class Name"
                h.styles.height = "auto"

                ipt = Input(placeholder = "Change class name", id = "class_name")
                ipt.styles.width = "50%"
                yield ipt

                label = Label(f"Current Class Name: {self.class_name}")
                label.styles.width = "50%"
                yield label
            
            # Change grade weights
            with Grid(classes = "class-edit") as g:
                g.border_title = "Grade Weights"
                g.styles.grid_size_columns = 2
                g.styles.grid_size_rows = 2
                g.styles.height = "auto"

                ipt = Input(placeholder = "Change Assignment Weight (integer)", id = "assignment_weight", type = "number")
                yield ipt

                label = Label(f"Current Assignment Weight: {self.assignment_weight}")
                yield label

                ipt = Input(placeholder = "Change Assignment Weight (integer)", id = "test_weight", type = "number")
                yield ipt

                label = Label(f"Current Test Weight: {self.test_weight}")
                yield label

            # Save and/or Exit
            with Horizontal(classes = "class-edit") as h:
                h.styles.height = "auto"

                save = Button("Save and exit", id = "save")
                save.styles.width = "50%"
                yield save

                cancel = Button("Cancel", id = "cancel")
                cancel.styles.width = "50%"
                yield cancel
    #endregion

    # Events
    #region
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "save":
            self._handle_submission()

        if event.button.id == "cancel":
            self.dismiss(None)

    # Helpers
    #region
    def _handle_submission(self) -> None:
        data = {
            "name": self.class_name,
            "assignment": self.assignment_weight,
            "test": self.test_weight
        }

        class_name = self.query_one("#class_name", Input).value
        assignment = self.query_one("#assignment_weight", Input).value
        tests = self.query_one("#test_weight", Input).value

        if data["name"] != class_name and class_name:
            data["name"] = class_name

        if data["assignment"] != assignment and assignment:
            data["assignment"] = assignment

        if data["test"] != tests and assignment:
            data["test"] = tests

        self.dismiss(data)
    #endregion

class AddGrade(ModalScreen):
    pass
