from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSizePolicy

from lib.gui import LS
from lib.gui.element.form import FormInput
from lib.gui.element.form.check import CheckBox
from lib.gui.element.component.switcher import Switcher
from lib.gui.element.form.integer import IntegerInput
from lib.gui.element.text import Text
from lib.gui.layout.factory import LayoutFactory
from lib.gui.layout.type import LayoutType

from app.hooks import i18n
from app.network.neuron.lppool1d import LocalPooling1d
from app.network.neuron.lppool1d.params import LPPool1dParams
from app.network.neuron.lppool1d.options import LPPool1dOptions
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.neuron.lppool1d.view import Dimension1dSwitcher, Dimension1dView
from app.gui.neuron.lppool1d.dimension import SingleDimensionStrategy


# Main

class NeuronBuilderLocalPooling1dStrategy(NeuronStrategy):
    class Watch(str):
        DIMENSION_SWITCHER = "dimension_1d_switcher"

    def __init__(self, dependencies):
        super().__init__(dependencies)

        self._power = FormInput(self.default_params["power"])
        self._ceil_mode = FormInput(self.default_params["ceil_mode"])

        self._input_height = LS.rem(1.6)

    @property
    def params(self):
        return NeuronStrategyParams(
            params=LPPool1dParams(
                power=self._power.value,
                **self.dimension_params.params,
                ceil_mode=self._ceil_mode.value
            ),
            options=LPPool1dOptions()
        )

    @property
    def default_params(self):
        return LocalPooling1d.default_params()

    @property
    def default_options(self):
        return LocalPooling1d.default_options()

    def load(self, params, options):
        self._power.update(params["power"])
        self._ceil_mode.update(params["ceil_mode"])

    @property
    def dimension_params(self):
        return self.dimension_switcher_program.params

    @property
    def dimension_switcher_program(self):
        return self.get(NeuronBuilderLocalPooling1dStrategy.Watch.DIMENSION_SWITCHER).program

    def render(self, root):
        return (
            LayoutFactory(LayoutType.VERTICAL).create()
            .append(
                LayoutFactory(LayoutType.HORIZONTAL).create()
                .margin_vertical(LS.rem(.8))
                .add(
                    Text(root, i18n("window.screens.network.neurons.lppool1d.labels.power"))
                )
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .align(Qt.AlignLeft)
                    .margin_horizontal(LS.rem(.2))
                    .add(
                        IntegerInput(root, self._power.value)
                        .Bind(self._power)
                        .Height(self._input_height)
                    )
                )
            )
            .add(
                self.watch(
                    NeuronBuilderLocalPooling1dStrategy.Watch.DIMENSION_SWITCHER,
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
                .margin_vertical(LS.rem(.8))
                .add(
                    Text(root, i18n("window.screens.network.neurons.lppool1d.labels.ceil_mode"))
                )
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .align(Qt.AlignLeft)
                    .margin_horizontal(LS.rem(.2))
                    .add(
                        CheckBox(root, self._ceil_mode.value)
                        .Bind(self._ceil_mode)
                    )
                )
            )
        )
