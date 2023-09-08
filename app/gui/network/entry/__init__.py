from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor

from lib.gui import LS
from lib.gui.element.button import Button
from lib.gui.element.font import Font
from lib.gui.element.switcher.strategy import SwitcherStrategy
from lib.gui.element.text import Text
from lib.gui.event import Event
from lib.gui.layout.factory import LayoutFactory
from lib.gui.layout.type import LayoutType

from app.hooks import i18n


# Main

class NeuronOperationEntryStrategy(SwitcherStrategy):
    def __init__(self, dependencies):
        super().__init__(dependencies)

        self._form_title_font = Font().Size(LS.rem(1.2)).Bold().Underline()
        self._form_description_font = Font().Size(LS.rem(.9))

        self._button_cursor = QCursor(Qt.PointingHandCursor)

    @property
    def params(self):
        return {}

    def action_creation(self):
        action = self.dependencies["action_creation"]
        return action() or True

    def render(self, root):
        return (
            LayoutFactory(LayoutType.VERTICAL).create()
            .weight(1)
            .append(
                LayoutFactory(LayoutType.VERTICAL).create()
                .weight(1)
                .add(
                    Text(root, i18n("window.screens.network.entry.title"))
                    .Font(self._form_title_font)
                )
                .stretch()
            )
            .append(
                LayoutFactory(LayoutType.VERTICAL).create()
                .weight(4)
                .append(
                    LayoutFactory(LayoutType.HORIZONTAL).create()
                    .add(
                        Text(root, i18n("window.screens.network.entry.description.0"))
                        .Font(self._form_description_font)
                        .Wrap()
                    )
                )
                .append(
                    LayoutFactory(LayoutType.HORIZONTAL).create()
                    .add(
                        Text(root, i18n("window.screens.network.entry.description.1"))
                        .Font(self._form_description_font)
                        .Wrap()
                    )
                )
                .append(
                    LayoutFactory(LayoutType.HORIZONTAL).create()
                    .add(
                        Text(root, i18n("window.screens.network.entry.description.2"))
                        .Font(self._form_description_font)
                        .Wrap()
                    )
                )
            )
            .append(
                LayoutFactory(LayoutType.VERTICAL).create()
                .weight(1)
                .stretch()
                .add(
                    Button(root, i18n("window.screens.network.entry.buttons.add"))
                    .Height(LS.rem(2))
                    .Cursor(self._button_cursor)
                    .On(
                        Event.Type.Click, self.action_creation,
                        with_target=False,
                        with_event=False
                    )
                )
            )
        )
