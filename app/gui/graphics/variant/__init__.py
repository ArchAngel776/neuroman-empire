from abc import abstractmethod, ABC
from enum import Enum

from lib.gui.element.canvas.program.variant import CanvasProgramVariant


# Data

class NetworkBuilderVariantType(Enum):
    NETWORK = 0
    NEURON = 1


# Main

class NetworkBuilderVariant(CanvasProgramVariant, ABC):
    @abstractmethod
    def get_height(self):
        pass

    @abstractmethod
    def mark_neuron(self, point):
        pass

    @abstractmethod
    def click_neuron(self, point):
        pass
