from typing import TypedDict, Literal

# Types

ReplicationPad3dBoundaryParam = int | tuple[int, int, int, int, int, int]

ReplicationPad3dBoundaryParamsKeyof = Literal["padding"]


# Main

class ReplicationPad3dBoundaryParams(TypedDict):
    padding: ReplicationPad3dBoundaryParam
