from enum import IntEnum


class PixelColor(IntEnum):
    """Defines the color of a Pixel"""
    WHITE = 0
    BLACK = 1
    BOTH = 2


class Pixel:
    """Defines a Pixel in a Binary Image"""

    def __init__(self, x: int, y: int, color: PixelColor):
        """Creates a pixel with a position and a color"""

        self.x = x
        self.y = y
        self.color = color

        self.neighbours = []

    def __str__(self) -> str:
        return f'[Coords : ({self.x}, {self.y}), Color : {self.color.name}]'

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    def __hash__(self) -> int:
        return hash(str(self.x + self.y))

    def is_adjacent(self, pixel, connexity=4) -> bool:
        """Returns true if pixel is adjacent to self given the connexity"""

        if connexity == 4:
            return pow(self.x - pixel.x, 2) + pow(self.y - pixel.y, 2) <= 1
        elif connexity == 8:
            return pow(self.x - pixel.x, 2) + pow(self.y - pixel.y, 2) <= 2
        else:
            raise ValueError("Error : invalid connexity!")