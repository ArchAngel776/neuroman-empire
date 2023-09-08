from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor

from lib.gui import LS
from lib.gui.element.button import Button
from lib.gui.element.font import Font
from lib.gui.element.image import Image
from lib.gui.element.text import Text
from lib.gui.event import Event
from lib.gui.layout.factory import LayoutFactory
from lib.gui.layout.type import LayoutType
from lib.gui.screen import Screen

from app.hooks import home_image, i18n
from app.network import Network


# Main

class HomeScreen(Screen):
    def __init__(self, root):
        super().__init__(root)

        self._title_font = Font().Size(LS.rem(1.6)).Bold()
        self._caption_font = Font().Size(LS.rem(1))

        self._button_cursor = QCursor(Qt.PointingHandCursor)

    def create_new_network(self):
        self.root.create_network(Network([]))
        return True

    def render(self):
        return (
            LayoutFactory(LayoutType.VERTICAL).create()
            .append(
                LayoutFactory(LayoutType.VERTICAL).create()
                .weight(2)
                .align(Qt.AlignVCenter)
                .margin(horizontal=LS.rem(.8), vertical=LS.rem(1.2))
                .add(
                    Image(self.root, "assets/ai.png")
                    .Align(Qt.AlignHCenter)
                    .On(
                        Event.Type.Resize, home_image,
                        with_target=True,
                        with_event=False
                    )
                )
                .add(
                    Text(self.root, i18n("window.screens.home.title"))
                    .Font(self._title_font)
                    .Align(Qt.AlignHCenter)
                    .Margin(LS.rem(.8), LS.rem(.8))
                )
                .add(
                    Text(self.root, i18n("window.screens.home.description"))
                    .Font(self._caption_font)
                    .Align(Qt.AlignHCenter)
                    .Wrap()
                )
            )
            .append(
                LayoutFactory(LayoutType.VERTICAL).create()
                .weight(1)
                .margin(horizontal=LS.rem(.2), vertical=LS.rem(.2))
                .add(
                    Button(self.root, i18n("window.screens.home.menu.create"))
                    .Height(LS.rem(2.4))
                    .Cursor(self._button_cursor)
                    .On(
                        Event.Type.Click, self.create_new_network,
                        with_target=False,
                        with_event=False
                    )
                )
            )
        )
