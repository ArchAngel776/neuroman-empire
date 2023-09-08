from typing import Callable, TypeVar, ParamSpec

from .decorator import Decorator

# Types

DecoratorMethodResult = TypeVar("DecoratorMethodResult")
DecoratorMethodArguments = ParamSpec("DecoratorMethodArguments")


# Main

def method(decorator: type[Decorator[DecoratorMethodResult, DecoratorMethodArguments]]) -> Callable[
    [Callable[DecoratorMethodArguments, DecoratorMethodResult]],
    Callable[DecoratorMethodArguments, DecoratorMethodResult]
]:
    def wrapper(target: Callable[DecoratorMethodArguments, DecoratorMethodResult]) -> Callable[
        DecoratorMethodArguments, DecoratorMethodResult
    ]:
        def inner(
                *args: DecoratorMethodArguments.args,
                **kwargs: DecoratorMethodArguments.kwargs
        ) -> DecoratorMethodResult: ...
