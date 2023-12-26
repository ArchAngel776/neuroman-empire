from PyQt5.QtCore import Qt

from lib.gui import LS
from lib.gui.element.form import FormInput
from lib.gui.element.form.integer import IntegerInput
from lib.gui.element.text import Text
from lib.gui.layout.factory import LayoutFactory
from lib.gui.layout.type import LayoutType

from app.hooks import i18n
from app.network.neuron.maxpool1d import MaxPooling1d
from app.network.neuron.maxpool1d.dimension.params import MaxPool1dDimensionParams
from app.network.neuron.maxpool1d.dimension.options import MaxPool1dDimensionOptions
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.neuron.strategy import NeuronStrategy


# Main

class SingleDimensionStrategy(NeuronStrategy):
    def __init__(self, dependencies):
        super().__init__(dependencies)

        self._kernel_size = FormInput(self.default_params["kernel_size"])
        self._stride = FormInput(self.default_params["stride"])
        self._padding = FormInput(self.default_params["padding"])
        self._dilation = FormInput(self.default_params["dilation"])

        self._input_height = LS.rem(1.6)

    @property
    def params(self):
        return NeuronStrategyParams(
            params=MaxPool1dDimensionParams(
                kernel_size=self._kernel_size.value,
                stride=self._stride.value,
                padding=self._padding.value,
                dilation=self._dilation.value
            ),
            options=MaxPool1dDimensionOptions()
        )

    @property
    def default_params(self):
        return MaxPooling1d.default_params()

    @property
    def default_options(self):
        return MaxPooling1d.default_options()

    def load(self, params, options):
        self._kernel_size.update(params["kernel_size"])
        self._stride.update(params["stride"])
        self._padding.update(params["padding"])
        self._dilation.update(params["dilation"])

    def render(self, root):
        return (
            LayoutFactory(LayoutType.VERTICAL).create()
            .append(
                LayoutFactory(LayoutType.HORIZONTAL).create()
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .weight(2)
                    .add(
                        Text(root, i18n("window.screens.network.neurons.maxpool1d.labels.kernel"))
                        .Align(Qt.AlignRight | Qt.AlignVCenter)
                    )
                )
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .weight(3)
                    .add(
                        IntegerInput(root, self._kernel_size.value)
                        .Bind(self._kernel_size)
                        .Height(self._input_height)
                    )
                )
            )
            .append(
                LayoutFactory(LayoutType.HORIZONTAL).create()
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .weight(2)
                    .add(
                        Text(root, i18n("window.screens.network.neurons.maxpool1d.labels.stride"))
                        .Align(Qt.AlignRight | Qt.AlignVCenter)
                    )
                )
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .weight(3)
                    .add(
                        IntegerInput(root, self._stride.value)
                        .Bind(self._stride)
                        .Height(self._input_height)
                    )
                )
            )
            .append(
                LayoutFactory(LayoutType.HORIZONTAL).create()
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .weight(2)
                    .add(
                        Text(root, i18n("window.screens.network.neurons.maxpool1d.labels.padding"))
                        .Align(Qt.AlignRight | Qt.AlignVCenter)
                    )
                )
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .weight(3)
                    .add(
                        IntegerInput(root, self._padding.value)
                        .Bind(self._padding)
                        .Height(self._input_height)
                    )
                )
            )
            .append(
                LayoutFactory(LayoutType.HORIZONTAL).create()
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .weight(2)
                    .add(
                        Text(root, i18n("window.screens.network.neurons.maxpool1d.labels.dilation"))
                        .Align(Qt.AlignRight | Qt.AlignVCenter)
                    )
                )
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .weight(3)
                    .add(
                        IntegerInput(root, self._dilation.value)
                        .Bind(self._dilation)
                        .Height(self._input_height)
                    )
                )
            )
        )
