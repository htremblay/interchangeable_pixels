import copy

from algorithme_B4W4.New_Conception_v2.src.utils import Direction
from algorithme_B4W4.New_Conception_v2.src.models.pixel import Pixel, PixelColor
from algorithme_B4W4.New_Conception_v2.src.models.binary_image import BinaryImage
from algorithme_B4W4.New_Conception_v2.src.solvers.B4W8.b4w8_solver import B4W8_Solver
from algorithme_B4W4.New_Conception_v2.src.graphics.binary_image_displayer import BinaryImageDisplayer

BLACK_CONNEXITY = 8
WHITE_CONNEXITY = 4
INTERCHANGE_CONNEXITY = 8


class B8W4_Solver:
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

        # Todo Solving 2nd image

        return self.interchange

    def resolve_image(self, binary_image: BinaryImage) -> int:
        nb_interchange = 0
        p = self.get_p(binary_image)
        array_interchange = []

        if not binary_image.is_cut_vertex(p):
            n = binary_image.get_pixel_adjacent(p, Direction.N)
            w = binary_image.get_pixel_adjacent(p, Direction.W)
            n_w = binary_image.get_pixel_directional(p, [Direction.N, Direction.W])
            s_w = binary_image.get_pixel_directional(p, [Direction.S, Direction.W])
            if n.color == PixelColor.BLACK:
                n_e = binary_image.get_pixel_directional(p, [Direction.N, Direction.E])
                array_interchange.append((p.get_coords(), n_e.get_coords()))
                binary_image.swap_pixels(p.get_coords(), n_e.get_coords())
                nb_interchange += 1
            elif n_w.color == PixelColor.BLACK or w.color == PixelColor.BLACK:
                array_interchange.append((p.get_coords(), n.get_coords()))
                binary_image.swap_pixels(p.get_coords(), n.get_coords())
                nb_interchange += 1
            elif n_w.color == PixelColor.WHITE and w.color == PixelColor.WHITE and s_w.color == PixelColor.BLACK:
                if not binary_image.is_cut_vertex(w):
                    array_interchange.append((p.get_coords(), w.get_coords()))
                    binary_image.swap_pixels(p.get_coords(), w.get_coords())
                    nb_interchange += 1
                else:
                    array_interchange.append((p.get_coords(), n_w.get_coords()))
                    binary_image.swap_pixels(p.get_coords(), n_w.get_coords())
                    nb_interchange += 1
        else:
            w = binary_image.get_pixel_adjacent(p, Direction.W)
            if not binary_image.is_cut_vertex(w):
                array_interchange.append((p.get_coords(), w.get_coords()))
                binary_image.swap_pixels(p.get_coords(), w.get_coords())
                nb_interchange += 1
            else:

                #g potentiellement blanc ?!
                g = n_w_w = binary_image.get_pixel_directional(p, [Direction.N, Direction.W, Direction.W])
                n = binary_image.get_pixel_adjacent(p, Direction.N)
                s_w = binary_image.get_pixel_directional(p, [Direction.S, Direction.W])
                path_found_sw, south_west_path = B4W8_Solver.find_path(g, p, binary_image,
                                                                       pixel_bridge=s_w,
                                                                       connexity=binary_image.black_connexity)
                path_found_n, north_path = B4W8_Solver.find_path(g, p, binary_image,
                                                                 pixel_bridge=n,
                                                                 connexity=binary_image.black_connexity)

                if path_found_sw and south_west_path:
                    n_w = binary_image.get_pixel_directional(p, [Direction.N, Direction.W])
                    array_interchange.append((p.get_coords(), n_w.get_coords()))
                    binary_image.swap_pixels(p.get_coords(), n_w.get_coords())
                    nb_interchange += 1
                elif path_found_n and north_path:
                    l = self.compute_l(p, binary_image)
                    s_l = binary_image.get_pixel_adjacent(l, Direction.S)
                    if not binary_image.is_cut_vertex(s_l):
                        s_e_l = binary_image.get_pixel_directional(l, [Direction.S, Direction.E])
                        array_interchange.append((s_e_l.get_coords(), s_l.get_coords()))
                        binary_image.swap_pixels(s_e_l.get_coords(), s_l.get_coords())
                        nb_interchange += 1
                    else:
                        s_s_w_l = binary_image.get_pixel_directional(l, [Direction.S, Direction.S, Direction.W])
                        if not binary_image.is_cut_vertex(s_s_w_l):
                            array_interchange.append((s_s_w_l.get_coords(), s_l.get_coords()))
                            binary_image.swap_pixels(s_s_w_l.get_coords(), s_l.get_coords())
                            nb_interchange += 1
                        else:
                            h, B = self.compute_h(g, binary_image)
                            z = self.compute_z(B, binary_image)
                            if z is not None:
                                n_z = binary_image.get_pixel_adjacent(z, Direction.N)
                                n_n_z = binary_image.get_pixel_directional(z, [Direction.N, Direction.N])
                                if n_z.color == n_n_z.color == PixelColor.WHITE:
                                    n_e_z = binary_image.get_pixel_directional(z, [Direction.N, Direction.E])
                                    array_interchange.append((z.get_coords(), n_e_z.get_coords()))
                                    binary_image.swap_pixels(z.get_coords(), n_e_z.get_coords())
                                    nb_interchange += 1
                                elif n_z.color == PixelColor.BLACK or n_n_z.color == PixelColor.BLACK:
                                    s_s_s_w_l = binary_image.get_pixel_directional(l, [Direction.S, Direction.S,
                                                                                       Direction.S, Direction.W])
                                    if z.get_coords() == s_s_s_w_l.get_coords():
                                        w_h = binary_image.get_pixel_adjacent(h, Direction.W)
                                        array_interchange.append((h.get_coords(), w_h.get_coords()))
                                        binary_image.swap_pixels(h.get_coords(), w_h.get_coords())
                                        nb_interchange += 1
                                    else:
                                        e_e_z = binary_image.get_pixel_directional(z, [Direction.E, Direction.E])
                                        e_e_e_z = binary_image.get_pixel_directional(e_e_z, [Direction.E])

                                        n_e_e_z = binary_image.get_pixel_directional(e_e_z, [Direction.N])
                                        n_e_e_e_z = binary_image.get_pixel_directional(n_e_e_z, [Direction.E])

                                        n_n_e_e_z = binary_image.get_pixel_directional(n_e_e_z, [Direction.N])
                                        n_n_e_e_e_z = binary_image.get_pixel_directional(n_n_e_e_z, [Direction.E])

                                        n_e_z = binary_image.get_pixel_directional(z, [Direction.N, Direction.E])

                                        array_interchange.append((e_e_z.get_coords(), e_e_e_z.get_coords()))
                                        array_interchange.append((n_e_e_z.get_coords(), n_e_e_e_z.get_coords()))
                                        array_interchange.append((n_n_e_e_z.get_coords(), n_n_e_e_e_z.get_coords()))
                                        array_interchange.append((z.get_coords(), n_e_z.get_coords()))
                                        nb_interchange += binary_image.multiple_swap_pixels(array_interchange)
                            else:
                                n_w_h = binary_image.get_pixel_directional(h, [Direction.N, Direction.W])
                                s_w_g = binary_image.get_pixel_directional(g, [Direction.S, Direction.W])
                                if h.get_coords() == g.get_coords():
                                    if n_w_h.color == PixelColor.BLACK and s_w_g.color == PixelColor.BLACK:
                                        w_g = binary_image.get_pixel_directional(g, [Direction.W])
                                        array_interchange.append((g.get_coords(), w_g.get_coords()))
                                        binary_image.swap_pixels(g.get_coords(), w_g.get_coords())
                                        nb_interchange += 1
                                    else:
                                        e_g = binary_image.get_pixel_directional(g, [Direction.E])
                                        e_e_g = binary_image.get_pixel_directional(e_g, [Direction.E])
                                        e_e_e_n_g = binary_image.get_pixel_directional(e_e_g, [Direction.E,
                                                                                               Direction.N])

                                        array_interchange.append((g.get_coords(), e_g.get_coords()))
                                        array_interchange.append((e_e_g.get_coords(), e_e_e_n_g.get_coords()))
                                        nb_interchange += binary_image.multiple_swap_pixels(array_interchange)
                                else:
                                    s_w_g = binary_image.get_pixel_directional(g, [Direction.S, Direction.W])
                                    n_w_h = binary_image.get_pixel_directional(h, [Direction.N, Direction.W])
                                    path, s_w_path = B4W8_Solver.find_path(g, p, binary_image,
                                                                           binary_image.black_connexity, s_w_g)
                                    path_2, n_w_path = B4W8_Solver.find_path(g, p, binary_image,
                                                                             binary_image.black_connexity, n_w_h)
                                    if path and s_w_path:
                                        n_e_g = binary_image.get_pixel_directional(g, [Direction.N, Direction.E])
                                        array_interchange.append((g.get_coords(), n_e_g.get_coords()))
                                        binary_image.swap_pixels(g.get_coords(), n_e_g.get_coords())
                                        nb_interchange += 1
                                    elif path_2 and n_w_path:
                                        e_h = binary_image.get_pixel_directional(h, [Direction.E])
                                        e_e_h = binary_image.get_pixel_directional(e_h, [Direction.E])
                                        e_e_e_n_h = binary_image.get_pixel_directional(e_e_h, [Direction.E,
                                                                                               Direction.N])

                                        array_interchange.append((h.get_coords(), e_h.get_coords()))
                                        array_interchange.append((e_e_h.get_coords(), e_e_e_n_h.get_coords()))
                                        nb_interchange += binary_image.multiple_swap_pixels(array_interchange)

        if nb_interchange > 0:
            self.array_interchange = [*self.array_interchange, *array_interchange]
            binary_image.expand_image()
            binary_image.reduce_image()

        return nb_interchange

    def compute_z(self, array_pixel: [Pixel], binary_image: BinaryImage) -> Pixel or None:
        current_pixel = None
        min_x = float("inf")
        for b in array_pixel:
            if binary_image.get_pixel_adjacent(b, Direction.W).color == PixelColor.BLACK:
                if b.x < min_x:
                    current_pixel = b

        return current_pixel

    def compute_h(self, g: Pixel, binary_image: BinaryImage) -> (Pixel, [Pixel]):
        pixels_between = [g]
        current_pixel = g

        while binary_image.get_pixel_adjacent(current_pixel, Direction.N).color != PixelColor.WHITE:
            current_pixel = binary_image.get_pixel_adjacent(current_pixel, Direction.N)
            pixels_between.append(current_pixel)

        return current_pixel, pixels_between

    def compute_l(self, p: Pixel, binary_image: BinaryImage) -> Pixel:
        w_n = binary_image.get_pixel_directional(p, [Direction.W, Direction.N])
        current_pixel = binary_image.get_pixel_adjacent(w_n, Direction.N)

        while current_pixel.color != PixelColor.BLACK:
            current_pixel = binary_image.get_pixel_adjacent(current_pixel, Direction.N)

        return current_pixel

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

    @staticmethod
    def get_p(img: BinaryImage) -> Pixel:
        p = None

        for pix in img.black_pixels:
            s = img.get_pixel_directional(pix, [Direction.S])
            if s.color == PixelColor.WHITE:
                if p is None or pix.x >= p.x:
                    s = img.get_pixel_adjacent(pix, Direction.S)
                    east_clear = B8W4_Solver.direction_clear(s, Direction.E, img)
                    north_clear = B8W4_Solver.direction_clear(img.get_pixel_adjacent(s, Direction.E),
                                                              Direction.N, img, p_included=True)

                    if east_clear and north_clear:
                        p = pix
        return p
