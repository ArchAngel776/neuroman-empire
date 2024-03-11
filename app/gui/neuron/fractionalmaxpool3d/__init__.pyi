from lib import void
from lib.gui.element.form import FormInput
from lib.gui.event.check_box_changed import CheckBoxChangedEvent
from lib.gui.layout import Layout

from app.network.neuron.fractionalmaxpool3d.params import FractionalMaxPool3dParams
from app.network.neuron.fractionalmaxpool3d.options import FractionalMaxPool3dOptions
from app.network.neuron.fractionalmaxpool3d.dimension.params import FractionalMaxPool3dDimensionParams
from app.network.neuron.fractionalmaxpool3d.dimension.options import FractionalMaxPool3dDimensionOptions
from app.gui import MainWindow
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams

from .view import Dimension3dSwitcher


# Main

class NeuronBuilderFractionalMaxPooling3dStrategy(NeuronStrategy[FractionalMaxPool3dParams, FractionalMaxPool3dOptions]):
    class Watch(str):
        DIMENSION_SWITCHER = ... #type: NeuronBuilderFractionalMaxPooling3dStrategy.Watch

    _return_indices: FormInput[bool]

    _reflection: FormInput[bool]

    _input_height: int

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[FractionalMaxPool3dParams, FractionalMaxPool3dOptions]: ...

    @property
    def default_params(self) -> FractionalMaxPool3dParams: ...

    @property
    def default_options(self) -> FractionalMaxPool3dOptions: ...

    def load(self, params: FractionalMaxPool3dParams, options: FractionalMaxPool3dOptions) -> void: ...

    @property
    def dimension_params(self) -> NeuronStrategyParams[
        FractionalMaxPool3dDimensionParams, FractionalMaxPool3dDimensionOptions
    ]: ...

    def change_dimension(self, event: CheckBoxChangedEvent) -> bool: ...

    @property
    def dimension_switcher_program(self) -> Dimension3dSwitcher: ...

    def render(self, root: MainWindow) -> Layout: ...
