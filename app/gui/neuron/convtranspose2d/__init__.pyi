from lib import void
from lib.gui.element.form import FormInput
from lib.gui.event.check_box_changed import CheckBoxChangedEvent
from lib.gui.layout import Layout

from app.network.neuron.convtranspose2d.params import ConvTranspose2dParams
from app.network.neuron.convtranspose2d.options import ConvTranspose2dOptions
from app.network.neuron.convtranspose2d.dimension.params import ConvTranspose2dDimensionParams
from app.network.neuron.convtranspose2d.dimension.options import ConvTranspose2dDimensionOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams

from .view import Dimension2dSwitcher, Dimension2dView


# Main

class NeuronBuilderTransposedConvolution2dStrategy(NeuronStrategy[ConvTranspose2dParams, ConvTranspose2dOptions]):
    class Watch(str):
        DIMENSION_SWITCHER = ... #type: NeuronBuilderTransposedConvolution2dStrategy.Watch

    _input_channels: FormInput[int]
    _output_channels: FormInput[int]
    _groups: FormInput[int]
    _bias: FormInput[bool]

    _reflection: FormInput[bool]

    _input_height: int

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[ConvTranspose2dParams, ConvTranspose2dOptions]: ...

    @property
    def default_params(self) -> ConvTranspose2dParams: ...

    @property
    def default_options(self) -> ConvTranspose2dOptions: ...

    def load(self, params: ConvTranspose2dParams, options: ConvTranspose2dOptions) -> void: ...

    @property
    def dimension_params(self) -> NeuronStrategyParams[ConvTranspose2dDimensionParams, ConvTranspose2dDimensionOptions]: ...

    @staticmethod
    def value_to_dimension(value: bool) -> Dimension2dView: ...

    def change_dimension(self, event: CheckBoxChangedEvent) -> bool: ...

    @property
    def dimension_switcher_program(self) -> Dimension2dSwitcher: ...

    def render(self, root: MainWindow) -> Layout: ...
