import copy

from algorithme_B4W4.New_Conception_v2.src.utils import Direction
from algorithme_B4W4.New_Conception_v2.src.models.pixel import Pixel, PixelColor
from algorithme_B4W4.New_Conception_v2.src.models.binary_image import BinaryImage
from algorithme_B4W4.New_Conception_v2.src.graphics.binary_image_displayer import BinaryImageDisplayer
from algorithme_B4W4.New_Conception_v2.src.solvers.B4W8.b4w8_solver import B4W8_Solver
from algorithme_B4W4.New_Conception_v2.src.solvers.B8W4.b8w4_solver import B8W4_Solver

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
                # if self.interchange % 100 == 0:
                #     displayer = BinaryImageDisplayer()
                #     displayer.show(self.imageStart, subtitle=self.interchange)
                temp = self.resolve_image(self.imageStart)
                self.interchange += temp

        return self.interchange

    def resolve_image(self, binary_image: BinaryImage) -> int:
        nb_interchange = 0
        p = B8W4_Solver.get_p(binary_image)
        array_interchange = []

        if not binary_image.is_cut_vertex(p):
            n = binary_image.get_pixel_adjacent(p, Direction.N)
            if n.color == PixelColor.BLACK:
                n_e = binary_image.get_pixel_directional(p, [Direction.N, Direction.E])
                array_interchange.append((p.get_coords(), n_e.get_coords()))
            else:
                n_w = binary_image.get_pixel_directional(p, [Direction.N, Direction.W])
                w = binary_image.get_pixel_adjacent(p, Direction.W)
                if n_w.color == PixelColor.BLACK or w.color == PixelColor.BLACK:
                    array_interchange.append((p.get_coords(), n.get_coords()))
                else:
                    w_w = binary_image.get_pixel_directional(p, [Direction.W, Direction.W])
                    if w_w.color == PixelColor.BLACK:
                        array_interchange.append((p.get_coords(), n_w.get_coords()))
                    else:
                        array_interchange.append((p.get_coords(), w.get_coords()))
        else:
            n_w = binary_image.get_pixel_directional(p, [Direction.N, Direction.W])
            w = binary_image.get_pixel_adjacent(p, Direction.W)
            if n_w.color == PixelColor.BLACK:
                array_interchange.append((p.get_coords(), w.get_coords()))
            else:
                if not binary_image.is_cut_vertex(w):
                    array_interchange.append((p.get_coords(), w.get_coords()))
                else:
                    array_interchange.append((p.get_coords(), n_w.get_coords()))

        nb_interchange = binary_image.multiple_swap_pixels(array_interchange)


        if nb_interchange > 0:
            self.array_interchange = [*self.array_interchange, *array_interchange]
            binary_image.expand_image()
            binary_image.reduce_image()

        return nb_interchange