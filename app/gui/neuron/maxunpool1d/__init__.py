from PyQt5.QtWidgets import QSizePolicy

from lib.hooks import filtering, entities
from lib.gui import LS
from lib.gui.element.form import FormInput
from lib.gui.element.component.switcher import Switcher
from lib.gui.element.form.select import SelectBox
from lib.gui.element.text import Text
from lib.gui.layout.factory import LayoutFactory
from lib.gui.layout.type import LayoutType

from app.hooks import i18n, map_neurons
from app.network.neuron.type import NeuronType
from app.network.neuron.maxunpool1d import MaxUnpooling1d
from app.network.neuron.maxunpool1d.params import MaxUnpool1dParams
from app.network.neuron.maxunpool1d.options import MaxUnpool1dOptions
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.neuron.maxunpool1d.view import Dimension1dSwitcher, Dimension1dView
from app.gui.neuron.maxunpool1d.dimension import SingleDimensionStrategy


# Main

class NeuronBuilderMaxUnpooling1dStrategy(NeuronStrategy):
    class Watch(str):
        DIMENSION_SWITCHER = "dimension_1d_switcher"

    def __init__(self, dependencies):
        super().__init__(dependencies)

        self._pool_layer = None

        self._input_height = LS.rem(1.6)

    def beforeShow(self):
        super().beforeShow()
        self._pool_layer = FormInput((0, self.default_pool_layer_neuron))

    @property
    def params(self):
        return NeuronStrategyParams(
            params=MaxUnpool1dParams(
                **self.dimension_params.params
            ),
            options=MaxUnpool1dOptions(
                pooling=self.pool_layer_neuron.uuid
            )
        )

    @property
    def default_params(self):
        return MaxUnpooling1d.default_params()

    @property
    def default_options(self):
        return MaxUnpooling1d.default_options()

    def load(self, params, options):
        for index, data in entities(self.pooling_neurons):
            name, neuron = data
            if neuron.uuid != options["pooling"]:
                continue
            self._pool_layer.update((index, neuron))

    @property
    def dimension_params(self):
        return self.dimension_switcher_program.params

    @property
    def dimension_switcher_program(self):
        return self.get(NeuronBuilderMaxUnpooling1dStrategy.Watch.DIMENSION_SWITCHER).program

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
        return neuron.type() == NeuronType.MAXPOOL1D and neuron.params["return_indices"]

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
                    Text(root, i18n("window.screens.network.neurons.maxunpool1d.labels.indices"))
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
            .add(
                self.watch(
                    NeuronBuilderMaxUnpooling1dStrategy.Watch.DIMENSION_SWITCHER,
                    Switcher(
                        root,
                        Dimension1dSwitcher(Dimension1dView.SINGLE, self.dependencies),
                        LayoutType.VERTICAL
                    )
                    .InnerSizing(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
                    .Payload(self.neuron_payload_provider.provide())
                    .AutoInit()
                )
            )
        )
