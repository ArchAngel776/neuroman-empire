from abc import abstractmethod, ABC
from enum import Enum
from typing import Optional

from PyQt5.QtCore import QPoint

from lib import void
from lib.gui.element.canvas.program.variant import CanvasProgramVariant

from app.network.neuron import Neuron
from app.gui.graphics import NetworkBuilderCanvasProgram


# Data

class NetworkBuilderVariantType(Enum):
    NETWORK = ... #type: NetworkBuilderVariantType
    NEURON = ... #type: NetworkBuilderVariantType


# Main

class NetworkBuilderVariant(CanvasProgramVariant[NetworkBuilderCanvasProgram], ABC):
    @abstractmethod
    def get_height(self) -> int: ...

    @abstractmethod
    def mark_neuron(self, point: QPoint) -> void: ...

    @abstractmethod
    def click_neuron(self, point: QPoint) -> Optional[Neuron]: ...
