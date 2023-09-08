from lib.gui.event import Event


# Main

class ButtonClickEvent(Event):
    def __init__(self):
        super().__init__(Event.Type.Click)
