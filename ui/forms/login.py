from textual.app import ComposeResult
from textual.screen import ModalScreen
from textual.widgets import Label, Input, Button
from textual.containers import Vertical

__all__ = [
    "LoginForm",
    "CreateAccountForm"
]

class LoginForm(ModalScreen):
    def compose(self) -> ComposeResult:
        with Vertical(classes = "main-container") as vertical:
            vertical.border_title = "Login Form"
            vertical.styles.height = "auto"
            vertical.styles.border_title_align = "center"

            yield Input(placeholder = "Enter in your username", id = "username")
            yield Input(placeholder = "Enter in your password (Leave blank if no password set)", id = "password", password = True)
        
            yield Button("Sign In", id = "submit")
            yield Button("Cancel", id = "cancel")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "submit":
            self._handle_login()

        if event.button.id == "cancel":
            self.dismiss(None)
        
    def _handle_login(self) -> None:
        data = {}
        username = self.query_one("#username", Input).value
        password = self.query_one("#password", Input).value

        if not username:
            self.notify("You must entry in a username!", severity = "error")
            return
        
        data["username"] = username
        data["password"] = password
        self.dismiss(data)

class CreateAccountForm(ModalScreen):
    def compose(self) -> ComposeResult:
        yield Label("Create an account")

        yield Input(placeholder = "Enter in your username", id = "username")
        yield Input(placeholder = "Enter in your password (Leave blank if no password set)", id = "password", password = True)
        yield Input(placeholder = "Retype your password", id = "password2", password = True)

        yield Button("Sign In", id = "submit")
        yield Button("Cancel", id = "cancel")
    
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "submit":
            self._create_account()
        
        if event.button.id == "cancel":
            self.dismiss(None)

    def _create_account(self) -> None:
        data = {}
        username = self.query_one("#username", Input).value
        password = self.query_one("#password", Input).value
        retyped_password = self.query_one("#password2", Input).value

        if username is None:
            self.notify("You must entry in a username!", severity = "error")
            return
        
        if password != retyped_password:
            self.notify("Retyped password incorrect!", severity = "error")
            return
        
        data["username"] = username
        data["password"] = password
        self.dismiss(data)
