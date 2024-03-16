from typing import TypedDict, Literal

# Types

ConstantPad1dBoundaryParam = int | tuple[int, int]

ConstantPad1dBoundaryParamsKeyof = Literal["padding"]


# Main

class ConstantPad1dBoundaryParams(TypedDict):
    padding: ConstantPad1dBoundaryParam
