from lib import void
from lib.gui.element.font import Font
from lib.gui.element.form import FormInput
from lib.gui.layout import Layout

from app.network.neuron.convtranspose3d.dimension.params import ConvTranspose3dDimensionParams
from app.network.neuron.convtranspose3d.dimension.options import ConvTranspose3dDimensionOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams


# Main

class TripleDimensionStrategy(NeuronStrategy[ConvTranspose3dDimensionParams, ConvTranspose3dDimensionOptions]):
    class Dimension(int):
        DEPTH = ... #type: TripleDimensionStrategy.Dimension
        HEIGHT = ... #type: TripleDimensionStrategy.Dimension
        WIDTH = ... #type: TripleDimensionStrategy.Dimension

    _kernel_size_depth: FormInput[int]
    _stride_depth: FormInput[int]
    _padding_depth: FormInput[int]
    _dilation_depth: FormInput[int]
    _output_padding_depth: FormInput[int]

    _kernel_size_height: FormInput[int]
    _stride_height: FormInput[int]
    _padding_height: FormInput[int]
    _dilation_height: FormInput[int]
    _output_padding_height: FormInput[int]

    _kernel_size_width: FormInput[int]
    _stride_width: FormInput[int]
    _padding_width: FormInput[int]
    _dilation_width: FormInput[int]
    _output_padding_width: FormInput[int]

    _input_height: int
    _font_caption_title: Font

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[ConvTranspose3dDimensionParams, ConvTranspose3dDimensionOptions]: ...

    @property
    def default_params(self) -> ConvTranspose3dDimensionParams: ...

    @property
    def default_options(self) -> ConvTranspose3dDimensionOptions: ...

    def load(self, params: ConvTranspose3dDimensionParams, options: ConvTranspose3dDimensionOptions) -> void: ...

    def render(self, root: MainWindow) -> Layout: ...
