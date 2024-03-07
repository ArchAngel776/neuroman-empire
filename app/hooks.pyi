from typing import Iterable

from PyQt5.QtGui import QIcon

from lib.gui.element.form import FormInput
from lib.gui.element.image import Image

from app.network.neuron import Neuron
from app.i18n.message import I18NMessage


# Modules

def main_icon() -> QIcon: ...


def i18n(xpath: str, *values: str | float) -> I18NMessage: ...


def home_image(image: Image) -> bool: ...


def value_to_form(value: int, index: int) -> FormInput[int]: ...


def form_to_value(form: FormInput[int], index: int) -> int: ...


def map_neurons(network: Iterable[Neuron]) -> list[tuple[str, Neuron]]: ...
