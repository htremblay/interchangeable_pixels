from enum import IntEnum


class Direction(IntEnum):
    """Enum for cardinal directions (N for North, E for East, S for South and W for West)"""
    N = 1
    NE = 5
    E = 2
    SE = 6
    S = 3
    SW = 7
    W = 4
    NW = 8


def array_to_string(array: list) -> str:
    """Returns given array to string"""

    res = "["
    for elem in array:
        res += str(elem) + ", "
    res += "]"
    return res
