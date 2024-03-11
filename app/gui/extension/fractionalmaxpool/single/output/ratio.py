from lib.gui import LS
from lib.gui.element.font import Font
from lib.gui.element.form import FormInput
from lib.gui.element.form.number import NumberInput
from lib.gui.element.text import Text
from lib.gui.layout.factory import LayoutFactory
from lib.gui.layout.type import LayoutType

from app.hooks import i18n
from app.network.extension.fractionalmaxpool.single import FractionalMaxPoolingSingleExtension
from app.network.extension.fractionalmaxpool.single.params.output.ratio import \
    FractionalMaxPoolSingleDimensionOutputRatioParams
from app.network.extension.fractionalmaxpool.single.options.output.ratio import \
    FractionalMaxPoolSingleDimensionOutputRatioOptions
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.neuron.strategy import NeuronStrategy


# Main

class OutputRatioStrategy(NeuronStrategy):
    def __init__(self, dependencies):
        super().__init__(dependencies)

        self._output_ratio = FormInput(self.default_params["output_ratio"])

        self._input_height = LS.rem(1.6)
        self._font_caption_title = Font().Size(LS.rem(.8)).Bold().Underline()

    @property
    def params(self):
        return NeuronStrategyParams(
            params=FractionalMaxPoolSingleDimensionOutputRatioParams(
                output_ratio=self._output_ratio.value
            ),
            options=FractionalMaxPoolSingleDimensionOutputRatioOptions()
        )

    @property
    def default_params(self):
        return FractionalMaxPoolingSingleExtension.default_params()

    @property
    def default_options(self):
        return FractionalMaxPoolingSingleExtension.default_options()

    def load(self, params, options):
        self._output_ratio.update(params["output_ratio"])

    def render(self, root):
        return (
            LayoutFactory(LayoutType.HORIZONTAL).create()
            .margin_horizontal(0)
            .append(
                LayoutFactory(LayoutType.HORIZONTAL).create()
                .add(
                    Text(root, i18n("window.screens.network.extension.fractionalmaxpool.single.labels.output_ratio"))
                )
                .add(
                    NumberInput(root, self._output_ratio.value)
                    .Bind(self._output_ratio)
                    .Min(0.01)
                    .Max(0.99)
                    .Height(self._input_height)
                )
            )
        )
