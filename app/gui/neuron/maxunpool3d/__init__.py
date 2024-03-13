from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSizePolicy

from lib.hooks import entities, filtering
from lib.gui import LS
from lib.gui.element.form import FormInput
from lib.gui.element.form.select import SelectBox
from lib.gui.element.form.check import CheckBox
from lib.gui.element.scrollable import Scrollable
from lib.gui.element.component.switcher import Switcher
from lib.gui.element.text import Text
from lib.gui.event import Event
from lib.gui.layout.factory import LayoutFactory
from lib.gui.layout.type import LayoutType

from app import SCROLLBAR_SIZE
from app.hooks import i18n, map_neurons
from app.network.neuron.type import NeuronType
from app.network.neuron.maxunpool3d import MaxUnpooling3d
from app.network.neuron.maxunpool3d.params import MaxUnpool3dParams
from app.network.neuron.maxunpool3d.options import MaxUnpool3dOptions
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.neuron.maxunpool3d.view import Dimension3dView, Dimension3dSwitcher


# Main

class NeuronBuilderMaxUnpooling3dStrategy(NeuronStrategy):
    class Watch(str):
        DIMENSION_SWITCHER = "dimension_3d_switcher"

    def __init__(self, dependencies):
        super().__init__(dependencies)

        self._pool_layer = None

        self._reflection = FormInput(self.default_options["cube"])
        self._input_height = LS.rem(1.6)

    def beforeShow(self):
        super().beforeShow()
        self._pool_layer = FormInput((0, self.default_pool_layer_neuron))

    @property
    def params(self):
        return NeuronStrategyParams(
            params=MaxUnpool3dParams(
                **self.dimension_params.params
            ),
            options=MaxUnpool3dOptions(
                pooling=self.pool_layer_neuron.uuid,
                cube=self._reflection.value
            )
        )

    @property
    def default_params(self):
        return MaxUnpooling3d.default_params()

    @property
    def default_options(self):
        return MaxUnpooling3d.default_options()

    def load(self, params, options):
        for index, data in entities(self.pooling_neurons):
            name, neuron = data
            if neuron.uuid != options["pooling"]:
                continue
            self._pool_layer.update((index, neuron))

        self._reflection.update(options["cube"])

    @property
    def dimension_params(self):
        return self.dimension_switcher_program.params

    @staticmethod
    def value_to_dimension(value):
        return Dimension3dView.SINGLE if value else Dimension3dView.TRIPLE

    def change_dimension(self, event):
        self.make(
            NeuronBuilderMaxUnpooling3dStrategy.Watch.DIMENSION_SWITCHER,
            lambda switcher: switcher.change_strategy(self.value_to_dimension(event.checked))
        )
        return True

    @property
    def dimension_switcher_program(self):
        return self.get(NeuronBuilderMaxUnpooling3dStrategy.Watch.DIMENSION_SWITCHER).program

    @property
    def pool_layer(self):
        if self._pool_layer is None:
            raise ValueError("Not specified value yet.")
        return self._pool_layer

    @property
    def pool_layer_index(self):
        index, neuron = self.pool_layer.value
        return index

    @property
    def pool_layer_neuron(self):
        index, neuron = self.pool_layer.value
        return neuron

    @property
    def pooling_neurons(self):
        return map_neurons(filtering(self.dependencies["network"], self.select_indicated_pooling))

    @staticmethod
    def select_indicated_pooling(neuron, index):
        return neuron.type() == NeuronType.MAXPOOL3D and neuron.params["return_indices"]

    @property
    def default_pool_layer_neuron(self):
        pooling_neurons = self.pooling_neurons

        if len(pooling_neurons) > 0:
            name, neuron = pooling_neurons[0]
            return neuron

        raise BrokenPipeError("Cannot detect any MaxPooling1D layer with enabled indices.")

    def render(self, root):
        return (
            LayoutFactory(LayoutType.VERTICAL).create()
            .append(
                LayoutFactory(LayoutType.HORIZONTAL).create()
                .add(
                    Text(root, i18n("window.screens.network.neurons.maxunpool3d.labels.indices"))
                )
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .add(
                        SelectBox(root)
                        .Bind(self.pool_layer)
                        .Generate(self.pooling_neurons)
                        .Active(self.pool_layer_index)
                    )
                )
            )
            .append(
                LayoutFactory(LayoutType.HORIZONTAL).create()
                .margin_vertical(LS.rem(.8))
                .add(
                    Text(root, i18n("window.screens.network.neurons.maxunpool3d.labels.cube"))
                )
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .align(Qt.AlignLeft)
                    .margin_horizontal(LS.rem(.2))
                    .add(
                        CheckBox(root, self._reflection.value)
                        .Bind(self._reflection)
                        .On(
                            Event.Type.Change, self.change_dimension,
                            with_target=False,
                            with_event=True
                        )
                    )
                )
            )
            .add(
                Scrollable(root)
                .ScrollX(True, size=SCROLLBAR_SIZE)
                .ScrollY(False)
                .Adjust(Scrollable.SizeAdjustPolicy.AdjustToContents)
                .Content(
                    self.watch(
                        NeuronBuilderMaxUnpooling3dStrategy.Watch.DIMENSION_SWITCHER,
                        Switcher(
                            root,
                            Dimension3dSwitcher(self.value_to_dimension(self._reflection.value), self.dependencies),
                            LayoutType.VERTICAL
                        )
                        .InnerSizing(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
                        .Payload(self.neuron_payload_provider.provide())
                    )
                )
            )
        )
