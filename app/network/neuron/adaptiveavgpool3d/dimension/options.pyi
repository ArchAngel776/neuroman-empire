from typing import TypedDict, Literal, NotRequired

# Types

AdaptiveAvgPool3dDimensionOptionsKeyof = Literal["output_enabled"]


# Main

class AdaptiveAvgPool3dDimensionOptions(TypedDict):
    output_enabled: NotRequired[tuple[bool, bool, bool]]
