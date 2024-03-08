from abc import ABC, abstractmethod

from PyQt5.QtCore import pyqtSignal

from lib.decorators import method
from lib.decorators.decorator import Decorator
from lib.foundations import Foundation


# Decorators

class UpdateConnection(Decorator):
    def method(self, target, key):
        target.current_strategy.view_updated.disconnect(target.view_update)
        super().method(target, key)
        target.current_strategy.view_updated.connect(target.view_update)


class DeepUpdate(Decorator):
    def method(self, target, dependencies, update_strategies):
        if update_strategies:
            for key in target.strategy:
                target.strategy[key].update_dependencies(dependencies)
        return super().method(target, dependencies)


# Meta

class SwitcherProgramMeta(type(Foundation), type(ABC)):
    pass


# Main

class SwitcherProgram(Foundation, ABC, metaclass=SwitcherProgramMeta):
    # Signals

    view_updated = pyqtSignal()

    def __init__(self, key, dependencies):
        super().__init__()
        self._key = key
        self._dependencies = dependencies

    def config(self):
        self.current_strategy.view_updated.connect(self.view_update)

    @property
    @abstractmethod
    def strategy(self):
        pass

    @property
    def current_strategy(self):
        return self.strategy[self._key]

    @property
    def params(self):
        return self.current_strategy.params

    @property
    def dependencies(self):
        return self._dependencies

    @method(UpdateConnection)
    def change_key(self, key):
        self._key = key

    @method(DeepUpdate)
    def update(self, dependencies):
        self._dependencies = dependencies

    def render_element(self, root):
        return self.current_strategy.render(root)

    # Slots

    def view_update(self):
        self.view_updated.emit()

    def strategy_before_hook(self):
        self.current_strategy.beforeShow()

    def strategy_after_hook(self):
        self.current_strategy.afterShow()
