from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer, TabPane, TabbedContent, Button
from os.path import join, dirname

from ..widgets import Tabs, LoginPage, CreateAccountPage
from ..logic import Services

class HomePage(Screen):
    CSS_PATH = [join(dirname(__file__), "..", "styles", "base.tcss"), join(dirname(__file__), "..", "styles", "selection.tcss")]

    def __init__(self) -> None:
        super().__init__()
        self.services = Services()
        self.tabs = self.services.get_tabs()

    def compose(self) -> ComposeResult:
        yield Header("TaskTrail")

        with TabbedContent():
            for tab in self.tabs:
                with TabPane(tab["name"]):
                    yield Tabs(tab["type"], tab["name"], tab["static"], self.services)

        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.has_class("login"):
            self.app.push_screen(LoginPage(), callback = self.login_callback)

        if event.button.has_class("signout"):
            self.services.signout()
            self.refresh(recompose = True)
        
        if event.button.has_class("create-account"):
            self.app.push_screen(CreateAccountPage(), callback = self.create_account_callback)

    def create_account_callback(self, data: dict) -> None:
        if data is None:
            return

        result = self.services.create_account(data["username"], data["password"])

        if result:
            result = self.services.login(data["username"], data["password"])
            if result:
                self.notify(f"Logged into {data["username"]}")
            
            self.app.refresh(recompose = True)

        else:
            self.notify(f"Username: {data["username"]} is already taken!", severity = "warning")

    def login_callback(self, data: dict) -> None:
        if data is None:
            return

        result = self.services.login(data["username"], data["password"])

        if result:
            self.notify(f"You are now logged into: {data["username"]}")
            self.refresh(recompose = True)

        else:
            self.notify(f"Invalid username or password!", severity = "error")
            self.app.push_screen(LoginPage(), callback = self.login_callback)
