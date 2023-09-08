from abc import abstractmethod, ABC
from typing import Generic, TypeVar, TypedDict

from PyQt5.QtWidgets import QWidget

from lib import void
from lib.gui import Watcher
from lib.gui.layout import Layout

# Types

SwitcherStrategyDependencies = TypeVar("SwitcherStrategyDependencies", dict, TypedDict)
SwitcherStrategyParams = TypeVar("SwitcherStrategyParams", dict, TypedDict)


# Main

class SwitcherStrategy(Watcher, ABC, Generic[SwitcherStrategyDependencies, SwitcherStrategyParams]):
    _dependencies: SwitcherStrategyDependencies

    def __init__(self, dependencies: SwitcherStrategyDependencies) -> None: ...

    @property
    @abstractmethod
    def params(self) -> SwitcherStrategyParams: ...

    @property
    def dependencies(self) -> SwitcherStrategyDependencies: ...

    @abstractmethod
    def render(self, root: QWidget) -> Layout: ...

    def update_dependencies(self, dependencies: SwitcherStrategyDependencies) -> void: ...
