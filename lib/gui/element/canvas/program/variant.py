from abc import abstractmethod, ABC


# Main

class CanvasProgramVariant(ABC):
    def __init__(self, program):
        self._program = program

    @abstractmethod
    def draw(self, painter):
        pass

    @property
    def program(self):
        return self._program
