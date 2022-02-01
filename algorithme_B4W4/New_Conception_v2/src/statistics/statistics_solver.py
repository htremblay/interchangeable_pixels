import copy
import random

from algorithme_B4W4.New_Conception_v2.src.utils import Direction
from algorithme_B4W4.New_Conception_v2.src.models.pixel import Pixel, PixelColor
from algorithme_B4W4.New_Conception_v2.src.models.binary_image import BinaryImage
from algorithme_B4W4.New_Conception_v2.src.graphics.binary_image_displayer import BinaryImageDisplayer
from algorithme_B4W4.New_Conception_v2.src.solvers.B4W8.b4w8_solver import B4W8_Solver
from algorithme_B4W4.New_Conception_v2.src.solvers.B8W4.b8w4_solver import B8W4_Solver
from algorithme_B4W4.New_Conception_v2.src.solvers.B8W8.b8w8_solver import B8W8_Solver
from algorithme_B4W4.New_Conception_v2.src.solvers.B4W4.b4w4_solver import B4W4_Solver



class Statistics:
    def __init__(self):
        self.total_interchanges = 0
        self.dic_interchanges = {}
        self.nb_iterations = 0

    def statistics_from_random_images(self, black_connexity=4, white_connexity=4, nb_iter=10, size_image=50,
                                      nb_tick=5, incr_size_image=10, seed_min=0, seed_max=500000):
        for i in range(nb_iter):
            total_interchange = 0
            seeds = []
            for j in range(nb_tick):
                seed = random.randint(seed_min, seed_max)
                binary_image = BinaryImage.create_random_img(n=size_image, black_connexity=black_connexity,
                                                             white_connexity=white_connexity, seed=seed)
                solver = None


                if black_connexity == white_connexity == 4:
                    solver = B4W4_Solver(binary_image, BinaryImage.create_img_vertical(binary_image.size))
                elif black_connexity == 4 and white_connexity == 8:
                    solver = B4W8_Solver(binary_image, BinaryImage.create_img_vertical(binary_image.size))
                elif black_connexity == 8 and white_connexity == 4:
                    solver = B8W4_Solver(binary_image, BinaryImage.create_img_vertical(binary_image.size))
                elif black_connexity == white_connexity == 8:
                    solver = B8W8_Solver(binary_image, BinaryImage.create_img_vertical(binary_image.size))


                nb_interchange = solver.solve()
                total_interchange += nb_interchange
                seeds.append(seed)

            average_tick_interchange = total_interchange/nb_tick

            self.dic_interchanges[size_image] = [seeds, average_tick_interchange]
            size_image += incr_size_image

        print("Total average for solver B", black_connexity, "W", white_connexity, " is ", self.dic_interchanges)

    # def generate_statistics_B4W4(self, nb_tick=5, size_image=50, seed=0):
    #     total_interchange = 0
    #
    #     for i in range(nb_tick):
    #         binary_image = BinaryImage.create_random_img(size_image, black_connexity=4, white_connexity=4, seed=seed)
    #
    #         solver = B4W4_Solver(binary_image, BinaryImage.create_img_vertical(binary_image.size))
    #         nb_interchange = solver.solve()
    #         total_interchange += nb_interchange
    #
    #         print("Tick n°", i, " has done ", nb_interchange, " interchanges")
    #
    #     return total_interchange / nb_tick
    #
    # def generate_statistics_B4W8(self, nb_tick=5, size_image=50, seed=0):
    #     total_interchange = 0
    #
    #     for i in range(nb_tick):
    #         binary_image = BinaryImage.create_random_img(size_image, black_connexity=4, white_connexity=8, seed=seed)
    #
    #         solver = B4W8_Solver(binary_image, BinaryImage.create_img_vertical(binary_image.size))
    #         nb_interchange = solver.solve()
    #         total_interchange += nb_interchange
    #
    #     return total_interchange / nb_tick
    #
    # def generate_statistics_B8W4(self, nb_tick=5, size_image=50, seed=0):
    #     total_interchange = 0
    #
    #     for i in range(nb_tick):
    #         binary_image = BinaryImage.create_random_img(size_image, black_connexity=8, white_connexity=4, seed=seed)
    #
    #         solver = B8W4_Solver(binary_image, BinaryImage.create_img_vertical(binary_image.size))
    #         nb_interchange = solver.solve()
    #         total_interchange += nb_interchange
    #
    #     return total_interchange / nb_tick
    #
    # def generate_statistics_B8W8(self, nb_tick=5, size_image=50, seed=0):
    #     total_interchange = 0
    #
    #     for i in range(nb_tick):
    #         binary_image = BinaryImage.create_random_img(size_image, black_connexity=8, white_connexity=8, seed=seed)
    #
    #         solver = B4W4_Solver(binary_image, BinaryImage.create_img_vertical(binary_image.size))
    #         nb_interchange = solver.solve()
    #         total_interchange += nb_interchange
    #
    #     return total_interchange / nb_tick

    def get_average_interchange(self):
        return self.total_interchanges / self.nb_iterations
