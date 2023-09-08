# Main

class I18NMessage(str):
    _message: str

    def __init__(self, message: str) -> None: ...

    def __str__(self) -> str: ...
