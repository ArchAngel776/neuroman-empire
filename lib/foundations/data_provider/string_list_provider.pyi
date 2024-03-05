from lib import void
from lib.foundations.data_provider import DataProvider


# Main

class StringListProvider(DataProvider[str]):
    _list: list[str]

    def __init__(self) -> None: ...

    def add(self, *data: str) -> void: ...

    def provide(self) -> str: ...

    def clear(self) -> void: ...

    @property
    def list(self) -> list[str]: ...
