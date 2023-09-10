from typing import Generic, TypeVar, TypedDict

# Type

NeuronParams = TypeVar("NeuronParams", dict, TypedDict)
NeuronOptions = TypeVar("NeuronOptions", dict, TypedDict)


# Main

class NeuronStrategyParams(dict, Generic[NeuronParams, NeuronOptions]):
    _params: NeuronParams
    _options: NeuronOptions

    def __init__(self, params: NeuronParams, options: NeuronOptions) -> None: ...

    @property
    def params(self) -> NeuronParams: ...

    @property
    def options(self) -> NeuronOptions: ...
