from typing import TypedDict, Literal

# Types

ZeroPad3dBoundaryParam = int | tuple[int, int, int, int, int, int]

ZeroPad3dBoundaryParamsKeyof = Literal["padding"]


# Main

class ZeroPad3dBoundaryParams(TypedDict):
    padding: ZeroPad3dBoundaryParam
