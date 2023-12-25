from abc import ABC, abstractmethod

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QScrollArea, QApplication

from lib.decorators import method
from lib.decorators.decorator import Decorator
from lib.gui.element import Element
from lib.gui.element.scrollable.fitter.horizontal import ScrollableHorizontalFitter
from lib.gui.element.scrollable.fitter.vertical import ScrollableVerticalFitter
from lib.gui.event import Event
from lib.gui.event.scroll_area_content import ScrollAreaContent


# Base

class ScrollFit(Decorator, ABC):
    def method(self, target, enabled=True):
        if not enabled:
            target.add_event_listener(
                Event.Type.ScrollContent, self.scroll_content_fitting,
                with_target=True, with_event=True
            )
        return super().method(target, enabled)

    def scroll_content_fitting(self, area, event):
        event.content_widget.add_event_listener(
            Event.Type.Resize, self.createFitter(area).fitting,
            with_target=True, with_event=True
        )
        return True

    @abstractmethod
    def createFitter(self, area):
        pass


# Decorators

class ScrollXSize(Decorator):
    def method(self, target, enabled=True, size=None):
        if enabled and size:
            target.horizontalScrollBar().setFixedHeight(size)
        return super().method(target, enabled)


class ScrollXFit(ScrollFit):
    def createFitter(self, area):
        return ScrollableHorizontalFitter(area)


class ScrollYSize(Decorator):
    def method(self, target, enabled=True, size=None):
        if enabled and size:
            target.verticalScrollBar().setFixedWidth(size)
        return super().method(target, enabled)


class ScrollYFit(ScrollFit):
    def createFitter(self, area):
        return ScrollableVerticalFitter(area)


class ConfigScrollableElement(Decorator):
    def config(self, target, content):
        content.config()
        return self


class EmitScrollContentEvent(Decorator):
    def method(self, target, content):
        super().method(target, content)
        QApplication.sendEvent(target, ScrollAreaContent(content))
        return target


# Main

class Scrollable(QScrollArea, Element):
    def config(self):
        super().config()
        self.setWidgetResizable(True)

    @method(ScrollXSize)
    @method(ScrollXFit)
    def ScrollX(self, enabled=True):
        self.horizontalScrollBar().setEnabled(enabled)
        if enabled:
            self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        else:
            self.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        return self

    @method(ScrollYSize)
    @method(ScrollYFit)
    def ScrollY(self, enabled=True):
        self.verticalScrollBar().setEnabled(enabled)
        if enabled:
            self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        else:
            self.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        return self

    def Align(self, alignment):
        self.setAlignment(alignment)
        return self

    def Adjust(self, adjust):
        self.setSizeAdjustPolicy(adjust)
        return self

    @method(ConfigScrollableElement)
    @method(EmitScrollContentEvent)
    def Content(self, content):
        self.setWidget(content)
        return self
