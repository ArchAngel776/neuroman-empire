from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSizePolicy

from lib.gui import LS
from lib.gui.event import Event
from lib.gui.element.font import Font
from lib.gui.element.form import FormInput
from lib.gui.element.form.integer import IntegerInput
from lib.gui.element.form.radio import RadioButton
from lib.gui.element.text import Text
from lib.gui.element.component.switcher import Switcher
from lib.gui.layout.factory import LayoutFactory
from lib.gui.layout.type import LayoutType

from app.hooks import i18n
from app.network.neuron.fractionalmaxpool2d import FractionalMaxPooling2d
from app.network.neuron.fractionalmaxpool2d.dimension.params import FractionalMaxPool2dDimensionParams
from app.network.neuron.fractionalmaxpool2d.dimension.options import FractionalMaxPool2dDimensionOptions
from app.network.neuron.fractionalmaxpool2d.dimension.options.output import Output
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.neuron.fractionalmaxpool2d.dimension.output import OutputSwitcher


# Main

class DoubleDimensionStrategy(NeuronStrategy):
    class Watch(str):
        OUTPUT_SWITCHER = "double_dimension_strategy_output_switcher"

    class Dimension(int):
        HEIGHT = 0
        WIDTH = 1

    def __init__(self, dependencies):
        super().__init__(dependencies)

        self._kernel_size_height = FormInput(self.default_params["kernel_size"][self.Dimension.HEIGHT])

        self._kernel_size_width = FormInput(self.default_params["kernel_size"][self.Dimension.WIDTH])

        self._output = FormInput(self.default_options["output"])

        self._input_height = LS.rem(1.6)
        self._font_caption_title = Font().Size(LS.rem(.8)).Bold().Underline()

    @property
    def params(self):
        return NeuronStrategyParams(
            params=FractionalMaxPool2dDimensionParams(
                kernel_size=(
                    self._kernel_size_height.value,
                    self._kernel_size_width.value
                ),
                **self.output_params.params
            ),
            options=FractionalMaxPool2dDimensionOptions(
                output=self._output.value
            )
        )

    @property
    def default_params(self):
        return FractionalMaxPooling2d.default_params()

    @property
    def default_options(self):
        return FractionalMaxPooling2d.default_options()

    def load(self, params, options):
        self._kernel_size_height.update(params["kernel_size"][self.Dimension.HEIGHT])
        self._kernel_size_width.update(params["kernel_size"][self.Dimension.WIDTH])

        self._output.update(options["output"])

    @property
    def output_params(self):
        return self.output_switcher_program.params

    def toggle_output(self, event):
        key = event.value
        self.make(DoubleDimensionStrategy.Watch.OUTPUT_SWITCHER, lambda switcher: switcher.change_strategy(key))
        return True

    @property
    def output_switcher_program(self):
        return self.get(DoubleDimensionStrategy.Watch.OUTPUT_SWITCHER).program

    def render(self, root):
        return (
            LayoutFactory(LayoutType.VERTICAL).create()
            .append(
                LayoutFactory(LayoutType.HORIZONTAL).create()
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .weight(1)
                    .add(
                        Text(root, i18n("window.screens.network.neurons.fractionalmaxpool2d.dimensions.height"))
                        .Font(self._font_caption_title)
                        .Align(Qt.AlignCenter)
                        .Margin(LS.rem(0), LS.rem(.6))
                    )
                    .append(
                        LayoutFactory(LayoutType.VERTICAL).create()
                        .add(
                            Text(root, i18n("window.screens.network.neurons.fractionalmaxpool2d.labels.kernel"))
                        )
                        .add(
                            IntegerInput(root, self._kernel_size_height.value)
                            .Bind(self._kernel_size_height)
                            .Height(self._input_height)
                        )
                    )
                )
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .weight(1)
                    .add(
                        Text(root, i18n("window.screens.network.neurons.fractionalmaxpool2d.dimensions.width"))
                        .Font(self._font_caption_title)
                        .Align(Qt.AlignCenter)
                        .Margin(LS.rem(0), LS.rem(.6))
                    )
                    .append(
                        LayoutFactory(LayoutType.VERTICAL).create()
                        .add(
                            Text(root, i18n("window.screens.network.neurons.fractionalmaxpool2d.labels.kernel"))
                        )
                        .add(
                            IntegerInput(root, self._kernel_size_width.value)
                            .Bind(self._kernel_size_width)
                            .Height(self._input_height)
                        )
                    )
                )
            )
            .add(
                self.watch(
                    DoubleDimensionStrategy.Watch.OUTPUT_SWITCHER,
                    Switcher(root, OutputSwitcher(self._output.value, self.dependencies), LayoutType.HORIZONTAL)
                    .InnerSizing(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
                    .InnerMargin(LS.rem(0), LS.rem(0))
                    .Payload(self.neuron_payload_provider.provide())
                )
            )
            .append(
                LayoutFactory(LayoutType.HORIZONTAL).create()
                .align(Qt.AlignmentFlag.AlignCenter)
                .add(
                    RadioButton(root, LayoutType.HORIZONTAL, self._output.value)
                    .Sizing(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
                    .Bind(self._output)
                    .On(
                        Event.Type.Toggled, self.toggle_output,
                        with_target=False,
                        with_event=True
                    )
                    .Add(Output.SIZE, i18n("window.screens.network.neurons.fractionalmaxpool2d.labels.size"))
                    .Add(Output.RATIO, i18n("window.screens.network.neurons.fractionalmaxpool2d.labels.ratio"))
                )
            )
        )
