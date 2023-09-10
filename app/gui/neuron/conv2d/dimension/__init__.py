from PyQt5.QtCore import Qt

from app.network.neuron.conv2d.dimension.options import Conv2dDimensionOptions
from lib.gui import LS
from lib.gui.element.font import Font
from lib.gui.element.form import FormInput
from lib.gui.element.form.integer import IntegerInput
from lib.gui.element.text import Text
from lib.gui.layout.factory import LayoutFactory
from lib.gui.layout.type import LayoutType

from app.hooks import i18n
from app.network.neuron.conv2d import Convolution2d
from app.network.neuron.conv2d.dimension.params import Conv2dDimensionParams
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.params import NeuronStrategyParams


# Main

class DoubleDimensionStrategy(NeuronStrategy):
    class Dimension(int):
        HEIGHT = 0
        WIDTH = 1

    def __init__(self, dependencies):
        super().__init__(dependencies)

        self._kernel_size_height = FormInput(self.default_params["kernel_size"][self.Dimension.HEIGHT])
        self._stride_height = FormInput(self.default_params["stride"][self.Dimension.HEIGHT])
        self._padding_height = FormInput(self.default_params["padding"][self.Dimension.HEIGHT])
        self._dilation_height = FormInput(self.default_params["dilation"][self.Dimension.HEIGHT])

        self._kernel_size_width = FormInput(self.default_params["kernel_size"][self.Dimension.WIDTH])
        self._stride_width = FormInput(self.default_params["kernel_size"][self.Dimension.WIDTH])
        self._padding_width = FormInput(self.default_params["padding"][self.Dimension.WIDTH])
        self._dilation_width = FormInput(self.default_params["dilation"][self.Dimension.WIDTH])

        self._input_height = LS.rem(1.6)
        self._font_caption_title = Font().Size(LS.rem(.8)).Bold().Underline()

    @property
    def params(self):
        return NeuronStrategyParams(
            params=Conv2dDimensionParams(
                kernel_size=(
                    self._kernel_size_height.value,
                    self._kernel_size_width.value
                ),
                stride=(
                    self._stride_height.value,
                    self._stride_width.value
                ),
                padding=(
                    self._padding_height.value,
                    self._padding_width.value
                ),
                dilation=(
                    self._dilation_height.value,
                    self._dilation_width.value
                )
            ),
            options=Conv2dDimensionOptions()
        )

    @property
    def default_params(self):
        return Convolution2d.default_params()

    @property
    def default_options(self):
        return Convolution2d.default_options()

    @property
    def init_param(self):
        return self.dependencies["init_param"]

    @property
    def init_option(self):
        return self.dependencies["init_option"]

    def render(self, root):
        return (
            LayoutFactory(LayoutType.HORIZONTAL).create()
            .append(
                LayoutFactory(LayoutType.VERTICAL).create()
                .weight(1)
                .add(
                    Text(root, i18n("window.screens.network.neurons.conv2d.dimensions.height"))
                    .Font(self._font_caption_title)
                    .Align(Qt.AlignCenter)
                    .Margin(0, LS.rem(.6))
                )
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .add(
                        Text(root, i18n("window.screens.network.neurons.conv2d.labels.kernel"))
                    )
                    .add(
                        IntegerInput(root, self._kernel_size_height.value)
                        .Bind(self._kernel_size_height)
                        .Height(self._input_height)
                    )
                )
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .add(
                        Text(root, i18n("window.screens.network.neurons.conv2d.labels.stride"))
                    )
                    .add(
                        IntegerInput(root, self._stride_height.value)
                        .Bind(self._stride_height)
                        .Height(self._input_height)
                    )
                )
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .add(
                        Text(root, i18n("window.screens.network.neurons.conv2d.labels.padding"))
                    )
                    .add(
                        IntegerInput(root, self._padding_height.value)
                        .Bind(self._padding_height)
                        .Height(self._input_height)
                    )
                )
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .add(
                        Text(root, i18n("window.screens.network.neurons.conv2d.labels.dilation"))
                    )
                    .add(
                        IntegerInput(root, self._dilation_height.value)
                        .Bind(self._dilation_height)
                        .Height(self._input_height)
                    )
                )
            )
            .append(
                LayoutFactory(LayoutType.VERTICAL).create()
                .weight(1)
                .add(
                    Text(root, i18n("window.screens.network.neurons.conv2d.dimensions.width"))
                    .Font(self._font_caption_title)
                    .Align(Qt.AlignCenter)
                    .Margin(0, LS.rem(.6))
                )
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .add(
                        Text(root, i18n("window.screens.network.neurons.conv2d.labels.kernel"))
                    )
                    .add(
                        IntegerInput(root, self._kernel_size_width.value)
                        .Bind(self._kernel_size_width)
                        .Height(self._input_height)
                    )
                )
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .add(
                        Text(root, i18n("window.screens.network.neurons.conv2d.labels.stride"))
                    )
                    .add(
                        IntegerInput(root, self._stride_width.value)
                        .Bind(self._stride_width)
                        .Height(self._input_height)
                    )
                )
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .add(
                        Text(root, i18n("window.screens.network.neurons.conv2d.labels.padding"))
                    )
                    .add(
                        IntegerInput(root, self._padding_width.value)
                        .Bind(self._padding_width)
                        .Height(self._input_height)
                    )
                )
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .add(
                        Text(root, i18n("window.screens.network.neurons.conv2d.labels.dilation"))
                    )
                    .add(
                        IntegerInput(root, self._dilation_width.value)
                        .Bind(self._dilation_width)
                        .Height(self._input_height)
                    )
                )
            )
        )
