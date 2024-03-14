from PyQt5.QtCore import Qt

from lib.gui import LS
from lib.gui.element.font import Font
from lib.gui.element.form import FormInput
from lib.gui.element.form.integer import IntegerInput
from lib.gui.element.text import Text
from lib.gui.layout.factory import LayoutFactory
from lib.gui.layout.type import LayoutType

from app.hooks import i18n
from app.network.neuron.adaptiveavgpool2d import AdaptiveAveragePooling2d
from app.network.neuron.adaptiveavgpool2d.dimension.params import AdaptiveAvgPool2dDimensionParams
from app.network.neuron.adaptiveavgpool2d.dimension.options import AdaptiveAvgPool2dDimensionOptions
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.params import NeuronStrategyParams


# Main

class DoubleDimensionStrategy(NeuronStrategy):
    class Dimension(int):
        HEIGHT = 0
        WIDTH = 1

    def __init__(self, dependencies):
        super().__init__(dependencies)

        self._output_size_height = FormInput(self.default_params["output_size"][self.Dimension.HEIGHT])

        self._output_size_width = FormInput(self.default_params["output_size"][self.Dimension.WIDTH])

        self._input_height = LS.rem(1.6)
        self._font_caption_title = Font().Size(LS.rem(.8)).Bold().Underline()

    @property
    def params(self):
        return NeuronStrategyParams(
            params=AdaptiveAvgPool2dDimensionParams(
                output_size=(
                    self._output_size_height.value,
                    self._output_size_width.value
                )
            ),
            options=AdaptiveAvgPool2dDimensionOptions()
        )

    @property
    def default_params(self):
        return AdaptiveAveragePooling2d.default_params()

    @property
    def default_options(self):
        return AdaptiveAveragePooling2d.default_options()

    def load(self, params, options):
        self._output_size_height.update(params["output_size"][self.Dimension.HEIGHT])

        self._output_size_width.update(params["output_size"][self.Dimension.WIDTH])

    def render(self, root):
        return (
            LayoutFactory(LayoutType.HORIZONTAL).create()
            .append(
                LayoutFactory(LayoutType.VERTICAL).create()
                .weight(1)
                .add(
                    Text(root, i18n("window.screens.network.neurons.adaptiveavgpool2d.dimensions.height"))
                    .Font(self._font_caption_title)
                    .Align(Qt.AlignCenter)
                    .Margin(0, LS.rem(.6))
                )
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .add(
                        Text(root, i18n("window.screens.network.neurons.adaptiveavgpool2d.labels.output"))
                    )
                    .add(
                        IntegerInput(root, self._output_size_height.value)
                        .Bind(self._output_size_height)
                        .Height(self._input_height)
                    )
                )
            )
            .append(
                LayoutFactory(LayoutType.VERTICAL).create()
                .weight(1)
                .add(
                    Text(root, i18n("window.screens.network.neurons.adaptiveavgpool2d.dimensions.width"))
                    .Font(self._font_caption_title)
                    .Align(Qt.AlignCenter)
                    .Margin(0, LS.rem(.6))
                )
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .add(
                        Text(root, i18n("window.screens.network.neurons.adaptiveavgpool2d.labels.output"))
                    )
                    .add(
                        IntegerInput(root, self._output_size_width.value)
                        .Bind(self._output_size_width)
                        .Height(self._input_height)
                    )
                )
            )
        )
