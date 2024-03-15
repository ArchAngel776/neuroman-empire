from typing import TypedDict, Literal, NotRequired

# Types

AdaptiveMaxPool2dDimensionOptionsKeyof = Literal["output_enabled"]


# Main

class AdaptiveMaxPool2dDimensionOptions(TypedDict):
    output_enabled: NotRequired[tuple[bool, bool]]
