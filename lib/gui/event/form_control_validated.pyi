from typing import Optional

from lib.gui.event import Event


# Main

class FormControlValidated(Event):
    _valid: bool

    _message: Optional[str]

    def __init__(self, valid: bool, message: Optional[str]) -> None: ...

    @property
    def valid(self) -> bool: ...

    @property
    def message(self) -> str: ...
