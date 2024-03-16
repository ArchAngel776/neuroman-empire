from typing import TypedDict, Literal

# Types

ReplicationPad1dBoundaryParam = int | tuple[int, int]

ReplicationPad1dBoundaryParamsKeyof = Literal["padding"]


# Main

class ReplicationPad1dBoundaryParams(TypedDict):
    padding: ReplicationPad1dBoundaryParam
