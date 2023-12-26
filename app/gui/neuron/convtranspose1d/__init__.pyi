from lib import void
from lib.gui.element.form import FormInput
from lib.gui.layout import Layout

from app.network.neuron.convtranspose1d.params import ConvTranspose1dParams
from app.network.neuron.convtranspose1d.options import ConvTranspose1dOptions
from app.network.neuron.convtranspose1d.dimension.params import ConvTranspose1dDimensionParams
from app.network.neuron.convtranspose1d.dimension.options import ConvTranspose1dDimensionOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams

from .view import Dimension1dSwitcher, Dimension1dView


# Main

class NeuronBuilderTransposedConvolution1dStrategy(NeuronStrategy[ConvTranspose1dParams, ConvTranspose1dOptions]):
    DIMENSION_SWITCHER = ... #type: str

    _input_channels: FormInput[int]
    _output_channels: FormInput[int]
    _groups: FormInput[int]
    _bias: FormInput[bool]

    _input_height: int

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[ConvTranspose1dParams, ConvTranspose1dOptions]: ...

    @property
    def default_params(self) -> ConvTranspose1dParams: ...

    @property
    def default_options(self) -> ConvTranspose1dOptions: ...

    def load(self, params: ConvTranspose1dParams, options: ConvTranspose1dOptions) -> void: ...

    @property
    def dimension_params(self) -> NeuronStrategyParams[ConvTranspose1dDimensionParams, ConvTranspose1dDimensionOptions]: ...

    @property
    def dimension_switcher_program(self) -> Dimension1dSwitcher: ...

    def render(self, root: MainWindow) -> Layout: ...
