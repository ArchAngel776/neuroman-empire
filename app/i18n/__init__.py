from re import sub as regex_sub

from lib.decorators import method
from lib.decorators.decorator import Decorator
from lib.foundations.yaml import YAML


# Decorators

class SubstitutionMessage(Decorator):
    def __init__(self, original):
        super().__init__(original)
        self._i18n = I18N()

    def config(self, target, xpath):
        self._i18n.set_lang(target.lang)
        return self

    def method(self, target, xpath):
        message = super().method(target, xpath)
        return regex_sub(self.pattern, self.insert_message, message)

    def insert_message(self, message):
        xpath = message.group("xpath")
        return self._i18n.get_value(xpath)

    @property
    def pattern(self):
        return "{(?P<xpath>.+)}"


# Main

class I18N:
    _LANG = "pl_PL"

    def __init__(self, lang=None):
        self._lang = lang
        self._yaml = YAML(self.path)

    @method(SubstitutionMessage)
    def get_value(self, xpath):
        value = self._yaml.xpath(xpath)
        if isinstance(value, str):
            return value
        raise ValueError("i18n value must be a string")

    @property
    def lang(self):
        return self._lang if self._lang else self._LANG

    def set_lang(self, lang):
        self._lang = lang

    @property
    def path(self):
        return "lang/{}.yml".format(self.lang)

    @staticmethod
    def set_language(lang):
        I18N._LANG = lang
