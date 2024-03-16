from PyQt5.QtCore import Qt, QRectF, QPointF
from PyQt5.QtGui import QColor, QCursor, QPainter, QPainterPath, QPen, QLinearGradient

from lib.decorators import method
from lib.gui import LS
from lib.gui.element.font import Font
from lib.gui.element.canvas.program import CanvasProgram, CanvasCycle

from app import CANVAS_NEURON, CANVAS_PADDING, CANVAS_INDENT
from app.network.neuron.type import NeuronType
from app.gui.graphics.variant import NetworkBuilderVariantType, NetworkBuilderVariant
from app.gui.graphics.variant.network import NetworkBuilderNetworkVariant
from app.gui.graphics.variant.neuron import NetworkBuilderNeuronVariant


# Main

class NetworkBuilderCanvasProgram(CanvasProgram):
    def __init__(self, network):
        super().__init__(NetworkBuilderVariantType.NETWORK)
        self._network = network

        self._font_name = Font().Size(LS.rem(.8)).Bold()
        self._font_label = Font().Size(LS.rem(.8)).Italic()

        self._color_border = QColor(255, 255, 255)
        self._color_background = QColor(64, 64, 64)
        self._color_label = QColor(255, 255, 255)

        self._color_conv1d = QColor(64, 255, 255)
        self._color_conv2d = QColor(128, 255, 255)
        self._color_conv3d = QColor(192, 255, 255)
        self._color_convtranspose1d = QColor(255, 32, 128)
        self._color_convtranspose2d = QColor(255, 64, 128)
        self._color_convtranspose3d = QColor(255, 96, 128)
        self._color_unfold = QColor(160, 160, 160)
        self._color_fold = QColor(139, 139, 139)
        self._color_maxpool1d = QColor(128, 32, 255)
        self._color_maxpool2d = QColor(128, 64, 255)
        self._color_maxpool3d = QColor(128, 96, 255)
        self._color_maxunpool1d = QColor(128, 128, 192)
        self._color_maxunpool2d = QColor(164, 128, 218)
        self._color_maxunpool3d = QColor(192, 128, 255)
        self._color_avgpool1d = QColor(64, 255, 164)
        self._color_avgpool2d = QColor(64, 255, 192)
        self._color_avgpool3d = QColor(64, 255, 220)
        self._color_fractionalmaxpool2d = QColor(164, 255, 64)
        self._color_fractionalmaxpool3d = QColor(192, 255, 92)
        self._color_lppool1d = QColor(128, 232, 232)
        self._color_lppool2d = QColor(164, 232, 232)
        self._color_adaptivemaxpool1d = QColor(32, 132, 255)
        self._color_adaptivemaxpool2d = QColor(32, 164, 255)
        self._color_adaptivemaxpool3d = QColor(32, 196, 255)
        self._color_adaptiveavgpool1d = QColor(32, 255, 132)
        self._color_adaptiveavgpool2d = QColor(32, 255, 164)
        self._color_adaptiveavgpool3d = QColor(32, 255, 196)
        self._color_reflectionpad1d = QColor(255, 96, 96)
        self._color_reflectionpad2d = QColor(255, 96, 128)
        self._color_reflectionpad3d = QColor(255, 96, 156)
        self._color_replicationpad1d = QColor(232, 128, 96)
        self._color_replicationpad2d = QColor(232, 128, 128)
        self._color_replicationpad3d = QColor(232, 128, 156)
        self._color_zeropad1d = QColor(192, 164, 96)
        self._color_zeropad2d = QColor(192, 164, 128)
        self._color_zeropad3d = QColor(192, 164, 156)
        self._color_constantpad1d = QColor(192, 96, 96)
        self._color_constantpad2d = QColor(192, 128, 96)
        self._color_constantpad3d = QColor(192, 164, 96)
        self._color_circularpad1d = QColor(192, 96, 128)
        self._color_circularpad2d = QColor(192, 128, 128)
        self._color_circularpad3d = QColor(192, 164, 128)
        self._color_linear = QColor(128, 255, 128)

        self._cursor_active = QCursor(Qt.PointingHandCursor)
        self._cursor_default = QCursor(Qt.ArrowCursor)

    @property
    def variants(self):
        return {
            NetworkBuilderVariantType.NETWORK: NetworkBuilderNetworkVariant(self),
            NetworkBuilderVariantType.NEURON: NetworkBuilderNeuronVariant(self)
        }

    @method(CanvasCycle)
    def draw(self, event, painter):
        painter.setRenderHint(QPainter.RenderHint.HighQualityAntialiasing)

        self.background(painter)
        self.variant.draw(painter)

    @property
    def height(self):
        return self.variant.get_height()

    def background(self, painter):
        outer_rect = QRectF(0, 0, self.width, self.height)

        outer_path = QPainterPath()
        outer_path.addRoundedRect(outer_rect, self.radius, self.radius)

        inner_rect = QRectF(self.padding, self.padding, self.inner_width, self.inner_height)

        inner_path = QPainterPath()
        inner_path.addRoundedRect(inner_rect, self.inner_radius, self.inner_radius)

        painter.fillPath(outer_path, self.color_border)
        painter.fillPath(inner_path, self.color_background)

    def mark_neuron(self, point):
        self.variant.mark_neuron(point)

    def click_neuron(self, point):
        return self.variant.click_neuron(point)

    def draw_neuron(self, painter, index, color):
        path = QPainterPath()
        path.addEllipse(self.offset_x, self.offset_y(index), self.neuron_size, self.neuron_size)

        painter.fillPath(path, color)

    def draw_neuron_name(self, painter, index, name):
        offset_x = self.width / 2 - self.padding
        offset_y = index * (self.indent + self.neuron_size) + self.indent + (self.neuron_size + self.padding) / 2

        path = QPainterPath()
        path.addText(offset_x, offset_y, self.font_name, name)

        path.translate(-path.boundingRect().width(), 0)

        painter.fillPath(path, self.color_label)

    def draw_neuron_label(self, painter, index, label):
        offset_x = self.width / 2 - self.padding
        offset_y = index * (self.indent + self.neuron_size) + self.indent + (self.neuron_size + self.padding) / 2

        path = QPainterPath()
        path.addText(offset_x, offset_y, self.font_label, label)

        path.translate(-path.boundingRect().width(), (self.neuron_size - self.padding) / 2)

        painter.fillPath(path, self.color_label)

    def draw_neuron_connection(self, painter, index, neurons):
        offset_x = (self.width + self.neuron_size) / 2 + self.padding
        offset_y = (index + 1) * (self.indent + self.neuron_size) + self.padding

        start_point = QPointF(offset_x, offset_y)
        end_point = QPointF(offset_x, offset_y + self.indent)

        path = QPainterPath()
        path.moveTo(start_point)
        path.lineTo(end_point)

        pen = QPen()
        pen.setWidth(LS.rem(.3))
        pen.setBrush(self.connection_color((start_point, end_point), *neurons))

        painter.strokePath(path, pen)

    def neuron_color(self, neuron):
        match neuron.type():
            case NeuronType.CONV1D:
                return self.color_conv1d
            case NeuronType.CONV2D:
                return self.color_conv2d
            case NeuronType.CONV3D:
                return self.color_conv3d
            case NeuronType.CONVTRANSPOSE1D:
                return self.color_convtranspose1d
            case NeuronType.CONVTRANSPOSE2D:
                return self.color_convtranspose2d
            case NeuronType.CONVTRANSPOSE3D:
                return self.color_convtranspose3d
            case NeuronType.UNFOLD:
                return self.color_unfold
            case NeuronType.FOLD:
                return self.color_fold
            case NeuronType.MAXPOOL1D:
                return self.color_maxpool1d
            case NeuronType.MAXPOOL2D:
                return self.color_maxpool2d
            case NeuronType.MAXPOOL3D:
                return self.color_maxpool3d
            case NeuronType.MAXUNPOOL1D:
                return self.color_maxunpool1d
            case NeuronType.MAXUNPOOL2D:
                return self.color_maxunpool2d
            case NeuronType.MAXUNPOOL3D:
                return self.color_maxunpool3d
            case NeuronType.AVGPOOL1D:
                return self.color_avgpool1d
            case NeuronType.AVGPOOL2D:
                return self.color_avgpool2d
            case NeuronType.AVGPOOL3D:
                return self.color_avgpool3d
            case NeuronType.FRACTIONALMAXPOOL2D:
                return self.color_fractionalmaxpool2d
            case NeuronType.FRACTIONALMAXPOOL3D:
                return self._color_fractionalmaxpool3d
            case NeuronType.LPPOOL1D:
                return self.color_lppool1d
            case NeuronType.LPPOOL2D:
                return self.color_lppool2d
            case NeuronType.ADAPTIVEMAXPOOL1D:
                return self.color_adaptivemaxpool1d
            case NeuronType.ADAPTIVEMAXPOOL2D:
                return self.color_adaptivemaxpool2d
            case NeuronType.ADAPTIVEMAXPOOL3D:
                return self.color_adaptivemaxpool3d
            case NeuronType.ADAPTIVEAVGPOOL1D:
                return self.color_adaptiveavgpool1d
            case NeuronType.ADAPTIVEAVGPOOL2D:
                return self.color_adaptiveavgpool2d
            case NeuronType.ADAPTIVEAVGPOOL3D:
                return self.color_adaptiveavgpool3d
            case NeuronType.REFLECTIONPAD1D:
                return self.color_reflectionpad1d
            case NeuronType.REFLECTIONPAD2D:
                return self.color_reflectionpad2d
            case NeuronType.REFLECTIONPAD3D:
                return self.color_reflectionpad3d
            case NeuronType.REPLICATIONPAD1D:
                return self.color_replicationpad1d
            case NeuronType.REPLICATIONPAD2D:
                return self.color_replicationpad2d
            case NeuronType.REPLICATIONPAD3D:
                return self.color_replicationpad3d
            case NeuronType.ZEROPAD1D:
                return self.color_zeropad1d
            case NeuronType.ZEROPAD2D:
                return self.color_zeropad2d
            case NeuronType.ZEROPAD3D:
                return self.color_zeropad3d
            case NeuronType.CONSTANTPAD1D:
                return self.color_constantpad1d
            case NeuronType.CONSTANTPAD2D:
                return self.color_constantpad2d
            case NeuronType.CONSTANTPAD3D:
                return self.color_constantpad3d
            case NeuronType.CIRCULARPAD1D:
                return self.color_circularpad1d
            case NeuronType.CIRCULARPAD2D:
                return self.color_circularpad2d
            case NeuronType.CIRCULARPAD3D:
                return self.color_circularpad3d
            case NeuronType.LINEAR:
                return self.color_linear
            case _:
                raise ValueError("Invalid neuron type.")

    def connection_color(self, coordinates, start, end):
        gradient = QLinearGradient(*coordinates)

        gradient.setColorAt(0, self.neuron_color(start))
        gradient.setColorAt(1, self.neuron_color(end))

        return gradient

    # Attributes

    @property
    def variant(self):
        return self.variants[self.variant_type]

    @property
    def network(self):
        return self._network

    @property
    def offset_x(self):
        return self.width / 2 + self.padding

    def offset_y(self, index):
        return index * (self.indent + self.neuron_size) + self.indent + self.padding

    @property
    def neuron_size(self):
        return CANVAS_NEURON

    @property
    def padding(self):
        return CANVAS_PADDING

    @property
    def indent(self):
        return CANVAS_INDENT

    @property
    def inner_width(self):
        return self.width - self.padding * 2

    @property
    def inner_height(self):
        return self.height - self.padding * 2

    @property
    def radius(self):
        return 16

    @property
    def inner_radius(self):
        return 12

    # Properties

    @property
    def font_name(self):
        return self._font_name

    @property
    def font_label(self):
        return self._font_label

    @property
    def color_border(self):
        return self._color_border

    @property
    def color_background(self):
        return self._color_background

    @property
    def color_label(self):
        return self._color_label

    @property
    def color_conv1d(self):
        return self._color_conv1d

    @property
    def color_conv2d(self):
        return self._color_conv2d

    @property
    def color_conv3d(self):
        return self._color_conv3d

    @property
    def color_convtranspose1d(self):
        return self._color_convtranspose1d

    @property
    def color_convtranspose2d(self):
        return self._color_convtranspose2d

    @property
    def color_convtranspose3d(self):
        return self._color_convtranspose3d

    @property
    def color_unfold(self):
        return self._color_unfold

    @property
    def color_fold(self):
        return self._color_fold

    @property
    def color_maxpool1d(self):
        return self._color_maxpool1d

    @property
    def color_maxpool2d(self):
        return self._color_maxpool2d

    @property
    def color_maxpool3d(self):
        return self._color_maxpool3d

    @property
    def color_maxunpool1d(self):
        return self._color_maxunpool1d

    @property
    def color_maxunpool2d(self):
        return self._color_maxunpool2d

    @property
    def color_maxunpool3d(self):
        return self._color_maxunpool3d

    @property
    def color_avgpool1d(self):
        return self._color_avgpool1d

    @property
    def color_avgpool2d(self):
        return self._color_avgpool2d

    @property
    def color_avgpool3d(self):
        return self._color_avgpool3d

    @property
    def color_fractionalmaxpool2d(self):
        return self._color_fractionalmaxpool2d

    @property
    def color_fractionalmaxpool3d(self):
        return self._color_fractionalmaxpool3d

    @property
    def color_lppool1d(self):
        return self._color_lppool1d

    @property
    def color_lppool2d(self):
        return self._color_lppool2d

    @property
    def color_adaptivemaxpool1d(self):
        return self._color_adaptivemaxpool1d

    @property
    def color_adaptivemaxpool2d(self):
        return self._color_adaptivemaxpool2d

    @property
    def color_adaptivemaxpool3d(self):
        return self._color_adaptivemaxpool3d

    @property
    def color_adaptiveavgpool1d(self):
        return self._color_adaptiveavgpool1d

    @property
    def color_adaptiveavgpool2d(self):
        return self._color_adaptiveavgpool2d

    @property
    def color_adaptiveavgpool3d(self):
        return self._color_adaptiveavgpool3d

    @property
    def color_reflectionpad1d(self):
        return self._color_reflectionpad1d

    @property
    def color_reflectionpad2d(self):
        return self._color_reflectionpad1d

    @property
    def color_reflectionpad3d(self):
        return self._color_reflectionpad1d

    @property
    def color_replicationpad1d(self):
        return self._color_replicationpad1d

    @property
    def color_replicationpad2d(self):
        return self._color_replicationpad2d

    @property
    def color_replicationpad3d(self):
        return self._color_replicationpad3d

    @property
    def color_zeropad1d(self):
        return self._color_zeropad1d

    @property
    def color_zeropad2d(self):
        return self._color_zeropad2d

    @property
    def color_zeropad3d(self):
        return self._color_zeropad3d

    @property
    def color_constantpad1d(self):
        return self._color_constantpad1d

    @property
    def color_constantpad2d(self):
        return self._color_constantpad2d

    @property
    def color_constantpad3d(self):
        return self._color_constantpad3d

    @property
    def color_circularpad1d(self):
        return self._color_circularpad1d

    @property
    def color_circularpad2d(self):
        return self._color_circularpad2d

    @property
    def color_circularpad3d(self):
        return self._color_circularpad3d

    @property
    def color_linear(self):
        return self._color_linear

    @property
    def cursor_active(self):
        return self._cursor_active

    @property
    def cursor_default(self):
        return self._cursor_default
