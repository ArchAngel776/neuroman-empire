from lib import void
from lib.gui.element.font import Font
from lib.gui.element.form import FormInput
from lib.gui.layout import Layout

from app.network.neuron.convtranspose2d.dimension.params import ConvTranspose2dDimensionParams
from app.network.neuron.convtranspose2d.dimension.options import ConvTranspose2dDimensionOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.params import NeuronStrategyParams


# Main

class DoubleDimensionStrategy(NeuronStrategy[ConvTranspose2dDimensionParams, ConvTranspose2dDimensionOptions]):
    class Dimension(int):
        HEIGHT = ... #type: DoubleDimensionStrategy.Dimension
        WIDTH = ... #type: DoubleDimensionStrategy.Dimension

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

    def __init__(self) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[ConvTranspose2dDimensionParams, ConvTranspose2dDimensionOptions]: ...

    @property
    def default_params(self) -> ConvTranspose2dDimensionParams: ...

    @property
    def default_options(self) -> ConvTranspose2dDimensionOptions: ...

    def load(self, params: ConvTranspose2dDimensionParams, options: ConvTranspose2dDimensionOptions) -> void: ...

    def render(self, root: MainWindow) -> Layout: ...
