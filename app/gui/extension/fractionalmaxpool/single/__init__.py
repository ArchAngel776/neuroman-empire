from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSizePolicy

from lib.gui import LS
from lib.gui.event import Event
from lib.gui.element.form import FormInput
from lib.gui.element.form.integer import IntegerInput
from lib.gui.element.form.radio import RadioButton
from lib.gui.element.text import Text
from lib.gui.element.component.switcher import Switcher
from lib.gui.layout.factory import LayoutFactory
from lib.gui.layout.type import LayoutType

from app.hooks import i18n
from app.network.extension.fractionalmaxpool.single import FractionalMaxPoolingSingleExtension
from app.network.extension.fractionalmaxpool.single.params import FractionalMaxPoolSingleDimensionParams
from app.network.extension.fractionalmaxpool.single.options import FractionalMaxPoolSingleDimensionOptions
from app.network.extension.fractionalmaxpool.single.options.output import Output
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.extension.fractionalmaxpool.single.output import OutputSwitcher


# Main

class SingleDimensionStrategy(NeuronStrategy):
    class Watch(str):
        OUTPUT_SWITCHER = "single_dimension_strategy_output_switcher"

    def __init__(self, dependencies):
        super().__init__(dependencies)

        self._kernel_size = FormInput(self.default_params["kernel_size"])

        self._output = FormInput(self.default_options["output"])

        self._input_height = LS.rem(1.6)

    @property
    def params(self):
        return NeuronStrategyParams(
            params=FractionalMaxPoolSingleDimensionParams(
                kernel_size=self._kernel_size.value,
                **self.output_params.params
            ),
            options=FractionalMaxPoolSingleDimensionOptions(
                output=self._output.value
            )
        )

    @property
    def default_params(self):
        return FractionalMaxPoolingSingleExtension.default_params()

    @property
    def default_options(self):
        return FractionalMaxPoolingSingleExtension.default_options()

    def load(self, params, options):
        self._kernel_size.update(params["kernel_size"])

        self._output.update(options["output"])

    @property
    def output_params(self):
        return self.output_switcher_program.params

    def toggle_output(self, event):
        self.make(SingleDimensionStrategy.Watch.OUTPUT_SWITCHER, lambda switcher: switcher.change_strategy(event.value))
        return True

    @property
    def output_switcher_program(self):
        return self.get(SingleDimensionStrategy.Watch.OUTPUT_SWITCHER).program

    def render(self, root):
        return (
            LayoutFactory(LayoutType.VERTICAL).create()
            .append(
                LayoutFactory(LayoutType.VERTICAL).create()
                .weight(1)
                .append(
                    LayoutFactory(LayoutType.HORIZONTAL).create()
                    .add(
                        Text(root, i18n("window.screens.network.extension.fractionalmaxpool.single.labels.kernel"))
                    )
                    .add(
                        IntegerInput(root, self._kernel_size.value)
                        .Bind(self._kernel_size)
                        .Height(self._input_height)
                    )
                )
            )
            .add(
                self.watch(
                    SingleDimensionStrategy.Watch.OUTPUT_SWITCHER,
                    Switcher(root, OutputSwitcher(self._output.value, self.dependencies), LayoutType.HORIZONTAL)
                    .InnerSizing(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
                    .InnerMargin(LS.rem(0), LS.rem(0))
                    .Payload(self.neuron_payload_provider.provide())
                )
            )
            .add(
                RadioButton(root, LayoutType.HORIZONTAL, self._output.value)
                .Sizing(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
                .Bind(self._output)
                .On(
                    Event.Type.Toggled, self.toggle_output,
                    with_target=False,
                    with_event=True
                )
                .Add(Output.SIZE, i18n("window.screens.network.extension.fractionalmaxpool.single.labels.size"))
                .Add(Output.RATIO, i18n("window.screens.network.extension.fractionalmaxpool.single.labels.ratio"))
            )
        )
