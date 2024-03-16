from typing import TypedDict, Literal

# Types

ConstantPad3dBoundaryParam = int | tuple[int, int, int, int, int, int]

ConstantPad3dBoundaryParamsKeyof = Literal["padding"]


# Main

class ConstantPad3dBoundaryParams(TypedDict):
    padding: ConstantPad3dBoundaryParam
