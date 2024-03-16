from typing import TypedDict, Literal

# Types

ReflectionPad3dBoundaryParam = int | tuple[int, int, int, int, int, int]

ReflectionPad3dBoundaryParamsKeyof = Literal["padding"]


# Main

class ReflectionPad3dBoundaryParams(TypedDict):
    padding: ReflectionPad3dBoundaryParam
