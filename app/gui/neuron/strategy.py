from abc import ABC, abstractmethod

from lib.gui.element.switcher.strategy import SwitcherStrategy


# Main

class NeuronStrategy(SwitcherStrategy, ABC):
    def __init__(self, dependencies):
        super().__init__(dependencies)

    @property
    @abstractmethod
    def default_params(self):
        pass

    @property
    @abstractmethod
    def default_options(self):
        pass

    @abstractmethod
    def load(self, params, options):
        pass
