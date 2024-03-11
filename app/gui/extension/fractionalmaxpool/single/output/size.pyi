from lib import void
from lib.gui.element.font import Font
from lib.gui.element.form import FormInput
from lib.gui.layout import Layout
from lib.gui.window import Window

from app.network.extension.fractionalmaxpool.single.params.output.size import \
    FractionalMaxPoolSingleDimensionOutputSizeParams
from app.network.extension.fractionalmaxpool.single.options.output.size import \
    FractionalMaxPoolSingleDimensionOutputSizeOptions
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies


# Main

class OutputSizeStrategy(
    NeuronStrategy[FractionalMaxPoolSingleDimensionOutputSizeParams, FractionalMaxPoolSingleDimensionOutputSizeOptions]
):
    _output_size: FormInput[int]

    _input_height: int
    _font_caption_title: Font

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[
        FractionalMaxPoolSingleDimensionOutputSizeParams,
        FractionalMaxPoolSingleDimensionOutputSizeOptions
    ]: ...

    @property
    def default_params(self) -> FractionalMaxPoolSingleDimensionOutputSizeParams: ...

    @property
    def default_options(self) -> FractionalMaxPoolSingleDimensionOutputSizeOptions: ...

    def load(
            self,
            params: FractionalMaxPoolSingleDimensionOutputSizeParams,
            options: FractionalMaxPoolSingleDimensionOutputSizeOptions
    ) -> void: ...

    def render(self, root: Window) -> Layout: ...
