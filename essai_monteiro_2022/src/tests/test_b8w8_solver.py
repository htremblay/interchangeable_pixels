import unittest

from algorithme_B4W4.New_Conception_v2.src.models.binary_image import BinaryImage
from algorithme_B4W4.New_Conception_v2.src.solvers.B8W8.b8w8_solver import B8W8_Solver

BLACK_CONNEXITY = 8
WHITE_CONNEXITY = 8

class AlgoB8W8Tests(unittest.TestCase):

    def test_p_not_cut_Np_black(self):
        img_depart = [[0, 0, 0],
                      [0, 1, 0],
                      [0, 1, 0],
                      [0, 0, 0]]

        img_soluce = [[0, 0, 0, 0],
                      [0, 1, 1, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0]]

        binary_image = BinaryImage.create_img_from_array(img_depart, BLACK_CONNEXITY, WHITE_CONNEXITY)

        solver = B8W8_Solver(binary_image, BinaryImage.create_img_vertical(binary_image.size))

        solver.resolve_image(binary_image)

        self.assertEqual(img_soluce,
                         binary_image.convert_pixels_to_img(),
                         "In case of p not cut vertex and N(p) black, the interchange should be <p, NE(p)>")
        self.assertEqual(1,
                         len(solver.array_interchange),
                         "The number interchange should be 1")

    def test_p_not_cut_Np_white_NWp_Black(self):
        img_depart = [[0, 0, 0, 0],
                      [0, 1, 0, 0],
                      [0, 0, 1, 0],
                      [0, 0, 0, 0]]

        img_soluce = [[0, 0, 0, 0],
                      [0, 1, 1, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0]]

        binary_image = BinaryImage.create_img_from_array(img_depart, BLACK_CONNEXITY, WHITE_CONNEXITY)

        solver = B8W8_Solver(binary_image, BinaryImage.create_img_vertical(binary_image.size))

        solver.resolve_image(binary_image)

        self.assertEqual(img_soluce,
                         binary_image.convert_pixels_to_img(),
                         "In case of p not cut vertex and N(p) white and NW(p) black,"
                         " the interchange should be <p, N(p)>")
        self.assertEqual(1,
                         len(solver.array_interchange),
                         "The number interchange should be 1")

    def test_p_not_cut_Np_white_Wp_Black(self):
        img_depart = [[0, 0, 0, 0],
                      [0, 1, 1, 0],
                      [0, 0, 0, 0]]

        img_soluce = [[0, 0, 0, 0],
                      [0, 0, 1, 0],
                      [0, 1, 0, 0],
                      [0, 0, 0, 0]]

        binary_image = BinaryImage.create_img_from_array(img_depart, BLACK_CONNEXITY, WHITE_CONNEXITY)

        solver = B8W8_Solver(binary_image, BinaryImage.create_img_vertical(binary_image.size))

        solver.resolve_image(binary_image)

        self.assertEqual(img_soluce,
                         binary_image.convert_pixels_to_img(),
                         "In case of p not cut vertex and N(p) white and W(p) black,"
                         " the interchange should be <p, N(p)>")
        self.assertEqual(1,
                         len(solver.array_interchange),
                         "The number interchange should be 1")

    def test_p_not_cut_Np_white_Wp_white_NWp_white_WWp_black(self):
        img_depart = [[0, 0, 0, 0, 0],
                      [0, 1, 0, 1, 0],
                      [0, 0, 1, 0, 0],
                      [0, 0, 0, 0, 0]]

        img_soluce = [[0, 0, 0, 0],
                      [0, 0, 1, 0],
                      [0, 1, 0, 0],
                      [0, 0, 1, 0],
                      [0, 0, 0, 0]]

        binary_image = BinaryImage.create_img_from_array(img_depart, BLACK_CONNEXITY, WHITE_CONNEXITY)

        solver = B8W8_Solver(binary_image, BinaryImage.create_img_vertical(binary_image.size))

        solver.resolve_image(binary_image)

        self.assertEqual(img_soluce,
                         binary_image.convert_pixels_to_img(),
                         "In case of p not cut vertex and N(p) and NW(p) and W(p) are white and WW(p) is black,"
                         " the interchange should be <p, NW(p)>")
        self.assertEqual(1,
                         len(solver.array_interchange),
                         "The number interchange should be 1")

    def test_p_not_cut_Np_white_Wp_white_NWp_white_WWp_white(self):
        img_depart = [[0, 0, 0, 0],
                      [0, 0, 1, 0],
                      [0, 1, 0, 0],
                      [0, 0, 0, 0]]

        img_soluce = [[0, 0, 0],
                      [0, 1, 0],
                      [0, 1, 0],
                      [0, 0, 0]]

        binary_image = BinaryImage.create_img_from_array(img_depart, BLACK_CONNEXITY, WHITE_CONNEXITY)

        solver = B8W8_Solver(binary_image, BinaryImage.create_img_vertical(binary_image.size))

        solver.resolve_image(binary_image)

        self.assertEqual(img_soluce,
                         binary_image.convert_pixels_to_img(),
                         "In case of p not cut vertex and N(p) and NW(p) and W(p) are white and WW(p) is white,"
                         " the interchange should be <p, W(p)>")
        self.assertEqual(1,
                         len(solver.array_interchange),
                         "The number interchange should be 1")

    def test_p_cut_NWp_black(self):
        img_depart = [[0, 0, 0, 0],
                      [0, 1, 1, 0],
                      [0, 0, 1, 0],
                      [0, 1, 0, 0],
                      [0, 0, 0, 0]]

        img_soluce = [[0, 0, 0, 0],
                      [0, 1, 1, 0],
                      [0, 1, 0, 0],
                      [0, 1, 0, 0],
                      [0, 0, 0, 0]]

        binary_image = BinaryImage.create_img_from_array(img_depart, BLACK_CONNEXITY, WHITE_CONNEXITY)

        solver = B8W8_Solver(binary_image, BinaryImage.create_img_vertical(binary_image.size))

        solver.resolve_image(binary_image)

        self.assertEqual(img_soluce,
                         binary_image.convert_pixels_to_img(),
                         "In case of p cut vertex and NW(p) is black"
                         " the interchange should be <p, W(p)>")
        self.assertEqual(1,
                         len(solver.array_interchange),
                         "The number interchange should be 1")

    def test_p_cut_NWp_White_Wp_not_cut(self):
        img_depart = [[0, 0, 0, 0],
                      [0, 0, 1, 0],
                      [0, 0, 1, 0],
                      [0, 1, 0, 0],
                      [0, 0, 0, 0]]

        img_soluce = [[0, 0, 0, 0],
                      [0, 0, 1, 0],
                      [0, 1, 0, 0],
                      [0, 1, 0, 0],
                      [0, 0, 0, 0]]

        binary_image = BinaryImage.create_img_from_array(img_depart, BLACK_CONNEXITY, WHITE_CONNEXITY)

        solver = B8W8_Solver(binary_image, BinaryImage.create_img_vertical(binary_image.size))

        solver.resolve_image(binary_image)

        self.assertEqual(img_soluce,
                         binary_image.convert_pixels_to_img(),
                         "In case of p cut vertex and NW(p) is white and W(p) is not cut"
                         " the interchange should be <p, W(p)>")
        self.assertEqual(1,
                         len(solver.array_interchange),
                         "The number interchange should be 1")

    def test_p_cut_NWp_white_Wp_cut(self):
        img_depart = [[0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 1, 0],
                      [0, 1, 1, 0, 1, 0],
                      [0, 1, 0, 1, 0, 0],
                      [0, 1, 1, 1, 0, 0],
                      [0, 0, 0, 0, 0, 0]]

        img_soluce = [[0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 1, 1, 0],
                      [0, 1, 1, 0, 0, 0],
                      [0, 1, 0, 1, 0, 0],
                      [0, 1, 1, 1, 0, 0],
                      [0, 0, 0, 0, 0, 0]]

        binary_image = BinaryImage.create_img_from_array(img_depart, BLACK_CONNEXITY, WHITE_CONNEXITY)

        solver = B8W8_Solver(binary_image, BinaryImage.create_img_vertical(binary_image.size))

        solver.resolve_image(binary_image)

        self.assertEqual(img_soluce,
                         binary_image.convert_pixels_to_img(),
                         "In case of p cut vertex and NW(p) is white and W(p) is cut vertex"
                         " the interchange should be <p, NW(p)>")
        self.assertEqual(1,
                         len(solver.array_interchange),
                         "The number interchange should be 1")
