from typing import IO

from lib import void
from lib.foundations.command import Command


class LangCreate(Command):
    _reader: IO

    def __init__(self):
        pass

    def run(self, lang: str) -> void:
        pass

    @property
    def template_path(self) -> str:
        return ""
