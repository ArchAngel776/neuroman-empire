from lib import void
from lib.gui.element.form import FormInput
from lib.gui.layout import Layout

from app.network.neuron.convtranspose1d.dimension.params import ConvTranspose1dDimensionParams
from app.network.neuron.convtranspose1d.dimension.options import ConvTranspose1dDimensionOptions
from app.gui import MainWindow
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.neuron.strategy import NeuronStrategy


# Main

class SingleDimensionStrategy(NeuronStrategy[ConvTranspose1dDimensionParams, ConvTranspose1dDimensionOptions]):
    _kernel_size: FormInput[int]
    _stride: FormInput[int]
    _padding: FormInput[int]
    _dilation: FormInput[int]
    _output_padding: FormInput[int]

    _input_height: int

    def __init__(self) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[ConvTranspose1dDimensionParams, ConvTranspose1dDimensionOptions]: ...

    @property
    def default_params(self) -> ConvTranspose1dDimensionParams: ...

    @property
    def default_options(self) -> ConvTranspose1dDimensionOptions: ...

    def load(self, params: ConvTranspose1dDimensionParams, options: ConvTranspose1dDimensionOptions) -> void: ...

    def render(self, root: MainWindow) -> Layout: ...