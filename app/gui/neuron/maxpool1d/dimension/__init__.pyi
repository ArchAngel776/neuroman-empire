from lib import void
from lib.gui.element.form import FormInput
from lib.gui.layout import Layout

from app.network.neuron.maxpool1d.dimension.params import MaxPool1dDimensionParams
from app.network.neuron.maxpool1d.dimension.options import MaxPool1dDimensionOptions
from app.gui import MainWindow
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.neuron.strategy import NeuronStrategy


# Main

class SingleDimensionStrategy(NeuronStrategy[MaxPool1dDimensionParams, MaxPool1dDimensionOptions]):
    _kernel_size: FormInput[int]
    _stride: FormInput[int]
    _padding: FormInput[int]
    _dilation: FormInput[int]

    _input_height: int

    def __init__(self) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[MaxPool1dDimensionParams, MaxPool1dDimensionOptions]: ...

    @property
    def default_params(self) -> MaxPool1dDimensionParams: ...

    @property
    def default_options(self) -> MaxPool1dDimensionOptions: ...

    def load(self, params: MaxPool1dDimensionParams, options: MaxPool1dDimensionOptions) -> void: ...

    def render(self, root: MainWindow) -> Layout: ...