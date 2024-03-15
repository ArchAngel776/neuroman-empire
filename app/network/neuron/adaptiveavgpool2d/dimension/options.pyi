from typing import TypedDict, Literal, NotRequired

# Types

AdaptiveAvgPool2dDimensionOptionsKeyof = Literal["output_enabled"]


# Main

class AdaptiveAvgPool2dDimensionOptions(TypedDict):
    output_enabled: NotRequired[tuple[bool, bool]]
