from lib import void
from lib.gui.element.form import FormInput
from lib.gui.element.component.switcher import Switcher
from lib.gui.event.check_box_changed import CheckBoxChangedEvent
from lib.gui.layout import Layout

from app.network.neuron.convtranspose3d.params import ConvTranspose3dParams
from app.network.neuron.convtranspose3d.options import ConvTranspose3dOptions
from app.network.neuron.convtranspose3d.dimension.params import ConvTranspose3dDimensionParams
from app.network.neuron.convtranspose3d.dimension.options import ConvTranspose3dDimensionOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams

from .view import Dimension3dView, Dimension3dSwitcher


# Main

class NeuronBuilderTransposedConvolution3dStrategy(NeuronStrategy[ConvTranspose3dParams, ConvTranspose3dOptions]):
    class Watch(str):
        DIMENSION_SWITCHER = ... #type: NeuronBuilderTransposedConvolution3dStrategy.Watch

    _input_channels: FormInput[int]
    _output_channels: FormInput[int]
    _groups: FormInput[int]
    _bias: FormInput[bool]

    _reflection: FormInput[bool]

    _input_height: int

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[ConvTranspose3dParams, ConvTranspose3dOptions]: ...

    @property
    def default_params(self) -> ConvTranspose3dParams: ...

    @property
    def default_options(self) -> ConvTranspose3dOptions: ...

    def load(self, params: ConvTranspose3dParams, options: ConvTranspose3dOptions) -> void: ...

    @property
    def dimension_params(self) -> NeuronStrategyParams[ConvTranspose3dDimensionParams, ConvTranspose3dDimensionOptions]: ...

    @staticmethod
    def value_to_dimension(value: bool) -> Dimension3dView: ...

    def change_dimension(self, event: CheckBoxChangedEvent) -> bool: ...

    @property
    def dimension_switcher_program(self) -> Dimension3dSwitcher: ...

    def render(self, root: MainWindow) -> Layout: ...
