import copy

from algorithme_B4W4.New_Conception_v2.src.utils import Direction
from algorithme_B4W4.New_Conception_v2.src.models.pixel import Pixel, PixelColor
from algorithme_B4W4.New_Conception_v2.src.models.binary_image import BinaryImage
from algorithme_B4W4.New_Conception_v2.src.graphics.binary_image_displayer import BinaryImageDisplayer


BLACK_CONNEXITY = 4
WHITE_CONNEXITY = 8
INTERCHANGE_CONNEXITY = 8


# Class that will resolve B4W4 binary images
class B4W8_Solver:
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
        while True:
            if self.imageStart.is_vertical():
                break
            else:
                self.interchange += self.resolve_image(self.imageStart)

        # Todo Solving 2nd image

        return self.interchange

    def resolve_image(self, binary_image: BinaryImage) -> int:
        nb_interchange = 0
        p = self.get_p(binary_image)
        array_interchange = []

        # displayer = BinaryImageDisplayer()
        # displayer.show(binary_image)

        if not binary_image.is_cut_vertex(p):
            n = binary_image.get_pixel_directional(p, [Direction.N])
            n_w = binary_image.get_pixel_directional(p, [Direction.N, Direction.W])
            if n.color == PixelColor.BLACK:
                n_e = binary_image.get_pixel_directional(p, [Direction.N, Direction.E])
                array_interchange.append((p.get_coords(), n_e.get_coords()))
                binary_image.swap_pixels(p.get_coords(), n_e.get_coords())
                nb_interchange += 1
            elif n_w.color == PixelColor.BLACK:
                array_interchange.append((p.get_coords(), n.get_coords()))
                binary_image.swap_pixels(p.get_coords(), n.get_coords())
                nb_interchange += 1
            else:
                array_interchange.append((p.get_coords(), n_w.get_coords()))
                binary_image.swap_pixels(p.get_coords(), n_w.get_coords())
                nb_interchange += 1
        else:
            w = binary_image.get_pixel_directional(p, [Direction.W])
            n = binary_image.get_pixel_directional(p, [Direction.N])
            n_w = binary_image.get_pixel_directional(p, [Direction.N, Direction.W])
            g = n_w_w = binary_image.get_pixel_directional(p, [Direction.N, Direction.W, Direction.W])
            n_n_w = binary_image.get_pixel_directional(p, [Direction.N, Direction.N, Direction.W])
            if not binary_image.is_cut_vertex(n_w):
                array_interchange.append((p.get_coords(), n_w.get_coords()))
                binary_image.swap_pixels(p.get_coords(), n_w.get_coords())
                nb_interchange += 1

            elif g.color == PixelColor.BLACK: # if we're here g should be black
                path_found, west_path = self.find_path(g, p, binary_image,
                                                       pixel_bridge=w, connexity=binary_image.black_connexity)

                if g.color != PixelColor.WHITE and path_found and west_path:
                    array_interchange.append((w.get_coords(), n_w.get_coords()))
                    binary_image.swap_pixels(w.get_coords(), n_w.get_coords())
                    nb_interchange += 1
                else:
                    if n_n_w.color == PixelColor.WHITE:
                        array_interchange.append((n.get_coords(), n_w.get_coords()))
                        binary_image.swap_pixels(n.get_coords(), n_w.get_coords())
                        nb_interchange += 1
                    else:
                        array_interchange.append((g.get_coords(),
                                                  binary_image.get_pixel_directional(g, [Direction.E]).get_coords()))
                        array_interchange.append((n.get_coords(),
                                                  binary_image.get_pixel_directional(n, [Direction.N, Direction.E]).get_coords()))
                        nb_interchange += binary_image.multiple_swap_pixels(array_interchange)

        if nb_interchange > 0:
            self.array_interchange = [*self.array_interchange, *array_interchange]
            binary_image.expand_image()
            binary_image.reduce_image()

        return nb_interchange

    @staticmethod
    def find_path(g: Pixel, p: Pixel, img: BinaryImage, connexity=4, pixel_bridge=None) -> (bool, bool):
        visited = [False] * len(img.black_pixels)

        queue = [g]

        visited[img.black_pixels.index(g)] = True

        pixel_bridge_bool = False

        while queue:
            n = queue.pop(0)

            if pixel_bridge is not None and n == pixel_bridge:
                pixel_bridge_bool = True

            if n == p:
                return True, pixel_bridge_bool

            ajd_pixels = img.get_neighbours(n, connexity, color=PixelColor.BLACK)
            for i in ajd_pixels:
                if not visited[img.black_pixels.index(i)]:
                    if i not in queue:
                        queue.append(i)
                    visited[img.black_pixels.index(n)] = True

        print(visited)

        return False, pixel_bridge_bool

    @staticmethod
    def get_p(img: BinaryImage) -> Pixel:
        p = None

        for pix in img.black_pixels:
            s = img.get_pixel_directional(pix, [Direction.S])
            if s.color == PixelColor.WHITE:
                if p is None or pix.x >= p.x:
                    east_clear = B4W8_Solver.direction_clear(pix, Direction.E, img)
                    north_clear = B4W8_Solver.direction_clear(img.get_pixel_adjacent(pix, Direction.E),
                                                              Direction.N, img, p_included=True)

                    if east_clear and north_clear:
                        p = pix
        return p

    @staticmethod
    def direction_clear(p: Pixel, direction: Direction, img: BinaryImage, p_included=False) -> bool:
        if p_included:
            current_pixel = p
        else:
            current_pixel = img.get_pixel_adjacent(p, direction)

        while 0 < current_pixel.x < img.height and 0 < current_pixel.y < img.width:
            if current_pixel.color != PixelColor.WHITE:
                return False
            else:
                current_pixel = img.get_pixel_adjacent(current_pixel, direction)

        return True
