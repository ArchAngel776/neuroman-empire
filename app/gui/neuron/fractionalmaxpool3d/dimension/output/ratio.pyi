from lib import void
from lib.gui.element.font import Font
from lib.gui.element.form import FormInput
from lib.gui.layout import Layout
from lib.gui.window import Window

from app.network.neuron.fractionalmaxpool3d.dimension.params.output.ratio import \
    FractionalMaxPool3dDimensionOutputRatioParams
from app.network.neuron.fractionalmaxpool3d.dimension.options.output.ratio import \
    FractionalMaxPool3dDimensionOutputRatioOptions
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies


# Main

class OutputRatioStrategy(
    NeuronStrategy[FractionalMaxPool3dDimensionOutputRatioParams, FractionalMaxPool3dDimensionOutputRatioOptions]
):
    class Dimension(int):
        DEPTH = ... #type: OutputRatioStrategy.Dimension
        HEIGHT = ... #type: OutputRatioStrategy.Dimension
        WIDTH = ... #type: OutputRatioStrategy.Dimension

    _output_ratio_depth: FormInput[float]

    _output_ratio_height: FormInput[float]

    _output_ratio_width: FormInput[float]

    _input_height: int
    _font_caption_title: Font

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[
        FractionalMaxPool3dDimensionOutputRatioParams,
        FractionalMaxPool3dDimensionOutputRatioOptions
    ]: ...

    @property
    def default_params(self) -> FractionalMaxPool3dDimensionOutputRatioParams: ...

    @property
    def default_options(self) -> FractionalMaxPool3dDimensionOutputRatioOptions: ...

    def load(
            self,
            params: FractionalMaxPool3dDimensionOutputRatioParams,
            options: FractionalMaxPool3dDimensionOutputRatioOptions
    ) -> void: ...

    def render(self, root: Window) -> Layout: ...
