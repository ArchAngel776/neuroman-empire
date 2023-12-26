from PyQt5.QtCore import Qt

from lib.gui import LS
from lib.gui.element.form import FormInput
from lib.gui.element.form.integer import IntegerInput
from lib.gui.element.text import Text
from lib.gui.layout.factory import LayoutFactory
from lib.gui.layout.type import LayoutType

from app.hooks import i18n
from app.network.neuron.convtranspose1d import TransposedConvolution1d
from app.network.neuron.convtranspose1d.dimension.params import ConvTranspose1dDimensionParams
from app.network.neuron.convtranspose1d.dimension.options import ConvTranspose1dDimensionOptions
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
        self._output_padding = FormInput(self.default_params["output_padding"])

        self._input_height = LS.rem(1.6)

    @property
    def params(self):
        return NeuronStrategyParams(
            params=ConvTranspose1dDimensionParams(
                kernel_size=self._kernel_size.value,
                stride=self._stride.value,
                padding=self._padding.value,
                dilation=self._dilation.value,
                output_padding=self._output_padding.value
            ),
            options=ConvTranspose1dDimensionOptions()
        )

    @property
    def default_params(self):
        return TransposedConvolution1d.default_params()

    @property
    def default_options(self):
        return TransposedConvolution1d.default_options()

    def load(self, params, options):
        self._kernel_size.update(params["kernel_size"])
        self._stride.update(params["stride"])
        self._padding.update(params["padding"])
        self._dilation.update(params["dilation"])
        self._output_padding.update(params["output_padding"])

    def render(self, root):
        return (
            LayoutFactory(LayoutType.VERTICAL).create()
            .append(
                LayoutFactory(LayoutType.HORIZONTAL).create()
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .weight(2)
                    .add(
                        Text(root, i18n("window.screens.network.neurons.convtranspose1d.labels.kernel"))
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
                        Text(root, i18n("window.screens.network.neurons.convtranspose1d.labels.stride"))
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
                        Text(root, i18n("window.screens.network.neurons.convtranspose1d.labels.padding"))
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
                        Text(root, i18n("window.screens.network.neurons.convtranspose1d.labels.dilation"))
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
            .append(
                LayoutFactory(LayoutType.HORIZONTAL).create()
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .weight(2)
                    .add(
                        Text(root, i18n("window.screens.network.neurons.convtranspose1d.labels.output_padding"))
                        .Align(Qt.AlignRight | Qt.AlignVCenter)
                    )
                )
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .weight(3)
                    .add(
                        IntegerInput(root, self._output_padding.value)
                        .Bind(self._output_padding)
                        .Height(self._input_height)
                    )
                )
            )
        )
