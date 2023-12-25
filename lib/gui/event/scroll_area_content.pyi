from lib.gui.element import Element
from lib.gui.event import Event


# Main

class ScrollAreaContent(Event):
    _content_widget: Element

    def __init__(self, content_widget: Element) -> None: ...

    @property
    def content_widget(self) -> Element: ...
