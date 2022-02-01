import copy

from algorithme_B4W4.New_Conception_v2.src.utils import Direction
from algorithme_B4W4.New_Conception_v2.src.models.pixel import Pixel, PixelColor
from algorithme_B4W4.New_Conception_v2.src.models.binary_image import BinaryImage
from algorithme_B4W4.New_Conception_v2.src.graphics.binary_image_displayer import BinaryImageDisplayer

BLACK_CONNEXITY = 4
WHITE_CONNEXITY = 4
INTERCHANGE_CONNEXITY = 8


# Class that will resolve B4W4 binary images
class B4W4_Elements:

    # Constructor with a BinaryImage
    def __init__(self, binary_image: BinaryImage):
        self.binary_image = binary_image
        self.__binary_image_save = copy.copy(binary_image)
        self.interchange = 0

        self.width = self.binary_image.black_pixels_width()
        self.frontier, self.adj_black_pixels_frontier = self.compute_frontier()
        self.anchor = self.compute_anchor()
        self.top_pixel = self.compute_top_pixel()
        self.all_elbows = self.compute_all_elbows()
        self.lead_elbow = self.compute_lead_elbow()
        self.array_interchange = []

        if self.anchor is None:
            self.height = None
        else:
            self.height = self.lead_elbow.x - self.anchor.x

    def get_saved_img(self):
        return copy.copy(self.__binary_image_save)

    # k_diagonal_interchange between p_1 and p_k. Return the nb of interchange
    def k_diagonal_interchange(self, p, p_1) -> int or None:
        compute_elbows_set = self.compute_set_elbows(p, p_1)
        array_interchange = []

        if self.binary_image.is_cut_vertex(p_1):
            for p_i in compute_elbows_set:
                n_w = self.binary_image.get_pixel_directional(p_i, [Direction.N, Direction.W])
                array_interchange.append((p_i.get_coords(), n_w.get_coords()))
        else:
            compute_elbows_set.remove(p)
            for p_i in compute_elbows_set:
                s_e = self.binary_image.get_pixel_directional(p_i, [Direction.S, Direction.E])
                array_interchange.append((p_i.get_coords(), s_e.get_coords()))

        nb_interchange = self.binary_image.multiple_swap_pixels(array_interchange)
        if nb_interchange is not None:
            self.array_interchange = [*self.array_interchange, *array_interchange]
            self.update_elements()

        return nb_interchange

    # From a pixel return the (k-diagonal_interchange, p_1) assiociated.
    # Return (0, None) it's a 0-diagonal interchange
    def lemme_5(self, pixel: Pixel) -> (int, Pixel):
        img_temp = copy.copy(self.binary_image)
        p = copy.copy(pixel)
        k = None
        p_1 = None
        if p in self.all_elbows:
            if not img_temp.is_cut_vertex(p):
                return 0, p_1

            n_w = img_temp.get_pixel_directional(p, [Direction.N, Direction.W])
            if not img_temp.is_cut_vertex(n_w):
                return 1, p

            n_n_w_w = img_temp.get_pixel_directional(p, [Direction.N, Direction.N, Direction.W, Direction.W])
            set_elbows = [p]  # The set of elbows on the diagonal {p, k}
            while True:
                if n_n_w_w is not None and n_n_w_w.color == PixelColor.BLACK and n_n_w_w in self.all_elbows:
                    set_elbows.append(n_n_w_w)
                    n_n_w_w = img_temp.get_pixel_directional(n_n_w_w, [Direction.N, Direction.N,
                                                                       Direction.W, Direction.W])
                else:
                    break

            p_1 = self.compute_p1(set_elbows)

            k = int(abs((p_1.y - p.y) / 2)) + 1

        return k, p_1

    def lemme_6(self) -> int:
        nb_interchange = self.first_condition()
        array_interchange = []

        if not self.binary_image.is_cut_vertex(self.lead_elbow):
            p = copy.copy(self.lead_elbow)
            k = self.top_pixel.x - p.x

            if k > 0:
                n_e = self.binary_image.get_pixel_directional(p, [Direction.N, Direction.E])
                array_interchange.append((p.get_coords(), n_e.get_coords()))

                for i in range(k - 1):
                    p = self.binary_image.pixels[self.binary_image.pixels.index(n_e)]
                    n_e = self.binary_image.get_pixel_adjacent(p, Direction.N)
                    array_interchange.append((p.get_coords(), n_e.get_coords()))

                n_e = self.binary_image.pixels[self.binary_image.pixels.index(n_e)]
                n = self.binary_image.get_pixel_directional(n_e, [Direction.N, Direction.W])
                array_interchange.append((n_e.get_coords(), n.get_coords()))

                nb_interchange = self.binary_image.multiple_swap_pixels(array_interchange)
            elif k == 0:
                n = self.binary_image.get_pixel_directional(p, [Direction.N])
                n_w = self.binary_image.get_pixel_directional(p, [Direction.N, Direction.W])
                n_n_w = self.binary_image.get_pixel_directional(p, [Direction.N, Direction.N, Direction.W])
                n_w_w = self.binary_image.get_pixel_directional(p, [Direction.N, Direction.W, Direction.W])
                q = n_n_w_w = self.binary_image.get_pixel_directional(p, [Direction.N, Direction.N,
                                                                      Direction.W, Direction.W])

                if n_w.color == PixelColor.BLACK:
                    self.binary_image.swap_pixels(p.get_coords(), n.get_coords())
                    array_interchange.append((p.get_coords(), n.get_coords()))
                    nb_interchange += 1
                elif n_w.color == PixelColor.WHITE and n_n_w.color == PixelColor.WHITE and \
                        not (n_n_w_w.color == PixelColor.BLACK and n_w_w.color == PixelColor.WHITE):
                    self.binary_image.swap_pixels(p.get_coords(), n_w.get_coords())
                    array_interchange.append((p.get_coords(), n_w.get_coords()))
                    nb_interchange += 1
                elif n_n_w_w.color == PixelColor.BLACK and n_w_w.color == PixelColor.WHITE:
                    k_diag, p_1 = self.lemme_5(n_n_w_w)
                    if p_1 is not None:
                        nb_interchange += self.k_diagonal_interchange(n_n_w_w, p_1)

                    if self.binary_image.get_pixel(q.x, q.y).color == PixelColor.WHITE:
                        self.binary_image.swap_pixels(p.get_coords(), n_w.get_coords())
                        array_interchange.append((p.get_coords(), n_w.get_coords()))
                        nb_interchange += 1
                    else:
                        s_e_q = self.binary_image.get_pixel_directional(q, [Direction.S, Direction.E])
                        array_interchange.append((q.get_coords(), s_e_q.get_coords()))
                        array_interchange.append((p.get_coords(), n.get_coords()))
                        nb_interchange += self.binary_image.multiple_swap_pixels(array_interchange)
        else:
            p = copy.copy(self.lead_elbow)
            k_diag, p_1 = self.lemme_5(p)
            nb_interchange += self.k_diagonal_interchange(p, p_1)

        if nb_interchange is not None:
            self.array_interchange = [*self.array_interchange, *array_interchange]
            self.update_elements()
            self.binary_image.expand_image()
            self.binary_image.reduce_image()

        return nb_interchange

    def first_condition(self) -> int:
        nb_interchange = 0
        n_w = self.binary_image.get_pixel_directional(self.top_pixel, [Direction.N, Direction.W])
        n_n_w = self.binary_image.get_pixel_directional(self.top_pixel, [Direction.N, Direction.N, Direction.W])
        while n_n_w.color == PixelColor.BLACK:
            if not (n_w.color == PixelColor.WHITE and n_n_w.color == PixelColor.BLACK):
                return nb_interchange
            else:
                k_diag, p_1 = self.lemme_5(n_n_w)
                if p_1 is not None:
                    nb_interchange += self.k_diagonal_interchange(n_n_w, p_1)

                if self.binary_image.get_pixel(n_n_w.x, n_n_w.y).color == PixelColor.BLACK:
                    n = self.binary_image.get_pixel_adjacent(self.top_pixel, Direction.N)
                    self.array_interchange.append((n_n_w.get_coords(), n.get_coords()))
                    self.binary_image.swap_pixels(n_n_w.get_coords(), n.get_coords())
                    nb_interchange += 1

                self.all_elbows = self.compute_all_elbows()
                self.top_pixel = self.compute_top_pixel()
                n_w = self.binary_image.get_pixel_directional(self.top_pixel, [Direction.N, Direction.W])
                n_n_w = self.binary_image.get_pixel_directional(self.top_pixel, [Direction.N, Direction.N, Direction.W])

        return nb_interchange

    # Compute p1 from a set of elbows, such that the set is define by {pi : 1 <= i <= k} in I,
    # and for each 1 <= i < k, pi = NNWW(pi+1)
    def compute_p1(self, array_elbows):
        p_1 = None
        min_x = float("inf")  # set to the biggest number
        for p in array_elbows:
            n_w = self.binary_image.get_pixel_directional(p, [Direction.N, Direction.W])
            is_cut_elbow = self.binary_image.is_cut_vertex(p)
            is_n_w_cut_vertex = (n_w.color == PixelColor.WHITE and self.binary_image.is_cut_vertex(n_w))
            if p.x < min_x and (not is_cut_elbow or not is_n_w_cut_vertex):
                p_1 = p
                min_x = p_1.x

        return p_1

    def compute_set_elbows(self, p, p_1):
        if p_1 is None or p_1 == p:
            return [p]

        set_elbows = [p]
        temp = copy.copy(p)
        while True:
            n_n_w_w = self.binary_image.get_pixel_directional(temp,
                                                              [Direction.N, Direction.N, Direction.W, Direction.W])
            if n_n_w_w is None or n_n_w_w.color == PixelColor.WHITE:
                break
            elif n_n_w_w == p_1:
                set_elbows.append(p_1)
                break
            else:
                set_elbows.append(n_n_w_w)
                temp = n_n_w_w

        return set_elbows[::-1]

    # Return list of black pixels in the frontier
    def compute_frontier(self) -> ([Pixel], [Pixel]):
        max_y = self.binary_image.black_pixels[0].y
        frontier = []
        adj_frontier = []

        for p in self.binary_image.black_pixels:
            if max_y == p.y:
                frontier.append(p)
            elif max_y < p.y:
                max_y = p.y
                if p.y == max_y - 1:
                    adj_frontier = frontier
                frontier = [p]
            elif p.y == max_y - 1:
                adj_frontier.append(p)

        return frontier, adj_frontier

    # Return the pixel that is the anchor
    def compute_anchor(self) -> Pixel:
        anchor = None
        if self.adj_black_pixels_frontier:
            anchor = self.adj_black_pixels_frontier[0]
            min_x = anchor.x

            for p in self.adj_black_pixels_frontier:
                if min_x > p.x:
                    min_x = p.x
                    anchor = p

        return anchor

    # Return the top pixel
    def compute_top_pixel(self) -> Pixel:
        frontier, _ = self.compute_frontier()
        top_pixel = frontier[0]
        max_x = top_pixel.x

        for p in frontier:
            if max_x < p.x:
                max_x = p.x
                top_pixel = p

        return top_pixel

    # Return an array of all elbows
    def compute_all_elbows(self) -> [Pixel]:
        elbows = []
        for p in self.binary_image.black_pixels:
            if self.is_elbow(p):
                elbows.append(p)

        return elbows

    # Return a boolean if a pixel is an elbow
    def is_elbow(self, pixel: Pixel) -> bool:
        p_e = self.binary_image.get_pixel_adjacent(pixel, Direction.E)
        p_se = self.binary_image.get_pixel_adjacent(pixel, Direction.SE)
        p_s = self.binary_image.get_pixel_adjacent(pixel, Direction.S)
        return p_e.color == PixelColor.WHITE and p_se.color == PixelColor.WHITE and p_s.color == PixelColor.WHITE

    # Return the lead elbow
    def compute_lead_elbow(self) -> Pixel:
        max_x = float('-inf')
        lead_elbow = None
        for p in self.frontier:
            if self.is_elbow(p) and max_x < p.x:
                lead_elbow = p

        return lead_elbow

    # Update all attributes of the Algorithm
    def update_elements(self) -> None:
        self.width = self.binary_image.black_pixels_width()
        self.frontier, adj_black_pixels = self.compute_frontier()
        self.anchor = self.compute_anchor()
        self.top_pixel = self.compute_top_pixel()
        self.all_elbows = self.compute_all_elbows()
        self.lead_elbow = self.compute_lead_elbow()
        if self.anchor is None:
            self.height = None
        else:
            self.height = self.lead_elbow.x - self.anchor.x

# Return a dictionnary {Pixel: k-diagonal-interchange} of all pixels
#    def k_diagonal_interchange_temp(self) -> {Pixel: int}:
#        img_temp = copy.copy(self.binary_image)         # Copy of the image
#        arr_k_diag = []                                    # Dict that we'll return
#        for p in self.all_elbows:                           # Run threw all elbows
#            loop = True                                     # Boolean for next loop
#            cut_elbow = img_temp.is_cut_vertex(p)           # Define if p is a cut_elbow
#            p_i = p                                         # p_i is the pixel intermediate pixel between 1 and k
#            i = 0                                           # final value of i determine the k_diag_interchange
#
#            # While the conditions are valid
#            while loop:
#                # If a pixel is on side, n_n_w_w doesn't exist, there is probably a better solution
#                if img_temp.height - 2 > p_i.x > 1 and 1 < p_i.y < img_temp.width - 2:
#                    # Compute n_n_w_w
#                    n_n_w_w = img_temp.get_pixel_directional(p_i, [Direction.N, Direction.N, Direction.W, Direction.W])
#                    s_s_e_e = img_temp.get_pixel_directional(p_i, [Direction.S, Direction.S, Direction.E, Direction.E])
#                    if n_n_w_w.color == PixelColor.BLACK:  # The article says p_i.color == n_n_w_w.color, it's the same
#                        # Computing n_w and s_e pixel
#                        n_w = img_temp.get_pixel_directional(p_i, [Direction.N, Direction.W])
#                        s_e = img_temp.get_pixel_directional(p_i, [Direction.S, Direction.E])
#                        if cut_elbow and img_temp.swap_pixels(p_i, n_w, swap_active=True):
#                            i += 1
#                            p_i = n_n_w_w
#                        elif not cut_elbow and img_temp.swap_pixels(p_i, s_e, swap_active=True):
#                            i += 1
#                            p_i = s_s_e_e
#                        else:
#                            if i > 0:
#                                arr_k_diag.append((i, p_i))
#                            loop = False
#                    else:
#                        loop = False
#                else:
#                    loop = False
#
#        return arr_k_diag
