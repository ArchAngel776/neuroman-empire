from abc import ABC, abstractmethod

from lib import void


# Main

class Command(ABC):
    @abstractmethod
    def run(self, *args) -> void: ...
