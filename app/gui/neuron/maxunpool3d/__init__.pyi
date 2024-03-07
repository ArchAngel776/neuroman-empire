from typing import Optional

from lib import void
from lib.gui.element.form import FormInput
from lib.gui.event.check_box_changed import CheckBoxChangedEvent
from lib.gui.layout import Layout

from app.network.neuron import Neuron
from app.network.neuron.maxunpool3d.params import MaxUnpool3dParams
from app.network.neuron.maxunpool3d.options import MaxUnpool3dOptions
from app.network.neuron.maxunpool3d.dimension.params import MaxUnpool3dDimensionParams
from app.network.neuron.maxunpool3d.dimension.options import MaxUnpool3dDimensionOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams

from .view import Dimension3dView, Dimension3dSwitcher


# Main

class NeuronBuilderMaxUnpooling3dStrategy(NeuronStrategy[MaxUnpool3dParams, MaxUnpool3dOptions]):
    class Watch(str):
        DIMENSION_SWITCHER = ... #type: NeuronBuilderMaxUnpooling3dStrategy.Watch

    _pool_layer: Optional[FormInput[tuple[int, Neuron]]]

    _reflection: FormInput[bool]

    _input_height: int

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    def beforeShow(self) -> void: ...

    @property
    def params(self) -> NeuronStrategyParams[MaxUnpool3dParams, MaxUnpool3dOptions]: ...

    @property
    def default_params(self) -> MaxUnpool3dParams: ...

    @property
    def default_options(self) -> MaxUnpool3dOptions: ...

    def load(self, params: MaxUnpool3dParams, options: MaxUnpool3dOptions) -> void: ...

    @property
    def dimension_params(self) -> NeuronStrategyParams[MaxUnpool3dDimensionParams, MaxUnpool3dDimensionOptions]: ...

    def change_dimension(self, event: CheckBoxChangedEvent) -> bool: ...

    @property
    def dimension_switcher_program(self) -> Dimension3dSwitcher: ...

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
