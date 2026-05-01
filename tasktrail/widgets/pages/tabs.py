from textual.app import ComposeResult
from textual.widgets import Static

# Tabs
class BaseTab(Static):
    def __init__(self, tab_name: str, is_static: bool) -> None:
        super().__init__()
        self.tab_name = tab_name
        self.is_static = is_static

    def get_static(self) -> bool: return self.is_static
    def get_name(self) -> str: return self.tab_name

    def compose(self) -> ComposeResult:
        yield Static(str(self.tab_name))

class HomeTab(BaseTab):
    def __init__(self, tab_name: str, is_static: bool) -> None:
        super().__init__(tab_name, is_static)

class SettingsTab(BaseTab):
    def __init__(self, tab_name: str, is_static: bool) -> None:
        super().__init__(tab_name, is_static)

class TodoTab(BaseTab):
    def __init__(self, tab_name: str, is_static: bool) -> None:
        super().__init__(tab_name, is_static)

class SchoolTab(BaseTab):
    def __init__(self, tab_name: str, is_static: bool) -> None:
        super().__init__(tab_name, is_static)

# Registry
TAB_REGISTRY: dict[str, type[Static]] = {
    "home": lambda name, static: HomeTab(tab_name = name, is_static = static),
    "settings": lambda name, static: SettingsTab(tab_name = name, is_static = static),
    "school": lambda name, static: SchoolTab(tab_name = name, is_static = static),
    "todo": lambda name, static: TodoTab(tab_name = name, is_static = static),
    "base": lambda name, static: BaseTab(tabname = name, is_static = static)
}

# Main
class Tabs(Static):
    def __init__(self, tab_type: str, tab_name: str, is_static: bool) -> None:
        super().__init__()
        self.tab_type = tab_type
        self.tab_name = tab_name
        self.is_static = is_static

    def compose(self) -> ComposeResult:
        tab = TAB_REGISTRY.get(self.tab_type)

        if not tab:
            raise ValueError(f"Invalid tab type: {self.tab_type}")

        else:
            yield tab(self.tab_name, self.is_static)
