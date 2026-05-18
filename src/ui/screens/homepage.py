from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import (
    Header, Footer, 
    Static, Label, Button, 
    TabbedContent, TabPane, Tabs,
    ListView, ListItem
)
from textual.containers import (
    Vertical, VerticalScroll, 
    Horizontal, Grid
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

    def compose(self) -> ComposeResult:
        yield Header()

        with TabbedContent():
            with TabPane("HomePage", id = "homePage-tab"):
                yield HomeTab(self.class_handler)
            
            with TabPane("Assignments", id = "assignments-tab"):
                yield AssignmentsTab(self.class_handler)

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

    # Callbacks
    #region
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
    #endregion
