from abc import ABC, abstractmethod
from typing import TypeVar, TypedDict, Generic

from lib.gui.element.switcher.strategy import SwitcherStrategy

# Types

NeuronStrategyDependencies = TypeVar("NeuronStrategyDependencies", dict, TypedDict)
NeuronStrategyParams = TypeVar("NeuronStrategyParams", dict, TypedDict)
NeuronStrategyOptions = TypeVar("NeuronStrategyOptions", dict, TypedDict)


# Main

class NeuronStrategy(
    SwitcherStrategy[NeuronStrategyDependencies, NeuronStrategyParams],
    ABC,
    Generic[NeuronStrategyDependencies, NeuronStrategyParams, NeuronStrategyOptions]
):
    @property
    @abstractmethod
    def default_params(self) -> NeuronStrategyParams: ...

    @property
    @abstractmethod
    def default_options(self) -> NeuronStrategyOptions: ...
