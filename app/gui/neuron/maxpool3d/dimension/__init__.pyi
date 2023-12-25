from lib import void
from lib.gui.element.font import Font
from lib.gui.element.form import FormInput
from lib.gui.layout import Layout

from app.network.neuron.maxpool3d.dimension.params import MaxPool3dDimensionParams
from app.network.neuron.maxpool3d.dimension.options import MaxPool3dDimensionOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.params import NeuronStrategyParams


# Main

class TripleDimensionStrategy(NeuronStrategy[MaxPool3dDimensionParams, MaxPool3dDimensionOptions]):
    class Dimension(int):
        DEPTH = ... #type: TripleDimensionStrategy.Dimension
        HEIGHT = ... #type: TripleDimensionStrategy.Dimension
        WIDTH = ... #type: TripleDimensionStrategy.Dimension

    _kernel_size_depth: FormInput[int]
    _stride_depth: FormInput[int]
    _padding_depth: FormInput[int]
    _dilation_depth: FormInput[int]

    _kernel_size_height: FormInput[int]
    _stride_height: FormInput[int]
    _padding_height: FormInput[int]
    _dilation_height: FormInput[int]

    _kernel_size_width: FormInput[int]
    _stride_width: FormInput[int]
    _padding_width: FormInput[int]
    _dilation_width: FormInput[int]

    _input_height: int
    _font_caption_title: Font

    def __init__(self) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[MaxPool3dDimensionParams, MaxPool3dDimensionOptions]: ...

    @property
    def default_params(self) -> MaxPool3dDimensionParams: ...

    @property
    def default_options(self) -> MaxPool3dDimensionOptions: ...

    def load(self, params: MaxPool3dDimensionParams, options: MaxPool3dDimensionOptions) -> void: ...

    def render(self, root: MainWindow) -> Layout: ...
