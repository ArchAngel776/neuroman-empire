from lib.gui.event import Event


# Main

class CheckBoxChangedEvent(Event):
    _checked: bool

    def __init__(self, checked: bool) -> None: ...

    @property
    def checked(self) -> bool: ...
