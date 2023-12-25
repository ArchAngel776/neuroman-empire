from PyQt5.QtGui import QIcon

from lib.gui.element.form import FormInput

from app import GUI_ICON
from app.i18n import I18N
from app.i18n.message import I18NMessage


# Modules

def main_icon():
    return QIcon(GUI_ICON)


def i18n(xpath, lang=None):
    international = I18N(lang)
    return I18NMessage(international.get_value(xpath))


def home_image(image):
    size = image.parent().size() / 3
    image.setMinimumSize(size)
    return True


def value_to_form(value, index):
    return FormInput(value)


def form_to_value(form, index):
    return form.value
