from PyQt5.QtCore import Qt

from lib.gui import LS
from lib.gui.element.font import Font
from lib.gui.element.form import FormInput
from lib.gui.element.form.integer import IntegerInput
from lib.gui.element.text import Text
from lib.gui.layout.factory import LayoutFactory
from lib.gui.layout.type import LayoutType

from app.hooks import i18n
from app.network.neuron.zeropad3d import ZeroPadding3d
from app.network.neuron.zeropad3d.boundary.params import ZeroPad3dBoundaryParams
from app.network.neuron.zeropad3d.boundary.options import ZeroPad3dBoundaryOptions
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.neuron.strategy import NeuronStrategy


# Main

class UnboundedBoundaryStrategy(NeuronStrategy):
    class Direction(int):
        LEFT = 0
        RIGHT = 1
        TOP = 2
        BOTTOM = 3
        FRONT = 4
        BACK = 5

    def __init__(self, dependencies):
        super().__init__(dependencies)

        self._padding_left = FormInput(self.default_params["padding"][UnboundedBoundaryStrategy.Direction.LEFT])

        self._padding_right = FormInput(self.default_params["padding"][UnboundedBoundaryStrategy.Direction.RIGHT])

        self._padding_top = FormInput(self.default_params["padding"][UnboundedBoundaryStrategy.Direction.TOP])

        self._padding_bottom = FormInput(self.default_params["padding"][UnboundedBoundaryStrategy.Direction.BOTTOM])

        self._padding_front = FormInput(self.default_params["padding"][UnboundedBoundaryStrategy.Direction.FRONT])

        self._padding_back = FormInput(self.default_params["padding"][UnboundedBoundaryStrategy.Direction.BACK])

        self._input_height = LS.rem(1.6)
        self._font_caption_title = Font().Size(LS.rem(.8)).Bold().Underline()

    @property
    def params(self):
        return NeuronStrategyParams(
            params=ZeroPad3dBoundaryParams(
                padding=(
                    self._padding_left.value,
                    self._padding_right.value,
                    self._padding_top.value,
                    self._padding_bottom.value,
                    self._padding_front.value,
                    self._padding_back.value
                )
            ),
            options=ZeroPad3dBoundaryOptions()
        )

    @property
    def default_params(self):
        return ZeroPadding3d.default_params()

    @property
    def default_options(self):
        return ZeroPadding3d.default_options()

    def load(self, params, options):
        self._padding_left.update(params["padding"][UnboundedBoundaryStrategy.Direction.LEFT])

        self._padding_right.update(params["padding"][UnboundedBoundaryStrategy.Direction.RIGHT])

        self._padding_top.update(params["padding"][UnboundedBoundaryStrategy.Direction.TOP])

        self._padding_bottom.update(params["padding"][UnboundedBoundaryStrategy.Direction.BOTTOM])

        self._padding_front.update(params["padding"][UnboundedBoundaryStrategy.Direction.FRONT])

        self._padding_back.update(params["padding"][UnboundedBoundaryStrategy.Direction.BACK])

    def render(self, root):
        return (
            LayoutFactory(LayoutType.HORIZONTAL).create()
            .append(
                LayoutFactory(LayoutType.VERTICAL).create()
                .weight(1)
                .add(
                    Text(root, i18n("window.screens.network.neurons.zeropad3d.boundaries.left"))
                    .Font(self._font_caption_title)
                    .Align(Qt.AlignCenter)
                    .Margin(0, LS.rem(.6))
                )
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .add(
                        Text(root, i18n("window.screens.network.neurons.zeropad3d.labels.padding"))
                    )
                    .add(
                        IntegerInput(root, self._padding_left.value)
                        .Bind(self._padding_left)
                        .Height(self._input_height)
                    )
                )
            )
            .append(
                LayoutFactory(LayoutType.VERTICAL).create()
                .weight(1)
                .add(
                    Text(root, i18n("window.screens.network.neurons.zeropad3d.boundaries.right"))
                    .Font(self._font_caption_title)
                    .Align(Qt.AlignCenter)
                    .Margin(0, LS.rem(.6))
                )
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .add(
                        Text(root, i18n("window.screens.network.neurons.zeropad3d.labels.padding"))
                    )
                    .add(
                        IntegerInput(root, self._padding_right.value)
                        .Bind(self._padding_right)
                        .Height(self._input_height)
                    )
                )
            )
            .append(
                LayoutFactory(LayoutType.VERTICAL).create()
                .weight(1)
                .add(
                    Text(root, i18n("window.screens.network.neurons.zeropad3d.boundaries.top"))
                    .Font(self._font_caption_title)
                    .Align(Qt.AlignCenter)
                    .Margin(0, LS.rem(.6))
                )
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .add(
                        Text(root, i18n("window.screens.network.neurons.zeropad3d.labels.padding"))
                    )
                    .add(
                        IntegerInput(root, self._padding_top.value)
                        .Bind(self._padding_top)
                        .Height(self._input_height)
                    )
                )
            )
            .append(
                LayoutFactory(LayoutType.VERTICAL).create()
                .weight(1)
                .add(
                    Text(root, i18n("window.screens.network.neurons.zeropad3d.boundaries.bottom"))
                    .Font(self._font_caption_title)
                    .Align(Qt.AlignCenter)
                    .Margin(0, LS.rem(.6))
                )
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .add(
                        Text(root, i18n("window.screens.network.neurons.zeropad3d.labels.padding"))
                    )
                    .add(
                        IntegerInput(root, self._padding_bottom.value)
                        .Bind(self._padding_bottom)
                        .Height(self._input_height)
                    )
                )
            )
            .append(
                LayoutFactory(LayoutType.VERTICAL).create()
                .weight(1)
                .add(
                    Text(root, i18n("window.screens.network.neurons.zeropad3d.boundaries.front"))
                    .Font(self._font_caption_title)
                    .Align(Qt.AlignCenter)
                    .Margin(0, LS.rem(.6))
                )
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .add(
                        Text(root, i18n("window.screens.network.neurons.zeropad3d.labels.padding"))
                    )
                    .add(
                        IntegerInput(root, self._padding_front.value)
                        .Bind(self._padding_front)
                        .Height(self._input_height)
                    )
                )
            )
            .append(
                LayoutFactory(LayoutType.VERTICAL).create()
                .weight(1)
                .add(
                    Text(root, i18n("window.screens.network.neurons.zeropad3d.boundaries.back"))
                    .Font(self._font_caption_title)
                    .Align(Qt.AlignCenter)
                    .Margin(0, LS.rem(.6))
                )
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .add(
                        Text(root, i18n("window.screens.network.neurons.zeropad3d.labels.padding"))
                    )
                    .add(
                        IntegerInput(root, self._padding_back.value)
                        .Bind(self._padding_back)
                        .Height(self._input_height)
                    )
                )
            )
        )
