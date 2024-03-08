from lib import void
from lib.gui.element.font import Font
from lib.gui.element.form import FormInput
from lib.gui.layout import Layout

from app.network.neuron.avgpool3d.dimension.params import AvgPool3dDimensionParams
from app.network.neuron.avgpool3d.dimension.options import AvgPool3dDimensionOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams


# Main

class TripleDimensionStrategy(NeuronStrategy[AvgPool3dDimensionParams, AvgPool3dDimensionOptions]):
    class Dimension(int):
        DEPTH = ... #type: TripleDimensionStrategy.Dimension
        HEIGHT = ... #type: TripleDimensionStrategy.Dimension
        WIDTH = ... #type: TripleDimensionStrategy.Dimension

    _kernel_size_depth: FormInput[int]
    _stride_depth: FormInput[int]
    _padding_depth: FormInput[int]

    _kernel_size_height: FormInput[int]
    _stride_height: FormInput[int]
    _padding_height: FormInput[int]

    _kernel_size_width: FormInput[int]
    _stride_width: FormInput[int]
    _padding_width: FormInput[int]

    _input_height: int
    _font_caption_title: Font

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[AvgPool3dDimensionParams, AvgPool3dDimensionOptions]: ...

    @property
    def default_params(self) -> AvgPool3dDimensionParams: ...

    @property
    def default_options(self) -> AvgPool3dDimensionOptions: ...

    def load(self, params: AvgPool3dDimensionParams, options: AvgPool3dDimensionOptions) -> void: ...

    def render(self, root: MainWindow) -> Layout: ...
