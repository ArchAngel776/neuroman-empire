from typing import TypedDict, TypeVar

from lib import void
from lib.decorators import method
from lib.decorators.decorator import Decorator
from lib.gui.element.font import Font
from lib.gui.element.form import FormInput
from lib.gui.layout import Layout

from app.network.neuron.unfold.params import UnfoldParams
from app.network.neuron.unfold.options import UnfoldOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams

# Types

TNeuronBuilderUnfoldStrategyUpdateOperation = TypeVar(
    "TNeuronBuilderUnfoldStrategyUpdateOperation",
    bound=NeuronBuilderUnfoldStrategy
)

class ListData(TypedDict):
    kernel_size: FormInput[int]
    stride: FormInput[int]
    padding: FormInput[int]
    dilation: FormInput[int]


# Decorators

class UpdateOperation(Decorator[bool, [NeuronBuilderUnfoldStrategy, ...]]):
    def method(
            self,
            target: TNeuronBuilderUnfoldStrategyUpdateOperation,
            *args: ...,
            **kwargs: ...
    ) -> ...: ...


# Main

class NeuronBuilderUnfoldStrategy(NeuronStrategy[UnfoldParams, UnfoldOptions]):
    class Watch(str):
        LIST_ELEMENT = ... #type: NeuronBuilderUnfoldStrategy.Watch

    _kernel_size: list[FormInput[int]]
    _stride: list[FormInput[int]]
    _padding: list[FormInput[int]]
    _dilation: list[FormInput[int]]

    _input_height: int
    _title_font: Font

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[UnfoldParams, UnfoldOptions]: ...

    @property
    def default_params(self) -> UnfoldParams: ...

    @property
    def default_options(self) -> UnfoldOptions: ...

    @method(UpdateOperation)
    def load(self, params: UnfoldParams, options: UnfoldOptions) -> void: ...

    def data(self) -> list[ListData]: ...

    @method(UpdateOperation)
    def add_dimension(self) -> bool: ...

    @method(UpdateOperation)
    def remove_dimension(self, index: int) -> bool: ...

    def render(self, root: MainWindow) -> Layout: ...
