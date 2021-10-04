import BinaryImage
import Pixel
import math

class AlgoB4W4:

    # Constructor, take as parameters a BinaryImage
    def __init__(self, binaryImage: BinaryImage):
        self.image = binaryImage
        self.solve()

    def swap_pixels(self, p, q):
        swap_done = False
        imageTemp = self.image
        pixel = self.image.get_pixel(3,3)
        pixel.black = True
        self.image[3][3] = 1
        # if self.is_8_adjacent(p, q) and p.black != q.black:
        #     self.image.show_image()
        #     pChange = self.image.change_color_pixel(p, not p.black)
        #     self.image.show_image()
        #     qChange = self.image.change_color_pixel(q, not q.black)
        #     self.image.show_image()
        #
        #     print("pChange", pChange)
        #     print("qChange", qChange)
        #
        #     swap_done = pChange and qChange
        #
        # if not swap_done:
        #     self.image = imageTemp

        return swap_done

    # TODO K_Diagonal

    def is_8_adjacent(self, p, q):
        return pow(p.x - q.x, 2) + pow(p.y - q.y, 2) <= 2

    def solve(self):
        swap = self.swap_pixels(self.image.get_pixel(1, 2), self.image.get_pixel(1, 3))

        return self.image