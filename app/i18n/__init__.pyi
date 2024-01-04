from re import Match
from typing import TypeVar, Callable, ClassVar

from lib import void
from lib.decorators import method
from lib.decorators.decorator import Decorator
from lib.foundations.yaml import YAML

# Types

TI18N = TypeVar("TI18N", bound=I18N)


# Decorators

class SubstitutionMessage(Decorator[str, [I18N, str]]):
    _i18n: I18N

    def __init__(self, original: Callable[[I18N, str], str]) -> None: ...

    def config(self, target: TI18N, xpath: str) -> SubstitutionMessage: ...

    def method(self, target: TI18N, xpath: str) -> str: ...

    @staticmethod
    def insert_message(message: Match) -> str: ...

    @property
    def pattern(self) -> str: ...


# Main

class I18N:
    _LANG: ClassVar[str] = ...

    _lang: str
    _yaml: YAML

    def __init__(self, lang: str = None) -> None: ...

    @method(SubstitutionMessage)
    def get_value(self, xpath: str) -> str: ...

    @property
    def lang(self) -> str: ...

    def set_lang(self, lang: str) -> void: ...

    @property
    def path(self) -> str: ...

    @staticmethod
    def set_language(lang: str) -> void: ...
