from lib.gui.event import Event


# Main

class FormControlValidated(Event):
    def __init__(self, valid, message):
        super().__init__(Event.Type.Validated)
        self._valid = valid
        self._message = message

    @property
    def valid(self):
        return self._valid

    @property
    def message(self):
        return self._message
