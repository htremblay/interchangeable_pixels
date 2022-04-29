from algorithme_B4W4.New_Conception_v2.src.models.binary_image import BinaryImage
from algorithme_B4W4.New_Conception_v2.src.solvers.B4W4.b4w4_elements import B4W4_Elements
from algorithme_B4W4.New_Conception_v2.src.graphics.binary_image_displayer import BinaryImageDisplayer
from algorithme_B4W4.New_Conception_v2.src.utils import Direction
from algorithme_B4W4.New_Conception_v2.src.models.pixel import Pixel, PixelColor
import copy


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
        self.array_interchange = []                                  # array of all interchange
        self.interchange = 0                                         # Number of swap

    # todo implement method
    def solve(self) -> int:
        nb_echange = 0
        while True:
            if self.imageElementsStart.binary_image.is_vertical():
                break
            else:
                temp = self.lemme_6(self.imageElementsStart)
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

    # k_diagonal_interchange between p_1 and p_k. Return the nb of interchange
    def k_diagonal_interchange(self, p : Pixel, p_1 : Pixel, elem: B4W4_Elements) -> int or None:
        compute_elbows_set = elem.compute_set_elbows(p, p_1)
        array_interchange = []

        if elem.binary_image.is_cut_vertex(p_1):
            for p_i in compute_elbows_set:
                n_w = elem.binary_image.get_pixel_directional(p_i, [Direction.N, Direction.W])
                array_interchange.append((p_i.get_coords(), n_w.get_coords()))
        else:
            compute_elbows_set.remove(p)
            for p_i in compute_elbows_set:
                s_e = elem.binary_image.get_pixel_directional(p_i, [Direction.S, Direction.E])
                array_interchange.append((p_i.get_coords(), s_e.get_coords()))

        nb_interchange = elem.binary_image.multiple_swap_pixels(array_interchange)
        if nb_interchange is not None:
            elem.array_interchange = [*elem.array_interchange, *array_interchange]
            elem.update_elements()

        return nb_interchange

    # From a pixel return the (k-diagonal_interchange, p_1) assiociated.
    # Return (0, None) it's a 0-diagonal interchange
    def lemme_5(self, pixel: Pixel, elem: B4W4_Elements) -> (int, Pixel):
        img_temp = copy.copy(elem.binary_image)
        p = copy.copy(pixel)
        k = None
        p_1 = None
        if p in elem.all_elbows:
            if not img_temp.is_cut_vertex(p):
                return 0, p_1

            n_w = img_temp.get_pixel_directional(p, [Direction.N, Direction.W])
            if not img_temp.is_cut_vertex(n_w):
                return 1, p

            n_n_w_w = img_temp.get_pixel_directional(p, [Direction.N, Direction.N, Direction.W, Direction.W])
            set_elbows = [p]  # The set of elbows on the diagonal {p, k}
            while True:
                if n_n_w_w is not None and n_n_w_w.color == PixelColor.BLACK and n_n_w_w in elem.all_elbows:
                    set_elbows.append(n_n_w_w)
                    n_n_w_w = img_temp.get_pixel_directional(n_n_w_w, [Direction.N, Direction.N,
                                                                       Direction.W, Direction.W])
                else:
                    break

            p_1 = self.compute_p1(set_elbows, elem)

            k = int(abs((p_1.y - p.y) / 2)) + 1

        return k, p_1

    def lemme_6(self, elem: B4W4_Elements) -> int:
        nb_interchange = self.first_condition(elem)
        array_interchange = []

        if not elem.binary_image.is_cut_vertex(elem.lead_elbow):
            p = copy.copy(elem.lead_elbow)
            k = elem.top_pixel.x - p.x

            if k > 0:
                n_e = elem.binary_image.get_pixel_directional(p, [Direction.N, Direction.E])
                array_interchange.append((p.get_coords(), n_e.get_coords()))

                for i in range(k - 1):
                    p = elem.binary_image.pixels[elem.binary_image.pixels.index(n_e)]
                    n_e = elem.binary_image.get_pixel_adjacent(p, Direction.N)
                    array_interchange.append((p.get_coords(), n_e.get_coords()))

                n_e = elem.binary_image.pixels[elem.binary_image.pixels.index(n_e)]
                n = elem.binary_image.get_pixel_directional(n_e, [Direction.N, Direction.W])
                array_interchange.append((n_e.get_coords(), n.get_coords()))

                nb_interchange = elem.binary_image.multiple_swap_pixels(array_interchange)
            elif k == 0:
                n = elem.binary_image.get_pixel_directional(p, [Direction.N])
                n_w = elem.binary_image.get_pixel_directional(p, [Direction.N, Direction.W])
                n_n_w = elem.binary_image.get_pixel_directional(p, [Direction.N, Direction.N, Direction.W])
                n_w_w = elem.binary_image.get_pixel_directional(p, [Direction.N, Direction.W, Direction.W])
                q = n_n_w_w = elem.binary_image.get_pixel_directional(p, [Direction.N, Direction.N,
                                                                          Direction.W, Direction.W])

                if n_w.color == PixelColor.BLACK:
                    elem.binary_image.swap_pixels(p.get_coords(), n.get_coords())
                    array_interchange.append((p.get_coords(), n.get_coords()))
                    nb_interchange += 1
                elif n_w.color == PixelColor.WHITE and n_n_w.color == PixelColor.WHITE and \
                        not (n_n_w_w.color == PixelColor.BLACK and n_w_w.color == PixelColor.WHITE):
                    elem.binary_image.swap_pixels(p.get_coords(), n_w.get_coords())
                    array_interchange.append((p.get_coords(), n_w.get_coords()))
                    nb_interchange += 1
                elif n_n_w_w.color == PixelColor.BLACK and n_w_w.color == PixelColor.WHITE:
                    k_diag, p_1 = self.lemme_5(n_n_w_w, elem)
                    if p_1 is not None:
                        nb_interchange += self.k_diagonal_interchange(n_n_w_w, p_1, elem)

                    if elem.binary_image.get_pixel(q.x, q.y).color == PixelColor.WHITE:
                        elem.binary_image.swap_pixels(p.get_coords(), n_w.get_coords())
                        array_interchange.append((p.get_coords(), n_w.get_coords()))
                        nb_interchange += 1
                    else:
                        s_e_q = elem.binary_image.get_pixel_directional(q, [Direction.S, Direction.E])
                        array_interchange.append((q.get_coords(), s_e_q.get_coords()))
                        array_interchange.append((p.get_coords(), n.get_coords()))
                        nb_interchange += elem.binary_image.multiple_swap_pixels(array_interchange)
        else:
            p = copy.copy(elem.lead_elbow)
            k_diag, p_1 = self.lemme_5(p, elem)
            nb_interchange += self.k_diagonal_interchange(p, p_1, elem)

        if nb_interchange is not None:
            elem.array_interchange = [*elem.array_interchange, *array_interchange]
            elem.update_elements()
            elem.binary_image.expand_image()
            elem.binary_image.reduce_image()

        return nb_interchange

    def first_condition(self, elem: B4W4_Elements) -> int:
        nb_interchange = 0
        n_w = elem.binary_image.get_pixel_directional(elem.top_pixel, [Direction.N, Direction.W])
        n_n_w = elem.binary_image.get_pixel_directional(elem.top_pixel, [Direction.N, Direction.N, Direction.W])
        while n_n_w.color == PixelColor.BLACK:
            if not (n_w.color == PixelColor.WHITE and n_n_w.color == PixelColor.BLACK):
                return nb_interchange
            else:
                k_diag, p_1 = self.lemme_5(n_n_w, elem)
                if p_1 is not None:
                    nb_interchange += self.k_diagonal_interchange(n_n_w, p_1, elem)

                if elem.binary_image.get_pixel(n_n_w.x, n_n_w.y).color == PixelColor.BLACK:
                    n = elem.binary_image.get_pixel_adjacent(elem.top_pixel, Direction.N)
                    elem.array_interchange.append((n_n_w.get_coords(), n.get_coords()))
                    elem.binary_image.swap_pixels(n_n_w.get_coords(), n.get_coords())
                    nb_interchange += 1

                elem.all_elbows = elem.compute_all_elbows()
                elem.top_pixel = elem.compute_top_pixel()
                n_w = elem.binary_image.get_pixel_directional(elem.top_pixel, [Direction.N, Direction.W])
                n_n_w = elem.binary_image.get_pixel_directional(elem.top_pixel,
                                                                [Direction.N, Direction.N, Direction.W])

        return nb_interchange

    # Compute p1 from a set of elbows, such that the set is define by {pi : 1 <= i <= k} in I,
    # and for each 1 <= i < k, pi = NNWW(pi+1)
    def compute_p1(self, array_elbows, elem):
        p_1 = None
        min_x = float("inf")  # set to the biggest number
        for p in array_elbows:
            n_w = elem.binary_image.get_pixel_directional(p, [Direction.N, Direction.W])
            is_cut_elbow = elem.binary_image.is_cut_vertex(p)
            is_n_w_cut_vertex = (n_w.color == PixelColor.WHITE and elem.binary_image.is_cut_vertex(n_w))
            if p.x < min_x and (not is_cut_elbow or not is_n_w_cut_vertex):
                p_1 = p
                min_x = p_1.x

        return p_1

