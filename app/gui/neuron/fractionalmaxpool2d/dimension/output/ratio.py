from lib.gui import LS
from lib.gui.element.font import Font
from lib.gui.element.form import FormInput
from lib.gui.element.form.number import NumberInput
from lib.gui.element.text import Text
from lib.gui.layout.factory import LayoutFactory
from lib.gui.layout.type import LayoutType

from app.hooks import i18n
from app.network.neuron.fractionalmaxpool2d import FractionalMaxPooling2d
from app.network.neuron.fractionalmaxpool2d.dimension.params.output.ratio import \
    FractionalMaxPool2dDimensionOutputRatioParams
from app.network.neuron.fractionalmaxpool2d.dimension.options.output.ratio import \
    FractionalMaxPool2dDimensionOutputRatioOptions
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.neuron.strategy import NeuronStrategy


# Main

class OutputRatioStrategy(NeuronStrategy):
    class Dimension(int):
        HEIGHT = 0
        WIDTH = 1

    def __init__(self, dependencies):
        super().__init__(dependencies)

        self._output_ratio_height = FormInput(self.default_params["output_ratio"][self.Dimension.HEIGHT])
        self._output_ratio_width = FormInput(self.default_params["output_ratio"][self.Dimension.WIDTH])

        self._input_height = LS.rem(1.6)
        self._font_caption_title = Font().Size(LS.rem(.8)).Bold().Underline()

    @property
    def params(self):
        return NeuronStrategyParams(
            params=FractionalMaxPool2dDimensionOutputRatioParams(
                output_ratio=(
                    self._output_ratio_height.value,
                    self._output_ratio_width.value
                )
            ),
            options=FractionalMaxPool2dDimensionOutputRatioOptions()
        )

    @property
    def default_params(self):
        return FractionalMaxPooling2d.default_params()

    @property
    def default_options(self):
        return FractionalMaxPooling2d.default_options()

    def load(self, params, options):
        self._output_ratio_height.update(params["output_ratio"][self.Dimension.HEIGHT])
        self._output_ratio_width.update(params["output_ratio"][self.Dimension.WIDTH])

    def render(self, root):
        return (
            LayoutFactory(LayoutType.HORIZONTAL).create()
            .margin_horizontal(0)
            .append(
                LayoutFactory(LayoutType.VERTICAL).create()
                .add(
                    Text(root, i18n("window.screens.network.neurons.fractionalmaxpool2d.labels.output_ratio"))
                )
                .add(
                    NumberInput(root, self._output_ratio_height.value)
                    .Bind(self._output_ratio_height)
                    .Min(0.01)
                    .Max(0.99)
                    .Height(self._input_height)
                )
            )
            .append(
                LayoutFactory(LayoutType.VERTICAL).create()
                .add(
                    Text(root, i18n("window.screens.network.neurons.fractionalmaxpool2d.labels.output_ratio"))
                )
                .add(
                    NumberInput(root, self._output_ratio_height.value)
                    .Bind(self._output_ratio_height)
                    .Min(0.01)
                    .Max(0.99)
                    .Height(self._input_height)
                )
            )
        )
