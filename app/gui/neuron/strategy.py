from abc import ABC, abstractmethod

from lib.gui.element.switcher.strategy import SwitcherStrategy


# Main

class NeuronStrategy(SwitcherStrategy, ABC):
    @property
    @abstractmethod
    def default_params(self):
        pass

    @property
    @abstractmethod
    def default_options(self):
        pass
