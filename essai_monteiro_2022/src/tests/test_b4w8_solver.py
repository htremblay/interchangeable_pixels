import unittest

from algorithme_B4W4.New_Conception_v2.src.models.binary_image import BinaryImage
from algorithme_B4W4.New_Conception_v2.src.solvers.B4W8.b4w8_solver import B4W8_Solver

BLACK_CONNEXITY = 4
WHITE_CONNEXITY = 8


class AlgoB4W8Tests(unittest.TestCase):

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

        solver = B4W8_Solver(binary_image, BinaryImage.create_img_vertical(binary_image.size))

        solver.resolve_image(binary_image)

        self.assertEqual(img_soluce,
                         binary_image.convert_pixels_to_img(),
                         "In case of p not cut vertex and N(p) black, the interchange should be <p, NE(p)>")
        self.assertEqual(1,
                         len(solver.array_interchange),
                         "In case of p not cut vertex and N(p) black, the number interchange should be 1")

    def test_p_not_cut_Np_white_NWp_black(self):
        img_depart = [[0, 0, 0, 0],
                      [0, 1, 0, 0],
                      [0, 1, 1, 0],
                      [0, 0, 0, 0]]

        img_soluce = [[0, 0, 0, 0],
                      [0, 1, 1, 0],
                      [0, 1, 0, 0],
                      [0, 0, 0, 0]]

        binary_image = BinaryImage.create_img_from_array(img_depart, BLACK_CONNEXITY, WHITE_CONNEXITY)

        solver = B4W8_Solver(binary_image, BinaryImage.create_img_vertical(binary_image.size))

        solver.resolve_image(binary_image)

        self.assertEqual(img_soluce,
                         binary_image.convert_pixels_to_img(),
                         "In case of p not cut vertex and N(p) white and NW(p) black,"
                         " the interchange should be <p, N(p)>")
        self.assertEqual(1,
                         len(solver.array_interchange),
                         "The number interchange should be 1")

    def test_p_not_cut_Np_white_NWp_white(self):
        img_depart = [[0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 1, 1, 0],
                      [0, 0, 0, 0]]

        img_soluce = [[0, 0, 0],
                      [0, 1, 0],
                      [0, 1, 0],
                      [0, 0, 0]]

        binary_image = BinaryImage.create_img_from_array(img_depart, BLACK_CONNEXITY, WHITE_CONNEXITY)

        solver = B4W8_Solver(binary_image, BinaryImage.create_img_vertical(binary_image.size))

        solver.resolve_image(binary_image)

        self.assertEqual(img_soluce,
                         binary_image.convert_pixels_to_img(),
                         "In case of p not cut vertex and N(p) white and NW(p) white,"
                         " the interchange should be <p, NW(p)>")
        self.assertEqual(1,
                         len(solver.array_interchange),
                         "The number interchange should be 1")

    def test_p_cut_Nwp_white_not_cut(self):
        img_depart = [[0, 0, 0, 0],
                      [0, 0, 1, 0],
                      [0, 1, 1, 0],
                      [0, 0, 0, 0]]

        img_soluce = [[0, 0, 0, 0],
                      [0, 1, 1, 0],
                      [0, 1, 0, 0],
                      [0, 0, 0, 0]]

        binary_image = BinaryImage.create_img_from_array(img_depart, BLACK_CONNEXITY, WHITE_CONNEXITY)

        solver = B4W8_Solver(binary_image, BinaryImage.create_img_vertical(binary_image.size))

        solver.resolve_image(binary_image)

        self.assertEqual(img_soluce,
                         binary_image.convert_pixels_to_img(),
                         "In case of p cut vertex and NW(p) white and not cut vextex,"
                         " the interchange should be <p, NW(p)>")
        self.assertEqual(1,
                         len(solver.array_interchange),
                         "The number interchange should be 1")

    def test_p_cut_g_to_p_from_Wp(self):
        img_depart = [[0, 0, 0, 0, 0, 0],
                      [0, 1, 1, 0, 1, 0],
                      [0, 1, 0, 1, 1, 0],
                      [0, 1, 1, 1, 0, 0],
                      [0, 0, 0, 0, 0, 0]]

        img_soluce = [[0, 0, 0, 0, 0, 0],
                      [0, 1, 1, 1, 1, 0],
                      [0, 1, 0, 0, 1, 0],
                      [0, 1, 1, 1, 0, 0],
                      [0, 0, 0, 0, 0, 0]]

        binary_image = BinaryImage.create_img_from_array(img_depart, BLACK_CONNEXITY, WHITE_CONNEXITY)

        solver = B4W8_Solver(binary_image, BinaryImage.create_img_vertical(binary_image.size))

        solver.resolve_image(binary_image)

        self.assertEqual(img_soluce,
                         binary_image.convert_pixels_to_img(),
                         "In case of p cut vertex and g=NWW(p) black and path from g to p is through W(p),"
                         " the interchange should be <W(p), NW(p)>")
        self.assertEqual(1,
                         len(solver.array_interchange),
                         "The number interchange should be 1")

    def test_p_cut_g_to_p_from_Np_NNWp_white(self):
        img_depart = [[0, 0, 0, 0, 0],
                      [0, 1, 1, 1, 0],
                      [0, 1, 0, 1, 0],
                      [0, 1, 0, 1, 0],
                      [0, 0, 1, 1, 0],
                      [0, 0, 0, 0, 0]]

        img_soluce = [[0, 0, 0, 0, 0],
                      [0, 1, 1, 1, 0],
                      [0, 1, 0, 1, 0],
                      [0, 1, 1, 0, 0],
                      [0, 0, 1, 1, 0],
                      [0, 0, 0, 0, 0]]

        binary_image = BinaryImage.create_img_from_array(img_depart, BLACK_CONNEXITY, WHITE_CONNEXITY)

        solver = B4W8_Solver(binary_image, BinaryImage.create_img_vertical(binary_image.size))

        solver.resolve_image(binary_image)

        self.assertEqual(img_soluce,
                         binary_image.convert_pixels_to_img(),
                         "In case of p cut vertex and g=NWW(p) black and path from g to p is through N(p) "
                         "and NNW(p) is white, the interchange should be <N(p), NW(p)>")
        self.assertEqual(1,
                         len(solver.array_interchange),
                         "The number interchange should be 1")

    def test_p_cut_g_to_p_from_Np_NNWWp_white(self):
        img_depart = [[0, 0, 0, 0, 0, 0],
                      [0, 1, 1, 1, 1, 0],
                      [0, 1, 0, 1, 1, 0],
                      [0, 1, 1, 0, 1, 0],
                      [0, 0, 0, 1, 1, 0],
                      [0, 0, 0, 0, 0, 0]]

        img_soluce = [[0, 0, 0, 0, 0, 0, 0],
                      [0, 1, 1, 1, 1, 0, 0],
                      [0, 1, 0, 1, 1, 1, 0],
                      [0, 1, 0, 1, 0, 0, 0],
                      [0, 0, 0, 1, 1, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0]]

        binary_image = BinaryImage.create_img_from_array(img_depart, BLACK_CONNEXITY, WHITE_CONNEXITY)

        solver = B4W8_Solver(binary_image, BinaryImage.create_img_vertical(binary_image.size))

        solver.resolve_image(binary_image)

        self.assertEqual(img_soluce,
                         binary_image.convert_pixels_to_img(),
                         "In case of p cut vertex and g=NWW(p) black and path from g to p is through N(p) "
                         "and NNW(p) is black and NNWW(p) is white, "
                         "the interchanges should be <g, E(g)> and <N(p), NNE(p)>")
        self.assertEqual(2,
                         len(solver.array_interchange),
                         "The number interchange should be 2")
