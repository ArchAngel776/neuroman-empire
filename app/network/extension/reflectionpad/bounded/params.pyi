from typing import TypedDict, Literal

# Types

ReflectionPadBoundedParam = int

ReflectionPadBoundedParamsKeyof = Literal["padding"]


# Main

class ReflectionPadBoundedParams(TypedDict):
    padding: ReflectionPadBoundedParam
