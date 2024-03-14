from lib import void
from lib.gui.layout import Layout

from app.network.neuron.adaptiveavgpool1d.params import AdaptiveAvgPool1dParams
from app.network.neuron.adaptiveavgpool1d.options import AdaptiveAvgPool1dOptions
from app.network.neuron.adaptiveavgpool1d.dimension.params import AdaptiveAvgPool1dDimensionParams
from app.network.neuron.adaptiveavgpool1d.dimension.options import AdaptiveAvgPool1dDimensionOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.params import NeuronStrategyParams

from .view import Dimension1dSwitcher, Dimension1dView


# Main

class NeuronBuilderAdaptiveAveragePooling1dStrategy(NeuronStrategy[AdaptiveAvgPool1dParams, AdaptiveAvgPool1dOptions]):
    class Watch(str):
        DIMENSION_SWITCHER = ... #type: NeuronBuilderAdaptiveAveragePooling1dStrategy.Watch

    @property
    def params(self) -> NeuronStrategyParams[AdaptiveAvgPool1dParams, AdaptiveAvgPool1dOptions]: ...

    @property
    def default_params(self) -> AdaptiveAvgPool1dParams: ...

    @property
    def default_options(self) -> AdaptiveAvgPool1dOptions: ...

    def load(self, params: AdaptiveAvgPool1dParams, options: AdaptiveAvgPool1dOptions) -> void: ...

    @property
    def dimension_params(self) -> NeuronStrategyParams[
        AdaptiveAvgPool1dDimensionParams, AdaptiveAvgPool1dDimensionOptions
    ]: ...

    @property
    def dimension_switcher_program(self) -> Dimension1dSwitcher: ...

    def render(self, root: MainWindow) -> Layout: ...
