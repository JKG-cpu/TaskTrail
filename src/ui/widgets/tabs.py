from textual.app import ComposeResult
from textual.containers import (
    Grid,
    Vertical,
    Horizontal
)
from textual.widgets import (
    Button, Static, Label,
    ListView, ListItem
)

from ...logic import ClassHandler
from .class_widgets import *

__all__ = [
    "HomeTab",
    "AssignmentsTab"
]

class HomeTab(Vertical):
    def __init__(self, class_handler: ClassHandler):
        super().__init__()
        self.class_handler = class_handler

    def compose(self) -> ComposeResult:
        grid = Grid()
        grid.styles.grid_size_rows = 1
        grid.styles.grid_size_columns = 2
        with grid:
            with Vertical(classes="main-container"):
                yield ClassWidgetHandler(True, self.class_handler.classes)

                with Horizontal(classes = "sub-container") as horizontal:
                    horizontal.styles.height = "auto"

                    button = Button("Add Class", classes = "add-class-btn")
                    button.styles.width = "50%"
                    yield button

                    button = Button("Remove Class", classes = "remove-class-btn")
                    button.styles.width = "50%"
                    yield button

            with Vertical(classes="main-container"):
                static = Static("Assignments", classes="sub-container")
                static.border_title = "Assignments"
                static.styles.height = "1fr"
                yield static

                vertical = Vertical(classes = "sub-container")
                vertical.border_title = "User Account"
                vertical.styles.height = "auto"

                with vertical:
                    yield Button("Log in", classes = "login-btn")
                    yield Button("Create Account", classes = "create-account-btn")

class AssignmentsTab(Vertical):
    def __init__(self, class_handler: ClassHandler) -> None:
        super().__init__()
        self.class_handler = class_handler
        self.selected_class: str | None = None
    
    def compose(self) -> ComposeResult:
        if self.selected_class is None:
            if self.class_handler.get_class_names():
                yield ListView(
                    *[ListItem(Label(class_name), name = class_name) for class_name in self.class_handler.get_class_names()],
                    classes = "class_names"
                )
                yield Button("Select a class", id = "select-class")

            else:
                yield Label("You have no classes!")

        else:
            yield Label(f"Selected class: {self.selected_class}")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "select-class":
            self._select_class()

    def _select_class(self) -> None:
        list_view = self.query_one(".class_names", ListView)
        selected = list_view.highlighted_child

        if selected is None:
            self.notify("You must select a class!", severity = "error")
            return

        self.selected_class = selected.name
        self.notify(f"Selected class: {self.selected_class}")
        self.refresh(recompose = True)

