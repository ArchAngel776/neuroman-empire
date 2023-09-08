from abc import ABC, abstractmethod
from typing import Generic, TypeVar, TypedDict

from .type import NeuronType

# Types

NeuronParams = TypeVar("NeuronParams", dict, TypedDict)
NeuronOptions = TypeVar("NeuronOptions", dict, TypedDict)


# Main

class Neuron(ABC, Generic[NeuronParams, NeuronOptions]):
    _name: str
    _params: NeuronParams
    _options: NeuronOptions

    def __init__(self, name: str, params: NeuronParams, options: NeuronOptions) -> None: ...

    @staticmethod
    @abstractmethod
    def type() -> NeuronType: ...

    @staticmethod
    @abstractmethod
    def title() -> str: ...

    @property
    def name(self) -> str: ...

    @property
    def params(self) -> NeuronParams: ...

    @property
    def options(self) -> NeuronOptions: ...

    @staticmethod
    @abstractmethod
    def default_params() -> NeuronParams: ...

    @staticmethod
    @abstractmethod
    def default_options() -> NeuronOptions: ...
