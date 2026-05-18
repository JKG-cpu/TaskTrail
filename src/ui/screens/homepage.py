from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer, Static, Button
from textual.containers import Vertical, VerticalScroll, Horizontal, Grid

from ..forms import *
from ..widgets import *
from ...logic import ClassHandler

__all__ = [
    "HomePage"
]

class HomePage(Screen):
    def __init__(self) -> None:
        super().__init__()
        self.class_handler = ClassHandler()

    def compose(self) -> ComposeResult:
        yield Header()

        with Vertical():
            grid = Grid()
            grid.styles.grid_size_rows = 1
            grid.styles.grid_size_columns = 2
            with grid:
                with VerticalScroll(classes="main-container"):
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

        yield Footer()
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.has_class("login-btn"):
            self.app.push_screen(LoginForm(), callback = self._login_callback)

        if event.button.has_class("create-account-btn"):
            self.app.push_screen(CreateAccountForm(), callback = self._create_account_callback)

        if event.button.has_class("add-class-btn"):
            self.app.push_screen(AddClassForm(), callback = self._add_class_callback)
        
        if event.button.has_class("remove-class-btn"):
            self.app.push_screen(RemoveClassForm(self.class_handler.get_class_names()), callback = self._remove_class_callback)

    def _login_callback(self, data: dict | None) -> None:
        if data is None:
            return
        
        self.notify(str(data))
    
    def _create_account_callback(self, data: dict | None) -> None:
        if data is None:
            return
        
        self.notify(str(data))

    def _add_class_callback(self, data: dict | None) -> None:
        if data is None:
            return
        
        self.class_handler.add_class(
            class_name = data["class_name"],
            assignment_weight = data["assignment_weight"],
            test_weight = data["test_weight"]
        )

        self.refresh(recompose = True)

    def _remove_class_callback(self, data: str | None) -> None:
        if data is None:
            return

        valid = self.class_handler.remove_class(data)

        if valid:
            self.notify(f"Removed class: {data}")
            self.refresh(recompose = True)

        else:
            raise ValueError(f"Invalid class: {valid}")
