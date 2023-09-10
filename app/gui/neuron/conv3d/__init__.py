from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSizePolicy

from lib.gui import LS
from lib.gui.element.form import FormInput
from lib.gui.element.form.check import CheckBox
from lib.gui.element.form.integer import IntegerInput
from lib.gui.element.scrollable import Scrollable
from lib.gui.element.switcher import Switcher
from lib.gui.element.text import Text
from lib.gui.event import Event
from lib.gui.layout.factory import LayoutFactory
from lib.gui.layout.type import LayoutType

from app import SCROLLBAR_SIZE
from app.hooks import i18n
from app.network.neuron.conv3d import Convolution3d
from app.network.neuron.conv3d.params import Conv3dParams
from app.network.neuron.conv3d.options import Conv3dOptions
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.neuron.conv3d.view import Dimension3dView, Dimension3dSwitcher


# Main

class NeuronBuilderConvolution3dStrategy(NeuronStrategy):
    DIMENSION_SWITCHER = "dimension_3d_switcher"

    def __init__(self, dependencies):
        super().__init__(dependencies)

        self._input_channels = FormInput(self.default_params["in_channels"])
        self._output_channels = FormInput(self.default_params["out_channels"])
        self._groups = FormInput(self.default_params["groups"])
        self._bias = FormInput(self.default_params["bias"])

        self._reflection = FormInput(self.default_options["cube"])
        self._input_height = LS.rem(1.6)

    @property
    def params(self):
        return NeuronStrategyParams(
            params=Conv3dParams(
                in_channels=self._input_channels.value,
                out_channels=self._output_channels.value,
                **self.dimension_params.params,
                groups=self._groups.value,
                bias=self._bias.value,
            ),
            options=Conv3dOptions(
                cube=self._reflection.value
            )
        )

    @property
    def default_params(self):
        return Convolution3d.default_params()

    @property
    def default_options(self):
        return Convolution3d.default_options()

    @property
    def dimension_params(self):
        return self.dimension_switcher_program.params

    @property
    def init_param(self):
        return self.dependencies["init_param"]

    @property
    def init_option(self):
        return self.dependencies["init_option"]

    def change_dimension(self, event):
        key = Dimension3dView.SINGLE if event.checked else Dimension3dView.TRIPLE
        self.update(
            NeuronBuilderConvolution3dStrategy.DIMENSION_SWITCHER,
            lambda switcher: switcher.change_strategy(key)
        )
        return True

    @staticmethod
    def adjust_dimension_params_area(switcher):
        scrollable = switcher.parent().parent()
        scrollable.setFixedHeight(switcher.height() + SCROLLBAR_SIZE)

        return True

    @property
    def dimension_switcher_program(self):
        return self.get(NeuronBuilderConvolution3dStrategy.DIMENSION_SWITCHER).program

    def render(self, root):
        return (
            LayoutFactory(LayoutType.VERTICAL).create()
            .append(
                LayoutFactory(LayoutType.VERTICAL).create()
                .append(
                    LayoutFactory(LayoutType.HORIZONTAL).create()
                    .add(
                        Text(root, i18n("window.screens.network.neurons.conv3d.labels.input"))
                    )
                    .append(
                        LayoutFactory(LayoutType.VERTICAL).create()
                        .add(
                            IntegerInput(root, self._input_channels.value)
                            .Bind(self._input_channels)
                            .Height(self._input_height)
                        )
                    )
                )
                .append(
                    LayoutFactory(LayoutType.HORIZONTAL).create()
                    .add(
                        Text(root, i18n("window.screens.network.neurons.conv3d.labels.output"))
                    )
                    .append(
                        LayoutFactory(LayoutType.VERTICAL).create()
                        .add(
                            IntegerInput(root, self._output_channels.value)
                            .Bind(self._output_channels)
                            .Height(self._input_height)
                        )
                    )
                )
            )
            .append(
                LayoutFactory(LayoutType.HORIZONTAL).create()
                .margin_vertical(LS.rem(.8))
                .add(
                    Text(root, i18n("window.screens.network.neurons.conv3d.labels.cube"))
                )
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .align(Qt.AlignLeft)
                    .margin_horizontal(LS.rem(.2))
                    .add(
                        CheckBox(root, self._reflection.value)
                        .Bind(self._reflection)
                        .On(
                            Event.Type.Change, self.change_dimension,
                            with_target=False,
                            with_event=True
                        )
                    )
                )
            )
            .add(
                Scrollable(root)
                .ScrollX(True, size=SCROLLBAR_SIZE)
                .ScrollY(False)
                .Adjust(Scrollable.SizeAdjustPolicy.AdjustToContents)
                .Content(
                    self.watch(
                        NeuronBuilderConvolution3dStrategy.DIMENSION_SWITCHER,
                        Switcher(
                            root,
                            Dimension3dSwitcher(Dimension3dView.TRIPLE, self.dependencies),
                            LayoutType.VERTICAL
                        )
                        .InnerSizing(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
                        .On(
                            Event.Type.Resize, self.adjust_dimension_params_area,
                            with_target=True,
                            with_event=False
                        )
                    )
                )
            )
            .append(
                LayoutFactory(LayoutType.HORIZONTAL).create()
                .add(
                    Text(root, i18n("window.screens.network.neurons.conv3d.labels.groups"))
                )
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .add(
                        IntegerInput(root, self._groups.value)
                        .Bind(self._groups)
                        .Height(self._input_height)
                    )
                )
            )
            .append(
                LayoutFactory(LayoutType.HORIZONTAL).create()
                .margin_vertical(LS.rem(.8))
                .add(
                    Text(root, i18n("window.screens.network.neurons.conv3d.labels.bias"))
                )
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .align(Qt.AlignLeft)
                    .margin_horizontal(LS.rem(.2))
                    .add(
                        CheckBox(root, self._bias.value)
                        .Bind(self._bias)
                    )
                )
            )
        )
