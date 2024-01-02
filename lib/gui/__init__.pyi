from typing import Callable, TypeVar

from lib import void
from lib.decorators import method
from lib.decorators.decorator import Decorator

from .element import Element
from .layout import Layout

# Types

TWatcherElement = TypeVar("TWatcherElement", bound=Element)

TWatcherExists = TypeVar("TWatcherExists", bound=Watcher)

WatcherCallback = Callable[[Element], void]


# Decorators

class MarginValidation(Decorator[int, [float]]):
    def method(self, size: float) -> int: ...


class ExistsWatcher(Decorator[void, [Watcher, str, WatcherCallback]]):
    def method(self, target: TWatcherExists, key: str, updater: WatcherCallback) -> void: ...


# Foundations

class LS:
    @staticmethod
    @method(MarginValidation)
    def rem(size: float) -> int: ...


# Base

class Watcher:
    _watched: dict[str, Element]

    def __init__(self) -> None: ...

    def watcher_exists(self, key: str) -> bool: ...

    def watch(self, key: str, element: TWatcherElement) -> TWatcherElement: ...

    def get(self, key: str) -> TWatcherElement: ...

    @method(ExistsWatcher)
    def make(self, key: str, updater: WatcherCallback) -> void: ...
