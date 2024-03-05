from PyQt5.QtCore import QObject, pyqtSignal

from lib.decorators import method
from lib.decorators.decorator import Decorator
from lib.gui.event import Event
from lib.gui.element.form.container.control.exception import ValidatorException


# Decorators

class FocusOn(Decorator):
    def config(self, target, event):
        target.form_control.setFocus()
        return self


class UpdateStyle(Decorator):
    def method(self, target, event):
        result = super().method(target, event)
        target.form_control.update_style()
        return result


# Main

class FormElementControl(QObject):
    # Signals

    validation = pyqtSignal(bool)
    validate = pyqtSignal(object)

    def __init__(self, form_control):
        super().__init__()
        self._form_control = form_control
        self._exception = ValidatorException()

    def config(self, element):
        self.validation.connect(element.send_validation_status)

    def Validator(self, validator):
        validator.add_event_listener(
            Event.Type.Validated, self.on_validate,
            with_target=False, with_event=True
        )
        self.validate.connect(validator.validate)
        return validator.bind(self._form_control)

    @method(FocusOn)
    @method(UpdateStyle)
    def on_validate(self, event):
        if event.valid:
            self._form_control.setProperty("valid", True)
            self._exception.setMessage(event.message).hide()
        else:
            self._form_control.setProperty("valid", False)
            self._exception.setMessage(event.message).prepare(self._form_control).show()
        self.validation.emit(event.valid)
        return True

    # Slots

    def make_validation(self):
        self.validate.emit(self._form_control.value)

    def hide_message(self):
        self._exception.hide()

    @property
    def form_control(self):
        return self._form_control
