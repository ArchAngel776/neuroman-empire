from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QSizePolicy

from lib.gui import LS
from lib.gui.element.form import FormInput
from lib.gui.element.form.check import CheckBox
from lib.gui.element.component.switcher import Switcher
from lib.gui.element.scrollable import Scrollable
from lib.gui.element.text import Text
from lib.gui.event import Event
from lib.gui.layout.factory import LayoutFactory
from lib.gui.layout.type import LayoutType

from app import SCROLLBAR_SIZE
from app.hooks import i18n
from app.network.neuron.zeropad2d import ZeroPadding2d
from app.network.neuron.zeropad2d.params import ZeroPad2dParams
from app.network.neuron.zeropad2d.options import ZeroPad2dOptions
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.neuron.zeropad2d.view import Boundary2dView, Boundary2dSwitcher


# Main

class NeuronBuilderZeroPadding2dStrategy(NeuronStrategy):
    class Watch(str):
        BOUNDARY_SWITCHER = "boundary_2d_switcher"

    def __init__(self, dependencies):
        super().__init__(dependencies)

        self._bounded = FormInput(self.default_options["bounded"])

    @property
    def params(self):
        return NeuronStrategyParams(
            params=ZeroPad2dParams(
                **self.boundary_params.params
            ),
            options=ZeroPad2dOptions(
                bounded=self._bounded.value
            )
        )

    @property
    def default_params(self):
        return ZeroPadding2d.default_params()

    @property
    def default_options(self):
        return ZeroPadding2d.default_options()

    def load(self, params, options):
        self._bounded.update(options["bounded"])

    @property
    def boundary_params(self):
        return self.boundary_switcher_program.params

    @staticmethod
    def value_to_boundary(value):
        return Boundary2dView.BOUNDED if value else Boundary2dView.UNBOUNDED

    def change_boundary(self, event):
        self.make(
            NeuronBuilderZeroPadding2dStrategy.Watch.BOUNDARY_SWITCHER,
            lambda switcher: switcher.change_strategy(self.value_to_boundary(event.checked))
        )
        return True

    @property
    def boundary_switcher_program(self):
        return self.get(NeuronBuilderZeroPadding2dStrategy.Watch.BOUNDARY_SWITCHER).program

    def render(self, root):
        return (
            LayoutFactory(LayoutType.VERTICAL).create()
            .add(
                Scrollable(root)
                .ScrollX(True, size=SCROLLBAR_SIZE)
                .ScrollY(False)
                .Adjust(Scrollable.SizeAdjustPolicy.AdjustToContents)
                .Content(
                    self.watch(
                        NeuronBuilderZeroPadding2dStrategy.Watch.BOUNDARY_SWITCHER,
                        Switcher(
                            root,
                            Boundary2dSwitcher(self.value_to_boundary(self._bounded.value), self.dependencies),
                            LayoutType.VERTICAL
                        )
                        .InnerSizing(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
                        .Payload(self.neuron_payload_provider.provide())
                        .AutoInit()
                    )
                )
            )
            .append(
                LayoutFactory(LayoutType.HORIZONTAL).create()
                .margin_vertical(LS.rem(.8))
                .add(
                    Text(root, i18n("window.screens.network.neurons.zeropad2d.labels.bounded"))
                )
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .align(Qt.AlignLeft)
                    .margin_horizontal(LS.rem(.2))
                    .add(
                        CheckBox(root, self._bounded.value)
                        .Bind(self._bounded)
                        .On(
                            Event.Type.Change, self.change_boundary,
                            with_target=False,
                            with_event=True
                        )
                    )
                )
            )
        )
