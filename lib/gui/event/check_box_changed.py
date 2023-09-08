from lib.gui.event import Event


# Main

class CheckBoxChangedEvent(Event):
    def __init__(self, checked):
        super().__init__(Event.Type.Change)
        self._checked = checked

    @property
    def checked(self):
        return self._checked
