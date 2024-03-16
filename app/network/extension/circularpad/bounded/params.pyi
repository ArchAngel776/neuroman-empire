from typing import TypedDict, Literal

# Types

CircularPadBoundedParam = int

CircularPadBoundedParamsKeyof = Literal["padding"]


# Main

class CircularPadBoundedParams(TypedDict):
    padding: CircularPadBoundedParam
