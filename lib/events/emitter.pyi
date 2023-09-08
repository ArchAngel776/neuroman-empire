from enum import Enum
from typing import Generic, TypeVar

from lib import void
from lib.decorators import method
from lib.decorators.decorator import Decorator
from lib.events.listener import EventListener, EventListenerCallback

# Types

EventType = TypeVar("EventType", int, str, Enum)
TEvent = TypeVar("TEvent", bound=object)

TEventEmitterAppendFirst = TypeVar("TEventEmitterAppendFirst", bound=EventEmitter)
EventTypeAppendFirst = TypeVar("EventTypeAppendFirst", int, str, Enum)
EventAppendFirst = TypeVar("EventAppendFirst", bound=object)

TEventEmitterOnlyExist = TypeVar("TEventEmitterOnlyExist", bound=EventEmitter)
EventTypeOnlyExist = TypeVar("EventTypeOnlyExist", int, str, Enum)
EventOnlyExist = TypeVar("EventOnlyExist", bound=object)


# Decorators

class AppendFirst(
    Decorator[
        void, [
            EventEmitter[EventTypeAppendFirst, EventAppendFirst],
            EventTypeAppendFirst,
            EventListenerCallback,
            bool,
            bool
        ]
    ],
    Generic[EventTypeAppendFirst, EventAppendFirst]
):
    def config(
            self,
            target: TEventEmitterAppendFirst,
            name: EventTypeAppendFirst,
            callback: EventListenerCallback,
            with_target: bool = True,
            with_event: bool = True
    ) -> AppendFirst[EventTypeAppendFirst, EventAppendFirst]: ...


class OnlyExist(
    Decorator[bool, [EventEmitter[EventTypeOnlyExist, EventOnlyExist], EventTypeOnlyExist, EventOnlyExist]],
    Generic[EventTypeOnlyExist, EventOnlyExist]
):
    def method(self, target: TEventEmitterOnlyExist, name: EventTypeOnlyExist, event: EventOnlyExist) -> bool: ...



# Main

class EventEmitter(Generic[EventType, TEvent]):
    _listeners: dict[EventType, list[EventListener]]

    def __init__(self) -> None: ...

    @method(AppendFirst[EventType, TEvent])
    def add_event_listener(
            self,
            name: EventType,
            callback: EventListenerCallback,
            with_target: bool = True,
            with_event: bool = True
    ) -> void: ...

    @method(OnlyExist[EventType, TEvent])
    def emit(self, name: EventType, event: TEvent) -> bool: ...

    def call(self, listener: EventListener, event: TEvent) -> bool: ...

    @property
    def listeners(self) -> dict[EventType, list[EventListener]]: ...
