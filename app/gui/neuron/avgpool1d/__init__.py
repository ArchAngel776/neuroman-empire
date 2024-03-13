from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSizePolicy

from lib.gui import LS
from lib.gui.element.form import FormInput
from lib.gui.element.form.check import CheckBox
from lib.gui.element.component.switcher import Switcher
from lib.gui.element.text import Text
from lib.gui.layout.factory import LayoutFactory
from lib.gui.layout.type import LayoutType

from app.hooks import i18n
from app.network.neuron.avgpool1d import AveragePooling1d
from app.network.neuron.avgpool1d.params import AvgPool1dParams
from app.network.neuron.avgpool1d.options import AvgPool1dOptions
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.neuron.avgpool1d.view import Dimension1dSwitcher, Dimension1dView
from app.gui.neuron.avgpool1d.dimension import SingleDimensionStrategy


# Main

class NeuronBuilderAveragePooling1dStrategy(NeuronStrategy):
    class Watch(str):
        DIMENSION_SWITCHER = "dimension_1d_switcher"

    def __init__(self, dependencies):
        super().__init__(dependencies)

        self._ceil_mode = FormInput(self.default_params["ceil_mode"])
        self._count_include_pad = FormInput(self.default_params["count_include_pad"])

        self._input_height = LS.rem(1.6)

    @property
    def params(self):
        return NeuronStrategyParams(
            params=AvgPool1dParams(
                **self.dimension_params.params,
                ceil_mode=self._ceil_mode.value,
                count_include_pad=self._count_include_pad.value
            ),
            options=AvgPool1dOptions()
        )

    @property
    def default_params(self):
        return AveragePooling1d.default_params()

    @property
    def default_options(self):
        return AveragePooling1d.default_options()

    def load(self, params, options):
        self._ceil_mode.update(params["ceil_mode"])
        self._count_include_pad.update(params["count_include_pad"])

    @property
    def dimension_params(self):
        return self.dimension_switcher_program.params

    @property
    def dimension_switcher_program(self):
        return self.get(NeuronBuilderAveragePooling1dStrategy.Watch.DIMENSION_SWITCHER).program

    def render(self, root):
        return (
            LayoutFactory(LayoutType.VERTICAL).create()
            .add(
                self.watch(
                    NeuronBuilderAveragePooling1dStrategy.Watch.DIMENSION_SWITCHER,
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
                    Text(root, i18n("window.screens.network.neurons.avgpool1d.labels.ceil_mode"))
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
            .append(
                LayoutFactory(LayoutType.HORIZONTAL).create()
                .add(
                    Text(root, i18n("window.screens.network.neurons.avgpool1d.labels.count_include_pad"))
                )
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .add(
                        CheckBox(root, self._count_include_pad.value)
                        .Bind(self._count_include_pad)
                        .Height(self._input_height)
                    )
                )
            )
        )
