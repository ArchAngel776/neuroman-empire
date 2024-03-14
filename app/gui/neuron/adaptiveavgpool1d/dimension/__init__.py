from PyQt5.QtCore import Qt

from lib.gui import LS
from lib.gui.element.form import FormInput
from lib.gui.element.form.integer import IntegerInput
from lib.gui.element.text import Text
from lib.gui.layout.factory import LayoutFactory
from lib.gui.layout.type import LayoutType

from app.hooks import i18n
from app.network.neuron.adaptiveavgpool1d import AdaptiveAveragePooling1d
from app.network.neuron.adaptiveavgpool1d.dimension.params import AdaptiveAvgPool1dDimensionParams
from app.network.neuron.adaptiveavgpool1d.dimension.options import AdaptiveAvgPool1dDimensionOptions
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.neuron.strategy import NeuronStrategy


# Main

class SingleDimensionStrategy(NeuronStrategy):
    def __init__(self, dependencies):
        super().__init__(dependencies)

        self._output_size = FormInput(self.default_params["output_size"])

        self._input_height = LS.rem(1.6)

    @property
    def params(self):
        return NeuronStrategyParams(
            params=AdaptiveAvgPool1dDimensionParams(
                output_size=self._output_size.value
            ),
            options=AdaptiveAvgPool1dDimensionOptions()
        )

    @property
    def default_params(self):
        return AdaptiveAveragePooling1d.default_params()

    @property
    def default_options(self):
        return AdaptiveAveragePooling1d.default_options()

    def load(self, params, options):
        self._output_size.update(params["output_size"])

    def render(self, root):
        return (
            LayoutFactory(LayoutType.VERTICAL).create()
            .append(
                LayoutFactory(LayoutType.HORIZONTAL).create()
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .weight(2)
                    .add(
                        Text(root, i18n("window.screens.network.neurons.adaptiveavgpool1d.labels.output"))
                        .Align(Qt.AlignRight | Qt.AlignVCenter)
                    )
                )
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .weight(3)
                    .add(
                        IntegerInput(root, self._output_size.value)
                        .Bind(self._output_size)
                        .Height(self._input_height)
                    )
                )
            )
        )
