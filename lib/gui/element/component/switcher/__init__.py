from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QLayout

from lib.decorators import method
from lib.decorators.decorator import Decorator
from lib.gui.element.component import Component
from lib.gui.event.switcher_switch import SwitcherSwitchEvent
from lib.gui.event import Event


# Decorators

class UpdateStrategy(Decorator):
    def method(self, target, key):
        super().method(target, key)
        target.update_view()


class ConstraintLayout(Decorator):
    def method(self, target, root):
        return super().method(target, root).constraint(QLayout.SizeConstraint.SetMinAndMaxSize)


# Main

class Switcher(Component):
    # Signals

    beforeShown = pyqtSignal()

    afterShown = pyqtSignal()

    def __init__(self, root, program, orientation):
        super().__init__(root, orientation)
        self._program = program

        self.beforeShown.connect(self.program.strategy_before_hook)
        self.afterShown.connect(self.program.strategy_after_hook)

        self.afterShown.connect(self.switchEvent)

    def config(self):
        super().config()
        self.layout().setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)

    def AutoInit(self):
        self.add_event_listener(
            Event.Type.Show, lambda switcher: switcher.update_view(),
            with_target=True, with_event=False
        )
        return self

    @method(UpdateStrategy)
    def change_strategy(self, key):
        self.program.change_key(key)

    def update_dependencies(self, dependencies, update_strategies=False):
        self.program.update(dependencies, update_strategies)
        return self

    def update_view(self):
        self.beforeShown.emit()
        super().update_view()
        self.afterShown.emit()

    @method(ConstraintLayout)
    def render_view(self, root):
        return self.program.render_element(root)

    @property
    def program(self):
        return self._program

    # Slots

    def switchEvent(self):
        self.emit(Event.Type.Switch, SwitcherSwitchEvent())
