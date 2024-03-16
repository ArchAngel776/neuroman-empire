from typing import TypedDict, Literal

# Types

ZeroPad1dBoundaryParam = int | tuple[int, int]

ZeroPad1dBoundaryParamsKeyof = Literal["padding"]


# Main

class ZeroPad1dBoundaryParams(TypedDict):
    padding: ZeroPad1dBoundaryParam
