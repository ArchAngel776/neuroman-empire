from typing import TypedDict, Literal

# Types

CircularPad1dBoundaryParam = int | tuple[int, int]

CircularPad1dBoundaryParamsKeyof = Literal["padding"]


# Main

class CircularPad1dBoundaryParams(TypedDict):
    padding: CircularPad1dBoundaryParam
