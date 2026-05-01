from textual.app import ComposeResult
from textual.widgets import Static, Label
from textual.containers import Grid, Vertical

__all__ = [
    "Tabs"
]

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

    def compose(self) -> ComposeResult:
        yield Label(str(self.tab_name))

        with Grid():
            for i in range(4):
                with Vertical(classes = "grid-section"):
                    yield Static(f"Object {i + 1}", classes = "grid-item")

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
    "home": HomeTab,
    "settings": SettingsTab,
    "school": SchoolTab,
    "todo": TodoTab,
    "base": BaseTab
}

# Main
class Tabs(Vertical):
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
            yield tab(tab_name = self.tab_name, is_static = self.is_static)
