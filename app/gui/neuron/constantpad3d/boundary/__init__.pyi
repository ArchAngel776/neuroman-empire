from lib import void
from lib.gui.element.font import Font
from lib.gui.element.form import FormInput
from lib.gui.layout import Layout
from lib.gui.window import Window

from app.network.neuron.constantpad3d.boundary.params import ConstantPad3dBoundaryParams
from app.network.neuron.constantpad3d.boundary.options import ConstantPad3dBoundaryOptions
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies


# Main

class UnboundedBoundaryStrategy(NeuronStrategy[ConstantPad3dBoundaryParams, ConstantPad3dBoundaryOptions]):
    class Direction(int):
        LEFT = ... #type: UnboundedBoundaryStrategy.Direction
        RIGHT = ... #type: UnboundedBoundaryStrategy.Direction
        TOP = ... #type: UnboundedBoundaryStrategy.Direction
        BOTTOM = ... #type: UnboundedBoundaryStrategy.Direction
        FRONT = ... #type: UnboundedBoundaryStrategy.Direction
        BACK = ... #type: UnboundedBoundaryStrategy.Direction

    _padding_left: FormInput[int]

    _padding_right: FormInput[int]

    _padding_top: FormInput[int]

    _padding_bottom: FormInput[int]

    _padding_front: FormInput[int]

    _padding_back: FormInput[int]

    _input_height: int
    _font_caption_title: Font

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[ConstantPad3dBoundaryParams, ConstantPad3dBoundaryOptions]: ...

    @property
    def default_params(self) -> ConstantPad3dBoundaryParams: ...

    @property
    def default_options(self) -> ConstantPad3dBoundaryOptions: ...

    def load(self, params: ConstantPad3dBoundaryParams, options: ConstantPad3dBoundaryOptions) -> void: ...

    def render(self, root: Window) -> Layout: ...
