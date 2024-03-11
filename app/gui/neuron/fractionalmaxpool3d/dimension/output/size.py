from lib.gui import LS
from lib.gui.element.font import Font
from lib.gui.element.form import FormInput
from lib.gui.element.form.integer import IntegerInput
from lib.gui.element.text import Text
from lib.gui.layout.factory import LayoutFactory
from lib.gui.layout.type import LayoutType

from app.hooks import i18n
from app.network.neuron.fractionalmaxpool3d import FractionalMaxPooling3d
from app.network.neuron.fractionalmaxpool3d.dimension.params.output.size import \
    FractionalMaxPool3dDimensionOutputSizeParams
from app.network.neuron.fractionalmaxpool3d.dimension.options.output.size import \
    FractionalMaxPool3dDimensionOutputSizeOptions
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.neuron.strategy import NeuronStrategy


# Main

class OutputSizeStrategy(NeuronStrategy):
    class Dimension(int):
        DEPTH = 0
        HEIGHT = 1
        WIDTH = 2

    def __init__(self, dependencies):
        super().__init__(dependencies)

        self._output_size_depth = FormInput(self.default_params["output_size"][self.Dimension.DEPTH])
        self._output_size_height = FormInput(self.default_params["output_size"][self.Dimension.HEIGHT])
        self._output_size_width = FormInput(self.default_params["output_size"][self.Dimension.WIDTH])

        self._input_height = LS.rem(1.6)
        self._font_caption_title = Font().Size(LS.rem(.8)).Bold().Underline()

    @property
    def params(self):
        return NeuronStrategyParams(
            params=FractionalMaxPool3dDimensionOutputSizeParams(
                output_size=(
                    self._output_size_depth.value,
                    self._output_size_height.value,
                    self._output_size_width.value
                )
            ),
            options=FractionalMaxPool3dDimensionOutputSizeOptions()
        )

    @property
    def default_params(self):
        return FractionalMaxPooling3d.default_params()

    @property
    def default_options(self):
        return FractionalMaxPooling3d.default_options()

    def load(self, params, options):
        self._output_size_depth.update(params["output_size"][self.Dimension.DEPTH])
        self._output_size_height.update(params["output_size"][self.Dimension.HEIGHT])
        self._output_size_width.update(params["output_size"][self.Dimension.WIDTH])

    def render(self, root):
        return (
            LayoutFactory(LayoutType.HORIZONTAL).create()
            .margin_horizontal(0)
            .append(
                LayoutFactory(LayoutType.VERTICAL).create()
                .add(
                    Text(root, i18n("window.screens.network.neurons.fractionalmaxpool3d.labels.output_size"))
                )
                .add(
                    IntegerInput(root, self._output_size_depth.value)
                    .Bind(self._output_size_depth)
                    .Height(self._input_height)
                )
            )
            .append(
                LayoutFactory(LayoutType.VERTICAL).create()
                .add(
                    Text(root, i18n("window.screens.network.neurons.fractionalmaxpool3d.labels.output_size"))
                )
                .add(
                    IntegerInput(root, self._output_size_height.value)
                    .Bind(self._output_size_height)
                    .Height(self._input_height)
                )
            )
            .append(
                LayoutFactory(LayoutType.VERTICAL).create()
                .add(
                    Text(root, i18n("window.screens.network.neurons.fractionalmaxpool3d.labels.output_size"))
                )
                .add(
                    IntegerInput(root, self._output_size_width.value)
                    .Bind(self._output_size_width)
                    .Height(self._input_height)
                )
            )
        )
