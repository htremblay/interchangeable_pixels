import unittest

from algorithme_B4W4.New_Conception_v2.src.models.binary_image import BinaryImage
from algorithme_B4W4.New_Conception_v2.src.solvers.B4W4.b4w4_elements import B4W4_Elements

BLACK_CONNEXITY = 4
WHITE_CONNEXITY = 4

IMG_TEST_CASE_1 = [[0, 0, 0],
                   [0, 1, 0],
                   [0, 0, 0]]



IMG_ALGO_B4W4_ELEMENTS = [[0, 0, 0, 1, 1, 0, 0],
                          [0, 0, 0, 1, 0, 0, 1],
                          [0, 0, 1, 1, 1, 1, 1],
                          [0, 0, 1, 0, 0, 1, 0],
                          [0, 0, 1, 1, 0, 1, 1],
                          [0, 0, 1, 0, 0, 0, 1],
                          [0, 0, 0, 0, 0, 0, 0]]


class AlgoB4W4Tests(unittest.TestCase):


    # Test for compute frontier
    def test_compute_frontier(self):
        binary_image = BinaryImage.create_img_from_array(IMG_ALGO_B4W4_ELEMENTS, BLACK_CONNEXITY, WHITE_CONNEXITY)
        algo = B4W4_Elements(binary_image)

        frontier_test = [algo.binary_image.get_pixel(1, 5),
                         algo.binary_image.get_pixel(2, 5),
                         algo.binary_image.get_pixel(4, 5),
                         algo.binary_image.get_pixel(5, 5)]

        frontier_algo, temp = algo.compute_frontier()

        self.assertEqual(frontier_test,
                         frontier_algo,
                         "Pixels that should be in frontier [(1, 5), (2, 5), (4, 5), (5, 5)]")

    # Test compute anchor
    def test_compute_anchor(self):
        binary_image = BinaryImage.create_img_from_array(IMG_ALGO_B4W4_ELEMENTS, BLACK_CONNEXITY, WHITE_CONNEXITY)
        algo = B4W4_Elements(binary_image)

        self.assertEqual(algo.binary_image.get_pixel(2, 4),
                         algo.compute_anchor(),
                         "Anchor should be (2, 4)")

        binary_image = BinaryImage.create_img_from_array(IMG_TEST_CASE_1, BLACK_CONNEXITY, WHITE_CONNEXITY)
        algo = B4W4_Elements(binary_image)
        self.assertEqual(None,
                         algo.compute_anchor(),
                         "Anchor should be None on vertical image")

    # Test compute lead_elbow
    def test_compute_lead_elbow(self):
        binary_image = BinaryImage.create_img_from_array(IMG_ALGO_B4W4_ELEMENTS, BLACK_CONNEXITY, WHITE_CONNEXITY)
        algo = B4W4_Elements(binary_image)

        self.assertEqual(algo.binary_image.get_pixel(4, 5),
                         algo.compute_lead_elbow(),
                         "lead elbow should be (4, 5)")

    # Test compute height
    def test_compute_height(self):
        binary_image = BinaryImage.create_img_from_array(IMG_ALGO_B4W4_ELEMENTS, BLACK_CONNEXITY, WHITE_CONNEXITY)
        algo = B4W4_Elements(binary_image)

        self.assertEqual(2,
                         algo.height,
                         "height should be -1")

        binary_image = BinaryImage.create_img_from_array(IMG_TEST_CASE_1, BLACK_CONNEXITY, WHITE_CONNEXITY)
        algo = B4W4_Elements(binary_image)
        self.assertEqual(None,
                         algo.height,
                         "height should be 0 in vertical image")

    # Test compute top pixel
    def test_compute_top_pixel(self):
        binary_image = BinaryImage.create_img_from_array(IMG_ALGO_B4W4_ELEMENTS, BLACK_CONNEXITY, WHITE_CONNEXITY)
        algo = B4W4_Elements(binary_image)

        self.assertEqual(algo.binary_image.get_pixel(5, 5),
                         algo.compute_top_pixel(),
                         "Anchor should be (5, 5)")

    # Test compute all elbows
    def test_compute_all_elbows(self):
        binary_image = BinaryImage.create_img_from_array(IMG_ALGO_B4W4_ELEMENTS, BLACK_CONNEXITY, WHITE_CONNEXITY)
        algo = B4W4_Elements(binary_image)

        elbows_test = [algo.binary_image.get_pixel(1, 1),
                       algo.binary_image.get_pixel(1, 5),
                       algo.binary_image.get_pixel(2, 2),
                       algo.binary_image.get_pixel(4, 5),
                       algo.binary_image.get_pixel(6, 3)]

        elbows_algo = algo.compute_all_elbows()

        self.assertEqual(elbows_test,
                         elbows_algo,
                         "Pixels that should be in frontier [(1, 1), (1, 5), (2, 2), (4, 5), (6, 3)]")

    # Test is_elbow
    def test_is_elbow(self):
        binary_image = BinaryImage.create_img_from_array(IMG_ALGO_B4W4_ELEMENTS, BLACK_CONNEXITY, WHITE_CONNEXITY)
        algo = B4W4_Elements(binary_image)

        for pixel in algo.binary_image.get_black_pixels():
            self.assertEqual(pixel in algo.compute_all_elbows(),
                             algo.is_elbow(pixel))
