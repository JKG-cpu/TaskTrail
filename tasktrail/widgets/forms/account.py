from textual.app import ComposeResult
from textual.screen import ModalScreen
from textual.widgets import Label, Input, Button

class LoginPage(ModalScreen):
    def compose(self) -> ComposeResult:
        yield Label("Enter in your account information", classes = "grid-title")
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

class CreateAccountPage(ModalScreen):
    def compose(self) -> ComposeResult:
        yield Label("Create an account", classes = "grid-title")
        yield Input(placeholder = "Enter in a username", id = "username")
        yield Input(placeholder = "Enter in a password", id = "password", password = True)
        yield Input(placeholder = "Retype password", id = "retype-password", password = True)
        yield Button("Create Account", id = "create-account")
        yield Button("Cancel", id = "cancel-btn")

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "create-account":
            username = self.query_one("#username", Input).value
            password = self.query_one("#password", Input).value
            retyped_password = self.query_one("#retype-password").value

            if username == "":
                self.notify("You must enter in a username", severity = "warning")
                return

            if password != retyped_password:
                self.notify("Incorrect password! (Not the same as typed previously)", severity = "warning")
                return

            data = {
                "username": username,
                "password": password
            }
            self.dismiss(data)

        if event.button.id == "cancel-btn":
            self.dismiss(None)