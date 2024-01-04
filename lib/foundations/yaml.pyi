from typing import Any, ClassVar


# Main

class YAML:
    XPATH_SPLITER: ClassVar[str] = ...

    _path: str

    def __init__(self, path: str) -> None: ...

    def load(self) -> str: ...

    def xpath(self, xpath: str) -> Any: ...

    @property
    def path(self) -> str: ...
