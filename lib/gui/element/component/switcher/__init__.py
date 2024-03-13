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

    beforeClosed = pyqtSignal()

    def __init__(self, root, program, orientation):
        super().__init__(root, orientation)
        self._program = program
        self._payload = None

        self.beforeShown.connect(self.program.strategy_before_hook)
        self.afterShown.connect(self.program.strategy_after_hook)
        self.beforeClosed.connect(self.program.strategy_close_hook)

        self.afterShown.connect(self.switchEvent)

        self.program.view_updated.connect(self.view_update)

    def config(self):
        super().config()
        self.program.config()
        self.layout().setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)

    def Payload(self, payload):
        self._payload = payload
        return self

    def AutoInit(self):
        self.add_event_listener(
            Event.Type.Show, lambda switcher: switcher.update_view(),
            with_target=True, with_event=False
        )
        return self

    def change_strategy(self, key):
        self.change_switcher_strategy(key)

    @method(UpdateStrategy)
    def change_switcher_strategy(self, key):
        self.beforeClosed.emit()
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
        strategy = self.program.current_strategy
        if self.payload:
            self.payload(strategy)
        return strategy.render(root)

    # Slots

    def switchEvent(self):
        self.emit(Event.Type.Switch, SwitcherSwitchEvent())

    def view_update(self):
        super().update_view()

    @property
    def program(self):
        return self._program

    @property
    def payload(self):
        return self._payload
