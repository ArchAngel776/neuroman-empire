from PyQt5.QtCore import Qt

from lib.gui import LS
from lib.gui.element.font import Font
from lib.gui.element.form import FormInput
from lib.gui.element.form.integer import IntegerInput
from lib.gui.element.text import Text
from lib.gui.layout.factory import LayoutFactory
from lib.gui.layout.type import LayoutType

from app.hooks import i18n
from app.network.neuron.circularpad1d import CircularPadding1d
from app.network.neuron.circularpad1d.boundary.params import CircularPad1dBoundaryParams
from app.network.neuron.circularpad1d.boundary.options import CircularPad1dBoundaryOptions
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.neuron.strategy import NeuronStrategy


# Main

class UnboundedBoundaryStrategy(NeuronStrategy):
    class Direction(int):
        LEFT = 0
        RIGHT = 1

    def __init__(self, dependencies):
        super().__init__(dependencies)

        self._padding_left = FormInput(self.default_params["padding"][UnboundedBoundaryStrategy.Direction.LEFT])

        self._padding_right = FormInput(self.default_params["padding"][UnboundedBoundaryStrategy.Direction.RIGHT])

        self._input_height = LS.rem(1.6)
        self._font_caption_title = Font().Size(LS.rem(.8)).Bold().Underline()

    @property
    def params(self):
        return NeuronStrategyParams(
            params=CircularPad1dBoundaryParams(
                padding=(
                    self._padding_left.value,
                    self._padding_right.value
                )
            ),
            options=CircularPad1dBoundaryOptions()
        )

    @property
    def default_params(self):
        return CircularPadding1d.default_params()

    @property
    def default_options(self):
        return CircularPadding1d.default_options()

    def load(self, params, options):
        self._padding_left.update(params["padding"][UnboundedBoundaryStrategy.Direction.LEFT])

        self._padding_right.update(params["padding"][UnboundedBoundaryStrategy.Direction.RIGHT])

    def render(self, root):
        return (
            LayoutFactory(LayoutType.HORIZONTAL).create()
            .append(
                LayoutFactory(LayoutType.VERTICAL).create()
                .weight(1)
                .add(
                    Text(root, i18n("window.screens.network.neurons.circularpad1d.boundaries.left"))
                    .Font(self._font_caption_title)
                    .Align(Qt.AlignCenter)
                    .Margin(0, LS.rem(.6))
                )
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .add(
                        Text(root, i18n("window.screens.network.neurons.circularpad1d.labels.padding"))
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
                    Text(root, i18n("window.screens.network.neurons.circularpad1d.boundaries.right"))
                    .Font(self._font_caption_title)
                    .Align(Qt.AlignCenter)
                    .Margin(0, LS.rem(.6))
                )
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .add(
                        Text(root, i18n("window.screens.network.neurons.circularpad1d.labels.padding"))
                    )
                    .add(
                        IntegerInput(root, self._padding_right.value)
                        .Bind(self._padding_right)
                        .Height(self._input_height)
                    )
                )
            )
        )
