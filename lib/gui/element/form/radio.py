from PyQt5.QtWidgets import QRadioButton, QApplication

from lib.decorators import method
from lib.decorators.decorator import Decorator
from lib.gui.element.form import FormControl
from lib.gui.event.radio_button_toggled import RadioButtonToggled
from lib.gui.layout.factory import LayoutFactory


# Decorators

class ToggleActive(Decorator):
    def method(self, target, selected):
        if selected:
            super().method(target)


# Main

class RadioButton(FormControl):
    def __init__(self, root, orientation, initial_value=None):
        super().__init__(root)
        self._orientation = orientation
        self._initial_value = initial_value
        self._radios = {}

    def config(self):
        super().config()
        self.setLayout(self.createLayout().element)

        for value, radio in self._radios.items():
            self.layout().addWidget(radio)

            radio.toggled.connect(self.selectInput)
            radio.toggled.connect(self.selectRadio)

            if value == self._initial_value:
                radio.toggle()

    def react(self, value):
        if not self._radios[value].isChecked():
            self._radios[value].toggle()

    def Add(self, value, label=None):
        self._radios[value] = QRadioButton(label)
        return self

    def createLayout(self):
        return LayoutFactory(self._orientation).create()

    @property
    def selected(self):
        for value, radio in self._radios.items():
            if radio.isChecked():
                return value

        return None

    # Slots

    @method(ToggleActive)
    def selectRadio(self):
        assert self.selected
        QApplication.sendEvent(self, RadioButtonToggled(self.selected))

    @method(ToggleActive)
    def selectInput(self):
        assert self.selected
        self.input(self.selected)
