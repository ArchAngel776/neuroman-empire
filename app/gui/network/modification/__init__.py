from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QSizePolicy

from lib.gui import LS
from lib.gui.element.button import Button
from lib.gui.element.font import Font
from lib.gui.element.scrollable import Scrollable
from lib.gui.element.component.switcher import Switcher
from lib.gui.element.component.switcher.strategy import SwitcherStrategy
from lib.gui.element.text import Text
from lib.gui.event import Event
from lib.gui.layout.factory import LayoutFactory
from lib.gui.layout.type import LayoutType

from app import SCROLLBAR_SIZE
from app.hooks import i18n
from app.gui.neuron import NeuronBuilderSwitcher
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.network.modification.params import NeuronModificationParams


# Main

class NeuronOperationModificationStrategy(SwitcherStrategy):
    NEURON_SWITCHER_ELEMENT = "neuron_switcher_element"

    def __init__(self, dependencies):
        super().__init__(dependencies)

        self._form_title_font = Font().Size(LS.rem(1.2)).Bold().Underline()
        self._form_label_font = Font().Size(LS.rem(.8))
        self._form_value_font = Font().Size(LS.rem(.8)).Bold()

        self._button_cursor = QCursor(Qt.PointingHandCursor)

    def params(self):
        return NeuronModificationParams(
            name=self.neuron.name,
            params=self.neuron.params
        )

    @property
    def neuron(self):
        return self.dependencies["neuron"]

    @property
    def neuron_type(self):
        return self.neuron.type()

    @property
    def remove(self):
        return self.dependencies["remove"]

    @property
    def action_entry(self):
        return self.dependencies["action_entry"]

    def modify_neuron(self):
        return True

    def remove_neuron(self):
        self.remove(self.neuron)
        self.action_entry()
        return True

    def cancel(self):
        self.action_entry()
        return True

    def init_switcher(self):
        self.switcher_program.strategy[self.neuron_type].load(self.neuron.params, self.neuron.options)
        return True

    @property
    def switcher_program(self):
        return self.get(NeuronOperationModificationStrategy.NEURON_SWITCHER_ELEMENT).program

    @property
    def neuron_dependencies(self):
        return NeuronBuilderDependencies(
            network=self.dependencies["network"]
        )

    def render(self, root):
        return (
            LayoutFactory(LayoutType.VERTICAL).create()
            .weight(1)
            .add(
                Text(root, i18n("window.screens.network.modification.title"))
                .Font(self._form_title_font)
            )
            .append(
                LayoutFactory(LayoutType.VERTICAL).create()
                .weight(1)
                .append(
                    LayoutFactory(LayoutType.HORIZONTAL).create()
                    .add(
                        Text(root, i18n("window.screens.network.modification.labels.name"))
                        .Font(self._form_label_font)
                    )
                    .append(
                        LayoutFactory(LayoutType.VERTICAL).create()
                        .add(
                            Text(root, self.neuron.name)
                            .Font(self._form_value_font)
                        )
                    )
                )
                .append(
                    LayoutFactory(LayoutType.HORIZONTAL).create()
                    .add(
                        Text(root, i18n("window.screens.network.modification.labels.type"))
                        .Font(self._form_label_font)
                    )
                    .append(
                        LayoutFactory(LayoutType.VERTICAL).create()
                        .add(
                            Text(root, self.neuron.title())
                            .Font(self._form_value_font)
                        )
                    )
                )
            )
            .append(
                LayoutFactory(LayoutType.VERTICAL).create()
                .weight(4)
                .add(
                    Scrollable(root)
                    .ScrollX(False)
                    .ScrollY(True, size=SCROLLBAR_SIZE)
                    .Content(
                        self.watch(
                            NeuronOperationModificationStrategy.NEURON_SWITCHER_ELEMENT,
                            Switcher(
                                root,
                                NeuronBuilderSwitcher(self.neuron_type, self.neuron_dependencies),
                                LayoutType.VERTICAL
                            )
                            .InnerSizing(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
                            .On(
                                Event.Type.Show, self.init_switcher,
                                with_target=False,
                                with_event=False
                            )
                            .AutoInit()
                        )
                    )
                )
            )
            .append(
                LayoutFactory(LayoutType.VERTICAL).create()
                .append(
                    LayoutFactory(LayoutType.HORIZONTAL).create()
                    .append(
                        LayoutFactory(LayoutType.VERTICAL).create()
                        .add(
                            Button(root, i18n("window.screens.network.modification.buttons.modify"))
                            .Height(LS.rem(2))
                            .Cursor(self._button_cursor)
                            .On(
                                Event.Type.Click, self.modify_neuron,
                                with_target=False,
                                with_event=False
                            )
                        )
                    )
                    .append(
                        LayoutFactory(LayoutType.VERTICAL).create()
                        .add(
                            Button(root, i18n("window.screens.network.modification.buttons.remove"))
                            .Height(LS.rem(2))
                            .Cursor(self._button_cursor)
                            .On(
                                Event.Type.Click, self.remove_neuron,
                                with_target=False,
                                with_event=False
                            )
                        )
                    )
                )
                .append(
                    LayoutFactory(LayoutType.HORIZONTAL).create()
                    .append(
                        LayoutFactory(LayoutType.VERTICAL).create()
                        .add(
                            Button(root, i18n("window.screens.network.modification.buttons.cancel"))
                            .Height(LS.rem(2))
                            .Cursor(self._button_cursor)
                            .On(
                                Event.Type.Click, self.cancel,
                                with_target=False,
                                with_event=False
                            )
                        )
                    )
                )
            )
        )
