from PyQt5.QtCore import Qt

from lib.gui import LS
from lib.gui.element.font import Font
from lib.gui.element.form import FormInput
from lib.gui.element.form.integer import IntegerInput
from lib.gui.element.text import Text
from lib.gui.layout.factory import LayoutFactory
from lib.gui.layout.type import LayoutType

from app.hooks import i18n
from app.network.extension.replicationpad.bounded import ReplicationPaddingBoundedExtension
from app.network.extension.replicationpad.bounded.params import ReplicationPadBoundedParams
from app.network.extension.replicationpad.bounded.options import ReplicationPadBoundedOptions
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.neuron.strategy import NeuronStrategy


# Main

class BoundedBoundaryStrategy(NeuronStrategy):
    def __init__(self, dependencies):
        super().__init__(dependencies)

        self._padding = FormInput(self.default_params["padding"])

        self._input_height = LS.rem(1.6)
        self._font_caption_title = Font().Size(LS.rem(.8)).Bold().Underline()

    @property
    def params(self):
        return NeuronStrategyParams(
            params=ReplicationPadBoundedParams(
                padding=self._padding.value
            ),
            options=ReplicationPadBoundedOptions()
        )

    @property
    def default_params(self):
        return ReplicationPaddingBoundedExtension.default_params()

    @property
    def default_options(self):
        return ReplicationPaddingBoundedExtension.default_options()

    def load(self, params, options):
        self._padding.update(params["padding"])

    def render(self, root):
        return (
            LayoutFactory(LayoutType.VERTICAL).create()
            .append(
                LayoutFactory(LayoutType.HORIZONTAL).create()
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .weight(2)
                    .add(
                        Text(root, i18n("window.screens.network.extension.replicationpad.bounded.labels.padding"))
                        .Align(Qt.AlignRight | Qt.AlignVCenter)
                    )
                )
                .append(
                    LayoutFactory(LayoutType.VERTICAL).create()
                    .weight(3)
                    .add(
                        IntegerInput(root, self._padding.value)
                        .Bind(self._padding)
                        .Height(self._input_height)
                    )
                )
            )
        )
