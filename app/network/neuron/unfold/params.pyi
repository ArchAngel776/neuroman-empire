from typing import Literal, TypedDict

# Types

UnfoldParamsKeyof = Literal["kernel_size", "dilation", "padding", "stride"]


# Main

class UnfoldParams(TypedDict):
    kernel_size: list[int]
    dilation: list[int]
    padding: list[int]
    stride: list[int]
