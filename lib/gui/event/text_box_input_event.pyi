from lib.gui.event import Event


# Main

class TextBoxInputEvent(Event):
    _text: str

    def __init__(self, text: str) -> None: ...

    @property
    def text(self) -> str: ...
