from typing import Generic, TypeVar, TypedDict, Callable, Optional

from lib import void
from lib.foundations.data_provider import DataProvider

from app.gui.neuron.strategy import NeuronStrategy

# Types

NeuronPayloadProviderParams = TypeVar("NeuronPayloadProviderParams", dict, TypedDict)
NeuronPayloadProviderOptions = TypeVar("NeuronPayloadProviderOptions", dict, TypedDict)


# Main

class NeuronPayloadProvider(
    DataProvider[
        tuple[NeuronPayloadProviderParams, NeuronPayloadProviderOptions],
        Callable[[NeuronStrategy[NeuronPayloadProviderParams, NeuronPayloadProviderOptions]], void]
    ],
    Generic[NeuronPayloadProviderParams, NeuronPayloadProviderOptions]
):
    _params: Optional[NeuronPayloadProviderParams]

    _options: Optional[NeuronPayloadProviderOptions]

    def __init__(self) -> None: ...

    def add(self, params: NeuronPayloadProviderParams, options: NeuronPayloadProviderOptions) -> void: ...

    def provide(self) -> Callable[
        [NeuronStrategy[NeuronPayloadProviderParams, NeuronPayloadProviderOptions]], void
    ]: ...

    def clear(self) -> void: ...

    def callback(
            self,
            neuron_strategy: NeuronStrategy[NeuronPayloadProviderParams, NeuronPayloadProviderOptions]
    ) -> void: ...

    @property
    def params(self) -> Optional[NeuronPayloadProviderParams]: ...

    @property
    def options(self) -> Optional[NeuronPayloadProviderOptions]: ...
