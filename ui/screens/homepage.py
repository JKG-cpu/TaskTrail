from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer, Static, Button
from textual.containers import Vertical, VerticalScroll, Horizontal, Grid

from ..forms import *
from ..widgets import *

__all__ = [
    "HomePage"
]

class HomePage(Screen):
    def compose(self) -> ComposeResult:
        yield Header()

        with Vertical():
            grid = Grid()
            grid.styles.grid_size_rows = 1
            grid.styles.grid_size_columns = 2
            with grid:
                with VerticalScroll(classes="main-container"):
                    yield ClassWidgetHandler(True, {
                        "AP CPS": {
                            "name": "AP CPS",
                            "percent": 100,
                            "assignment_weight": 0.5,
                            "test_weight": 0.5,
                            "assignments": {},
                            "tests": {}
                        },
                        "AP CP": {
                            "name": "AP CPS",
                            "percent": 100,
                            "assignment_weight": 0.5,
                            "test_weight": 0.5,
                            "assignments": {},
                            "tests": {}
                        },
                        "AP CS": {
                            "name": "AP CPS",
                            "percent": 100,
                            "assignment_weight": 0.5,
                            "test_weight": 0.5,
                            "assignments": {},
                            "tests": {}
                        },
                        "AP PS": {
                            "name": "AP CPS",
                            "percent": 100,
                            "assignment_weight": 0.5,
                            "test_weight": 0.5,
                            "assignments": {},
                            "tests": {}
                        },
                        "APCPS": {
                            "name": "AP CPS",
                            "percent": 100,
                            "assignment_weight": 0.5,
                            "test_weight": 0.5,
                            "assignments": {},
                            "tests": {}
                        },
                        "A CPS": {
                            "name": "AP CPS",
                            "percent": 100,
                            "assignment_weight": 0.5,
                            "test_weight": 0.5,
                            "assignments": {},
                            "tests": {}
                        }
                    })

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
            self.app.push_screen(RemoveClassForm(["Class 1", "Class 2"]), callback = self._remove_class_callback)

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
        
        self.notify(str(data))

    def _remove_class_callback(self, data: dict | None) -> None:
        if data is None:
            return
        
        self.notify(str(data))
