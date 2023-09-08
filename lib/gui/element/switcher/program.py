from abc import ABC, abstractmethod

from lib.decorators import method
from lib.decorators.decorator import Decorator


# Decorators

class DeepUpdate(Decorator):
    def method(self, target, dependencies, update_strategies):
        if update_strategies:
            for key in target.strategy:
                target.strategy[key].update_dependencies(dependencies)
        return super().method(target, dependencies)


# Main

class SwitcherProgram(ABC):
    def __init__(self, key, dependencies):
        self._key = key
        self._dependencies = dependencies

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

    def change_key(self, key):
        self._key = key

    @method(DeepUpdate)
    def update(self, dependencies):
        self._dependencies = dependencies

    def render_element(self, root):
        return self.current_strategy.render(root).element
