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
from lib.gui.element.component.switcher import Switcher
from lib.gui.element.component.switcher.strategy import SwitcherStrategy
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
from app.network.neuron.convtranspose1d import TransposedConvolution1d
from app.network.neuron.convtranspose2d import TransposedConvolution2d
from app.network.neuron.convtranspose3d import TransposedConvolution3d
from app.network.neuron.unfold import Unfold
from app.network.neuron.fold import Fold
from app.network.neuron.maxpool1d import MaxPooling1d
from app.network.neuron.maxpool2d import MaxPooling2d
from app.network.neuron.maxpool3d import MaxPooling3d
from app.network.neuron.linear import Linear
from app.gui.neuron import NeuronBuilderSwitcher
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.network.creation.params import NeuronCreationParams


# Main

class NeuronOperationCreationStrategy(SwitcherStrategy):
    class Watch(str):
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
            params=self.switcher_program.params.params,
            options=self.switcher_program.params.options
        )

    def select_neuron(self, event):
        self.make(
            NeuronOperationCreationStrategy.Watch.NEURON_SWITCHER_ELEMENT,
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
        return self.get(NeuronOperationCreationStrategy.Watch.NEURON_SWITCHER_ELEMENT).program

    @property
    def neuron_dependencies(self):
        return NeuronBuilderDependencies(
            network=self.dependencies["network"]
        )

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
                            .Group("Convolution")
                            .Option("Convolution", Convolution1d.title(), Convolution1d)
                            .Option("Convolution", Convolution2d.title(), Convolution2d)
                            .Option("Convolution", Convolution3d.title(), Convolution3d)
                            .Option("Convolution", TransposedConvolution1d.title(), TransposedConvolution1d)
                            .Option("Convolution", TransposedConvolution2d.title(), TransposedConvolution2d)
                            .Option("Convolution", TransposedConvolution3d.title(), TransposedConvolution3d)
                            .Option("Convolution", Unfold.title(), Unfold)
                            .Option("Convolution", Fold.title(), Fold)
                            .Group("Pooling")
                            .Option("Pooling", MaxPooling1d.title(), MaxPooling1d)
                            .Option("Pooling", MaxPooling2d.title(), MaxPooling2d)
                            .Option("Pooling", MaxPooling3d.title(), MaxPooling3d)
                            .Group("Linear")
                            .Option("Linear", Linear.title(), Linear)
                            .Active(self.neuron_index)
                        )
                    )

                )
                .add(
                    Scrollable(root)
                    .ScrollY(True, size=SCROLLBAR_SIZE)
                    .Content(
                        self.watch(
                            NeuronOperationCreationStrategy.Watch.NEURON_SWITCHER_ELEMENT,
                            Switcher(
                                root,
                                NeuronBuilderSwitcher(NeuronType.CONV1D, self.neuron_dependencies),
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
