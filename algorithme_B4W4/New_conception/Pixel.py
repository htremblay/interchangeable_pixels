class Pixel:
    # Constructor with a precreated image
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.neighbours = []    # Pour pouvoir faire un graphe


    def __str__(self):
        return ("[My coords : (" + str(self.x) + ", " + str(self.y) + "), "
                + "Color : " + str(self.color)
                + "]")

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash(str(self.x + self.y))