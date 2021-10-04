from enum import Enum


# Enum for cardinal directions
# N for North, E for East, S for South, W for West
class Direction(Enum):
    N = 1
    NE = 5
    E = 2
    SE = 6
    S = 3
    SW = 7
    W = 4
    NW = 8


# Enum for cardinal directions
# N for North, E for East, S for South, W for West
class BinaryElement(Enum):
    White = 0
    Black = 1
    Both = 2
