from lib.foundations.command import Command
from commands.lang_create import LangCreate


def commands() -> dict[str, type[Command]]:
    return {
        "lang-create": LangCreate
    }
