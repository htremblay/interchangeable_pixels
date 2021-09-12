# Class that define a pixel
class Pixel:

    # Constructor with a precreated image
    def __init__(self, x, y, isBlack):
        self.x = x
        self.y = y
        self.black = isBlack
        self.elbow = False
        self.cutVertex = False
        self.anchor = False
        self.topPixel = False
        self.leadElbow = False

    def __str__(self):
        return ("My coords : (" + str(self.x) + ", " + str(self.y) + ") "
                + "\nBlack : " + str(self.black)
                + "\nElbow : " + str(self.elbow)
                + "\nCut vertex : " + str(self.cutVertex)
                + "\nAnchor : " + str(self.anchor)
                + "\nTop pixel : " + str(self.topPixel)
                + "\nLead Elbow : " + str(self.leadElbow))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y