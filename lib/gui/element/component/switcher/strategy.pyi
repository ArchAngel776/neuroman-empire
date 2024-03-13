from abc import abstractmethod, ABC
from typing import Generic, TypeVar, TypedDict, ClassVar

from PyQt5.QtCore import pyqtSignal

from lib import void
from lib.foundations import Foundation
from lib.gui import Watcher
from lib.gui.layout import Layout
from lib.gui.window import Window

# Types

SwitcherStrategyDependencies = TypeVar("SwitcherStrategyDependencies", dict, TypedDict)
SwitcherStrategyParams = TypeVar("SwitcherStrategyParams", dict, TypedDict)


# Meta

class SwitcherStrategyMeta(type(Foundation), type(ABC)):
    ...


# Main

class SwitcherStrategy(
    Foundation,
    Watcher,
    ABC,
    Generic[SwitcherStrategyDependencies, SwitcherStrategyParams],
    metaclass=SwitcherStrategyMeta
):
    _dependencies: SwitcherStrategyDependencies

    # Signals

    view_updated: ClassVar[pyqtSignal] = ...

    def __init__(self, dependencies: SwitcherStrategyDependencies) -> None: ...

    def beforeShow(self) -> void: ...

    def afterShow(self) -> void: ...

    def beforeClose(self) -> void: ...

    @property
    @abstractmethod
    def params(self) -> SwitcherStrategyParams: ...

    @property
    def dependencies(self) -> SwitcherStrategyDependencies: ...

    @abstractmethod
    def render(self, root: Window) -> Layout: ...

    def update_view(self) -> void: ...

    def update_dependencies(self, dependencies: SwitcherStrategyDependencies) -> void: ...
