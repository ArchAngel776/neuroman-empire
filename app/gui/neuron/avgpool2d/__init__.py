from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSizePolicy

from lib.gui import LS
from lib.gui.element.form import FormInput
from lib.gui.element.form.check import CheckBox
from lib.gui.element.form.integer import IntegerInput
from lib.gui.element.scrollable import Scrollable
from lib.gui.element.component.switcher import Switcher
from lib.gui.element.text import Text
from lib.gui.event import Event
from lib.gui.layout.type import LayoutType
from lib.gui.layout.factory import LayoutFactory

from app import SCROLLBAR_SIZE
from app.hooks import i18n
from app.network.neuron.avgpool2d import AveragePooling2d
from app.network.neuron.avgpool2d.params import AvgPool2dParams
from app.network.neuron.avgpool2d.options import AvgPool2dOptions
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.neuron.avgpool2d.view import Dimension2dView, Dimension2dSwitcher


# Main

class NeuronBuilderAveragePooling2dStrategy(NeuronStrategy):
    class Watch(str):
        DIMENSION_SWITCHER = "dimension_2d_switcher"

    def __init__(self, dependencies):
        super().__init__(dependencies)

        self._ceil_mode = FormInput(self.default_params["ceil_mode"])
        self._count_include_pad = FormInput(self.default_params["count_include_pad"])
        self._divisor_override = FormInput(self.default_params["divisor_override"])

        self._reflection = FormInput(self.default_options["square"])
        self._divisor_enabled = FormInput(self.default_options["divisor_enabled"])

        self._input_height = LS.rem(1.6)

    @property
    def params(self):
        return NeuronStrategyParams(
            params=AvgPool2dParams(
                **self.dimension_params.params,
                ceil_mode=self._ceil_mode.value,
                count_include_pad=self._count_include_pad.value,
                divisor_override=self._divisor_override.value
            ),
            options=AvgPool2dOptions(
                square=self._reflection.value,
                divisor_enabled=self._divisor_enabled.value
            )
        )

    @property
    def default_params(self):
        return AveragePooling2d.default_params()

    @property
    def default_options(self):
        return AveragePooling2d.default_options()

    def load(self, params, options):
        self._reflection.update(options["square"])

        self._ceil_mode.update(params["ceil_mode"])
        self._count_include_pad.update(params["count_include_pad"])

        self._divisor_enabled.update(options["divisor_enabled"])
        self._divisor_override.update(params["divisor_override"])

    @property
    def dimension_params(self):
        return self.dimension_switcher_program.params

    @staticmethod
    def value_to_dimension(value):
        return Dimension2dView.SINGLE if value else Dimension2dView.DOUBLE

    def change_dimension(self, event):
        self.make(
            NeuronBuilderAveragePooling2dStrategy.Watch.DIMENSION_SWITCHER,
            lambda switcher: switcher.change_strategy(self.value_to_dimension(event.checked))
        )
        return True

    @property
    def dimension_switcher_program(self):
        return self.get(NeuronBuilderAveragePooling2dStrategy.Watch.DIMENSION_SWITCHER).program

    def toggle_divisor(self, event):
        if not event.checked == self._divisor_enabled.value:
            self.update_view()
        return True

    def update_view(self):
        dimension = self.dimension_params
        super().update_view()
        self.dimension_switcher_program.current_strategy.read(dimension.params, dimension.options)

    def render(self, root):
        return (
            LayoutFactory(LayoutType.VERTICAL).create()
            .append(
                LayoutFactory(LayoutType.HORIZONTAL).create()
                .margin_vertical(LS.rem(.8))
                .add(
                    Text(root, i18n("window.screens.network.neurons.avgpool2d.labels.square"))
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
                        NeuronBuilderAveragePooling2dStrategy.Watch.DIMENSION_SWITCHER,
                        Switcher(
                            root,
                            Dimension2dSwitcher(self.value_to_dimension(self._reflection.value), self.dependencies),
                            LayoutType.VERTICAL
                        )
                        .InnerSizing(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
                        .Payload(self.neuron_payload_provider.provide())
                    )
                )
            )
            .append(
                LayoutFactory(LayoutType.HORIZONTAL).create()
                .margin_vertical(LS.rem(.8))
                .add(
                    Text(root, i18n("window.screens.network.neurons.avgpool2d.labels.ceil_mode"))
                )
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .align(Qt.AlignLeft)
                    .margin_horizontal(LS.rem(.2))
                    .add(
                        CheckBox(root, self._ceil_mode.value)
                        .Bind(self._ceil_mode)
                    )
                )
            )
            .append(
                LayoutFactory(LayoutType.HORIZONTAL).create()
                .margin_vertical(LS.rem(.8))
                .add(
                    Text(root, i18n("window.screens.network.neurons.avgpool2d.labels.count_include_pad"))
                )
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .align(Qt.AlignLeft)
                    .margin_horizontal(LS.rem(.2))
                    .add(
                        CheckBox(root, self._count_include_pad.value)
                        .Bind(self._count_include_pad)
                    )
                )
            )
            .append(
                LayoutFactory(LayoutType.HORIZONTAL).create()
                .margin_vertical(LS.rem(.8))
                .add(
                    Text(root, i18n("window.screens.network.neurons.avgpool2d.labels.divisor_enabled"))
                )
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .align(Qt.AlignLeft)
                    .margin_horizontal(LS.rem(.2))
                    .add(
                        CheckBox(root, self._divisor_enabled.value)
                        .Bind(self._divisor_enabled)
                        .On(
                            Event.Type.Change, self.toggle_divisor,
                            with_target=False,
                            with_event=True
                        )
                    )
                )
            )
            .append(
                LayoutFactory(LayoutType.HORIZONTAL).create()
                .margin_vertical(LS.rem(.8))
                .add(
                    Text(root, i18n("window.screens.network.neurons.avgpool2d.labels.divisor_override"))
                )
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .align(Qt.AlignLeft)
                    .margin_horizontal(LS.rem(.2))
                    .add(
                        IntegerInput(root, self._divisor_override.value)
                        .Bind(self._divisor_override)
                    )
                ),
                allow=self._divisor_enabled.value
            )
        )
