import unittest

from algorithme_B4W4.New_Conception_v2.src.models.binary_image import BinaryImage
from algorithme_B4W4.New_Conception_v2.src.solvers.B8W4.b8w4_solver import B8W4_Solver

BLACK_CONNEXITY = 8
WHITE_CONNEXITY = 4


class AlgoB8W4Tests(unittest.TestCase):

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

        solver = B8W4_Solver(binary_image, BinaryImage.create_img_vertical(binary_image.size))

        solver.resolve_image(binary_image)

        self.assertEqual(img_soluce,
                         binary_image.convert_pixels_to_img(),
                         "In case of p not cut vertex and N(p) black, the interchange should be <p, NE(p)>")
        self.assertEqual(1,
                         len(solver.array_interchange),
                         "The number interchange should be 1")

    def test_p_not_cut_Wp_NWp_black(self):
        img_depart = [[0, 0, 0, 0],
                      [0, 1, 0, 0],
                      [0, 1, 1, 0],
                      [0, 0, 0, 0]]

        img_soluce = [[0, 0, 0, 0],
                      [0, 1, 1, 0],
                      [0, 1, 0, 0],
                      [0, 0, 0, 0]]

        binary_image = BinaryImage.create_img_from_array(img_depart, BLACK_CONNEXITY, WHITE_CONNEXITY)

        solver = B8W4_Solver(binary_image, BinaryImage.create_img_vertical(binary_image.size))

        solver.resolve_image(binary_image)

        self.assertEqual(img_soluce,
                         binary_image.convert_pixels_to_img(),
                         "In case of p not cut vertex and NW(p) & W(p) black, the interchange should be <p, N(p)>")
        self.assertEqual(1,
                         len(solver.array_interchange),
                         "The number interchange should be 1")

    def test_p_not_cut_NWp_black(self):
        img_depart = [[0, 0, 0, 0],
                      [0, 1, 0, 0],
                      [0, 0, 1, 0],
                      [0, 0, 0, 0]]

        img_soluce = [[0, 0, 0, 0],
                      [0, 1, 1, 0],
                      [0, 0, 0, 0],
                      [0, 0, 0, 0]]

        binary_image = BinaryImage.create_img_from_array(img_depart, BLACK_CONNEXITY, WHITE_CONNEXITY)

        solver = B8W4_Solver(binary_image, BinaryImage.create_img_vertical(binary_image.size))

        solver.resolve_image(binary_image)

        self.assertEqual(img_soluce,
                         binary_image.convert_pixels_to_img(),
                         "In case of p not cut vertex and NW(p) & W(p) white, the interchange should be <p, N(p)>")
        self.assertEqual(1,
                         len(solver.array_interchange),
                         "The number interchange should be 1")

    def test_p_not_cut_Wp_black(self):
        img_depart = [[0, 0, 0, 0],
                      [0, 0, 0, 0],
                      [0, 1, 1, 0],
                      [0, 0, 0, 0]]

        img_soluce = [[0, 0, 0, 0],
                      [0, 0, 1, 0],
                      [0, 1, 0, 0],
                      [0, 0, 0, 0]]

        binary_image = BinaryImage.create_img_from_array(img_depart, BLACK_CONNEXITY, WHITE_CONNEXITY)

        solver = B8W4_Solver(binary_image, BinaryImage.create_img_vertical(binary_image.size))

        solver.resolve_image(binary_image)

        self.assertEqual(img_soluce,
                         binary_image.convert_pixels_to_img(),
                         "In case of p not cut vertex and W(p) black & NW(p) white, the interchange should be <p, N(p)>")
        self.assertEqual(1,
                         len(solver.array_interchange),
                         "The number interchange should be 1")

    def test_p_not_cut_SWp_black_W_white_not_cut(self):
        img_depart = [[0, 0, 0, 0],
                      [0, 0, 1, 0],
                      [0, 1, 0, 0],
                      [0, 0, 0, 0]]

        img_soluce = [[0, 0, 0],
                      [0, 1, 0],
                      [0, 1, 0],
                      [0, 0, 0]]

        binary_image = BinaryImage.create_img_from_array(img_depart, BLACK_CONNEXITY, WHITE_CONNEXITY)

        solver = B8W4_Solver(binary_image, BinaryImage.create_img_vertical(binary_image.size))

        solver.resolve_image(binary_image)

        self.assertEqual(img_soluce,
                         binary_image.convert_pixels_to_img(),
                         "In case of p not cut vertex and SW(p) black & W(p) white and not cut,"
                         " the interchange should be <p, W(p)>")
        self.assertEqual(1,
                         len(solver.array_interchange),
                         "The number interchange should be 1")

    def test_p_not_cut_SWp_black_W_white_cut(self):
        img_depart = [[0, 0, 0, 0, 0, 0],
                      [0, 1, 1, 0, 0, 0],
                      [0, 1, 0, 0, 1, 0],
                      [0, 1, 1, 1, 0, 0],
                      [0, 0, 0, 0, 0, 0]]

        img_soluce = [[0, 0, 0, 0, 0],
                      [0, 1, 1, 1, 0],
                      [0, 1, 0, 0, 0],
                      [0, 1, 1, 1, 0],
                      [0, 0, 0, 0, 0]]

        binary_image = BinaryImage.create_img_from_array(img_depart, BLACK_CONNEXITY, WHITE_CONNEXITY)

        solver = B8W4_Solver(binary_image, BinaryImage.create_img_vertical(binary_image.size))

        solver.resolve_image(binary_image)

        self.assertEqual(img_soluce,
                         binary_image.convert_pixels_to_img(),
                         "In case of p not cut vertex and SW(p) black & W(p) white cut,"
                         " the interchange should be <p, NW(p)>")
        self.assertEqual(1,
                         len(solver.array_interchange),
                         "The number interchange should be 1")

    def test_p_cut_Wp_white_not_cut(self):
        img_depart = [[0, 0, 0, 0, 0, 0],
                      [0, 1, 1, 1, 1, 0],
                      [0, 0, 0, 0, 1, 0],
                      [0, 1, 1, 1, 0, 0],
                      [0, 0, 0, 0, 0, 0]]

        img_soluce = [[0, 0, 0, 0, 0, 0],
                      [0, 1, 1, 1, 1, 0],
                      [0, 0, 0, 1, 0, 0],
                      [0, 1, 1, 1, 0, 0],
                      [0, 0, 0, 0, 0, 0]]

        binary_image = BinaryImage.create_img_from_array(img_depart, BLACK_CONNEXITY, WHITE_CONNEXITY)

        solver = B8W4_Solver(binary_image, BinaryImage.create_img_vertical(binary_image.size))

        solver.resolve_image(binary_image)

        self.assertEqual(img_soluce,
                         binary_image.convert_pixels_to_img(),
                         "In case of p cut vertex and W(p) white not cut,"
                         " the interchange should be <p, W(p)>")
        self.assertEqual(1,
                         len(solver.array_interchange),
                         "The number interchange should be 1")

    def test_p_cut_Wp_white_cut_G_through_SWp(self):
        img_depart = [[0, 0, 0, 0, 0, 0],
                      [0, 1, 1, 0, 1, 0],
                      [0, 1, 0, 0, 1, 0],
                      [0, 1, 1, 1, 0, 0],
                      [0, 0, 0, 0, 0, 0]]

        img_soluce = [[0, 0, 0, 0, 0, 0],
                      [0, 1, 1, 1, 1, 0],
                      [0, 1, 0, 0, 0, 0],
                      [0, 1, 1, 1, 0, 0],
                      [0, 0, 0, 0, 0, 0]]

        binary_image = BinaryImage.create_img_from_array(img_depart, BLACK_CONNEXITY, WHITE_CONNEXITY)

        solver = B8W4_Solver(binary_image, BinaryImage.create_img_vertical(binary_image.size))

        solver.resolve_image(binary_image)

        self.assertEqual(img_soluce,
                         binary_image.convert_pixels_to_img(),
                         "In case of p cut vertex and W(p) white cut, g goes to p through SW(p)"
                         " the interchange should be <p, NW(p)>")
        self.assertEqual(1,
                         len(solver.array_interchange),
                         "The number interchange should be 1")

    def test_p_cut_Wp_white_cut_G_through_Np_Sl_not_cut(self):
        img_depart = [[0, 0, 0, 0, 0, 0],
                      [0, 0, 1, 1, 0, 0],
                      [0, 1, 0, 0, 1, 0],
                      [0, 1, 0, 0, 1, 0],
                      [0, 1, 1, 0, 1, 0],
                      [0, 0, 0, 0, 1, 0],
                      [0, 0, 0, 1, 0, 0],
                      [0, 0, 0, 0, 0, 0]]

        img_soluce = [[0, 0, 0, 0, 0, 0],
                      [0, 0, 1, 1, 0, 0],
                      [0, 1, 0, 1, 0, 0],
                      [0, 1, 0, 0, 1, 0],
                      [0, 1, 1, 0, 1, 0],
                      [0, 0, 0, 0, 1, 0],
                      [0, 0, 0, 1, 0, 0],
                      [0, 0, 0, 0, 0, 0]]

        binary_image = BinaryImage.create_img_from_array(img_depart, BLACK_CONNEXITY, WHITE_CONNEXITY)

        solver = B8W4_Solver(binary_image, BinaryImage.create_img_vertical(binary_image.size))

        solver.resolve_image(binary_image)

        self.assertEqual(img_soluce,
                         binary_image.convert_pixels_to_img(),
                         "In case of p cut vertex and W(p) white cut, g goes to p through N(p)"
                         "and S(l) is not cut vertex the interchange should be <SE(l), S(l)>")
        self.assertEqual(1,
                         len(solver.array_interchange),
                         "The number interchange should be 1")

    def test_p_cut_Wp_white_cut_G_through_Np_Sl_cut_SSWl_not_cut(self):
        img_depart = [[0, 0, 0, 0, 0, 0],
                      [0, 0, 1, 1, 1, 0],
                      [0, 1, 0, 0, 1, 0],
                      [0, 0, 1, 0, 1, 0],
                      [0, 0, 0, 0, 1, 0],
                      [0, 0, 0, 1, 0, 0],
                      [0, 0, 0, 0, 0, 0]]

        img_soluce = [[0, 0, 0, 0, 0, 0],
                      [0, 0, 1, 1, 1, 0],
                      [0, 1, 0, 1, 1, 0],
                      [0, 0, 0, 0, 1, 0],
                      [0, 0, 0, 0, 1, 0],
                      [0, 0, 0, 1, 0, 0],
                      [0, 0, 0, 0, 0, 0]]

        binary_image = BinaryImage.create_img_from_array(img_depart, BLACK_CONNEXITY, WHITE_CONNEXITY)

        solver = B8W4_Solver(binary_image, BinaryImage.create_img_vertical(binary_image.size))

        solver.resolve_image(binary_image)

        self.assertEqual(img_soluce,
                         binary_image.convert_pixels_to_img(),
                         "In case of p cut vertex and W(p) white cut, g goes to p through N(p)"
                         "and l is cut vertex but SSW(l) is not cut the interchange should be <SSW(l), S(l)>")
        self.assertEqual(1,
                         len(solver.array_interchange),
                         "The number interchange should be 1")

    def test_p_cut_Wp_white_cut_G_through_Np_Sl_cut_SSWl_cut_z_exist_Nz_and_NNz_white(self):
        img_depart = [[0, 0, 0, 0, 0, 0],
                      [0, 0, 1, 1, 1, 0],
                      [0, 1, 0, 0, 1, 0],
                      [0, 0, 1, 0, 1, 0],
                      [0, 1, 0, 0, 1, 0],
                      [0, 1, 0, 0, 1, 0],
                      [0, 1, 1, 0, 1, 0],
                      [0, 0, 1, 0, 1, 0],
                      [0, 0, 0, 0, 1, 0],
                      [0, 0, 0, 1, 0, 0],
                      [0, 0, 0, 0, 0, 0]]

        img_soluce = [[0, 0, 0, 0, 0, 0],
                      [0, 0, 1, 1, 1, 0],
                      [0, 1, 0, 0, 1, 0],
                      [0, 0, 1, 0, 1, 0],
                      [0, 1, 0, 0, 1, 0],
                      [0, 1, 0, 1, 1, 0],
                      [0, 1, 0, 0, 1, 0],
                      [0, 0, 1, 0, 1, 0],
                      [0, 0, 0, 0, 1, 0],
                      [0, 0, 0, 1, 0, 0],
                      [0, 0, 0, 0, 0, 0]]

        binary_image = BinaryImage.create_img_from_array(img_depart, BLACK_CONNEXITY, WHITE_CONNEXITY)

        solver = B8W4_Solver(binary_image, BinaryImage.create_img_vertical(binary_image.size))

        solver.resolve_image(binary_image)

        self.assertEqual(img_soluce,
                         binary_image.convert_pixels_to_img(),
                         "In case of p cut vertex and W(p) white cut, g goes to p through N(p)"
                         "and l is cut vertex and SSW(l) is cut. z exist such as w(z) is black and N(z) and NN(z) are "
                         "white, the interchange should be <z, NE(z)>")
        self.assertEqual(1,
                         len(solver.array_interchange),
                         "The number interchange should be 1")

    def test_p_cut_Wp_white_cut_G_through_Np_Sl_cut_SSWl_cut_z_exist_Nz_or_NNz_black_and_z_equal_ssswl(self):
        img_depart = [[0, 0, 0, 0, 0, 0],
                      [0, 0, 1, 1, 1, 0],
                      [0, 1, 0, 0, 1, 0],
                      [0, 0, 1, 0, 1, 0],
                      [0, 1, 1, 0, 1, 0],
                      [0, 1, 1, 0, 1, 0],
                      [0, 1, 1, 0, 1, 0],
                      [0, 0, 1, 0, 1, 0],
                      [0, 0, 0, 0, 1, 0],
                      [0, 0, 0, 1, 0, 0],
                      [0, 0, 0, 0, 0, 0]]

        img_soluce = [[0, 0, 0, 0, 0, 0],
                      [0, 0, 1, 1, 1, 0],
                      [0, 1, 0, 0, 1, 0],
                      [0, 1, 0, 0, 1, 0],
                      [0, 1, 1, 0, 1, 0],
                      [0, 1, 1, 0, 1, 0],
                      [0, 1, 1, 0, 1, 0],
                      [0, 0, 1, 0, 1, 0],
                      [0, 0, 0, 0, 1, 0],
                      [0, 0, 0, 1, 0, 0],
                      [0, 0, 0, 0, 0, 0]]

        binary_image = BinaryImage.create_img_from_array(img_depart, BLACK_CONNEXITY, WHITE_CONNEXITY)

        solver = B8W4_Solver(binary_image, BinaryImage.create_img_vertical(binary_image.size))

        solver.resolve_image(binary_image)

        self.assertEqual(img_soluce,
                         binary_image.convert_pixels_to_img(),
                         "In case of p cut vertex and W(p) white cut, g goes to p through N(p)"
                         "and l is cut vertex and SSW(l) is cut. z exist such as w(z) is black and N(z) or NN(z) is "
                         "black. If z == sssw(l) the interchange should be <h, W(z)>")
        self.assertEqual(1,
                         len(solver.array_interchange),
                         "The number interchange should be 1")

    def test_p_cut_Wp_white_cut_G_through_Np_Sl_cut_SSWl_cut_z_exist_Nz_or_NNz_black_and_z_in_south_wssssl(self):
        img_depart = [[0, 0, 0, 0, 0, 0],
                      [0, 0, 1, 1, 1, 0],
                      [0, 1, 0, 0, 1, 0],
                      [0, 0, 1, 0, 1, 0],
                      [0, 1, 0, 0, 1, 0],
                      [0, 1, 1, 0, 1, 0],
                      [0, 1, 1, 0, 1, 0],
                      [0, 0, 1, 0, 1, 0],
                      [0, 0, 0, 0, 1, 0],
                      [0, 0, 0, 1, 0, 0],
                      [0, 0, 0, 0, 0, 0]]

        img_soluce = [[0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 1, 1, 1, 0, 0],
                      [0, 1, 0, 0, 1, 0, 0],
                      [0, 0, 1, 0, 0, 1, 0],
                      [0, 1, 0, 1, 0, 1, 0],
                      [0, 1, 0, 0, 0, 1, 0],
                      [0, 1, 1, 0, 1, 0, 0],
                      [0, 0, 1, 0, 1, 0, 0],
                      [0, 0, 0, 0, 1, 0, 0],
                      [0, 0, 0, 1, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0]]

        binary_image = BinaryImage.create_img_from_array(img_depart, BLACK_CONNEXITY, WHITE_CONNEXITY)

        solver = B8W4_Solver(binary_image, BinaryImage.create_img_vertical(binary_image.size))

        solver.resolve_image(binary_image)

        self.assertEqual(img_soluce,
                         binary_image.convert_pixels_to_img(),
                         "In case of p cut vertex and W(p) white cut, g goes to p through N(p)"
                         "and l is cut vertex and SSW(l) is cut. z exist such as w(z) is black and N(z) or NN(z) is "
                         "black. If z == wssss+(l) the 4-vertical interchange should be "
                         "<EE(z), EEE(z)>, <NEE(z), ZEEE(z), <NNEE(z), NNEEE(z)>, <z, NE(z)>")
        self.assertEqual(4,
                         len(solver.array_interchange),
                         "The number interchange should be 4")


    def test_p_cut_Wp_white_cut_G_through_Np_Sl_cut_SSWl_cut_z_no_exist_g_equal_h_SWg_NW_g_black(self):
        img_depart = [[0, 0, 0, 0, 0, 0],
                      [0, 0, 1, 1, 1, 0],
                      [0, 1, 0, 0, 1, 0],
                      [0, 0, 1, 0, 1, 0],
                      [0, 1, 0, 0, 1, 0],
                      [0, 0, 1, 0, 1, 0],
                      [0, 1, 0, 0, 1, 0],
                      [0, 0, 0, 1, 0, 0],
                      [0, 0, 0, 0, 0, 0]]

        img_soluce = [[0, 0, 0, 0, 0, 0],
                      [0, 0, 1, 1, 1, 0],
                      [0, 1, 0, 0, 1, 0],
                      [0, 0, 1, 0, 1, 0],
                      [0, 1, 0, 0, 1, 0],
                      [0, 1, 0, 0, 1, 0],
                      [0, 1, 0, 0, 1, 0],
                      [0, 0, 0, 1, 0, 0],
                      [0, 0, 0, 0, 0, 0]]

        binary_image = BinaryImage.create_img_from_array(img_depart, BLACK_CONNEXITY, WHITE_CONNEXITY)

        solver = B8W4_Solver(binary_image, BinaryImage.create_img_vertical(binary_image.size))

        solver.resolve_image(binary_image)

        self.assertEqual(img_soluce,
                         binary_image.convert_pixels_to_img(),
                         "In case of p cut vertex and W(p) white cut, g goes to p through N(p)"
                         "and l is cut vertex and SSW(l) is cut. all z exist such as w(z) is white"
                         "if g == h and SW(g) and NW(g) are black then the interchange is"
                         "<g, W(g)>")
        self.assertEqual(1,
                         len(solver.array_interchange),
                         "The number interchange should be 1")

    def test_p_cut_Wp_white_cut_G_through_Np_Sl_cut_SSWl_cut_z_no_exist_and_path_through_SWg(self):
        img_depart = [[0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 1, 1, 0, 0],
                      [0, 0, 1, 0, 0, 1, 0],
                      [0, 0, 0, 1, 0, 1, 0],
                      [0, 0, 1, 0, 0, 1, 0],
                      [0, 1, 0, 0, 0, 1, 0],
                      [0, 1, 0, 1, 0, 1, 0],
                      [0, 1, 0, 1, 0, 1, 0],
                      [0, 0, 1, 0, 0, 1, 0],
                      [0, 0, 0, 0, 1, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0]]

        img_soluce = [[0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 1, 1, 0, 0],
                      [0, 0, 1, 0, 0, 1, 0],
                      [0, 0, 0, 1, 0, 1, 0],
                      [0, 0, 1, 0, 0, 1, 0],
                      [0, 1, 0, 0, 0, 1, 0],
                      [0, 1, 0, 1, 1, 1, 0],
                      [0, 1, 0, 0, 0, 1, 0],
                      [0, 0, 1, 0, 0, 1, 0],
                      [0, 0, 0, 0, 1, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0]]

        binary_image = BinaryImage.create_img_from_array(img_depart, BLACK_CONNEXITY, WHITE_CONNEXITY)

        solver = B8W4_Solver(binary_image, BinaryImage.create_img_vertical(binary_image.size))

        solver.resolve_image(binary_image)

        self.assertEqual(img_soluce,
                         binary_image.convert_pixels_to_img(),
                         "In case of p cut vertex and W(p) white cut, g goes to p through N(p)"
                         "and l is cut vertex and SSW(l) is cut. all z exist such as w(z) is white"
                         "if g != h and path is through SW(g) then the interchange is"
                         "<g, NE(g)>")
        self.assertEqual(1,
                         len(solver.array_interchange),
                         "The number interchange should be 1")

    def test_p_cut_Wp_white_cut_G_through_Np_Sl_cut_SSWl_cut_z_no_exist_and_path_through_NWh(self):
        img_depart = [[0, 0, 0, 0, 0, 0],
                      [0, 0, 1, 1, 1, 0],
                      [0, 1, 0, 0, 1, 0],
                      [0, 0, 1, 0, 1, 0],
                      [0, 1, 0, 0, 1, 0],
                      [0, 0, 1, 0, 1, 0],
                      [0, 0, 1, 0, 1, 0],
                      [0, 0, 0, 0, 1, 0],
                      [0, 0, 0, 1, 0, 0],
                      [0, 0, 0, 0, 0, 0]]

        img_soluce = [[0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 1, 1, 1, 0, 0],
                      [0, 1, 0, 0, 1, 0, 0],
                      [0, 0, 1, 0, 1, 0, 0],
                      [0, 1, 0, 0, 1, 1, 0],
                      [0, 0, 0, 1, 0, 0, 0],
                      [0, 0, 1, 0, 1, 0, 0],
                      [0, 0, 0, 0, 1, 0, 0],
                      [0, 0, 0, 1, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0]]

        binary_image = BinaryImage.create_img_from_array(img_depart, BLACK_CONNEXITY, WHITE_CONNEXITY)

        solver = B8W4_Solver(binary_image, BinaryImage.create_img_vertical(binary_image.size))

        solver.resolve_image(binary_image)

        self.assertEqual(img_soluce,
                         binary_image.convert_pixels_to_img(),
                         "In case of p cut vertex and W(p) white cut, g goes to p through N(p)"
                         "and l is cut vertex and SSW(l) is cut. all z exist such as w(z) is white"
                         "if g != h and path is through NW(h) then the interchange is"
                         "<h, E(h)>, <EE(h), NEEE(h)>")
        self.assertEqual(2,
                         len(solver.array_interchange),
                         "The number interchange should be 2")



