from PyQt5.QtWidgets import QSizePolicy

from lib.gui.element.component.switcher import Switcher
from lib.gui.layout.factory import LayoutFactory
from lib.gui.layout.type import LayoutType

from app.network.neuron.adaptiveavgpool1d import AdaptiveAveragePooling1d
from app.network.neuron.adaptiveavgpool1d.params import AdaptiveAvgPool1dParams
from app.network.neuron.adaptiveavgpool1d.options import AdaptiveAvgPool1dOptions
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.neuron.adaptiveavgpool1d.view import Dimension1dSwitcher, Dimension1dView
from app.gui.neuron.adaptiveavgpool1d.dimension import SingleDimensionStrategy


# Main

class NeuronBuilderAdaptiveAveragePooling1dStrategy(NeuronStrategy):
    class Watch(str):
        DIMENSION_SWITCHER = "dimension_1d_switcher"

    @property
    def params(self):
        return NeuronStrategyParams(
            params=AdaptiveAvgPool1dParams(
                **self.dimension_params.params
            ),
            options=AdaptiveAvgPool1dOptions()
        )

    @property
    def default_params(self):
        return AdaptiveAveragePooling1d.default_params()

    @property
    def default_options(self):
        return AdaptiveAveragePooling1d.default_options()

    def load(self, params, options):
        return

    @property
    def dimension_params(self):
        return self.dimension_switcher_program.params

    @property
    def dimension_switcher_program(self):
        return self.get(NeuronBuilderAdaptiveAveragePooling1dStrategy.Watch.DIMENSION_SWITCHER).program

    def render(self, root):
        return (
            LayoutFactory(LayoutType.VERTICAL).create()
            .add(
                self.watch(
                    NeuronBuilderAdaptiveAveragePooling1dStrategy.Watch.DIMENSION_SWITCHER,
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
        )
