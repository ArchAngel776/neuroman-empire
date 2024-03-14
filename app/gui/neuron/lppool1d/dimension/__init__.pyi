from lib import void
from lib.gui.element.form import FormInput
from lib.gui.layout import Layout

from app.network.neuron.lppool1d.dimension.params import LPPool1dDimensionParams
from app.network.neuron.lppool1d.dimension.options import LPPool1dDimensionOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams


# Main

class SingleDimensionStrategy(NeuronStrategy[LPPool1dDimensionParams, LPPool1dDimensionOptions]):
    _kernel_size: FormInput[int]
    _stride: FormInput[int]

    _input_height: int

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[LPPool1dDimensionParams, LPPool1dDimensionOptions]: ...

    @property
    def default_params(self) -> LPPool1dDimensionParams: ...

    @property
    def default_options(self) -> LPPool1dDimensionOptions: ...

    def load(self, params: LPPool1dDimensionParams, options: LPPool1dDimensionOptions) -> void: ...

    def render(self, root: MainWindow) -> Layout: ...