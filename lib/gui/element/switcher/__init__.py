from PyQt5.QtWidgets import QSizePolicy, QHBoxLayout, QVBoxLayout, QLayout

from lib.decorators import method
from lib.decorators.decorator import Decorator
from lib.gui.event.switcher_switch import SwitcherSwitchEvent
from lib.helpers.gui_remover import GUIRemover
from lib.hooks import layout_widget
from lib.gui.element import Element
from lib.gui.element.switcher.program import SwitcherProgram
from lib.gui.event import Event
from lib.gui.layout.type import LayoutType


# Decorators

class UpdateStrategy(Decorator):
    def method(self, target, key):
        super().method(target, key)
        target.implement_strategy()


class RemoveOldStrategy(Decorator):
    def __init__(self, original):
        super().__init__(original)
        self._gui_remover = GUIRemover()

    def config(self, target):
        self._gui_remover.remove_widget(target)
        return self


# Main

class Switcher(Element):
    def __init__(self, root, program, orientation):
        super().__init__(root)
        self._program = program
        self._orientation = orientation
        self._sizing = QSizePolicy()

    def config(self):
        super().config()

        if self._orientation == LayoutType.HORIZONTAL:
            self.setLayout(QHBoxLayout())
        elif self._orientation == LayoutType.VERTICAL:
            self.setLayout(QVBoxLayout())

        self.layout().setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)

    def InnerSizing(self, horizontal, vertical):
        self._sizing.setHorizontalPolicy(horizontal)
        self._sizing.setVerticalPolicy(vertical)
        return self

    @method(UpdateStrategy)
    def change_strategy(self, key):
        self.program.change_key(key)

    def update_dependencies(self, dependencies, update_strategies=False):
        self.program.update(dependencies, update_strategies)
        return self

    @method(RemoveOldStrategy)
    def implement_strategy(self):
        widget = layout_widget(self.program.render_element(self.root))

        widget.setSizePolicy(self._sizing)
        widget.layout().setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)

        self.layout().addWidget(widget)
        self.emit(Event.Type.Switch, SwitcherSwitchEvent())

    @property
    def program(self):
        return self._program
