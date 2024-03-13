from enum import Enum
from typing import Generic, TypeVar, TypedDict, Self, ClassVar, Optional, Callable

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QShowEvent

from lib import void
from lib.decorators import method
from lib.decorators.decorator import Decorator
from lib.gui.element.component import Component
from lib.gui.layout import Layout
from lib.gui.layout.type import LayoutType
from lib.gui.window import Window
from .program import SwitcherProgram
from .strategy import SwitcherStrategy

# Types

TSwitcherStrategy = TypeVar("TSwitcherStrategy", bound=SwitcherStrategy)

SwitcherKey = TypeVar("SwitcherKey", int, str, Enum)
SwitcherDependencies = TypeVar("SwitcherDependencies", dict, TypedDict)
SwitcherParams = TypeVar("SwitcherParams", dict, TypedDict)

TSwitcherUpdateStrategy = TypeVar("TSwitcherUpdateStrategy", bound=Switcher)
SwitcherUpdateStrategyKey = TypeVar("SwitcherUpdateStrategyKey", int, str, Enum)
SwitcherUpdateStrategyDependencies = TypeVar("SwitcherUpdateStrategyDependencies", dict, TypedDict)
SwitcherUpdateStrategyParams = TypeVar("SwitcherUpdateStrategyParams", dict, TypedDict)

TSwitcherConstraintLayout = TypeVar("TSwitcherConstraintLayout", bound=Switcher)
SwitcherConstraintLayoutKey = TypeVar("SwitcherConstraintLayoutKey", int, str, Enum)
SwitcherConstraintLayoutDependencies = TypeVar("SwitcherConstraintLayoutDependencies", dict, TypedDict)
SwitcherConstraintLayoutParams = TypeVar("SwitcherConstraintLayoutParams", dict, TypedDict)


# Decorators

class UpdateStrategy(
    Decorator[
        void, [
            Switcher[SwitcherUpdateStrategyKey, SwitcherUpdateStrategyDependencies, SwitcherUpdateStrategyParams],
            SwitcherUpdateStrategyKey
        ]
    ],
    Generic[SwitcherUpdateStrategyKey, SwitcherUpdateStrategyDependencies, SwitcherUpdateStrategyParams]
):
    def method(self, target: TSwitcherUpdateStrategy, key: SwitcherUpdateStrategyKey) -> void: ...


class ConstraintLayout(
    Decorator[
        Layout, [
            Switcher[SwitcherConstraintLayoutKey, SwitcherConstraintLayoutDependencies, SwitcherConstraintLayoutParams],
            Window
        ]
    ],
    Generic[SwitcherConstraintLayoutKey, SwitcherConstraintLayoutDependencies, SwitcherConstraintLayoutParams]
):
    def method(self, target: TSwitcherConstraintLayout, root: Window) -> Layout: ...


# Main

class Switcher(Component, Generic[SwitcherKey, SwitcherDependencies, SwitcherParams]):
    _program: SwitcherProgram[SwitcherKey, SwitcherDependencies, SwitcherParams]

    _payload: Optional[Callable[[SwitcherStrategy[SwitcherDependencies, SwitcherParams]], void]]

    # Signals

    beforeShown: ClassVar[pyqtSignal] = ...

    afterShown: ClassVar[pyqtSignal] = ...

    beforeClosed: ClassVar[pyqtSignal] = ...

    def __init__(
            self,
            root: Window,
            program: SwitcherProgram[SwitcherKey, SwitcherDependencies, SwitcherParams],
            orientation: LayoutType
    ) -> None: ...

    def config(self) -> void: ...

    def showEvent(self, event: Optional[QShowEvent]) -> void: ...

    def Payload(
            self,
            payload: Callable[[TSwitcherStrategy], void]
    ) -> Self: ...

    def AutoInit(self) -> Self: ...

    def change_strategy(self, key: SwitcherKey) -> void: ...

    @method(UpdateStrategy[SwitcherKey, SwitcherDependencies, SwitcherParams])
    def change_switcher_strategy(self, key: SwitcherKey) -> void: ...

    def update_dependencies(self, dependencies: SwitcherDependencies, update_strategies: bool = ...) -> Self: ...

    def update_view(self) -> void: ...

    @method(ConstraintLayout[SwitcherKey, SwitcherDependencies, SwitcherParams])
    def render_view(self, root: Window) -> Layout: ...

    # Slots

    def switchEvent(self) -> void: ...

    def view_update(self) -> void: ...

    @property
    def program(self) -> SwitcherProgram[SwitcherKey, SwitcherDependencies, SwitcherParams]: ...

    @property
    def payload(self) -> Optional[Callable[[SwitcherStrategy[SwitcherDependencies, SwitcherParams]], void]]: ...
