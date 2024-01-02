from typing import TypedDict, TypeVar

from lib import void
from lib.decorators import method
from lib.decorators.decorator import Decorator
from lib.gui.element.font import Font
from lib.gui.element.form import FormInput
from lib.gui.layout import Layout

from app.network.neuron.fold.params import FoldParams
from app.network.neuron.fold.options import FoldOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams

# Types

TNeuronBuilderFoldStrategyUpdateOperation = TypeVar(
    "TNeuronBuilderFoldStrategyUpdateOperation",
    bound=NeuronBuilderFoldStrategy
)

class ListData(TypedDict):
    output_size: FormInput[int]
    kernel_size: FormInput[int]
    stride: FormInput[int]
    padding: FormInput[int]
    dilation: FormInput[int]


# Decorators

class UpdateOperation(Decorator[bool, [NeuronBuilderFoldStrategy, ...]]):
    def method(
            self,
            target: TNeuronBuilderFoldStrategyUpdateOperation,
            *args: ...,
            **kwargs: ...
    ) -> ...: ...


# Main

class NeuronBuilderFoldStrategy(NeuronStrategy[FoldParams, FoldOptions]):
    class Watch(str):
        LIST_ELEMENT = ... #type: NeuronBuilderFoldStrategy.Watch

    _output_size: list[FormInput[int]]
    _kernel_size: list[FormInput[int]]
    _stride: list[FormInput[int]]
    _padding: list[FormInput[int]]
    _dilation: list[FormInput[int]]

    _input_height: int
    _title_font: Font

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[FoldParams, FoldOptions]: ...

    @property
    def default_params(self) -> FoldParams: ...

    @property
    def default_options(self) -> FoldOptions: ...

    @method(UpdateOperation)
    def load(self, params: FoldParams, options: FoldOptions) -> void: ...

    def data(self) -> list[ListData]: ...

    @method(UpdateOperation)
    def add_dimension(self) -> bool: ...

    @method(UpdateOperation)
    def remove_dimension(self, index: int) -> bool: ...

    def render(self, root: MainWindow) -> Layout: ...
