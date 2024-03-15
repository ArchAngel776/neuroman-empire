from typing import TypedDict, Literal, NotRequired

# Types

AdaptiveMaxPool3dDimensionOptionsKeyof = Literal["output_enabled"]


# Main

class AdaptiveMaxPool3dDimensionOptions(TypedDict):
    output_enabled: NotRequired[tuple[bool, bool, bool]]
