from lib import void
from lib.gui.element.font import Font
from lib.gui.element.form import FormInput
from lib.gui.layout import Layout

from app.network.neuron.adaptiveavgpool3d.dimension.params import AdaptiveAvgPool3dDimensionParams
from app.network.neuron.adaptiveavgpool3d.dimension.options import AdaptiveAvgPool3dDimensionOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams


# Main

class TripleDimensionStrategy(NeuronStrategy[AdaptiveAvgPool3dDimensionParams, AdaptiveAvgPool3dDimensionOptions]):
    class Dimension(int):
        DEPTH = ... #type: TripleDimensionStrategy.Dimension
        HEIGHT = ... #type: TripleDimensionStrategy.Dimension
        WIDTH = ... #type: TripleDimensionStrategy.Dimension

    _output_size_depth: FormInput[int]

    _output_size_height: FormInput[int]

    _output_size_width: FormInput[int]

    _input_height: int
    _font_caption_title: Font

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[AdaptiveAvgPool3dDimensionParams, AdaptiveAvgPool3dDimensionOptions]: ...

    @property
    def default_params(self) -> AdaptiveAvgPool3dDimensionParams: ...

    @property
    def default_options(self) -> AdaptiveAvgPool3dDimensionOptions: ...

    def load(self, params: AdaptiveAvgPool3dDimensionParams, options: AdaptiveAvgPool3dDimensionOptions) -> void: ...

    def render(self, root: MainWindow) -> Layout: ...
