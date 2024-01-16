from PyQt5.QtCore import QObject


# Main

class FormContainer(QObject):
    def __init__(self):
        super().__init__()
        self._elements = []
        self._is_valid = True

    def add(self, element):
        self._elements.append(element)
        return self

    def validate(self):
        self._is_valid = True
        for element in self._elements:
            element.validate()

    # Slots

    def update_validation_status(self, is_valid):
        if self._is_valid:
            self._is_valid = is_valid

    @property
    def is_valid(self):
        return self._is_valid
