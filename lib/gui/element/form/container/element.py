from PyQt5.QtCore import QObject, pyqtSignal

from lib.decorators import method
from lib.decorators.decorator import Decorator
from lib.gui.element.form.container.control import FormElementControl


# Decorators

class ConfigControl(Decorator):
    def method(self, target, form_control):
        control = super().method(target, form_control)
        control.config(target)
        return control


# Main

class FormElement(QObject):
    # Signals

    validation = pyqtSignal()
    update_validation = pyqtSignal(bool)

    def __init__(self, container):
        super().__init__()
        self.update_validation.connect(container.add(self).update_validation_status)

    @method(ConfigControl)
    def Control(self, form_control):
        control = FormElementControl(form_control)
        self.validation.connect(control.make_validation)
        return control

    def validate(self):
        self.validation.emit()

    # Slots

    def send_validation_status(self, status):
        self.update_validation.emit(status)
