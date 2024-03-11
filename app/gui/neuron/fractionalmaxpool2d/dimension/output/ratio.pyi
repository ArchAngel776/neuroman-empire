from lib import void
from lib.gui.element.font import Font
from lib.gui.element.form import FormInput
from lib.gui.layout import Layout
from lib.gui.window import Window

from app.network.neuron.fractionalmaxpool2d.dimension.params.output.ratio import \
    FractionalMaxPool2dDimensionOutputRatioParams
from app.network.neuron.fractionalmaxpool2d.dimension.options.output.ratio import \
    FractionalMaxPool2dDimensionOutputRatioOptions
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies


# Main

class OutputRatioStrategy(
    NeuronStrategy[FractionalMaxPool2dDimensionOutputRatioParams, FractionalMaxPool2dDimensionOutputRatioOptions]
):
    class Dimension(int):
        HEIGHT = ... #type: OutputRatioStrategy.Dimension
        WIDTH = ... #type: OutputRatioStrategy.Dimension

    _output_ratio_height: FormInput[float]

    _output_ratio_width: FormInput[float]

    _input_height: int
    _font_caption_title: Font

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[
        FractionalMaxPool2dDimensionOutputRatioParams,
        FractionalMaxPool2dDimensionOutputRatioOptions
    ]: ...

    @property
    def default_params(self) -> FractionalMaxPool2dDimensionOutputRatioParams: ...

    @property
    def default_options(self) -> FractionalMaxPool2dDimensionOutputRatioOptions: ...

    def load(
            self,
            params: FractionalMaxPool2dDimensionOutputRatioParams,
            options: FractionalMaxPool2dDimensionOutputRatioOptions
    ) -> void: ...

    def render(self, root: Window) -> Layout: ...
