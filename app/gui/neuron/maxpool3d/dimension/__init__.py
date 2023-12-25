from PyQt5.QtCore import Qt

from app.network.neuron.conv3d.dimension.options import Conv3dDimensionOptions
from lib.gui import LS
from lib.gui.element.font import Font
from lib.gui.element.form import FormInput
from lib.gui.element.form.integer import IntegerInput
from lib.gui.element.text import Text
from lib.gui.layout.factory import LayoutFactory
from lib.gui.layout.type import LayoutType

from app.hooks import i18n
from app.network.neuron.conv3d import Convolution3d
from app.network.neuron.conv3d.dimension.params import Conv3dDimensionParams
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.params import NeuronStrategyParams


# Main

class TripleDimensionStrategy(NeuronStrategy):
    class Dimension(int):
        DEPTH = 0
        HEIGHT = 1
        WIDTH = 2

    def __init__(self):
        super().__init__()

        self._kernel_size_depth = FormInput(self.default_params["kernel_size"][self.Dimension.DEPTH])
        self._stride_depth = FormInput(self.default_params["stride"][self.Dimension.DEPTH])
        self._padding_depth = FormInput(self.default_params["padding"][self.Dimension.DEPTH])
        self._dilation_depth = FormInput(self.default_params["dilation"][self.Dimension.DEPTH])

        self._kernel_size_height = FormInput(self.default_params["kernel_size"][self.Dimension.HEIGHT])
        self._stride_height = FormInput(self.default_params["stride"][self.Dimension.HEIGHT])
        self._padding_height = FormInput(self.default_params["padding"][self.Dimension.HEIGHT])
        self._dilation_height = FormInput(self.default_params["dilation"][self.Dimension.HEIGHT])

        self._kernel_size_width = FormInput(self.default_params["kernel_size"][self.Dimension.WIDTH])
        self._stride_width = FormInput(self.default_params["stride"][self.Dimension.WIDTH])
        self._padding_width = FormInput(self.default_params["padding"][self.Dimension.WIDTH])
        self._dilation_width = FormInput(self.default_params["dilation"][self.Dimension.WIDTH])

        self._input_height = LS.rem(1.6)
        self._font_caption_title = Font().Size(LS.rem(.8)).Bold().Underline()

    @property
    def params(self):
        return NeuronStrategyParams(
            params=Conv3dDimensionParams(
                kernel_size=(
                    self._kernel_size_depth.value,
                    self._kernel_size_height.value,
                    self._kernel_size_width.value
                ),
                stride=(
                    self._stride_depth.value,
                    self._stride_height.value,
                    self._stride_width.value
                ),
                padding=(
                    self._padding_depth.value,
                    self._padding_height.value,
                    self._padding_width.value
                ),
                dilation=(
                    self._dilation_depth.value,
                    self._dilation_height.value,
                    self._dilation_width.value
                )
            ),
            options=Conv3dDimensionOptions()
        )

    @property
    def default_params(self):
        return Convolution3d.default_params()

    @property
    def default_options(self):
        return Convolution3d.default_options()

    def load(self, params, options):
        self._kernel_size_depth.update(params["kernel_size"][self.Dimension.DEPTH])
        self._stride_depth.update(params["stride"][self.Dimension.DEPTH])
        self._padding_depth.update(params["padding"][self.Dimension.DEPTH])
        self._dilation_depth.update(params["dilation"][self.Dimension.DEPTH])

        self._kernel_size_height.update(params["kernel_size"][self.Dimension.HEIGHT])
        self._stride_height.update(params["stride"][self.Dimension.HEIGHT])
        self._padding_height.update(params["padding"][self.Dimension.HEIGHT])
        self._dilation_height.update(params["dilation"][self.Dimension.HEIGHT])

        self._kernel_size_width.update(params["kernel_size"][self.Dimension.WIDTH])
        self._stride_width.update(params["stride"][self.Dimension.WIDTH])
        self._padding_width.update(params["padding"][self.Dimension.WIDTH])
        self._dilation_width.update(params["dilation"][self.Dimension.WIDTH])

    def render(self, root):
        return (
            LayoutFactory(LayoutType.HORIZONTAL).create()
            .append(
                LayoutFactory(LayoutType.VERTICAL).create()
                .weight(1)
                .add(
                    Text(root, i18n("window.screens.network.neurons.maxpool3d.dimensions.depth"))
                    .Font(self._font_caption_title)
                    .Align(Qt.AlignCenter)
                    .Margin(0, LS.rem(.6))
                )
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .add(
                        Text(root, i18n("window.screens.network.neurons.maxpool3d.labels.kernel"))
                    )
                    .add(
                        IntegerInput(root, self._kernel_size_depth.value)
                        .Bind(self._kernel_size_depth)
                        .Height(self._input_height)
                    )
                )
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .add(
                        Text(root, i18n("window.screens.network.neurons.maxpool3d.labels.stride"))
                    )
                    .add(
                        IntegerInput(root, self._stride_depth.value)
                        .Bind(self._stride_depth)
                        .Height(self._input_height)
                    )
                )
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .add(
                        Text(root, i18n("window.screens.network.neurons.maxpool3d.labels.padding"))
                    )
                    .add(
                        IntegerInput(root, self._padding_depth.value)
                        .Bind(self._padding_depth)
                        .Height(self._input_height)
                    )
                )
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .add(
                        Text(root, i18n("window.screens.network.neurons.maxpool3d.labels.dilation"))
                    )
                    .add(
                        IntegerInput(root, self._dilation_depth.value)
                        .Bind(self._dilation_depth)
                        .Height(self._input_height)
                    )
                )
            )
            .append(
                LayoutFactory(LayoutType.VERTICAL).create()
                .weight(1)
                .add(
                    Text(root, i18n("window.screens.network.neurons.maxpool3d.dimensions.height"))
                    .Font(self._font_caption_title)
                    .Align(Qt.AlignCenter)
                    .Margin(0, LS.rem(.6))
                )
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .add(
                        Text(root, i18n("window.screens.network.neurons.maxpool3d.labels.kernel"))
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
                        Text(root, i18n("window.screens.network.neurons.maxpool3d.labels.stride"))
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
                        Text(root, i18n("window.screens.network.neurons.maxpool3d.labels.padding"))
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
                        Text(root, i18n("window.screens.network.neurons.maxpool3d.labels.dilation"))
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
                    Text(root, i18n("window.screens.network.neurons.maxpool3d.dimensions.width"))
                    .Font(self._font_caption_title)
                    .Align(Qt.AlignCenter)
                    .Margin(0, LS.rem(.6))
                )
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .add(
                        Text(root, i18n("window.screens.network.neurons.maxpool3d.labels.kernel"))
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
                        Text(root, i18n("window.screens.network.neurons.maxpool3d.labels.stride"))
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
                        Text(root, i18n("window.screens.network.neurons.maxpool3d.labels.padding"))
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
                        Text(root, i18n("window.screens.network.neurons.maxpool3d.labels.dilation"))
                    )
                    .add(
                        IntegerInput(root, self._dilation_width.value)
                        .Bind(self._dilation_width)
                        .Height(self._input_height)
                    )
                )
            )
        )
