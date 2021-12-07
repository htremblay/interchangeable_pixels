import copy

from algorithme_B4W4.New_Conception_v2.src.utils import Direction
from algorithme_B4W4.New_Conception_v2.src.models.pixel import Pixel, PixelColor
from algorithme_B4W4.New_Conception_v2.src.models.binary_image import BinaryImage
from algorithme_B4W4.New_Conception_v2.src.graphics.binary_image_displayer import BinaryImageDisplayer

BLACK_CONNEXITY = 8
WHITE_CONNEXITY = 8
INTERCHANGE_CONNEXITY = 8


class B8W8_Solver:
    # Constructor with a BinaryImage
    def __init__(self, binaryImageStart: BinaryImage, binaryImageFinal: BinaryImage):
        if binaryImageStart.size != binaryImageFinal.size:
            print("Size of images must be the same !")
            exit()

        self.__imageStart_saved = copy.copy(binaryImageStart)

        self.imageStart = binaryImageStart  # starting image

        self.imageFinal = binaryImageFinal  # final image
        self.array_interchange = []  # array of all interchange
        self.interchange = 0  # Number of swap

    def get_image_save(self) -> BinaryImage:
        return self.__imageStart_saved

    def solve(self) -> int:
        self.interchange = 0
        while True:
            if self.imageStart.is_vertical():
                break
            else:
                print("first image : ", self.interchange)
                temp = self.__resolve_image(self.imageStart)
                self.interchange += temp

        return self.interchange

    def __resolve_image(self, binary_image: BinaryImage) -> int:
        nb_interchange = 0
        p = self.get_p(binary_image)
        array_interchange = []

        if nb_interchange > 0:
            self.array_interchange = [*self.array_interchange, *array_interchange]
            binary_image.expand_image()
            binary_image.reduce_image()

        return nb_interchange