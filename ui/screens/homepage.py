from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer, Static, Button, Label
from textual.containers import Vertical, VerticalScroll, Grid

from ..forms import *

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
                with VerticalScroll(classes="main-container") as classes_panel:
                    classes_panel.border_title = "Classes"
                    yield Static("Classes")

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

    def _login_callback(self, data: dict | None) -> None:
        if data is None:
            return
        
        self.notify(str(data))
    
    def _create_account_callback(self, data: dict | None) -> None:
        if data is None:
            return
        
        self.notify(str(data))
