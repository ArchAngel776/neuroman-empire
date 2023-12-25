from app.gui.neuron.unfold import NeuronBuilderUnfoldStrategy


# Main

class DimensionRemover:
    _target: NeuronBuilderUnfoldStrategy

    _index: int

    def __init__(self, target: NeuronBuilderUnfoldStrategy, index: int) -> None: ...

    def remove(self) -> bool: ...

    @property
    def target(self) -> NeuronBuilderUnfoldStrategy: ...

    @property
    def index(self) -> int: ...
