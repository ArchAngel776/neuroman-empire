from lib.gui.event import Event


# Main

class SelectBoxSelectedEvent(Event):
    def __init__(self, title, data):
        super().__init__(Event.Type.Select)
        self._title = title
        self._data = data

    @property
    def title(self):
        return self._title

    @property
    def data(self):
        return self._data
