from abc import ABC, abstractmethod

from PyQt5.QtGui import QPainter

from lib.decorators import method
from lib.decorators.decorator import Decorator
from lib.gui.element.canvas.program.variant import CanvasProgramVariant


# Decorators

class UpdateVariant(Decorator):
    def method(self, target, variant):
        super().method(target, variant)
        target.update()


class HasCanvas(Decorator):
    def method(self, target):
        result = super().method(target)
        if result is None:
            raise AttributeError("Canvas hasn't initialized yet.")
        return result


class HasVariant(Decorator):
    def method(self, target):
        result = super().method(target)
        if result is None:
            raise AttributeError("Variant hasn't established yet.")
        return result


class CanvasCycle(Decorator):
    def method(self, target, event, painter):
        painter.begin(target.canvas)
        super().method(target, event, painter)
        painter.end()


# Main

class CanvasProgram(ABC):
    def __init__(self, variant=None):
        self._canvas = None
        self._variant = variant

    def handle(self, event, canvas):
        self._canvas = canvas
        self.draw(event, QPainter())

    @method(UpdateVariant)
    def change_variant(self, variant):
        self._variant = variant

    def update(self):
        self.canvas.repaint()

    @abstractmethod
    def draw(self, event, painter):
        pass

    @property
    @method(HasCanvas)
    def canvas(self):
        return self._canvas

    @property
    @method(HasVariant)
    def variant_type(self):
        return self._variant

    @property
    def variants(self):
        return {}

    @property
    def variant(self):
        return self.variants[self.variant_type]

    @property
    def width(self):
        return self._canvas.size().width()

    @property
    def height(self):
        return self._canvas.size().height()
