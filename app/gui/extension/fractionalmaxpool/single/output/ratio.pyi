from lib import void
from lib.gui.element.font import Font
from lib.gui.element.form import FormInput
from lib.gui.layout import Layout
from lib.gui.window import Window

from app.network.extension.fractionalmaxpool.single.params.output.ratio import \
    FractionalMaxPoolSingleDimensionOutputRatioParams
from app.network.extension.fractionalmaxpool.single.options.output.ratio import \
    FractionalMaxPoolSingleDimensionOutputRatioOptions
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies


# Main

class OutputRatioStrategy(
    NeuronStrategy[
        FractionalMaxPoolSingleDimensionOutputRatioParams,
        FractionalMaxPoolSingleDimensionOutputRatioOptions
    ]
):
    _output_ratio: FormInput[float]

    _input_height: int
    _font_caption_title: Font

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[
        FractionalMaxPoolSingleDimensionOutputRatioParams,
        FractionalMaxPoolSingleDimensionOutputRatioOptions
    ]: ...

    @property
    def default_params(self) -> FractionalMaxPoolSingleDimensionOutputRatioParams: ...

    @property
    def default_options(self) -> FractionalMaxPoolSingleDimensionOutputRatioOptions: ...

    def load(
            self,
            params: FractionalMaxPoolSingleDimensionOutputRatioParams,
            options: FractionalMaxPoolSingleDimensionOutputRatioOptions
    ) -> void: ...

    def render(self, root: Window) -> Layout: ...
