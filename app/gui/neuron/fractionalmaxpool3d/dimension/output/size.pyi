from lib import void
from lib.gui.element.font import Font
from lib.gui.element.form import FormInput
from lib.gui.layout import Layout
from lib.gui.window import Window

from app.network.neuron.fractionalmaxpool3d.dimension.params.output.size import \
    FractionalMaxPool3dDimensionOutputSizeParams
from app.network.neuron.fractionalmaxpool3d.dimension.options.output.size import \
    FractionalMaxPool3dDimensionOutputSizeOptions
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies


# Main

class OutputSizeStrategy(
    NeuronStrategy[FractionalMaxPool3dDimensionOutputSizeParams, FractionalMaxPool3dDimensionOutputSizeOptions]
):
    class Dimension(int):
        DEPTH = ... #type: OutputSizeStrategy.Dimension
        HEIGHT = ... #type: OutputSizeStrategy.Dimension
        WIDTH = ... #type: OutputSizeStrategy.Dimension

    _output_size_depth: FormInput[int]

    _output_size_height: FormInput[int]

    _output_size_width: FormInput[int]

    _input_height: int
    _font_caption_title: Font

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[
        FractionalMaxPool3dDimensionOutputSizeParams,
        FractionalMaxPool3dDimensionOutputSizeOptions
    ]: ...

    @property
    def default_params(self) -> FractionalMaxPool3dDimensionOutputSizeParams: ...

    @property
    def default_options(self) -> FractionalMaxPool3dDimensionOutputSizeOptions: ...

    def load(
            self,
            params: FractionalMaxPool3dDimensionOutputSizeParams,
            options: FractionalMaxPool3dDimensionOutputSizeOptions
    ) -> void: ...

    def render(self, root: Window) -> Layout: ...
