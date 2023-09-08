from lib.decorators import method
from lib.decorators.decorator import Decorator


# Decorators

class ConnectAction(Decorator):
    def method(self, target, name, action, callback):
        action.triggered.connect(callback)
        return super().method(target, name, action)


# Main

class Menu:
    def __init__(self, menu):
        self._menu = menu
        self._actions = {}

    def create(self, name, title):
        self._actions[name] = self._menu.addMenu(title)
        return self

    @method(ConnectAction)
    def add(self, name, action):
        self._actions[name].addAction(action)
        return self

    def get(self, name):
        return self._actions[name]
