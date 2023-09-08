from typing import Any


# Main

class YAML:
    XPATH_SPLITER = ... #type: str

    _path: str

    def __init__(self, path: str) -> None: ...

    def load(self) -> str: ...

    def xpath(self, xpath: str) -> Any: ...

    @property
    def path(self) -> str: ...
