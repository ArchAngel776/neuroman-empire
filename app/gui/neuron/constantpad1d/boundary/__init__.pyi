from lib import void
from lib.gui.element.font import Font
from lib.gui.element.form import FormInput
from lib.gui.layout import Layout
from lib.gui.window import Window

from app.network.neuron.constantpad1d.boundary.params import ConstantPad1dBoundaryParams
from app.network.neuron.constantpad1d.boundary.options import ConstantPad1dBoundaryOptions
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies


# Main

class UnboundedBoundaryStrategy(NeuronStrategy[ConstantPad1dBoundaryParams, ConstantPad1dBoundaryOptions]):
    class Direction(int):
        LEFT = ... #type: UnboundedBoundaryStrategy.Direction
        RIGHT = ... #type: UnboundedBoundaryStrategy.Direction

    _padding_left: FormInput[int]

    _padding_right: FormInput[int]

    _input_height: int
    _font_caption_title: Font

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[ConstantPad1dBoundaryParams, ConstantPad1dBoundaryOptions]: ...

    @property
    def default_params(self) -> ConstantPad1dBoundaryParams: ...

    @property
    def default_options(self) -> ConstantPad1dBoundaryOptions: ...

    def load(self, params: ConstantPad1dBoundaryParams, options: ConstantPad1dBoundaryOptions) -> void: ...

    def render(self, root: Window) -> Layout: ...
