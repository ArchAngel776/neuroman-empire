from PyQt5.QtGui import QResizeEvent, QMouseEvent

from lib import void
from lib.gui.element.canvas import Canvas
from lib.gui.element.scrollable import Scrollable
from lib.gui.layout import Layout
from lib.gui.screen import Screen

from app.network import Network
from app.network.neuron import Neuron
from app.gui import MainWindow
from app.gui.graphics import NetworkBuilderCanvasProgram
from app.gui.network import NeuronOperationSwitcher
from app.gui.network.dependencies import NeuronOperationDependencies


# Main

class CreateNetworkScreen(Screen[MainWindow]):
    class Watch(str):
        CANVAS_ELEMENT = ... #type: CreateNetworkScreen.Watch
        NEURON_OPERATION_SWITCHER = ... #type: CreateNetworkScreen.Watch

    _network: Network

    def __init__(self, root: MainWindow, network: Network) -> None: ...

    def canvas_setup(self, area: Scrollable, event: QResizeEvent) -> bool: ...

    def update_canvas(self) -> void: ...

    def create_neuron(self, neuron: type[Neuron]) -> void: ...

    def remove_neuron(self, neuron: Neuron) -> void: ...

    @staticmethod
    def mouse_move_canvas(canvas: Canvas[NetworkBuilderCanvasProgram], event: QMouseEvent) -> bool: ...

    def click_canvas(self, canvas: Canvas[NetworkBuilderCanvasProgram], event: QMouseEvent) -> bool: ...

    def action_entry(self) -> void: ...

    def action_creation(self) -> void: ...

    @property
    def canvas_program(self) -> NetworkBuilderCanvasProgram: ...

    @property
    def switcher_program(self) -> NeuronOperationSwitcher: ...

    def neuron_operation_dependencies(self, neuron: Neuron = None) -> NeuronOperationDependencies: ...

    @property
    def network(self) -> Network: ...

    def render(self) -> Layout: ...
