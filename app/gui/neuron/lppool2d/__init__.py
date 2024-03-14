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
from app.network.neuron.lppool2d import LocalPooling2d
from app.network.neuron.lppool2d.params import LPPool2dParams
from app.network.neuron.lppool2d.options import LPPool2dOptions
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.neuron.lppool2d.view import Dimension2dView, Dimension2dSwitcher


# Main

class NeuronBuilderLocalPooling2dStrategy(NeuronStrategy):
    class Watch(str):
        DIMENSION_SWITCHER = "dimension_2d_switcher"

    def __init__(self, dependencies):
        super().__init__(dependencies)

        self._power = FormInput(self.default_params["power"])
        self._ceil_mode = FormInput(self.default_params["ceil_mode"])

        self._reflection = FormInput(self.default_options["square"])
        self._input_height = LS.rem(1.6)

    @property
    def params(self):
        return NeuronStrategyParams(
            params=LPPool2dParams(
                power=self._power.value,
                **self.dimension_params.params,
                ceil_mode=self._ceil_mode.value,
            ),
            options=LPPool2dOptions(
                square=self._reflection.value
            )
        )

    @property
    def default_params(self):
        return LocalPooling2d.default_params()

    @property
    def default_options(self):
        return LocalPooling2d.default_options()

    def load(self, params, options):
        self._power.update(params["power"])

        self._reflection.update(options["square"])

        self._ceil_mode.update(params["ceil_mode"])

    @property
    def dimension_params(self):
        return self.dimension_switcher_program.params

    @staticmethod
    def value_to_dimension(value):
        return Dimension2dView.SINGLE if value else Dimension2dView.DOUBLE

    def change_dimension(self, event):
        self.make(
            NeuronBuilderLocalPooling2dStrategy.Watch.DIMENSION_SWITCHER,
            lambda switcher: switcher.change_strategy(self.value_to_dimension(event.checked))
        )
        return True

    @property
    def dimension_switcher_program(self):
        return self.get(NeuronBuilderLocalPooling2dStrategy.Watch.DIMENSION_SWITCHER).program

    def render(self, root):
        return (
            LayoutFactory(LayoutType.VERTICAL).create()
            .append(
                LayoutFactory(LayoutType.HORIZONTAL).create()
                .margin_vertical(LS.rem(.8))
                .add(
                    Text(root, i18n("window.screens.network.neurons.lppool2d.labels.power"))
                )
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .weight(1)
                    .align(Qt.AlignLeft)
                    .margin_horizontal(LS.rem(.2))
                    .add(
                        IntegerInput(root, self._power.value)
                        .Bind(self._power)
                        .Height(self._input_height)
                    )
                )
            )
            .append(
                LayoutFactory(LayoutType.HORIZONTAL).create()
                .margin_vertical(LS.rem(.8))
                .add(
                    Text(root, i18n("window.screens.network.neurons.lppool2d.labels.square"))
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
                        NeuronBuilderLocalPooling2dStrategy.Watch.DIMENSION_SWITCHER,
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
                    Text(root, i18n("window.screens.network.neurons.lppool2d.labels.ceil_mode"))
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
        )