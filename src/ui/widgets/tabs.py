from textual.app import ComposeResult
from textual.message import Message
from textual.containers import (
    Grid,
    Vertical,
    Horizontal
)
from textual.widgets import (
    Button, Static
)

from ...logic import ClassHandler
from ..forms import *
from .class_widgets import *
from .assignment_widgets import *

__all__ = [
    "HomeTab",
    "ClassesTab",
    "AssignmentsTab"
]

class HomeTab(Vertical):
    def __init__(self, class_handler: ClassHandler):
        super().__init__()
        self.class_handler = class_handler
        self.classes = "main-container"

    # Display
    #region
    def compose(self) -> ComposeResult:
        with Grid() as grid:
            grid.styles.grid_size_rows = 1
            grid.styles.grid_size_columns = 2
            
            with Vertical():
                yield ClassWidgetHandler(class_handler = self.class_handler, logged_in = True, class_data = self.class_handler.classes)

            with Vertical():
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
        self.classes = "main-container"

    # Display
    #region
    def compose(self) -> ComposeResult:
        with Vertical():
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
        self.classes = "main-container"

    # Display
    #region
    def compose(self) -> ComposeResult:
        with Grid() as g:
            g.styles.grid_size_columns = 2

            with Vertical():
                yield ClassWidgetHandler(
                    class_handler = self.class_handler,
                    logged_in = True,
                    class_data = self.class_handler.classes,
                    editing = False,
                )

            with Vertical(id="assignment-options"):
                yield AssignmentWidget(self.class_handler, self.selected_class)
    #endregion

    # Events
    #region
    def on_class_widget_handler_class_selected(self, event: ClassWidgetHandler.ClassSelected):
        self.selected_class = event.class_name

        container = self.query_one("#assignment-options", Vertical)
        container.query_one(AssignmentWidget).remove()
        container.mount(AssignmentWidget(self.class_handler, self.selected_class))
    #endregion
