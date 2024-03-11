from lib.gui.event import Event


# Main

class RadioButtonToggled(Event):
    def __init__(self, value):
        super().__init__(Event.Type.Toggled)
        self._value = value

    @property
    def value(self):
        return self._value
