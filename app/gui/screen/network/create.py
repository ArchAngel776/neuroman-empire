from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QSizePolicy

from lib.gui.element.canvas import Canvas
from lib.gui.element.scrollable import Scrollable
from lib.gui.element.component.switcher import Switcher
from lib.gui.event import Event
from lib.gui.layout.factory import LayoutFactory
from lib.gui.layout.type import LayoutType
from lib.gui.screen import Screen

from app import CANVAS_PADDING, SCROLLBAR_SIZE
from app.gui.graphics import NetworkBuilderCanvasProgram
from app.gui.graphics.variant import NetworkBuilderVariantType
from app.gui.network import NeuronOperationSwitcher
from app.gui.network.operation import NeuronOperation
from app.gui.network.dependencies import NeuronOperationDependencies


# Main

class CreateNetworkScreen(Screen):
    CANVAS_ELEMENT = "canvas_element"
    NEURON_OPERATION_SWITCHER = "neuron_operation_switcher"

    def __init__(self, root, network):
        super().__init__(root)
        self._network = network

    def canvas_setup(self, area, event):
        area_width = event.size().width()
        area_height = self.root.height() * .75

        area.setFixedSize(QSize(int(area_width), int(area_height)))

        canvas_width = area.width() - CANVAS_PADDING - SCROLLBAR_SIZE

        self.update(CreateNetworkScreen.CANVAS_ELEMENT, lambda canvas: canvas.Width(canvas_width))
        self.update_canvas()

        return True

    def update_canvas(self):
        self.update(CreateNetworkScreen.CANVAS_ELEMENT, lambda canvas: canvas.Height(canvas.program.height))

    def create_neuron(self, neuron):
        params = self.switcher_program.params
        self._network.add_neuron(neuron(params["name"], params["params"], params["options"]))

        self.update(
            CreateNetworkScreen.NEURON_OPERATION_SWITCHER,
            lambda switcher: switcher.change_strategy(NeuronOperation.ENTRY)
        )

        self.update_canvas()
        self.canvas_program.update()

    def remove_neuron(self, neuron):
        self._network.neurons.remove(neuron)

        self.update_canvas()
        self.canvas_program.update()

    @staticmethod
    def mouse_move_canvas(canvas, event):
        canvas.program.mark_neuron(event.pos())
        return True

    def click_canvas(self, canvas, event):
        neuron = canvas.program.click_neuron(event.pos())
        if neuron:
            self.canvas_program.change_variant(NetworkBuilderVariantType.NEURON)
            self.update(
                CreateNetworkScreen.NEURON_OPERATION_SWITCHER,
                lambda switcher: switcher
                .update_dependencies(self.neuron_operation_dependencies(neuron), True)
                .change_strategy(NeuronOperation.MODIFY)
            )
            self.update_canvas()
        return True

    def action_entry(self):
        self.canvas_program.change_variant(NetworkBuilderVariantType.NETWORK)
        self.update(
            CreateNetworkScreen.NEURON_OPERATION_SWITCHER,
            lambda switcher: switcher
            .update_dependencies(self.neuron_operation_dependencies(), True)
            .change_strategy(NeuronOperation.ENTRY)
        )
        self.update_canvas()

    def action_creation(self):
        self.canvas_program.change_variant(NetworkBuilderVariantType.NETWORK)
        self.update(
            CreateNetworkScreen.NEURON_OPERATION_SWITCHER,
            lambda switcher: switcher
            .update_dependencies(self.neuron_operation_dependencies(), True)
            .change_strategy(NeuronOperation.CREATE)
        )
        self.update_canvas()

    @property
    def canvas_program(self):
        return self.get(CreateNetworkScreen.CANVAS_ELEMENT).program

    @property
    def switcher_program(self):
        return self.get(CreateNetworkScreen.NEURON_OPERATION_SWITCHER).program

    def neuron_operation_dependencies(self, neuron=None):
        return NeuronOperationDependencies(
            network=self.network,
            neuron=neuron,
            create=self.create_neuron,
            remove=self.remove_neuron,
            action_entry=self.action_entry,
            action_creation=self.action_creation
        )

    @property
    def network(self):
        return self._network

    def render(self):
        return (
            LayoutFactory(LayoutType.VERTICAL).create()
            .append(
                LayoutFactory(LayoutType.HORIZONTAL).create()
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .weight(1)
                    .add(
                        Scrollable(self.root)
                        .ScrollY(True, size=SCROLLBAR_SIZE)
                        .Align(Qt.AlignVCenter)
                        .On(Event.Type.Resize, self.canvas_setup)
                        .Content(
                            self.watch(
                                CreateNetworkScreen.CANVAS_ELEMENT,
                                Canvas(self.root, NetworkBuilderCanvasProgram(self._network))
                                .On(
                                    Event.Type.Show, lambda canvas: canvas.setMouseTracking(True),
                                    with_target=True,
                                    with_event=False
                                )
                                .On(Event.Type.MouseMove, self.mouse_move_canvas)
                                .On(Event.Type.MouseButtonPress, self.click_canvas)
                            )
                        )
                    )
                )
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .weight(1)
                    .add(
                        self.watch(
                            CreateNetworkScreen.NEURON_OPERATION_SWITCHER,
                            Switcher(
                                self.root,
                                NeuronOperationSwitcher(NeuronOperation.ENTRY, self.neuron_operation_dependencies()),
                                LayoutType.VERTICAL
                            )
                            .InnerSizing(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.MinimumExpanding)
                            .AutoInit()
                        )
                    )
                )
            )
        )
