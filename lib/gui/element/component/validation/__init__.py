from PyQt5.QtCore import QPoint

from lib.decorators import method
from lib.decorators.decorator import Decorator
from lib.gui.element.component import Component
from lib.gui.element.component.validation.exception import ValidationException
from lib.gui.event import Event
from lib.gui.layout.factory import LayoutFactory


# Decorators

class UpdateStyle(Decorator):
    def method(self, target, control):
        super().method(target, control)
        control.update_style()


# Main

class ValidationField(Component):
    class Watch(str):
        FORM_INPUT = "form_input"

    def __init__(self, root, form_control, validator, orientation):
        super().__init__(root, orientation)
        self._form_control = form_control
        self._validator = validator
        self._exception = ValidationException(self)

    def config(self):
        super().config()
        self._form_control.add_event_listener(
            Event.Type.Input, self.validate_input,
            with_target=False, with_event=True
        )
        self._exception.config()
        self.update_view()

    def validate(self, text):
        if self._validator.validate(text):
            self.make(ValidationField.Watch.FORM_INPUT, self.clear_exception)
            return True
        else:
            self.make(ValidationField.Watch.FORM_INPUT, self.set_exception)
            return False

    def validate_input(self, event):
        self.validate(event.text)
        return True

    def validate_container(self):
        return self.validate(self.text)

    def Bind(self, container):
        container.register_field(self)
        return self

    @method(UpdateStyle)
    def set_exception(self, control):
        control.setFocus()
        control.setProperty("valid", False)
        self._exception.set_text(self._validator.error_message)
        self._exception.setup()

        if self._exception.isVisible():
            self._exception.repaint()
        else:
            self._exception.show()

    @method(UpdateStyle)
    def clear_exception(self, control):
        control.setFocus()
        control.setProperty("valid", True)
        self._exception.set_text(self._validator.error_message)
        self._exception.hide()

    def render_view(self, root):
        return (
            LayoutFactory(self._orientation).create()
            .add(
                self.watch(
                    ValidationField.Watch.FORM_INPUT,
                    self._form_control
                )
            )
        )

    @property
    def text(self):
        return self.get(ValidationField.Watch.FORM_INPUT).text()

    @property
    def position(self):
        return self.get(ValidationField.Watch.FORM_INPUT).mapTo(self.root, QPoint())

    @property
    def size(self):
        return self.get(ValidationField.Watch.FORM_INPUT).size()
