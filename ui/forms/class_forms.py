from textual.app import ComposeResult
from textual.screen import ModalScreen
from textual.widgets import Button, Input, ListView, ListItem, Label
from textual.containers import Vertical

__all__ = [
    "AddClassForm"
]

class AddClassForm(ModalScreen):
    def compose(self) -> ComposeResult:
        with Vertical(classes = "main-container") as vertical:
            vertical.border_title = "Create Class"
            vertical.styles.height = "auto"
            vertical.styles.border_title_align = "center"

            yield Input(placeholder = "Enter in the class name", id = "class-name")
            yield Input(placeholder = "Enter in the assignment weight (i.e 0.5)", id = "assignment-weight", type = "number")
            yield Input(placeholder = "Enter in the test weight (i.e 0.5)", id = "test-weight", type = "number")

            yield Button("Create Class", id = "create-class")
            yield Button("Cancel", id = "cancel")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "create-class":
            self._add_class()

        if event.button.id == "cancel":
            self.dismiss(None)

    def _add_class(self) -> None:
        data = {}

        class_name = self.query_one("#class-name", Input).value
        assignment_weight = self.query_one("#assignment-weight", Input).value
        test_weight = self.query_one("#test-weight", Input).value

        if (not class_name) or (not assignment_weight) or (not test_weight):
            self.notify("You must fill in all the options!")
            return

        data["class_name"] = class_name
        data["assignment_weight"] = assignment_weight
        data["test_weight"] = test_weight
        self.dismiss(data)

# class RemoveClassForm(ModalScreen):
#     def __init__(self, class_names: list[str]) -> None:
#         super().__init__()
#         self.class_names = class_names

#     def compose(self) -> ComposeResult:
#         with Vertical(classes = "main-container") as vertical:
#             vertical.border_title = "Create Class"
#             vertical.styles.height = "auto"
#             vertical.styles.border_title_align = "center"

#             yield ListView(
#                 *[ListItem(Label(class_name)) for class_name in self.class_names],
#                 id = "class"
#             )

#             yield Button("Remove Class", id = "remove-class")
#             yield Button("Cancel", id = "cancel")

#     def on_button_pressed(self, event: Button.Pressed) -> None:
#         if event.button.id == "remove-class":
#             self._remove_class()

#         if event.button.id == "cancel":
#             self.dismiss(None)

#     def _remove_class(self) -> None:
#         list_view = self.query_one("#class", ListView)

#         if list_view.highlighted_child is None:
#             return

#         label = list_view.highlighted_child.query_one(Label)
#         class_name = str(label.value)

#         self.dismiss(class_name)
