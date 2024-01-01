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


# Main

class Switcher(Component):
    def __init__(self, root, program, orientation):
        super().__init__(root, orientation)
        self._program = program

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
        super().update_view()
        self.emit(Event.Type.Switch, SwitcherSwitchEvent())

    def render_view(self):
        return self.program.render_element(self.root).constraint(QLayout.SizeConstraint.SetMinAndMaxSize)

    @property
    def program(self):
        return self._program
