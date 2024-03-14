from lib import void
from lib.gui.element.form import FormInput
from lib.gui.layout import Layout

from app.network.neuron.adaptivemaxpool1d.dimension.params import AdaptiveMaxPool1dDimensionParams
from app.network.neuron.adaptivemaxpool1d.dimension.options import AdaptiveMaxPool1dDimensionOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams


# Main

class SingleDimensionStrategy(NeuronStrategy[AdaptiveMaxPool1dDimensionParams, AdaptiveMaxPool1dDimensionOptions]):
    _output_size: FormInput[int]

    _input_height: int

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[AdaptiveMaxPool1dDimensionParams, AdaptiveMaxPool1dDimensionOptions]: ...

    @property
    def default_params(self) -> AdaptiveMaxPool1dDimensionParams: ...

    @property
    def default_options(self) -> AdaptiveMaxPool1dDimensionOptions: ...

    def load(self, params: AdaptiveMaxPool1dDimensionParams, options: AdaptiveMaxPool1dDimensionOptions) -> void: ...

    def render(self, root: MainWindow) -> Layout: ...