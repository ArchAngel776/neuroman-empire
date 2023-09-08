from lib.gui.element import Element


# Main

class Canvas(Element):
    def __init__(self, root, program):
        super().__init__(root)
        self._program = program

    def paintEvent(self, event):
        super().paintEvent(event)
        self.program.handle(event, self)

    @property
    def program(self):
        return self._program
