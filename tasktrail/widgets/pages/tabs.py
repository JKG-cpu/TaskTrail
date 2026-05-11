from textual.app import ComposeResult
from textual.widgets import Static, Button, SelectionList
from textual.widgets.selection_list import Selection
from textual.containers import Grid, Vertical, VerticalScroll

from ...logic import Services

__all__ = [
    "Tabs"
]

# Tabs
class BaseTab(Static):
    def __init__(self, tab_name: str, is_static: bool, services: Services, order: int) -> None:
        super().__init__()
        self.tab_name = tab_name
        self.is_static = is_static
        self.services = services
        self.order = order

    def get_static(self) -> bool: return self.is_static
    def get_name(self) -> str: return self.tab_name

    def compose(self) -> ComposeResult:
        yield Static(str(self.tab_name))

class HomeTab(BaseTab):
    def __init__(self, tab_name: str, is_static: bool, services: Services, order: str) -> None:
        super().__init__(tab_name, is_static, services, order)

    def compose(self) -> ComposeResult:
        loggedin = self.services.is_loggedin()

        if loggedin:
            grid = Grid()
            grid.styles.grid_size_columns = 2
            grid.styles.grid_columns = "1fr 1fr"
            grid.styles.height = "1fr"
            grid.styles.width = "1fr"

            with grid:
                # Todo's
                with Vertical(classes = "grid-section"):
                    yield Static("Todo's", classes = "grid-item")

                # Current Profile
                with Vertical(classes = "grid-section"):
                    yield Static("Current Profile", classes = "grid-item")

                # School Work
                with Vertical(classes = "grid-section"):
                    yield Static("School Work", classes = "grid-item")

                # Login
                with Vertical(classes = "grid-section"):
                    text = f"Welcome, {self.services.get_username()}"
                    login_label = Static(text, classes = "grid-item")
                    login_label.styles.height = "2fr";

                    yield login_label

                    button = Button("Sign out", classes = "signout")
                    button.styles.height = "1fr"
                    yield button

        else:
            yield Static("Your not logged in!", classes = "grid-title")

            yield Button("Login", classes = "login")
            yield Button("Create account", classes = "create-account")

class SettingsTab(BaseTab):
    def __init__(self, tab_name: str, is_static: bool, services: Services, order: str) -> None:
        super().__init__(tab_name, is_static, services, order)

    def compose(self) -> ComposeResult:
        if self.services.is_loggedin():
            with VerticalScroll():
                yield Static("Settings", classes = "grid-title")

                yield SelectionList[str](
                    *[Selection(setting[0], setting[1], setting[2]) for setting in self.services.get_settings(self.services.get_profile())],
                    id = "settings"
                )
        
        else:
            yield Static("You need to login!", classes = "grid-title")

    def on_selection_list_selected_changed(self, event: SelectionList.SelectedChanged):
        if event.selection_list.id == "settings":
            self.services.update_settings(event.selection_list.selected, self.services.get_profile())

class TodoTab(BaseTab):
    def __init__(self, tab_name: str, is_static: bool, services: Services, order: str) -> None:
        super().__init__(tab_name, is_static, services, order)
    
    def compose(self) -> ComposeResult:
        todo_data = self.services.get_page_data(self.order)

        tasks = todo_data.get("tasks")

        with VerticalScroll(classes = "grid-section"):
            yield Static(str(tasks))

class SchoolTab(BaseTab):
    def __init__(self, tab_name: str, is_static: bool, services: Services, order: str) -> None:
        super().__init__(tab_name, is_static, services, order)

    def compose(self) -> ComposeResult:
        school_data = self.services.get_page_data(self.order)

        yield Static(str(school_data))

# Registry
TAB_REGISTRY: dict[str, type[Static]] = {
    "home": HomeTab,
    "settings": SettingsTab,
    "school": SchoolTab,
    "todo": TodoTab,
    "base": BaseTab
}

# Main
class Tabs(Vertical):
    def __init__(self, tab_type: str, tab_name: str, is_static: bool, services: Services, order: str) -> None:
        super().__init__()
        self.tab_type = tab_type
        self.tab_name = tab_name
        self.is_static = is_static
        self.services = services
        self.order = order

    def compose(self) -> ComposeResult:
        tab = TAB_REGISTRY.get(self.tab_type)

        if not tab:
            raise ValueError(f"Invalid tab type: {self.tab_type}")

        else:
            yield tab(tab_name = self.tab_name, is_static = self.is_static, services = self.services, order = self.order)
