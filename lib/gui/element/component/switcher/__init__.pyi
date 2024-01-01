from enum import Enum
from typing import Generic, TypeVar, TypedDict, Self

from lib import void
from lib.decorators import method
from lib.decorators.decorator import Decorator
from lib.gui.element.component import Component
from lib.gui.layout import Layout
from lib.gui.layout.type import LayoutType
from lib.gui.window import Window
from .program import SwitcherProgram

# Types

SwitcherKey = TypeVar("SwitcherKey", int, str, Enum)
SwitcherDependencies = TypeVar("SwitcherDependencies", dict, TypedDict)
SwitcherParams = TypeVar("SwitcherParams", dict, TypedDict)

TSwitcherUpdateStrategy = TypeVar("TSwitcherUpdateStrategy", bound=Switcher)
SwitcherUpdateStrategyKey = TypeVar("SwitcherUpdateStrategyKey", int, str, Enum)
SwitcherUpdateStrategyDependencies = TypeVar("SwitcherUpdateStrategyDependencies", dict, TypedDict)
SwitcherUpdateStrategyParams = TypeVar("SwitcherUpdateStrategyParams", dict, TypedDict)


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


# Main

class Switcher(Component, Generic[SwitcherKey, SwitcherDependencies, SwitcherParams]):
    _program: SwitcherProgram[SwitcherKey, SwitcherDependencies, SwitcherParams]

    def __init__(
            self,
            root: Window,
            program: SwitcherProgram[SwitcherKey, SwitcherDependencies, SwitcherParams],
            orientation: LayoutType
    ) -> None: ...

    def config(self) -> void: ...

    def AutoInit(self) -> Self: ...

    @method(UpdateStrategy[SwitcherKey, SwitcherDependencies, SwitcherParams])
    def change_strategy(self, key: SwitcherKey) -> void: ...

    def update_dependencies(self, dependencies: SwitcherDependencies, update_strategies: bool = False) -> Self: ...

    def update_view(self) -> void: ...

    def render_view(self) -> Layout: ...

    @property
    def program(self) -> SwitcherProgram[SwitcherKey, SwitcherDependencies, SwitcherParams]: ...
