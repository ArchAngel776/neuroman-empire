from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSizePolicy

from lib.gui import LS
from lib.gui.element.form import FormInput
from lib.gui.element.form.check import CheckBox
from lib.gui.element.scrollable import Scrollable
from lib.gui.element.component.switcher import Switcher
from lib.gui.element.text import Text
from lib.gui.event import Event
from lib.gui.layout.factory import LayoutFactory
from lib.gui.layout.type import LayoutType

from app import SCROLLBAR_SIZE
from app.hooks import i18n
from app.network.neuron.adaptiveavgpool3d import AdaptiveAveragePooling3d
from app.network.neuron.adaptiveavgpool3d.params import AdaptiveAvgPool3dParams
from app.network.neuron.adaptiveavgpool3d.options import AdaptiveAvgPool3dOptions
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.neuron.adaptiveavgpool3d.view import Dimension3dView, Dimension3dSwitcher


# Main

class NeuronBuilderAdaptiveAveragePooling3dStrategy(NeuronStrategy):
    class Watch(str):
        DIMENSION_SWITCHER = "dimension_3d_switcher"

    def __init__(self, dependencies):
        super().__init__(dependencies)

        self._reflection = FormInput(self.default_options["cube"])
        self._input_height = LS.rem(1.6)

    @property
    def params(self):
        return NeuronStrategyParams(
            params=AdaptiveAvgPool3dParams(
                **self.dimension_params.params
            ),
            options=AdaptiveAvgPool3dOptions(
                cube=self._reflection.value,
                **self.dimension_params.options
            )
        )

    @property
    def default_params(self):
        return AdaptiveAveragePooling3d.default_params()

    @property
    def default_options(self):
        return AdaptiveAveragePooling3d.default_options()

    def load(self, params, options):
        self._reflection.update(options["cube"])

    @property
    def dimension_params(self):
        return self.dimension_switcher_program.params

    @staticmethod
    def value_to_dimension(value):
        return Dimension3dView.SINGLE if value else Dimension3dView.TRIPLE

    def change_dimension(self, event):
        self.make(
            NeuronBuilderAdaptiveAveragePooling3dStrategy.Watch.DIMENSION_SWITCHER,
            lambda switcher: switcher.change_strategy(self.value_to_dimension(event.checked))
        )
        return True

    @property
    def dimension_switcher_program(self):
        return self.get(NeuronBuilderAdaptiveAveragePooling3dStrategy.Watch.DIMENSION_SWITCHER).program

    def render(self, root):
        return (
            LayoutFactory(LayoutType.VERTICAL).create()
            .append(
                LayoutFactory(LayoutType.HORIZONTAL).create()
                .margin_vertical(LS.rem(.8))
                .add(
                    Text(root, i18n("window.screens.network.neurons.adaptiveavgpool3d.labels.cube"))
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
                        NeuronBuilderAdaptiveAveragePooling3dStrategy.Watch.DIMENSION_SWITCHER,
                        Switcher(
                            root,
                            Dimension3dSwitcher(self.value_to_dimension(self._reflection.value), self.dependencies),
                            LayoutType.VERTICAL
                        )
                        .InnerSizing(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
                        .Payload(self.neuron_payload_provider.provide())
                    )
                )
            )
        )
