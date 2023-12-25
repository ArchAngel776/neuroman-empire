from enum import Enum
from typing import Generic, TypeVar, TypedDict, Callable, Self

from PyQt5.QtWidgets import QSizePolicy

from lib import void
from lib.decorators import method
from lib.decorators.decorator import Decorator
from lib.helpers.gui_remover import GUIRemover
from lib.gui.element import Element
from .program import SwitcherProgram
from lib.gui.layout.type import LayoutType
from lib.gui.window import Window

# Types

SwitcherKey = TypeVar("SwitcherKey", int, str, Enum)
SwitcherDependencies = TypeVar("SwitcherDependencies", dict, TypedDict)
SwitcherParams = TypeVar("SwitcherParams", dict, TypedDict)

TSwitcherUpdateStrategy = TypeVar("TSwitcherUpdateStrategy", bound=Switcher)
SwitcherUpdateStrategyKey = TypeVar("SwitcherUpdateStrategyKey", int, str, Enum)
SwitcherUpdateStrategyDependencies = TypeVar("SwitcherUpdateStrategyDependencies", dict, TypedDict)
SwitcherUpdateStrategyParams = TypeVar("SwitcherUpdateStrategyParams", dict, TypedDict)

TSwitcherRemoveStrategy = TypeVar("TSwitcherRemoveStrategy", bound=Switcher)
SwitcherRemoveStrategyKey = TypeVar("SwitcherRemoveStrategyKey", int, str, Enum)
SwitcherRemoveStrategyDependencies = TypeVar("SwitcherRemoveStrategyDependencies", dict, TypedDict)
SwitcherRemoveStrategyParams = TypeVar("SwitcherRemoveStrategyParams", dict, TypedDict)


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


class RemoveOldStrategy(
    Decorator[
        void, [
            Switcher[SwitcherRemoveStrategyKey, SwitcherRemoveStrategyDependencies, SwitcherRemoveStrategyParams]
        ]
    ],
    Generic[SwitcherRemoveStrategyKey, SwitcherRemoveStrategyDependencies, SwitcherRemoveStrategyParams]
):
    _gui_remover: GUIRemover

    def __init__(self, original: Callable[[TSwitcherRemoveStrategy], void]) -> None: ...

    def config(self, target: TSwitcherRemoveStrategy) -> Self: ...


# Main

class Switcher(Element, Generic[SwitcherKey, SwitcherDependencies, SwitcherParams]):
    _program: SwitcherProgram[SwitcherKey, SwitcherDependencies, SwitcherParams]
    _orientation: LayoutType
    _sizing: QSizePolicy

    def __init__(
            self,
            root: Window,
            program: SwitcherProgram[SwitcherKey, SwitcherDependencies, SwitcherParams],
            orientation: LayoutType
    ) -> None: ...

    def config(self) -> void: ...

    def InnerSizing(self, horizontal: QSizePolicy.Policy, vertical: QSizePolicy.Policy) -> Self: ...

    def AutoInit(self) -> Self: ...

    @method(UpdateStrategy[SwitcherKey, SwitcherDependencies, SwitcherParams])
    def change_strategy(self, key: SwitcherKey) -> void: ...

    def update_dependencies(self, dependencies: SwitcherDependencies, update_strategies: bool = False) -> Self: ...

    @method(RemoveOldStrategy[SwitcherKey, SwitcherDependencies, SwitcherParams])
    def implement_strategy(self) -> void: ...

    @property
    def program(self) -> SwitcherProgram[SwitcherKey, SwitcherDependencies, SwitcherParams]: ...
