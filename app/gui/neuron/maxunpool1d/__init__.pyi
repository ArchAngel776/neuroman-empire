from typing import Optional

from lib import void
from lib.gui.element.form import FormInput
from lib.gui.layout import Layout

from app.network.neuron import Neuron
from app.network.neuron.maxunpool1d.params import MaxUnpool1dParams
from app.network.neuron.maxunpool1d.options import MaxUnpool1dOptions
from app.network.neuron.maxunpool1d.dimension.params import MaxUnpool1dDimensionParams
from app.network.neuron.maxunpool1d.dimension.options import MaxUnpool1dDimensionOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams

from .view import Dimension1dSwitcher, Dimension1dView


# Main

class NeuronBuilderMaxUnpooling1dStrategy(NeuronStrategy[MaxUnpool1dParams, MaxUnpool1dOptions]):
    class Watch(str):
        DIMENSION_SWITCHER = ... #type: NeuronBuilderMaxUnpooling1dStrategy.Watch

    _pool_layer: Optional[FormInput[tuple[int, Neuron]]]

    _input_height: int

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    def beforeShow(self) -> void: ...

    @property
    def params(self) -> NeuronStrategyParams[MaxUnpool1dParams, MaxUnpool1dOptions]: ...

    @property
    def default_params(self) -> MaxUnpool1dParams: ...

    @property
    def default_options(self) -> MaxUnpool1dOptions: ...

    def load(self, params: MaxUnpool1dParams, options: MaxUnpool1dOptions) -> void: ...

    @property
    def dimension_params(self) -> NeuronStrategyParams[MaxUnpool1dDimensionParams, MaxUnpool1dDimensionOptions]: ...

    @property
    def dimension_switcher_program(self) -> Dimension1dSwitcher: ...

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
