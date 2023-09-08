from abc import ABC, abstractmethod
from typing import TypeVar, Generic

from lib import void
from lib.gui import Watcher
from lib.gui.layout import Layout
from lib.gui.window import Window

# Types

TRoot = TypeVar("TRoot", bound=Window)


# Main

class Screen(Watcher, ABC, Generic[TRoot]):
    _root: TRoot

    def __init__(self, root: TRoot) -> None: ...

    def config(self) -> void: ...

    @abstractmethod
    def render(self) -> Layout: ...

    @property
    def root(self) -> TRoot: ...
