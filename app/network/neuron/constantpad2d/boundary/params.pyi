from typing import TypedDict, Literal

# Types

ConstantPad2dBoundaryParam = int | tuple[int, int, int, int]

ConstantPad2dBoundaryParamsKeyof = Literal["padding"]


# Main

class ConstantPad2dBoundaryParams(TypedDict):
    padding: ConstantPad2dBoundaryParam
