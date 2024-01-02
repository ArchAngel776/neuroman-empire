from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSizePolicy

from lib.gui import LS
from lib.gui.element.form import FormInput
from lib.gui.element.form.check import CheckBox
from lib.gui.element.scrollable import Scrollable
from lib.gui.element.component.switcher import Switcher
from lib.gui.element.text import Text
from lib.gui.event import Event
from lib.gui.layout.type import LayoutType
from lib.gui.layout.factory import LayoutFactory

from app import SCROLLBAR_SIZE
from app.hooks import i18n
from app.network.neuron.maxpool2d import MaxPooling2d
from app.network.neuron.maxpool2d.params import MaxPool2dParams
from app.network.neuron.maxpool2d.options import MaxPool2dOptions
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.neuron.maxpool2d.view import Dimension2dView, Dimension2dSwitcher


# Main

class NeuronBuilderMaxPooling2dStrategy(NeuronStrategy):
    class Watch(str):
        DIMENSION_SWITCHER = "dimension_2d_switcher"

    def __init__(self, dependencies):
        super().__init__(dependencies)

        self._return_indices = FormInput(self.default_params["return_indices"])
        self._ceil_mode = FormInput(self.default_params["ceil_mode"])

        self._reflection = FormInput(self.default_options["square"])
        self._input_height = LS.rem(1.6)

    @property
    def params(self):
        return NeuronStrategyParams(
            params=MaxPool2dParams(
                **self.dimension_params.params,
                return_indices=self._return_indices.value,
                ceil_mode=self._ceil_mode.value,
            ),
            options=MaxPool2dOptions(
                square=self._reflection.value
            )
        )

    @property
    def default_params(self):
        return MaxPooling2d.default_params()

    @property
    def default_options(self):
        return MaxPooling2d.default_options()

    def load(self, params, options):
        self._reflection.update(options["square"])
        self.dimension_switcher_program.current_strategy.load(params, options)

        self._return_indices.update(params["return_indices"])
        self._ceil_mode.update(params["ceil_mode"])

    @property
    def dimension_params(self):
        return self.dimension_switcher_program.params

    def change_dimension(self, event):
        key = Dimension2dView.SINGLE if event.checked else Dimension2dView.DOUBLE
        self.make(
            NeuronBuilderMaxPooling2dStrategy.Watch.DIMENSION_SWITCHER,
            lambda switcher: switcher.change_strategy(key)
        )
        return True

    @property
    def dimension_switcher_program(self):
        return self.get(NeuronBuilderMaxPooling2dStrategy.Watch.DIMENSION_SWITCHER).program

    def render(self, root):
        return (
            LayoutFactory(LayoutType.VERTICAL).create()
            .append(
                LayoutFactory(LayoutType.HORIZONTAL).create()
                .margin_vertical(LS.rem(.8))
                .add(
                    Text(root, i18n("window.screens.network.neurons.maxpool2d.labels.square"))
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
                        NeuronBuilderMaxPooling2dStrategy.Watch.DIMENSION_SWITCHER,
                        Switcher(
                            root,
                            Dimension2dSwitcher(Dimension2dView.DOUBLE, self.dependencies),
                            LayoutType.VERTICAL
                        )
                        .InnerSizing(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
                    )
                )
            )
            .append(
                LayoutFactory(LayoutType.HORIZONTAL).create()
                .add(
                    Text(root, i18n("window.screens.network.neurons.maxpool2d.labels.return_indices"))
                )
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .add(
                        CheckBox(root, self._return_indices.value)
                        .Bind(self._return_indices)
                        .Height(self._input_height)
                    )
                )
            )
            .append(
                LayoutFactory(LayoutType.HORIZONTAL).create()
                .margin_vertical(LS.rem(.8))
                .add(
                    Text(root, i18n("window.screens.network.neurons.maxpool2d.labels.ceil_mode"))
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
