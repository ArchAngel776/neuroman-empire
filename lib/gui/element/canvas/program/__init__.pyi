from abc import ABC, abstractmethod
from enum import Enum
from typing import TypeVar, Generic, Optional, Self

from PyQt5.QtGui import QPaintEvent, QPainter

from lib import void
from lib.decorators import method
from lib.decorators.decorator import Decorator
from lib.gui.element.canvas import Canvas

from .variant import CanvasProgramVariant

# Types

CanvasProgramVariantType = TypeVar("CanvasProgramVariantType", int, str, Enum)

TCanvasProgramUpdateVariant = TypeVar("TCanvasProgramUpdateVariant", bound=CanvasProgram)
CanvasProgramVariantTypeUpdateVariant = TypeVar("CanvasProgramVariantTypeUpdateVariant", int, str, Enum)

TCanvasProgramHasCanvas = TypeVar("TCanvasProgramHasCanvas", bound=CanvasProgram)
CanvasProgramVariantTypeHasCanvas = TypeVar("CanvasProgramVariantTypeHasCanvas", int, str, Enum)

TCanvasProgramHasVariant = TypeVar("TCanvasProgramHasVariant", bound=CanvasProgram)
CanvasProgramVariantTypeHasVariant = TypeVar("CanvasProgramVariantTypeHasVariant", int, str, Enum)

TCanvasProgramCanvasCycle = TypeVar("TCanvasProgramCanvasCycle", bound=CanvasProgram)
CanvasProgramVariantTypeCanvasCycle = TypeVar("CanvasProgramVariantTypeCanvasCycle", int, str, Enum)


# Decorators

class UpdateVariant(
    Decorator[void, [CanvasProgram[CanvasProgramVariantTypeUpdateVariant], CanvasProgramVariantTypeUpdateVariant]],
    Generic[CanvasProgramVariantTypeUpdateVariant]
):
    def method(self, target: TCanvasProgramUpdateVariant, variant: CanvasProgramVariantTypeUpdateVariant) -> void: ...


class HasCanvas(
    Decorator[Canvas[TCanvasProgramHasCanvas], [CanvasProgram[CanvasProgramVariantTypeHasCanvas]]],
    Generic[CanvasProgramVariantTypeHasCanvas]
):
    def method(self, target: TCanvasProgramHasCanvas) -> Canvas[TCanvasProgramHasCanvas]: ...


class HasVariant(
    Decorator[CanvasProgramVariantTypeHasVariant, [CanvasProgram[CanvasProgramVariantTypeHasVariant]]],
    Generic[CanvasProgramVariantTypeHasVariant]
):
    def method(self, target: TCanvasProgramHasVariant) -> CanvasProgramVariantTypeHasVariant: ...


class CanvasCycle(
    Decorator[void, [CanvasProgram[CanvasProgramVariantTypeCanvasCycle], QPaintEvent, QPainter]],
    Generic[CanvasProgramVariantTypeCanvasCycle]
):
    def method(self, target: TCanvasProgramCanvasCycle, event: QPaintEvent, painter: QPainter) -> void: ...


# Main

class CanvasProgram(ABC, Generic[CanvasProgramVariantType]):
    _canvas: Optional[Canvas[Self]]
    _variant: Optional[CanvasProgramVariantType]

    def __init__(self, variant: CanvasProgramVariantType = None) -> None: ...

    def handle(self, event: QPaintEvent, canvas: Canvas[Self]) -> void: ...

    @method(UpdateVariant[CanvasProgramVariantType])
    def change_variant(self, variant: CanvasProgramVariantType) -> void: ...

    def update(self) -> void: ...

    @abstractmethod
    def draw(self, event: QPaintEvent, painter: QPainter) -> void: ...

    @property
    @method(HasCanvas[CanvasProgramVariantType])
    def canvas(self) -> Canvas[Self]: ...

    @property
    @method(HasVariant[CanvasProgramVariantType])
    def variant_type(self) -> CanvasProgramVariantType: ...

    @property
    def variants(self) -> dict[CanvasProgramVariantType, CanvasProgramVariant[Self]]: ...

    @property
    def variant(self) -> CanvasProgramVariant[Self]: ...

    @property
    def width(self) -> int: ...

    @property
    def height(self) -> int: ...
