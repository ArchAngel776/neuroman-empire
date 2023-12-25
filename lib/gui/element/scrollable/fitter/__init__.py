from abc import ABC, abstractmethod


# Main

class ScrollableFitter(ABC):
    def __init__(self, area):
        self._area = area

    @abstractmethod
    def fitting(self, content, event):
        pass

    def additional_size(self, content):
        return self.scrollbar_size if self.is_scrollbar_visible(content) else 0

    @abstractmethod
    def is_scrollbar_visible(self, content):
        pass

    @property
    def area(self):
        return self._area

    @property
    @abstractmethod
    def scrollbar_size(self):
        pass
