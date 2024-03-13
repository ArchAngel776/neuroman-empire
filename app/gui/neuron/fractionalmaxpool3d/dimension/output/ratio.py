from lib.gui import LS
from lib.gui.element.font import Font
from lib.gui.element.form import FormInput
from lib.gui.element.form.number import NumberInput
from lib.gui.element.text import Text
from lib.gui.layout.factory import LayoutFactory
from lib.gui.layout.type import LayoutType

from app.hooks import i18n
from app.network.neuron.fractionalmaxpool3d import FractionalMaxPooling3d
from app.network.neuron.fractionalmaxpool3d.dimension.params.output.ratio import \
    FractionalMaxPool3dDimensionOutputRatioParams
from app.network.neuron.fractionalmaxpool3d.dimension.options.output.ratio import \
    FractionalMaxPool3dDimensionOutputRatioOptions
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.neuron.strategy import NeuronStrategy


# Main

class OutputRatioStrategy(NeuronStrategy):
    class Dimension(int):
        DEPTH = 0
        HEIGHT = 1
        WIDTH = 2

    def __init__(self, dependencies):
        super().__init__(dependencies)

        self._output_ratio_depth = FormInput(self.default_params["output_ratio"][self.Dimension.DEPTH])
        self._output_ratio_height = FormInput(self.default_params["output_ratio"][self.Dimension.HEIGHT])
        self._output_ratio_width = FormInput(self.default_params["output_ratio"][self.Dimension.WIDTH])

        self._input_height = LS.rem(1.6)
        self._font_caption_title = Font().Size(LS.rem(.8)).Bold().Underline()

    @property
    def params(self):
        return NeuronStrategyParams(
            params=FractionalMaxPool3dDimensionOutputRatioParams(
                output_ratio=(
                    self._output_ratio_depth.value,
                    self._output_ratio_height.value,
                    self._output_ratio_width.value
                )
            ),
            options=FractionalMaxPool3dDimensionOutputRatioOptions()
        )

    @property
    def default_params(self):
        return FractionalMaxPooling3d.default_params()

    @property
    def default_options(self):
        return FractionalMaxPooling3d.default_options()

    def load(self, params, options):
        self._output_ratio_depth.update(params["output_ratio"][self.Dimension.DEPTH])
        self._output_ratio_height.update(params["output_ratio"][self.Dimension.HEIGHT])
        self._output_ratio_width.update(params["output_ratio"][self.Dimension.WIDTH])

    def render(self, root):
        return (
            LayoutFactory(LayoutType.HORIZONTAL).create()
            .margin_horizontal(0)
            .append(
                LayoutFactory(LayoutType.VERTICAL).create()
                .add(
                    Text(root, i18n("window.screens.network.neurons.fractionalmaxpool3d.labels.output_ratio"))
                )
                .add(
                    NumberInput(root, self._output_ratio_depth.value)
                    .Bind(self._output_ratio_depth)
                    .Min(0.01)
                    .Max(0.99)
                    .Height(self._input_height)
                )
            )
            .append(
                LayoutFactory(LayoutType.VERTICAL).create()
                .add(
                    Text(root, i18n("window.screens.network.neurons.fractionalmaxpool3d.labels.output_ratio"))
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
                    Text(root, i18n("window.screens.network.neurons.fractionalmaxpool3d.labels.output_ratio"))
                )
                .add(
                    NumberInput(root, self._output_ratio_width.value)
                    .Bind(self._output_ratio_width)
                    .Min(0.01)
                    .Max(0.99)
                    .Height(self._input_height)
                )
            )
        )
