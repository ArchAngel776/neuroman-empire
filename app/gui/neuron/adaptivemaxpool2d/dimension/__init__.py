from PyQt5.QtCore import Qt

from lib.gui import LS
from lib.gui.element.font import Font
from lib.gui.element.form import FormInput
from lib.gui.element.form.check import CheckBox
from lib.gui.element.form.integer import IntegerInput
from lib.gui.element.text import Text
from lib.gui.event import Event
from lib.gui.layout.factory import LayoutFactory
from lib.gui.layout.type import LayoutType

from app.hooks import i18n
from app.network.neuron.adaptivemaxpool2d import AdaptiveMaxPooling2d
from app.network.neuron.adaptivemaxpool2d.dimension.params import AdaptiveMaxPool2dDimensionParams
from app.network.neuron.adaptivemaxpool2d.dimension.options import AdaptiveMaxPool2dDimensionOptions
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

        self._output_enabled_height = FormInput(self.default_options["output_enabled"][self.Dimension.HEIGHT])

        self._output_enabled_width = FormInput(self.default_options["output_enabled"][self.Dimension.WIDTH])

        self._input_height = LS.rem(1.6)
        self._font_caption_title = Font().Size(LS.rem(.8)).Bold().Underline()

    @property
    def params(self):
        return NeuronStrategyParams(
            params=AdaptiveMaxPool2dDimensionParams(
                output_size=(
                    self._output_size_height.value,
                    self._output_size_width.value
                )
            ),
            options=AdaptiveMaxPool2dDimensionOptions(
                output_enabled=(
                    self._output_enabled_height.value,
                    self._output_enabled_width.value
                )
            )
        )

    @property
    def default_params(self):
        return AdaptiveMaxPooling2d.default_params()

    @property
    def default_options(self):
        return AdaptiveMaxPooling2d.default_options()

    def load(self, params, options):
        self._output_size_height.update(params["output_size"][self.Dimension.HEIGHT])

        self._output_size_width.update(params["output_size"][self.Dimension.WIDTH])

        self._output_enabled_width.update(options["output_enabled"][self.Dimension.HEIGHT])

        self._output_enabled_height.update(options["output_enabled"][self.Dimension.WIDTH])

    def enable_height(self, event):
        if self._output_size_height.form_control is None:
            return True

        if event.checked:
            self._output_size_height.form_control.setEnabled(True)
        else:
            self._output_size_height.update(self.default_params["output_size"][self.Dimension.HEIGHT])
            self._output_size_height.form_control.setEnabled(False)

        return True

    def enable_width(self, event):
        if self._output_size_width.form_control is None:
            return True

        if event.checked:
            self._output_size_width.form_control.setEnabled(True)
        else:
            self._output_size_width.update(self.default_params["output_size"][self.Dimension.WIDTH])
            self._output_size_width.form_control.setEnabled(False)

        return True

    def render(self, root):
        return (
            LayoutFactory(LayoutType.HORIZONTAL).create()
            .append(
                LayoutFactory(LayoutType.VERTICAL).create()
                .weight(1)
                .add(
                    Text(root, i18n("window.screens.network.neurons.adaptivemaxpool2d.dimensions.height"))
                    .Font(self._font_caption_title)
                    .Align(Qt.AlignCenter)
                    .Margin(0, LS.rem(.6))
                )
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .align(Qt.AlignmentFlag.AlignCenter)
                    .add(
                        Text(root, i18n("window.screens.network.neurons.adaptivemaxpool2d.labels.output"))
                    )
                    .add(
                        IntegerInput(root, self._output_size_height.value)
                        .Bind(self._output_size_height)
                        .Height(self._input_height)
                    )
                    .append(
                        LayoutFactory(LayoutType.VERTICAL).create()
                        .align(Qt.AlignmentFlag.AlignHCenter)
                        .add(
                            CheckBox(root, self._output_enabled_height.value)
                            .Bind(self._output_enabled_height)
                            .On(
                                Event.Type.Change, self.enable_height,
                                with_target=False,
                                with_event=True
                            )
                        )
                    )
                )
            )
            .append(
                LayoutFactory(LayoutType.VERTICAL).create()
                .weight(1)
                .add(
                    Text(root, i18n("window.screens.network.neurons.adaptivemaxpool2d.dimensions.width"))
                    .Font(self._font_caption_title)
                    .Align(Qt.AlignCenter)
                    .Margin(0, LS.rem(.6))
                )
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .add(
                        Text(root, i18n("window.screens.network.neurons.adaptivemaxpool2d.labels.output"))
                    )
                    .add(
                        IntegerInput(root, self._output_size_width.value)
                        .Bind(self._output_size_width)
                        .Height(self._input_height)
                    )
                    .append(
                        LayoutFactory(LayoutType.VERTICAL).create()
                        .align(Qt.AlignmentFlag.AlignHCenter)
                        .add(
                            CheckBox(root, self._output_enabled_width.value)
                            .Bind(self._output_enabled_width)
                            .On(
                                Event.Type.Change, self.enable_width,
                                with_target=False,
                                with_event=True
                            )
                        )
                    )
                )
            )
        )
