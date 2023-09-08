from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QSizePolicy

from lib.gui import LS
from lib.gui.element.button import Button
from lib.gui.element.font import Font
from lib.gui.element.form import FormInput
from lib.gui.element.form.select import SelectBox
from lib.gui.element.form.text import TextInput
from lib.gui.element.scrollable import Scrollable
from lib.gui.element.switcher import Switcher
from lib.gui.element.switcher.strategy import SwitcherStrategy
from lib.gui.element.text import Text
from lib.gui.event import Event
from lib.gui.layout.factory import LayoutFactory
from lib.gui.layout.type import LayoutType

from app import SCROLLBAR_SIZE
from app.hooks import i18n
from app.network.neuron.type import NeuronType
from app.network.neuron.conv1d import Convolution1d
from app.network.neuron.conv2d import Convolution2d
from app.network.neuron.conv3d import Convolution3d
from app.network.neuron.linear import Linear
from app.gui.neuron import NeuronBuilderSwitcher
from app.gui.network.creation.params import NeuronCreationParams


# Main

class NeuronOperationCreationStrategy(SwitcherStrategy):
    NEURON_SWITCHER_ELEMENT = "neuron_switcher_element"

    def __init__(self, dependencies):
        super().__init__(dependencies)

        self._neuron_name = FormInput("")
        self._neuron_type = FormInput((0, Convolution1d))

        self._form_title_font = Font().Size(LS.rem(1.2)).Bold().Underline()
        self._form_label_font = Font().Size(LS.rem(.8))

        self._button_cursor = QCursor(Qt.PointingHandCursor)

    @property
    def params(self):
        return NeuronCreationParams(
            name=self._neuron_name.value,
            params=self.switcher_program.params
        )

    def select_neuron(self, event):
        self.update(
            NeuronOperationCreationStrategy.NEURON_SWITCHER_ELEMENT,
            lambda switcher: switcher.change_strategy(event.data.type())
        )
        return True

    @property
    def neuron_index(self):
        index, neuron = self._neuron_type.value
        return index

    @property
    def neuron_type(self):
        index, neuron = self._neuron_type.value
        return neuron

    @property
    def create(self):
        return self.dependencies["create"]

    def create_neuron(self):
        self.create(self.neuron_type)
        return True

    @property
    def switcher_program(self):
        return self.get(NeuronOperationCreationStrategy.NEURON_SWITCHER_ELEMENT).program

    def render(self, root):
        return (
            LayoutFactory(LayoutType.VERTICAL).create()
            .weight(1)
            .append(
                LayoutFactory(LayoutType.VERTICAL).create()
                .add(
                    Text(root, i18n("window.screens.network.creation.title"))
                    .Font(self._form_title_font)
                )
                .append(
                    LayoutFactory(LayoutType.HORIZONTAL).create()
                    .margin_vertical(LS.rem(.2))
                    .add(
                        Text(root, i18n("window.screens.network.creation.labels.name"))
                        .Font(self._form_label_font)
                    )
                    .append(
                        LayoutFactory(LayoutType.VERTICAL).create()
                        .add(
                            TextInput(root, self._neuron_name.value)
                            .Bind(self._neuron_name)
                        )
                    )
                )
                .append(
                    LayoutFactory(LayoutType.HORIZONTAL).create()
                    .margin_vertical(LS.rem(.2))
                    .add(
                        Text(root, i18n("window.screens.network.creation.labels.type"))
                        .Font(self._form_label_font)
                    )
                    .append(
                        LayoutFactory(LayoutType.VERTICAL).create()
                        .add(
                            SelectBox(root)
                            .Bind(self._neuron_type)
                            .On(
                                Event.Type.Select, self.select_neuron,
                                with_target=False,
                                with_event=True
                            )
                            .Option(Convolution1d.title(), Convolution1d)
                            .Option(Convolution2d.title(), Convolution2d)
                            .Option(Convolution3d.title(), Convolution3d)
                            .Option(Linear.title(), Linear)
                            .Active(self.neuron_index)
                        )
                    )
                )
                .add(
                    Scrollable(root)
                    .ScrollX(False)
                    .ScrollY(True, size=SCROLLBAR_SIZE)
                    .Content(
                        self.watch(
                            NeuronOperationCreationStrategy.NEURON_SWITCHER_ELEMENT,
                            Switcher(
                                root,
                                NeuronBuilderSwitcher(NeuronType.CONV1D, {}),
                                LayoutType.VERTICAL
                            )
                            .InnerSizing(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
                        )
                    )
                )
                .add(
                    Button(root, i18n("window.screens.network.creation.buttons.add"))
                    .Height(LS.rem(2))
                    .Cursor(self._button_cursor)
                    .On(
                        Event.Type.Click, self.create_neuron,
                        with_target=False,
                        with_event=False
                    )
                )
            )
        )
