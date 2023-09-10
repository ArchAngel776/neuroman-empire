from PyQt5.QtCore import Qt

from lib.gui import LS
from lib.gui.element.form import FormInput
from lib.gui.element.form.check import CheckBox
from lib.gui.element.form.integer import IntegerInput
from lib.gui.element.text import Text
from lib.gui.layout.type import LayoutType
from lib.gui.layout.factory import LayoutFactory

from app.hooks import i18n
from app.network.neuron.linear import Linear
from app.network.neuron.linear.params import LinearParams
from app.network.neuron.linear.options import LinearOptions
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.params import NeuronStrategyParams


# Main

class NeuronBuilderLinearStrategy(NeuronStrategy):
    def __init__(self, dependencies):
        super().__init__(dependencies)

        self._input_features = FormInput(self.default_params["in_features"])
        self._output_features = FormInput(self.default_params["out_features"])
        self._bias = FormInput(self.default_params["bias"])

        self._input_height = LS.rem(1.6)

    @property
    def params(self):
        return NeuronStrategyParams(
            params=LinearParams(
                in_features=self._input_features.value,
                out_features=self._output_features.value,
                bias=self._bias.value
            ),
            options=LinearOptions()
        )

    @property
    def default_params(self):
        return Linear.default_params()

    @property
    def default_options(self):
        return Linear.default_options()

    @property
    def init_param(self):
        return self.dependencies["init_param"]

    @property
    def init_option(self):
        return self.dependencies["init_option"]

    def render(self, root):
        return (
            LayoutFactory(LayoutType.VERTICAL).create()
            .append(
                LayoutFactory(LayoutType.HORIZONTAL).create()
                .add(
                    Text(root, i18n("window.screens.network.neurons.linear.labels.input"))
                )
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .add(
                        IntegerInput(root, self._input_features.value)
                        .Bind(self._input_features)
                        .Height(self._input_height)
                    )
                )
            )
            .append(
                LayoutFactory(LayoutType.HORIZONTAL).create()
                .add(
                    Text(root, i18n("window.screens.network.neurons.linear.labels.output"))
                )
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .add(
                        IntegerInput(root, self._output_features.value)
                        .Bind(self._output_features)
                        .Height(self._input_height)
                    )
                )
            )
            .append(
                LayoutFactory(LayoutType.HORIZONTAL).create()
                .margin_vertical(LS.rem(.8))
                .add(
                    Text(root, i18n("window.screens.network.neurons.linear.labels.bias"))
                )
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .align(Qt.AlignLeft)
                    .margin_horizontal(LS.rem(.2))
                    .add(
                        CheckBox(root, self._bias.value)
                        .Bind(self._bias)
                    )
                )
            )
        )
