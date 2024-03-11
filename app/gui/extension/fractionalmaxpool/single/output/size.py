from lib.gui import LS
from lib.gui.element.font import Font
from lib.gui.element.form import FormInput
from lib.gui.element.form.integer import IntegerInput
from lib.gui.element.text import Text
from lib.gui.layout.factory import LayoutFactory
from lib.gui.layout.type import LayoutType

from app.hooks import i18n
from app.network.extension.fractionalmaxpool.single import FractionalMaxPoolingSingleExtension
from app.network.neuron.fractionalmaxpool2d.dimension.params.output.size import \
    FractionalMaxPool2dDimensionOutputSizeParams
from app.network.neuron.fractionalmaxpool2d.dimension.options.output.size import \
    FractionalMaxPool2dDimensionOutputSizeOptions
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.neuron.strategy import NeuronStrategy


# Main

class OutputSizeStrategy(NeuronStrategy):
    def __init__(self, dependencies):
        super().__init__(dependencies)

        self._output_size = FormInput(self.default_params["output_size"])

        self._input_height = LS.rem(1.6)
        self._font_caption_title = Font().Size(LS.rem(.8)).Bold().Underline()

    @property
    def params(self):
        return NeuronStrategyParams(
            params=FractionalMaxPool2dDimensionOutputSizeParams(
                output_size=self._output_size.value
            ),
            options=FractionalMaxPool2dDimensionOutputSizeOptions()
        )

    @property
    def default_params(self):
        return FractionalMaxPoolingSingleExtension.default_params()

    @property
    def default_options(self):
        return FractionalMaxPoolingSingleExtension.default_options()

    def load(self, params, options):
        self._output_size.update(params["output_size"])

    def render(self, root):
        return (
            LayoutFactory(LayoutType.HORIZONTAL).create()
            .margin_horizontal(0)
            .append(
                LayoutFactory(LayoutType.HORIZONTAL).create()
                .add(
                    Text(root, i18n("window.screens.network.extension.fractionalmaxpool.single.labels.output_size"))
                )
                .add(
                    IntegerInput(root, self._output_size.value)
                    .Bind(self._output_size)
                    .Height(self._input_height)
                )
            )
        )
