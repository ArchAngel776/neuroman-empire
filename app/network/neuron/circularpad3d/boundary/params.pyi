from typing import TypedDict, Literal

# Types

CircularPad3dBoundaryParam = int | tuple[int, int, int, int, int, int]

CircularPad3dBoundaryParamsKeyof = Literal["padding"]


# Main

class CircularPad3dBoundaryParams(TypedDict):
    padding: CircularPad3dBoundaryParam
