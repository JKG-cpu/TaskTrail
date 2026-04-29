from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import Header, Footer, TabPane, TabbedContent, Button

from ..widgets import *
from ..logic import Services

class HomePageScreen(Screen):
    def __init__(self):
        super().__init__()
        self.services = Services()

    CSS_PATH = ["../styles/homepage.tcss", "../styles/base.tcss"]

    def compose(self) -> ComposeResult:
        header = Header("TaskTrail")
        header.styles.height = 3
        header.styles.content_align = ("center", "middle")
        header.styles.align = ("center", "middle")
        yield header

        with TabbedContent(initial="homePageTab"):
            with TabPane("Home Page", id = "homePageTab"):
                yield HomePage()

            with TabPane("Classes", id = "classesTab"):
                yield Classes(self.services.get_class_data())

            with TabPane("Settings", id = "settingsTab"):
                yield SettingsPage(self.services.get_username())

        footer = Footer()
        yield footer

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.has_class("login"):
            self.app.push_screen(LoginPage(), callback=self.on_login_callback)

        if event.button.has_class("signOut"):
            self.services.sign_out()
            self.refresh(recompose = True)

    def on_login_callback(self, data: dict) -> None:
        if data is None:
            return

        result = self.services.login(data["username"], data["password"])

        if result:
            self.notify(f"You are now logged into: {data["username"]}", timeout = 1)
            self.refresh(recompose = True)

        else:
            self.notify(f"Invalid username or password!", severity = "error")
            self.app.push_screen(LoginPage(), callback = self.on_login_callback)
