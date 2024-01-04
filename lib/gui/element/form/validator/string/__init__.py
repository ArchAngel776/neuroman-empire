from lib.gui.element.form.validator import FormValidator
from lib.gui.element.component.validation import ValidationField


# Main

class StringValidator(FormValidator):
    def Widget(self, root, form_control, orientation):
        return ValidationField(root, form_control, self, orientation)
