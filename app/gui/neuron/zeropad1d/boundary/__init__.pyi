from lib import void
from lib.gui.element.font import Font
from lib.gui.element.form import FormInput
from lib.gui.layout import Layout
from lib.gui.window import Window

from app.network.neuron.zeropad1d.boundary.params import ZeroPad1dBoundaryParams
from app.network.neuron.zeropad1d.boundary.options import ZeroPad1dBoundaryOptions
from app.gui.neuron.params import NeuronStrategyParams
from app.gui.neuron.strategy import NeuronStrategy
from app.gui.neuron.dependencies import NeuronBuilderDependencies


# Main

class UnboundedBoundaryStrategy(NeuronStrategy[ZeroPad1dBoundaryParams, ZeroPad1dBoundaryOptions]):
    class Direction(int):
        LEFT = ... #type: UnboundedBoundaryStrategy.Direction
        RIGHT = ... #type: UnboundedBoundaryStrategy.Direction

    _padding_left: FormInput[int]

    _padding_right: FormInput[int]

    _input_height: int
    _font_caption_title: Font

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    @property
    def params(self) -> NeuronStrategyParams[ZeroPad1dBoundaryParams, ZeroPad1dBoundaryOptions]: ...

    @property
    def default_params(self) -> ZeroPad1dBoundaryParams: ...

    @property
    def default_options(self) -> ZeroPad1dBoundaryOptions: ...

    def load(self, params: ZeroPad1dBoundaryParams, options: ZeroPad1dBoundaryOptions) -> void: ...

    def render(self, root: Window) -> Layout: ...
