from lib.gui.event import Event


# Main

class ScrollAreaContent(Event):
    def __init__(self, content_widget):
        super().__init__(Event.Type.ScrollContent)
        self._content_widget = content_widget

    @property
    def content_widget(self):
        return self._content_widget
