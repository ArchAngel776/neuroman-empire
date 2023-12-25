from abc import ABC, abstractmethod
from typing import TypeVar, TypedDict, Generic

from lib import void
from lib.gui.element.switcher.strategy import SwitcherStrategy

from app.gui.neuron.params import NeuronStrategyParams as StrategyParams

# Types

NeuronStrategyParams = TypeVar("NeuronStrategyParams", dict, TypedDict)
NeuronStrategyOptions = TypeVar("NeuronStrategyOptions", dict, TypedDict)


# Main

class NeuronStrategy(
    SwitcherStrategy[{}, StrategyParams[NeuronStrategyParams, NeuronStrategyOptions]],
    ABC,
    Generic[NeuronStrategyParams, NeuronStrategyOptions]
):
    def __init__(self) -> None: ...

    @property
    @abstractmethod
    def default_params(self) -> NeuronStrategyParams: ...

    @property
    @abstractmethod
    def default_options(self) -> NeuronStrategyOptions: ...

    @abstractmethod
    def load(self, params: NeuronStrategyParams, options: NeuronStrategyOptions) -> void: ...
