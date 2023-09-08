from lib.decorators import method
from lib.decorators.decorator import Decorator
from lib.events.listener import EventListener


# Decorators

class AppendFirst(Decorator):
    def config(self, target, name, callback, with_target=True, with_event=True):
        if name not in target.listeners:
            target.listeners[name] = []
        return self


class OnlyExist(Decorator):
    def method(self, target, name, event):
        return super().method(target, name, event) if name in target.listeners else True


# Main

class EventEmitter:
    def __init__(self):
        self._listeners = {}

    @method(AppendFirst)
    def add_event_listener(self, name, callback, with_target=True, with_event=True):
        self._listeners[name].append(EventListener(callback, with_target, with_event))

    @method(OnlyExist)
    def emit(self, name, event):
        for listener in self._listeners[name]:
            if not self.call(listener, event):
                return False
        return True

    def call(self, listener, event):
        arguments = []
        if listener.with_target:
            arguments.append(self)
        if listener.with_event:
            arguments.append(event)
        return listener.callback(*arguments)

    @property
    def listeners(self):
        return self._listeners
