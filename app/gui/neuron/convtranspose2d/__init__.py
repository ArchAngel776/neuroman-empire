from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSizePolicy

from app import SCROLLBAR_SIZE
from lib.gui import LS
from lib.gui.element.form import FormInput
from lib.gui.element.form.check import CheckBox
from lib.gui.element.form.integer import IntegerInput
from lib.gui.element.scrollable import Scrollable
from lib.gui.element.component.switcher import Switcher
from lib.gui.element.text import Text
from lib.gui.event import Event
from lib.gui.layout.type import LayoutType
from lib.gui.layout.factory import LayoutFactory

from app.hooks import i18n
from app.network.neuron.convtranspose2d import TransposedConvolution2d
from app.network.neuron.convtranspose2d.params import ConvTranspose2dParams
from app.network.neuron.convtranspose2d.options import ConvTranspose2dOptions
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.neuron.convtranspose2d.view import Dimension2dView, Dimension2dSwitcher


# Main

class NeuronBuilderTransposedConvolution2dStrategy(NeuronStrategy):
    DIMENSION_SWITCHER = "dimension_2d_switcher"

    def __init__(self, dependencies):
        super().__init__(dependencies)

        self._input_channels = FormInput(self.default_params["in_channels"])
        self._output_channels = FormInput(self.default_params["out_channels"])
        self._groups = FormInput(self.default_params["groups"])
        self._bias = FormInput(self.default_params["bias"])

        self._reflection = FormInput(self.default_options["square"])
        self._input_height = LS.rem(1.6)

    @property
    def params(self):
        return NeuronStrategyParams(
            params=ConvTranspose2dParams(
                in_channels=self._input_channels.value,
                out_channels=self._output_channels.value,
                **self.dimension_params.params,
                groups=self._groups.value,
                bias=self._bias.value,
            ),
            options=ConvTranspose2dOptions(
                square=self._reflection.value
            )
        )

    @property
    def default_params(self):
        return TransposedConvolution2d.default_params()

    @property
    def default_options(self):
        return TransposedConvolution2d.default_options()

    def load(self, params, options):
        self._input_channels.update(params["in_channels"])
        self._output_channels.update(params["out_channels"])

        self._reflection.update(options["square"])
        self.dimension_switcher_program.current_strategy.load(params, options)

        self._groups.update(params["groups"])
        self._bias.update(params["bias"])

    @property
    def dimension_params(self):
        return self.dimension_switcher_program.params

    def change_dimension(self, event):
        key = Dimension2dView.SINGLE if event.checked else Dimension2dView.DOUBLE
        self.update(
            NeuronBuilderTransposedConvolution2dStrategy.DIMENSION_SWITCHER,
            lambda switcher: switcher.change_strategy(key)
        )
        return True

    @property
    def dimension_switcher_program(self):
        return self.get(NeuronBuilderTransposedConvolution2dStrategy.DIMENSION_SWITCHER).program

    def render(self, root):
        return (
            LayoutFactory(LayoutType.VERTICAL).create()
            .append(
                LayoutFactory(LayoutType.VERTICAL).create()
                .append(
                    LayoutFactory(LayoutType.HORIZONTAL).create()
                    .add(
                        Text(root, i18n("window.screens.network.neurons.convtranspose2d.labels.input"))
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
                        Text(root, i18n("window.screens.network.neurons.convtranspose2d.labels.output"))
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
            .append(
                LayoutFactory(LayoutType.HORIZONTAL).create()
                .margin_vertical(LS.rem(.8))
                .add(
                    Text(root, i18n("window.screens.network.neurons.convtranspose2d.labels.square"))
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
                        NeuronBuilderTransposedConvolution2dStrategy.DIMENSION_SWITCHER,
                        Switcher(
                            root,
                            Dimension2dSwitcher(Dimension2dView.DOUBLE, self.dependencies),
                            LayoutType.VERTICAL
                        )
                        .InnerSizing(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
                    )
                )
            )
            .append(
                LayoutFactory(LayoutType.HORIZONTAL).create()
                .add(
                    Text(root, i18n("window.screens.network.neurons.convtranspose2d.labels.groups"))
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
                    Text(root, i18n("window.screens.network.neurons.convtranspose2d.labels.bias"))
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
