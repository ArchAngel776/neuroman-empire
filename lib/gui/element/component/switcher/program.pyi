from abc import ABC, abstractmethod
from enum import Enum
from typing import Generic, TypeVar, TypedDict, ClassVar

from PyQt5.QtCore import pyqtSignal

from lib import void
from lib.decorators import method
from lib.decorators.decorator import Decorator
from lib.foundations import Foundation
from lib.gui.element.component.switcher.strategy import SwitcherStrategy
from lib.gui.layout import Layout
from lib.gui.window import Window

# Types

SwitcherProgramKey = TypeVar("SwitcherProgramKey", int, str, Enum)
SwitcherProgramDependencies = TypeVar("SwitcherProgramDependencies", dict, TypedDict)
SwitcherProgramParams = TypeVar("SwitcherProgramParams", dict, TypedDict)

TSwitcherProgramUpdateConnection = TypeVar("TSwitcherProgramUpdateConnection", bound=SwitcherProgram)
SwitcherProgramKeyUpdateConnection = TypeVar("SwitcherProgramKeyUpdateConnection", int, str, Enum)
SwitcherProgramDependenciesUpdateConnection = TypeVar("SwitcherProgramDependenciesUpdateConnection", dict, TypedDict)
SwitcherProgramParamsUpdateConnection = TypeVar("SwitcherProgramParamsUpdateConnection", dict, TypedDict)

TSwitcherProgramDeepUpdate = TypeVar("TSwitcherProgramDeepUpdate", bound=SwitcherProgram)
SwitcherProgramKeyDeepUpdate = TypeVar("SwitcherProgramKeyDeepUpdate", int, str, Enum)
SwitcherProgramDependenciesDeepUpdate = TypeVar("SwitcherProgramDependenciesDeepUpdate", dict, TypedDict)
SwitcherProgramParamsDeepUpdate = TypeVar("SwitcherProgramParamsDeepUpdate", dict, TypedDict)


# Decorators

class UpdateConnection(
    Decorator[
        void, [
            SwitcherProgram[
                SwitcherProgramKeyUpdateConnection,
                SwitcherProgramDependenciesUpdateConnection,
                SwitcherProgramParamsUpdateConnection
            ],
            SwitcherProgramKeyUpdateConnection
        ]
    ],
    Generic[
        SwitcherProgramKeyUpdateConnection,
        SwitcherProgramDependenciesUpdateConnection,
        SwitcherProgramParamsUpdateConnection
    ]
):
    def method(self, target: TSwitcherProgramUpdateConnection, key: SwitcherProgramKeyUpdateConnection) -> void: ...


class DeepUpdate(
    Decorator[
        void, [
            SwitcherProgram[
                SwitcherProgramKeyDeepUpdate, SwitcherProgramDependenciesDeepUpdate, SwitcherProgramParamsDeepUpdate
            ],
            SwitcherProgramDependenciesDeepUpdate,
            bool
        ]
    ],
    Generic[SwitcherProgramKeyDeepUpdate, SwitcherProgramDependenciesDeepUpdate, SwitcherProgramParamsDeepUpdate]
):
    def method(
            self,
            target: TSwitcherProgramDeepUpdate,
            dependencies: SwitcherProgramDependenciesDeepUpdate,
            update_strategies: bool
    ) -> void: ...


# Meta

class SwitcherProgramMeta(type(Foundation), type(ABC)):
    ...


# Main

class SwitcherProgram(
    Foundation,
    ABC,
    Generic[SwitcherProgramKey, SwitcherProgramDependencies, SwitcherProgramParams],
    metaclass=SwitcherProgramMeta
):
    _key: SwitcherProgramKey
    _dependencies: SwitcherProgramDependencies

    # Signals

    view_updated: ClassVar[pyqtSignal] = ...

    def __init__(self, key: SwitcherProgramKey, dependencies: SwitcherProgramDependencies) -> None: ...

    def config(self) -> void: ...

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

    @method(UpdateConnection[SwitcherProgramKey, SwitcherProgramDependencies, SwitcherProgramParams])
    def change_key(self, key: SwitcherProgramKey) -> void: ...

    @method(DeepUpdate[SwitcherProgramKey, SwitcherProgramDependencies, SwitcherProgramParams])
    def update(self, dependencies: SwitcherProgramDependencies) -> void: ...

    def render_element(self, root: Window) -> Layout: ...

    # Slots

    def view_update(self) -> void: ...

    def strategy_before_hook(self) -> void: ...

    def strategy_after_hook(self) -> void: ...
