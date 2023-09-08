from lib.gui.element.form import FormInput
from lib.gui.layout import Layout

from app.network.neuron.conv1d.dimension.params import Conv1dDimensionParams
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy

from .dependencies import SingleDimensionStrategyDependencies


# Main

class SingleDimensionStrategy(NeuronStrategy[SingleDimensionStrategyDependencies, Conv1dDimensionParams, {}]):
    _kernel_size: FormInput[int]
    _stride: FormInput[int]
    _padding: FormInput[int]
    _dilation: FormInput[int]

    _input_height: int

    def __init__(self, dependencies: SingleDimensionStrategyDependencies) -> None: ...

    @property
    def params(self) -> Conv1dDimensionParams: ...

    @property
    def default_params(self) -> Conv1dDimensionParams: ...

    @property
    def default_options(self) -> {}: ...

    def render(self, root: MainWindow) -> Layout: ...