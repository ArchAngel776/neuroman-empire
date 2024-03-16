from typing import TypedDict, Literal

# Types

ZeroPad2dBoundaryParam = int | tuple[int, int, int, int]

ZeroPad2dBoundaryParamsKeyof = Literal["padding"]


# Main

class ZeroPad2dBoundaryParams(TypedDict):
    padding: ZeroPad2dBoundaryParam
