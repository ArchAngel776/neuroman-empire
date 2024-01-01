from abc import ABC, abstractmethod
from enum import Enum
from typing import Generic, TypeVar, TypedDict

from lib import void
from lib.decorators import method
from lib.decorators.decorator import Decorator
from lib.gui.element.component.switcher.strategy import SwitcherStrategy
from lib.gui.layout import Layout
from lib.gui.window import Window

# Types

SwitcherProgramKey = TypeVar("SwitcherProgramKey", int, str, Enum)
SwitcherProgramDependencies = TypeVar("SwitcherProgramDependencies", dict, TypedDict)
SwitcherProgramParams = TypeVar("SwitcherProgramParams", dict, TypedDict)

TSwitcherProgramUpdate = TypeVar("TSwitcherProgramUpdate", bound=SwitcherProgram)
UpdateSwitcherProgramKey = TypeVar("UpdateSwitcherProgramKey", int, str, Enum)
UpdateSwitcherProgramDependencies = TypeVar("UpdateSwitcherProgramDependencies", dict, TypedDict)
UpdateSwitcherProgramParams = TypeVar("UpdateSwitcherProgramParams", dict, TypedDict)


# Decorators

class DeepUpdate(
    Decorator[
        void, [
            SwitcherProgram[UpdateSwitcherProgramKey, UpdateSwitcherProgramDependencies, UpdateSwitcherProgramParams],
            UpdateSwitcherProgramDependencies,
            bool
        ]
    ],
    Generic[UpdateSwitcherProgramKey, UpdateSwitcherProgramDependencies, UpdateSwitcherProgramParams]
):
    def method(
            self,
            target: TSwitcherProgramUpdate,
            dependencies: UpdateSwitcherProgramDependencies,
            update_strategies: bool
    ) -> void: ...


# Main

class SwitcherProgram(ABC, Generic[SwitcherProgramKey, SwitcherProgramDependencies, SwitcherProgramParams]):
    _key: SwitcherProgramKey
    _dependencies: SwitcherProgramDependencies

    def __init__(self, key: SwitcherProgramKey, dependencies: SwitcherProgramDependencies) -> None: ...

    @property
    @abstractmethod
    def strategy(self) -> dict[
        SwitcherProgramKey,
        SwitcherStrategy[SwitcherProgramDependencies, SwitcherProgramParams]
    ]: ...

    @property
    def current_strategy(self) -> SwitcherStrategy[SwitcherProgramDependencies, SwitcherProgramParams]: ...

    @property
    def params(self) -> SwitcherProgramParams: ...

    @property
    def dependencies(self) -> SwitcherProgramDependencies: ...

    def change_key(self, key: SwitcherProgramKey) -> void: ...

    @method(DeepUpdate[SwitcherProgramKey, SwitcherProgramDependencies, SwitcherProgramParams])
    def update(self, dependencies: SwitcherProgramDependencies) -> void: ...

    def render_element(self, root: Window) -> Layout: ...
