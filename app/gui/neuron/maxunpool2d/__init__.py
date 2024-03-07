from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSizePolicy

from lib.hooks import entities, filtering
from lib.gui import LS
from lib.gui.element.form import FormInput
from lib.gui.element.form.check import CheckBox
from lib.gui.element.form.select import SelectBox
from lib.gui.element.scrollable import Scrollable
from lib.gui.element.component.switcher import Switcher
from lib.gui.element.text import Text
from lib.gui.event import Event
from lib.gui.layout.type import LayoutType
from lib.gui.layout.factory import LayoutFactory

from app import SCROLLBAR_SIZE
from app.hooks import i18n, map_neurons
from app.network.neuron.type import NeuronType
from app.network.neuron.maxunpool2d import MaxUnpooling2d
from app.network.neuron.maxunpool2d.params import MaxUnpool2dParams
from app.network.neuron.maxunpool2d.options import MaxUnpool2dOptions
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.neuron.maxunpool2d.view import Dimension2dView, Dimension2dSwitcher


# Main

class NeuronBuilderMaxUnpooling2dStrategy(NeuronStrategy):
    class Watch(str):
        DIMENSION_SWITCHER = "dimension_2d_switcher"

    def __init__(self, dependencies):
        super().__init__(dependencies)

        self._pool_layer = None
        self._reflection = FormInput(self.default_options["square"])

        self._input_height = LS.rem(1.6)

    def beforeShow(self):
        super().beforeShow()
        self._pool_layer = FormInput((0, self.default_pool_layer_neuron))

    @property
    def params(self):
        return NeuronStrategyParams(
            params=MaxUnpool2dParams(
                **self.dimension_params.params
            ),
            options=MaxUnpool2dOptions(
                pooling=self.pool_layer_neuron.uuid,
                square=self._reflection.value
            )
        )

    @property
    def default_params(self):
        return MaxUnpooling2d.default_params()

    @property
    def default_options(self):
        return MaxUnpooling2d.default_options()

    def load(self, params, options):
        for index, data in entities(self.pooling_neurons):
            name, neuron = data
            if neuron.uuid == options["pooling"]:
                self._pool_layer.update((index, neuron))

        self._reflection.update(options["square"])
        self.dimension_switcher_program.current_strategy.load(params, options)

    @property
    def dimension_params(self):
        return self.dimension_switcher_program.params

    def change_dimension(self, event):
        key = Dimension2dView.SINGLE if event.checked else Dimension2dView.DOUBLE
        self.make(
            NeuronBuilderMaxUnpooling2dStrategy.Watch.DIMENSION_SWITCHER,
            lambda switcher: switcher.change_strategy(key)
        )
        return True

    @property
    def dimension_switcher_program(self):
        return self.get(NeuronBuilderMaxUnpooling2dStrategy.Watch.DIMENSION_SWITCHER).program

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
        return neuron.type() == NeuronType.MAXPOOL2D and neuron.params["return_indices"]

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
                    Text(root, i18n("window.screens.network.neurons.maxunpool2d.labels.indices"))
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
                    Text(root, i18n("window.screens.network.neurons.maxunpool2d.labels.square"))
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
                        NeuronBuilderMaxUnpooling2dStrategy.Watch.DIMENSION_SWITCHER,
                        Switcher(
                            root,
                            Dimension2dSwitcher(Dimension2dView.DOUBLE, self.dependencies),
                            LayoutType.VERTICAL
                        )
                        .InnerSizing(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
                    )
                )
            )
        )