from lib.gui.event import Event
from lib.gui.element.form.validator import FormValidator


# Main

class StringValidator(FormValidator):
    def bind(self, form_control):
        return form_control.On(
            Event.Type.Input, self.validate_text_input,
            with_target=False, with_event=True
        )

    def validate_text_input(self, event):
        self.validate(event.text)
        return True
