from typing import Union, Callable

from lib.events.emitter import EventEmitter

# Types

EventListenerCallback = Union[
    Callable[[EventEmitter, object], bool],
    Callable[[object], bool],
    Callable[[EventEmitter], bool],
    Callable[[], bool]
]


# Main

class EventListener:
    _callback: EventListenerCallback
    _with_target: bool
    _with_event: bool

    def __init__(self, callback: EventListenerCallback, with_target: bool, with_event: bool) -> None: ...

    @property
    def callback(self) -> EventListenerCallback: ...

    @property
    def with_target(self) -> bool: ...

    @property
    def with_event(self) -> bool: ...
