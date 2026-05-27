from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import (
    Header, Footer, 
    Button, 
    TabbedContent, TabPane
)

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

    # Details
    #region
    def compose(self) -> ComposeResult:
        yield Header()

        with TabbedContent():
            with TabPane("HomePage", id = "homePage-tab"):
                yield HomeTab(self.class_handler)
            
            with TabPane("Classes", id = "classes-tab"):
                yield ClassesTab(self.class_handler)

            with TabPane("Assignments", id = "assignments-tab"):
                yield AssignmentsTab(self.class_handler)

        yield Footer(show_command_palette = False)
    #endregion

    # Events
    #region
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.has_class("login-btn"):
            self.app.push_screen(LoginForm(), callback = self._login_callback)

        if event.button.has_class("create-account-btn"):
            self.app.push_screen(CreateAccountForm(), callback = self._create_account_callback)
    
    def on_classes_tab_class_changed(self, event: ClassesTab.ClassChanged) -> None:
        self.query_one(HomeTab).refresh(recompose=True)
    #endregion

    # Helpers
    #region
    def _login_callback(self, data: dict | None) -> None:
        if data is None:
            return
        
        self.notify(str(data))
    
    def _create_account_callback(self, data: dict | None) -> None:
        if data is None:
            return
        
        self.notify(str(data))
    #endregion
