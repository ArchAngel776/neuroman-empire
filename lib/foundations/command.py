from abc import ABC, abstractmethod


# Main

class Command(ABC):
    @abstractmethod
    def run(self, *args):
        pass
