from typing import TypedDict, Literal

# Types

ConstantPadBoundedParam = int

ConstantPadBoundedParamsKeyof = Literal["padding"]


# Main

class ConstantPadBoundedParams(TypedDict):
    padding: ConstantPadBoundedParam
