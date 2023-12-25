from typing import Optional

from PyQt5.QtCore import QPoint, QPointF
from PyQt5.QtGui import QColor, QCursor, QPainter, QPaintEvent, QLinearGradient

from lib import void
from lib.decorators import method
from lib.gui.element.font import Font
from lib.gui.element.canvas.program import CanvasProgram, CanvasCycle

from app.network import Network
from app.network.neuron import Neuron

from .variant import NetworkBuilderVariantType, NetworkBuilderVariant
from .variant.network import NetworkBuilderNetworkVariant
from .variant.neuron import NetworkBuilderNeuronVariant


# Main

class NetworkBuilderCanvasProgram(CanvasProgram[NetworkBuilderVariantType]):
    _network: Network

    _font_name: Font
    _font_label: Font

    _color_border: QColor
    _color_background: QColor
    _color_label: QColor

    _color_conv1d: QColor
    _color_conv2d: QColor
    _color_conv3d: QColor
    _color_convtranspose1d: QColor
    _color_convtranspose2d: QColor
    _color_convtranspose3d: QColor
    _color_unfold: QColor
    _color_fold: QColor
    _color_maxpool1d: QColor
    _color_maxpool2d: QColor
    _color_maxpool3d: QColor
    _color_linear: QColor

    _cursor_active: QCursor
    _cursor_default: QCursor

    def __init__(self, network: Network) -> None: ...

    @property
    def variants(self) -> dict[NetworkBuilderVariantType, NetworkBuilderVariant]: ...

    @method(CanvasCycle[NetworkBuilderVariantType])
    def draw(self, event: QPaintEvent, painter: QPainter) -> void: ...

    @property
    def height(self) -> int: ...

    def background(self, painter: QPainter) -> void: ...

    def mark_neuron(self, point: QPoint) -> void: ...

    def click_neuron(self, point: QPoint) -> Optional[Neuron]: ...

    def draw_neuron(self, painter: QPainter, index: int, color: QColor) -> void: ...

    def draw_neuron_name(self, painter: QPainter, index: int, name: str) -> void: ...

    def draw_neuron_label(self, painter: QPainter, index: int, label: str) -> void: ...

    def draw_neuron_connection(self, painter: QPainter, index: int, neurons: tuple[Neuron, Neuron]) -> void: ...

    def neuron_color(self, neuron: Neuron) -> QColor: ...

    def connection_color(self, coordinates: tuple[QPointF, QPointF], start: Neuron, end: Neuron) -> QLinearGradient: ...

    # Attributes

    @property
    def variant(self) -> NetworkBuilderVariant: ...

    @property
    def network(self) -> Network: ...

    @property
    def offset_x(self) -> float: ...

    def offset_y(self, index: int) -> float: ...

    @property
    def neuron_size(self) -> int: ...

    @property
    def padding(self) -> int: ...

    @property
    def indent(self) -> int: ...

    @property
    def inner_width(self) -> int: ...

    @property
    def inner_height(self) -> int: ...

    @property
    def radius(self) -> float: ...

    @property
    def inner_radius(self) -> float: ...

    # Properties

    @property
    def font_name(self) -> Font: ...

    @property
    def font_label(self) -> Font: ...

    @property
    def color_border(self) -> QColor: ...

    @property
    def color_background(self) -> QColor: ...

    @property
    def color_label(self) -> QColor: ...

    @property
    def color_conv1d(self) -> QColor: ...

    @property
    def color_conv2d(self) -> QColor: ...

    @property
    def color_conv3d(self) -> QColor: ...

    @property
    def color_convtranspose1d(self) -> QColor: ...

    @property
    def color_convtranspose2d(self) -> QColor: ...

    @property
    def color_unfold(self) -> QColor: ...

    @property
    def color_fold(self) -> QColor: ...

    @property
    def color_convtranspose3d(self) -> QColor: ...

    @property
    def color_maxpool1d(self) -> QColor: ...

    @property
    def color_maxpool2d(self) -> QColor: ...

    @property
    def color_maxpool3d(self) -> QColor: ...

    @property
    def color_linear(self) -> QColor: ...

    @property
    def cursor_active(self) -> QCursor: ...

    @property
    def cursor_default(self) -> QCursor: ...
