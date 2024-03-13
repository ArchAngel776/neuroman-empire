from typing import Optional

from lib import void
from lib.gui.element.form import FormInput
from lib.gui.event.check_box_changed import CheckBoxChangedEvent
from lib.gui.layout import Layout

from app.network.neuron import Neuron
from app.network.neuron.maxunpool2d.params import MaxUnpool2dParams
from app.network.neuron.maxunpool2d.options import MaxUnpool2dOptions
from app.network.neuron.maxunpool2d.dimension.params import MaxUnpool2dDimensionParams
from app.network.neuron.maxunpool2d.dimension.options import MaxUnpool2dDimensionOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams

from .view import Dimension2dSwitcher, Dimension2dView


# Main

class NeuronBuilderMaxUnpooling2dStrategy(NeuronStrategy[MaxUnpool2dParams, MaxUnpool2dOptions]):
    class Watch(str):
        DIMENSION_SWITCHER = ... #type: NeuronBuilderMaxUnpooling2dStrategy.Watch

    _pool_layer: Optional[FormInput[tuple[int, Neuron]]]

    _reflection: FormInput[bool]

    _input_height: int

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    def beforeShow(self) -> void: ...

    @property
    def params(self) -> NeuronStrategyParams[MaxUnpool2dParams, MaxUnpool2dOptions]: ...

    @property
    def default_params(self) -> MaxUnpool2dParams: ...

    @property
    def default_options(self) -> MaxUnpool2dOptions: ...

    def load(self, params: MaxUnpool2dParams, options: MaxUnpool2dOptions) -> void: ...

    @property
    def dimension_params(self) -> NeuronStrategyParams[MaxUnpool2dDimensionParams, MaxUnpool2dDimensionOptions]: ...

    @staticmethod
    def value_to_dimension(value: bool) -> Dimension2dView: ...

    def change_dimension(self, event: CheckBoxChangedEvent) -> bool: ...

    @property
    def dimension_switcher_program(self) -> Dimension2dSwitcher: ...

    @property
    def pool_layer(self) -> FormInput[tuple[int, Neuron]]: ...

    @property
    def pool_layer_index(self) -> int: ...

    @property
    def pool_layer_neuron(self) -> Neuron: ...

    @property
    def pooling_neurons(self) -> list[tuple[str, Neuron]]: ...

    @staticmethod
    def select_indicated_pooling(neuron: Neuron, index: int) -> bool: ...

    @property
    def default_pool_layer_neuron(self) -> Neuron: ...

    def render(self, root: MainWindow) -> Layout: ...
