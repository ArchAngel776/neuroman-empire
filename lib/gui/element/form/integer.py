from PyQt5.QtWidgets import QSpinBox

from lib.gui.element.form import FormControl


# Main

class IntegerInput(QSpinBox, FormControl):
    def __init__(self, root, value):
        super().__init__(root)
        self.setValue(value)

    def config(self):
        super().config()
        self.valueChanged.connect(self.input)

    def react(self, value):
        self.setValue(value)

    def Min(self, value):
        self.setMinimum(value)
        return self

    def Max(self, value):
        self.setMaximum(value)
        return self
