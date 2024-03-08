from lib import void
from lib.gui.element.form import FormInput
from lib.gui.layout import Layout

from app.network.neuron.avgpool1d.dimension.params import AvgPool1dDimensionParams
from app.network.neuron.avgpool1d.dimension.options import AvgPool1dDimensionOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams


# Main

class SingleDimensionStrategy(NeuronStrategy[AvgPool1dDimensionParams, AvgPool1dDimensionOptions]):
    _kernel_size: FormInput[int]
    _stride: FormInput[int]
    _padding: FormInput[int]

    _input_height: int

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[AvgPool1dDimensionParams, AvgPool1dDimensionOptions]: ...

    @property
    def default_params(self) -> AvgPool1dDimensionParams: ...

    @property
    def default_options(self) -> AvgPool1dDimensionOptions: ...

    def load(self, params: AvgPool1dDimensionParams, options: AvgPool1dDimensionOptions) -> void: ...

    def render(self, root: MainWindow) -> Layout: ...