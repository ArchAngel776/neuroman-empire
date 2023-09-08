from typing import Generic, TypeVar, ParamSpec, Callable

# Types

TDecorator = TypeVar("TDecorator", bound="Decorator")

DecoratorResult = TypeVar("DecoratorResult")
DecoratorArguments = ParamSpec("DecoratorArguments")


# Main

class Decorator(Generic[DecoratorResult, DecoratorArguments]):
    _original: Callable[DecoratorArguments, DecoratorResult]

    def __init__(self, original: Callable[DecoratorArguments, DecoratorResult]) -> None: ...

    def config(self: TDecorator, *args: DecoratorArguments.args, **kwargs: DecoratorArguments.kwargs) -> TDecorator: ...

    def method(self, *args: DecoratorArguments.args, **kwargs: DecoratorArguments.kwargs) -> DecoratorResult: ...
