from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSizePolicy

from lib.gui import LS
from lib.gui.element.form import FormInput
from lib.gui.element.form.check import CheckBox
from lib.gui.element.form.integer import IntegerInput
from lib.gui.element.component.switcher import Switcher
from lib.gui.element.text import Text
from lib.gui.layout.factory import LayoutFactory
from lib.gui.layout.type import LayoutType

from app.hooks import i18n
from app.network.neuron.convtranspose1d import TransposedConvolution1d
from app.network.neuron.convtranspose1d.params import ConvTranspose1dParams
from app.network.neuron.convtranspose1d.options import ConvTranspose1dOptions
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.neuron.convtranspose1d.view import Dimension1dSwitcher, Dimension1dView
from app.gui.neuron.convtranspose1d.dimension import SingleDimensionStrategy


# Main

class NeuronBuilderTransposedConvolution1dStrategy(NeuronStrategy):
    class Watch(str):
        DIMENSION_SWITCHER = "dimension_1d_switcher"

    def __init__(self, dependencies):
        super().__init__(dependencies)

        self._input_channels = FormInput(self.default_params["in_channels"])
        self._output_channels = FormInput(self.default_params["out_channels"])
        self._groups = FormInput(self.default_params["groups"])
        self._bias = FormInput(self.default_params["bias"])

        self._input_height = LS.rem(1.6)

    @property
    def params(self):
        return NeuronStrategyParams(
            params=ConvTranspose1dParams(
                in_channels=self._input_channels.value,
                out_channels=self._output_channels.value,
                **self.dimension_params.params,
                groups=self._groups.value,
                bias=self._bias.value
            ),
            options=ConvTranspose1dOptions()
        )

    @property
    def default_params(self):
        return TransposedConvolution1d.default_params()

    @property
    def default_options(self):
        return TransposedConvolution1d.default_options()

    def load(self, params, options):
        self._input_channels.update(params["in_channels"])
        self._output_channels.update(params["out_channels"])

        self._groups.update(params["groups"])
        self._bias.update(params["bias"])

    @property
    def dimension_params(self):
        return self.dimension_switcher_program.params

    @property
    def dimension_switcher_program(self):
        return self.get(NeuronBuilderTransposedConvolution1dStrategy.Watch.DIMENSION_SWITCHER).program

    def render(self, root):
        return (
            LayoutFactory(LayoutType.VERTICAL).create()
            .append(
                LayoutFactory(LayoutType.VERTICAL).create()
                .append(
                    LayoutFactory(LayoutType.HORIZONTAL).create()
                    .add(
                        Text(root, i18n("window.screens.network.neurons.convtranspose1d.labels.input"))
                    )
                    .append(
                        LayoutFactory(LayoutType.VERTICAL).create()
                        .add(
                            IntegerInput(root, self._input_channels.value)
                            .Bind(self._input_channels)
                            .Height(self._input_height)
                        )
                    )
                )
                .append(
                    LayoutFactory(LayoutType.HORIZONTAL).create()
                    .add(
                        Text(root, i18n("window.screens.network.neurons.convtranspose1d.labels.output"))
                    )
                    .append(
                        LayoutFactory(LayoutType.VERTICAL).create()
                        .add(
                            IntegerInput(root, self._output_channels.value)
                            .Bind(self._output_channels)
                            .Height(self._input_height)
                        )
                    )
                )
            )
            .add(
                self.watch(
                    NeuronBuilderTransposedConvolution1dStrategy.Watch.DIMENSION_SWITCHER,
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
            .append(
                LayoutFactory(LayoutType.HORIZONTAL).create()
                .add(
                    Text(root, i18n("window.screens.network.neurons.convtranspose1d.labels.groups"))
                )
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .add(
                        IntegerInput(root, self._groups.value)
                        .Bind(self._groups)
                        .Height(self._input_height)
                    )
                )
            )
            .append(
                LayoutFactory(LayoutType.HORIZONTAL).create()
                .margin_vertical(LS.rem(.8))
                .add(
                    Text(root, i18n("window.screens.network.neurons.convtranspose1d.labels.bias"))
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
