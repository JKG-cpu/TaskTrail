from textual.app import ComposeResult
from textual.screen import ModalScreen
from textual.widgets import Label, Input, Button

class LoginPage(ModalScreen):
    def compose(self) -> ComposeResult:
        yield Label("Login Form")
        yield Input(placeholder = "Enter in your username", id = "username")
        yield Input(placeholder = "Enter in your password (Leave blank if you don't have a password)", id = "password", password = True)
        yield Button("Submit", id = "login-btn")
        yield Button("Cancel", id = "cancel-btn")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "login-btn":
            username = self.query_one("#username", Input).value
            password = self.query_one("#password", Input).value

            if username == "":
                self.notify("You must enter in a username", severity = "warning")
                return

            data = {
                "username": username,
                "password": password
            }
            self.dismiss(data)
        
        if event.button.id == "cancel-btn":
            self.dismiss(None)
