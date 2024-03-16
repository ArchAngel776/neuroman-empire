from typing import TypedDict, Literal

# Types

ReplicationPad2dBoundaryParam = int | tuple[int, int, int, int]

ReplicationPad2dBoundaryParamsKeyof = Literal["padding"]


# Main

class ReplicationPad2dBoundaryParams(TypedDict):
    padding: ReplicationPad2dBoundaryParam
