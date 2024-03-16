from typing import TypedDict, Literal

# Types

ReflectionPad1dBoundaryParam = int | tuple[int, int]

ReflectionPad1dBoundaryParamsKeyof = Literal["padding"]


# Main

class ReflectionPad1dBoundaryParams(TypedDict):
    padding: ReflectionPad1dBoundaryParam
