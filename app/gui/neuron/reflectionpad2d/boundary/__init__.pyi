from lib import void
from lib.gui.element.font import Font
from lib.gui.element.form import FormInput
from lib.gui.layout import Layout
from lib.gui.window import Window

from app.network.neuron.reflectionpad2d.boundary.params import ReflectionPad2dBoundaryParams
from app.network.neuron.reflectionpad2d.boundary.options import ReflectionPad2dBoundaryOptions
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies


# Main

class UnboundedBoundaryStrategy(NeuronStrategy[ReflectionPad2dBoundaryParams, ReflectionPad2dBoundaryOptions]):
    class Direction(int):
        LEFT = ... #type: UnboundedBoundaryStrategy.Direction
        RIGHT = ... #type: UnboundedBoundaryStrategy.Direction
        TOP = ... #type: UnboundedBoundaryStrategy.Direction
        BOTTOM = ... #type: UnboundedBoundaryStrategy.Direction

    _padding_left: FormInput[int]

    _padding_right: FormInput[int]

    _padding_top: FormInput[int]

    _padding_bottom: FormInput[int]

    _input_height: int
    _font_caption_title: Font

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[ReflectionPad2dBoundaryParams, ReflectionPad2dBoundaryOptions]: ...

    @property
    def default_params(self) -> ReflectionPad2dBoundaryParams: ...

    @property
    def default_options(self) -> ReflectionPad2dBoundaryOptions: ...

    def load(self, params: ReflectionPad2dBoundaryParams, options: ReflectionPad2dBoundaryOptions) -> void: ...

    def render(self, root: Window) -> Layout: ...
