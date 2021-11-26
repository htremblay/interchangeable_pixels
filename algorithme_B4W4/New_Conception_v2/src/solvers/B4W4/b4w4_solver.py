from algorithme_B4W4.New_Conception_v2.src.models.binary_image import BinaryImage
from algorithme_B4W4.New_Conception_v2.src.solvers.B4W4.b4w4_elements import B4W4_Elements
from algorithme_B4W4.New_Conception_v2.src.graphics.binary_image_displayer import BinaryImageDisplayer



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
        self.array_interchange = []
        self.interchange = 0                                         # Number of swap

    # todo implement method
    def solve(self) -> int:
        nb_echange = 0
        while True:
            if nb_echange == 31:
                displayer = BinaryImageDisplayer()
                displayer.show(self.imageElementsStart.binary_image)

            if self.imageElementsStart.binary_image.is_vertical():
                break
            else:
                print("first image : ", nb_echange)
                temp = self.imageElementsStart.lemme_6()
                nb_echange += temp if temp is not None else 0

        self.array_interchange = self.imageElementsStart.array_interchange

        # while True:
        #     if self.imageElementsFinal.binary_image.is_vertical():
        #         break
        #     else:
        #         temp = self.imageElementsFinal.lemme_6()
        #         nb_echange += temp if temp is not None else 0
        #
        # temp_array = self.imageElementsFinal.array_interchange[::-1]
        #
        # self.array_interchange = [*self.array_interchange, *temp_array]

        return nb_echange

