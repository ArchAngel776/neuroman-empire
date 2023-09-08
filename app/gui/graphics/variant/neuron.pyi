from typing import Optional

from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QPainter

from lib import void

from app.network.neuron import Neuron
from app.gui.graphics.variant import NetworkBuilderVariant


# Main

class NetworkBuilderNeuronVariant(NetworkBuilderVariant):
    def draw(self, painter: QPainter) -> void: ...

    def get_height(self) -> int: ...

    def mark_neuron(self, point: QPoint) -> void: ...

    def click_neuron(self, point: QPoint) -> Optional[Neuron]: ...
