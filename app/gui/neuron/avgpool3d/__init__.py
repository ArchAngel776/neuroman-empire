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
from lib.gui.layout.factory import LayoutFactory
from lib.gui.layout.type import LayoutType

from app import SCROLLBAR_SIZE
from app.hooks import i18n
from app.network.neuron.avgpool3d import AveragePooling3d
from app.network.neuron.avgpool3d.params import AvgPool3dParams
from app.network.neuron.avgpool3d.options import AvgPool3dOptions
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.neuron.avgpool3d.view import Dimension3dView, Dimension3dSwitcher


# Main

class NeuronBuilderAveragePooling3dStrategy(NeuronStrategy):
    class Watch(str):
        DIMENSION_SWITCHER = "dimension_3d_switcher"

    def __init__(self, dependencies):
        super().__init__(dependencies)

        self._ceil_mode = FormInput(self.default_params["ceil_mode"])
        self._count_include_pad = FormInput(self.default_params["count_include_pad"])
        self._divisor_override = FormInput(self.default_params["divisor_override"])

        self._reflection = FormInput(self.default_options["cube"])
        self._divisor_enabled = FormInput(self.default_options["divisor_enabled"])

        self._input_height = LS.rem(1.6)

    @property
    def params(self):
        return NeuronStrategyParams(
            params=AvgPool3dParams(
                **self.dimension_params.params,
                ceil_mode=self._ceil_mode.value,
                count_include_pad=self._count_include_pad.value,
                divisor_override=self._divisor_override.value
            ),
            options=AvgPool3dOptions(
                cube=self._reflection.value,
                divisor_enabled=self._divisor_enabled.value
            )
        )

    @property
    def default_params(self):
        return AveragePooling3d.default_params()

    @property
    def default_options(self):
        return AveragePooling3d.default_options()

    def load(self, params, options):
        self._reflection.update(options["cube"])
        self.dimension_switcher_program.current_strategy.load(params, options)

        self._ceil_mode.update(params["ceil_mode"])
        self._count_include_pad.update(params["count_include_pad"])

        self._divisor_enabled.update(options["divisor_enabled"])
        self._divisor_override.update(params["divisor_override"])

    @property
    def dimension_params(self):
        return self.dimension_switcher_program.params

    def change_dimension(self, event):
        key = Dimension3dView.SINGLE if event.checked else Dimension3dView.TRIPLE
        self.make(
            NeuronBuilderAveragePooling3dStrategy.Watch.DIMENSION_SWITCHER,
            lambda switcher: switcher.change_strategy(key)
        )
        return True

    @property
    def dimension_switcher_program(self):
        return self.get(NeuronBuilderAveragePooling3dStrategy.Watch.DIMENSION_SWITCHER).program

    def toggle_divisor(self, event):
        if not event.checked == self._divisor_enabled.value:
            self.update_view()
        return True

    def update_view(self):
        dimension = self.dimension_params
        super().update_view()
        self.dimension_switcher_program.current_strategy.load(dimension.params, dimension.options)

    def render(self, root):
        return (
            LayoutFactory(LayoutType.VERTICAL).create()
            .append(
                LayoutFactory(LayoutType.HORIZONTAL).create()
                .margin_vertical(LS.rem(.8))
                .add(
                    Text(root, i18n("window.screens.network.neurons.maxpool3d.labels.cube"))
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
                        NeuronBuilderAveragePooling3dStrategy.Watch.DIMENSION_SWITCHER,
                        Switcher(
                            root,
                            Dimension3dSwitcher(Dimension3dView.TRIPLE, self.dependencies),
                            LayoutType.VERTICAL
                        )
                        .InnerSizing(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
                    )
                )
            )
            .append(
                LayoutFactory(LayoutType.HORIZONTAL).create()
                .margin_vertical(LS.rem(.8))
                .add(
                    Text(root, i18n("window.screens.network.neurons.maxpool3d.labels.ceil_mode"))
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
                    Text(root, i18n("window.screens.network.neurons.avgpool3d.labels.count_include_pad"))
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
                    Text(root, i18n("window.screens.network.neurons.avgpool3d.labels.divisor_enabled"))
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
                    Text(root, i18n("window.screens.network.neurons.avgpool3d.labels.divisor_override"))
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
