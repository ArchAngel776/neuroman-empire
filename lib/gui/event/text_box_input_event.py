from lib.gui.event import Event


# Main

class TextBoxInputEvent(Event):
    def __init__(self, text):
        super().__init__(Event.Type.Input)
        self._text = text

    @property
    def text(self):
        return self._text
