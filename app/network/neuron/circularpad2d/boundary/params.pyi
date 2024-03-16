from typing import TypedDict, Literal

# Types

CircularPad2dBoundaryParam = int | tuple[int, int, int, int]

CircularPad2dBoundaryParamsKeyof = Literal["padding"]


# Main

class CircularPad2dBoundaryParams(TypedDict):
    padding: CircularPad2dBoundaryParam
