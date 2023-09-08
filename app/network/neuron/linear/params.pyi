from typing import TypedDict, Literal

# Types

LinearParamsKeyof = Literal["in_features", "out_features", "bias"]


# Main

class LinearParams(TypedDict):
    in_features: int
    out_features: int
    bias: bool
