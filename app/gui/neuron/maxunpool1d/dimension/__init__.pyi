from lib import void
from lib.gui.element.form import FormInput
from lib.gui.layout import Layout

from app.network.neuron.maxunpool1d.dimension.params import MaxUnpool1dDimensionParams
from app.network.neuron.maxunpool1d.dimension.options import MaxUnpool1dDimensionOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams


# Main

class SingleDimensionStrategy(NeuronStrategy[MaxUnpool1dDimensionParams, MaxUnpool1dDimensionOptions]):
    _kernel_size: FormInput[int]
    _stride: FormInput[int]
    _padding: FormInput[int]

    _input_height: int

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[MaxUnpool1dDimensionParams, MaxUnpool1dDimensionOptions]: ...

    @property
    def default_params(self) -> MaxUnpool1dDimensionParams: ...

    @property
    def default_options(self) -> MaxUnpool1dDimensionOptions: ...

    def load(self, params: MaxUnpool1dDimensionParams, options: MaxUnpool1dDimensionOptions) -> void: ...

    def render(self, root: MainWindow) -> Layout: ...
