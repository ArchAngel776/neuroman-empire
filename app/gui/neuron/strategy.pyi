from abc import ABC, abstractmethod
from typing import TypeVar, TypedDict, Generic

from lib import void
from lib.gui.element.component.switcher.strategy import SwitcherStrategy

from app.gui.neuron.dependencies import NeuronBuilderDependencies
from app.gui.neuron.params import NeuronStrategyParams as StrategyParams
from app.gui.neuron.payload_provider import NeuronPayloadProvider

# Types

NeuronStrategyParams = TypeVar("NeuronStrategyParams", dict, TypedDict)
NeuronStrategyOptions = TypeVar("NeuronStrategyOptions", dict, TypedDict)


# Main

class NeuronStrategy(
    SwitcherStrategy[NeuronBuilderDependencies, StrategyParams[NeuronStrategyParams, NeuronStrategyOptions]],
    ABC,
    Generic[NeuronStrategyParams, NeuronStrategyOptions]
):
    _neuron_payload_provider: NeuronPayloadProvider[NeuronStrategyParams, NeuronStrategyOptions]

    def __init__(self, dependencies: NeuronBuilderDependencies) -> None: ...

    def beforeClose(self) -> void: ...

    @property
    @abstractmethod
    def default_params(self) -> NeuronStrategyParams: ...

    @property
    @abstractmethod
    def default_options(self) -> NeuronStrategyOptions: ...

    @abstractmethod
    def load(self, params: NeuronStrategyParams, options: NeuronStrategyOptions) -> void: ...

    def read(self, params: NeuronStrategyParams, options: NeuronStrategyOptions) -> void: ...

    @property
    def neuron_payload_provider(self) -> NeuronPayloadProvider[NeuronStrategyParams, NeuronStrategyOptions]: ...
