from lib import void
from lib.gui.element.form import FormInput
from lib.gui.layout import Layout

from app.network.neuron.adaptiveavgpool1d.dimension.params import AdaptiveAvgPool1dDimensionParams
from app.network.neuron.adaptiveavgpool1d.dimension.options import AdaptiveAvgPool1dDimensionOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams


# Main

class SingleDimensionStrategy(NeuronStrategy[AdaptiveAvgPool1dDimensionParams, AdaptiveAvgPool1dDimensionOptions]):
    _output_size: FormInput[int]

    _input_height: int

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[AdaptiveAvgPool1dDimensionParams, AdaptiveAvgPool1dDimensionOptions]: ...

    @property
    def default_params(self) -> AdaptiveAvgPool1dDimensionParams: ...

    @property
    def default_options(self) -> AdaptiveAvgPool1dDimensionOptions: ...

    def load(self, params: AdaptiveAvgPool1dDimensionParams, options: AdaptiveAvgPool1dDimensionOptions) -> void: ...

    def render(self, root: MainWindow) -> Layout: ...