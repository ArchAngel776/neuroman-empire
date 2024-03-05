from PyQt5.QtCore import QObject, pyqtSignal

from lib import void
from lib.decorators import method
from lib.decorators.decorator import Decorator
from lib.gui.element.form.container.control import FormElementControl


# Decorators

class ConfigControl(Decorator):
    def method(self, target, form_control):
        control = super().method(target, form_control)
        control.config(target)
        return control


class ConnectValidation(Decorator):
    def method(self, target, form_control):
        control = super().method(target, form_control)
        target.validation.connect(control.make_validation)
        return control


class ConnectDestruction(Decorator):
    def config(self, target, form_control):
        form_control.destroyed.connect(target.remove)
        return self


class ConnectClose(Decorator):
    def method(self, target, form_control):
        control = super().method(target, form_control)
        target.closed.connect(control.hide_message)
        return control


# Main

class FormElement(QObject):
    # Signals

    validation = pyqtSignal()
    update_validation = pyqtSignal(bool)
    removed = pyqtSignal(QObject)
    closed = pyqtSignal()

    def __init__(self, container):
        super().__init__()
        self._container = container
        self._container.add(self)

    def config(self):
        self.update_validation.connect(self._container.update_validation_status)
        self.removed.connect(self._container.remove_element)

    @method(ConfigControl)
    @method(ConnectValidation)
    @method(ConnectDestruction)
    @method(ConnectClose)
    def Control(self, form_control):
        return FormElementControl(form_control)

    def validate(self):
        self.validation.emit()

    def remove(self):
        self.removed.emit(self)

    # Slots

    def send_validation_status(self, status):
        self.update_validation.emit(status)

    def close_exception(self):
        self.closed.emit()
