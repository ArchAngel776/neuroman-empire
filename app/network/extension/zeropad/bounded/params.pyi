from typing import TypedDict, Literal

# Types

ZeroPadBoundedParam = int

ZeroPadBoundedParamsKeyof = Literal["padding"]


# Main

class ZeroPadBoundedParams(TypedDict):
    padding: ZeroPadBoundedParam
