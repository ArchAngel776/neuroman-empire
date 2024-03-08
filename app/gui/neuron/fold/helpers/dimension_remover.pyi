from app.gui.neuron.fold import NeuronBuilderFoldStrategy


# Main

class DimensionRemover:
    _target: NeuronBuilderFoldStrategy

    _index: int

    def __init__(self, target: NeuronBuilderFoldStrategy, index: int) -> None: ...

    def remove(self) -> bool: ...

    @property
    def target(self) -> NeuronBuilderFoldStrategy: ...

    @property
    def index(self) -> int: ...
