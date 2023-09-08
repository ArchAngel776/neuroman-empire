from PyQt5.QtGui import QIcon

from lib.gui.element.image import Image

from app.i18n.message import I18NMessage


# Modules

def main_icon() -> QIcon: ...


def i18n(xpath: str, lang: str = None) -> I18NMessage: ...


def home_image(image: Image) -> bool: ...
