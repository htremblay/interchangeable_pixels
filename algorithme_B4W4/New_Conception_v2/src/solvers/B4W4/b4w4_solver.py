from algorithme_B4W4.New_Conception_v2.src.models.binary_image import BinaryImage
from algorithme_B4W4.New_Conception_v2.src.solvers.B4W4.b4w4_elements import B4W4_Elements



BLACK_CONNEXITY = 4
WHITE_CONNEXITY = 4
INTERCHANGE_CONNEXITY = 8


# Class that will resolve B4W4 binary images
class B4W4_Solver:
    # Constructor with a BinaryImage
    def __init__(self, binaryImageStart: BinaryImage, binaryImageFinal: BinaryImage):
        if binaryImageStart.size != binaryImageFinal.size:
            print("Size of images must be the same !")
            exit()

        self.imageElementsStart = B4W4_Elements(binaryImageStart)    # starting image
        self.imageElementsFinal = B4W4_Elements(binaryImageFinal)    # final image
        self.interchange = 0                                         # Number of swap

    # todo implement method
    def solve(self) -> BinaryImage:
        raise NotImplementedError()
