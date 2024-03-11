from lib import void
from lib.gui.element.font import Font
from lib.gui.element.form import FormInput
from lib.gui.layout import Layout
from lib.gui.window import Window

from app.network.neuron.fractionalmaxpool2d.dimension.params.output.size import \
    FractionalMaxPool2dDimensionOutputSizeParams
from app.network.neuron.fractionalmaxpool2d.dimension.options.output.size import \
    FractionalMaxPool2dDimensionOutputSizeOptions
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies


# Main

class OutputSizeStrategy(
    NeuronStrategy[FractionalMaxPool2dDimensionOutputSizeParams, FractionalMaxPool2dDimensionOutputSizeOptions]
):
    class Dimension(int):
        HEIGHT = ... #type: OutputSizeStrategy.Dimension
        WIDTH = ... #type: OutputSizeStrategy.Dimension

    _output_size_height: FormInput[int]

    _output_size_width: FormInput[int]

    _input_height: int
    _font_caption_title: Font

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[
        FractionalMaxPool2dDimensionOutputSizeParams,
        FractionalMaxPool2dDimensionOutputSizeOptions
    ]: ...

    @property
    def default_params(self) -> FractionalMaxPool2dDimensionOutputSizeParams: ...

    @property
    def default_options(self) -> FractionalMaxPool2dDimensionOutputSizeOptions: ...

    def load(
            self,
            params: FractionalMaxPool2dDimensionOutputSizeParams,
            options: FractionalMaxPool2dDimensionOutputSizeOptions
    ) -> void: ...

    def render(self, root: Window) -> Layout: ...
