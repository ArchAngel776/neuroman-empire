from abc import ABC, abstractmethod


# Main

class DataProvider(ABC):
    @abstractmethod
    def add(self, *data):
        pass

    @abstractmethod
    def provide(self):
        pass

    @abstractmethod
    def clear(self):
        pass
