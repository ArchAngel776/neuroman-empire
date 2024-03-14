from PyQt5.QtWidgets import QSizePolicy

from lib.gui import LS
from lib.gui.element.form import FormInput
from lib.gui.element.form.check import CheckBox
from lib.gui.element.component.switcher import Switcher
from lib.gui.element.text import Text
from lib.gui.layout.factory import LayoutFactory
from lib.gui.layout.type import LayoutType

from app.hooks import i18n
from app.network.neuron.adaptivemaxpool1d import AdaptiveMaxPooling1d
from app.network.neuron.adaptivemaxpool1d.params import AdaptiveMaxPool1dParams
from app.network.neuron.adaptivemaxpool1d.options import AdaptiveMaxPool1dOptions
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.neuron.adaptivemaxpool1d.view import Dimension1dSwitcher, Dimension1dView
from app.gui.neuron.adaptivemaxpool1d.dimension import SingleDimensionStrategy


# Main

class NeuronBuilderAdaptiveMaxPooling1dStrategy(NeuronStrategy):
    class Watch(str):
        DIMENSION_SWITCHER = "dimension_1d_switcher"

    def __init__(self, dependencies):
        super().__init__(dependencies)

        self._return_indices = FormInput(self.default_params["return_indices"])

        self._input_height = LS.rem(1.6)

    @property
    def params(self):
        return NeuronStrategyParams(
            params=AdaptiveMaxPool1dParams(
                **self.dimension_params.params,
                return_indices=self._return_indices.value
            ),
            options=AdaptiveMaxPool1dOptions()
        )

    @property
    def default_params(self):
        return AdaptiveMaxPooling1d.default_params()

    @property
    def default_options(self):
        return AdaptiveMaxPooling1d.default_options()

    def load(self, params, options):
        self._return_indices.update(params["return_indices"])

    @property
    def dimension_params(self):
        return self.dimension_switcher_program.params

    @property
    def dimension_switcher_program(self):
        return self.get(NeuronBuilderAdaptiveMaxPooling1dStrategy.Watch.DIMENSION_SWITCHER).program

    def render(self, root):
        return (
            LayoutFactory(LayoutType.VERTICAL).create()
            .add(
                self.watch(
                    NeuronBuilderAdaptiveMaxPooling1dStrategy.Watch.DIMENSION_SWITCHER,
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
                    Text(root, i18n("window.screens.network.neurons.adaptivemaxpool1d.labels.return_indices"))
                )
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .add(
                        CheckBox(root, self._return_indices.value)
                        .Bind(self._return_indices)
                        .Height(self._input_height)
                    )
                )
            )
        )
