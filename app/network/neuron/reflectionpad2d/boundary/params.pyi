from typing import TypedDict, Literal

# Types

ReflectionPad2dBoundaryParam = int | tuple[int, int, int, int]

ReflectionPad2dBoundaryParamsKeyof = Literal["padding"]


# Main

class ReflectionPad2dBoundaryParams(TypedDict):
    padding: ReflectionPad2dBoundaryParam
