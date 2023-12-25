from typing import Literal, TypedDict

# Types

FoldParamsKeyof = Literal["output_size", "kernel_size", "dilation", "padding", "stride"]


# Main

class FoldParams(TypedDict):
    output_size: list[int]
    kernel_size: list[int]
    dilation: list[int]
    padding: list[int]
    stride: list[int]
