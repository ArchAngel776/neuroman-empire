from lib.gui.event import Event


# Main

class SwitcherSwitchEvent(Event):
    def __init__(self):
        super().__init__(Event.Type.Switch)
