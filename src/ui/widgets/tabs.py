from textual.app import ComposeResult
from textual.message import Message
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
from ..forms import *
from .class_widgets import *

__all__ = [
    "HomeTab",
    "ClassesTab",
    "AssignmentsTab"
]

class HomeTab(Vertical):
    def __init__(self, class_handler: ClassHandler):
        super().__init__()
        self.class_handler = class_handler

    # Display
    #region
    def compose(self) -> ComposeResult:
        grid = Grid()
        grid.styles.grid_size_rows = 1
        grid.styles.grid_size_columns = 2
        with grid:
            with Vertical(classes="main-container"):
                yield ClassWidgetHandler(class_handler = self.class_handler, logged_in = True, class_data = self.class_handler.classes)

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
    #endregion

    # Events
    #region
    def on_class_widget_handler_class_edited(self) -> None:
        self.refresh(recompose=True)
    #endregion

class ClassesTab(Vertical):
    class ClassChanged(Message):
        pass

    def __init__(self, class_handler: ClassHandler) -> None:
        super().__init__()
        self.class_handler = class_handler

    # Display
    #region
    def compose(self) -> ComposeResult:
        with Vertical(classes = "main-container"):
            widget = ClassWidgetHandler(self.class_handler, True, self.class_handler.classes)
            widget.styles.height = "1fr"
            yield widget

            with Horizontal(classes = "sub-container") as horizontal:
                horizontal.styles.height = "auto"

                button = Button("Add Class", classes = "add-class-btn")
                button.styles.width = "50%"
                yield button

                button = Button("Remove Class", classes = "remove-class-btn")
                button.styles.width = "50%"
                yield button
    #endregion

    # Helpers
    #region
    def _add_class_callback(self, data: dict | None) -> None:
        if data is None:
            return
        
        valid = self.class_handler.add_class(
            class_name = data["class_name"],
            assignment_weight = data["assignment_weight"],
            test_weight = data["test_weight"]
        )

        if valid:
            self.refresh(recompose = True)
            self.post_message(self.ClassChanged())

        else:
            self.notify("That class already exists!", severity = "error")
    #endregion

    # Events
    #region
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.has_class("add-class-btn"):
            self.app.push_screen(AddClassForm(), callback = self._add_class_callback)
        
        if event.button.has_class("remove-class-btn"):
            self.app.push_screen(RemoveClassForm(self.class_handler.get_class_names()), callback = self._remove_class_callback)

    def _remove_class_callback(self, data: str | None) -> None:
        if data is None:
            return

        valid = self.class_handler.remove_class(data)

        if valid:
            self.notify(f"Removed class: {data}")
            self.refresh(recompose = True)
            self.post_message(self.ClassChanged())

        else:
            raise ValueError(f"Invalid class: {valid}")

    def on_class_widget_handler_class_edited(self) -> None:
        self.refresh(recompose=True)
    #endregion

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

