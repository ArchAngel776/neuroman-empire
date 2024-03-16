from typing import TypedDict, Literal

# Types

ReplicationPadBoundedParam = int

ReplicationPadBoundedParamsKeyof = Literal["padding"]


# Main

class ReplicationPadBoundedParams(TypedDict):
    padding: ReplicationPadBoundedParam
