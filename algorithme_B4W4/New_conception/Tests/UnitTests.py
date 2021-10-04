import unittest
from algorithme_B4W4.New_conception.BinaryImage import BinaryImage
from algorithme_B4W4.New_conception.Enumeration import BinaryElement
from algorithme_B4W4.New_conception.AlgoB4W4 import AlgoB4W4
import random

SEED = 4
BLACK_CONNEXITY = 4
WHITE_CONNEXITY = 4
SIZE_IMAGE = 100

IMG_TEST_CASE_1 = [[0, 0, 0],
                   [0, 1, 0],
                   [0, 0, 0]]

IMG_NOT_CONNECTED_B4 = [[0, 0, 0, 0],
                        [0, 1, 0, 0],
                        [0, 0, 1, 0],
                        [0, 0, 0, 0]]

IMG_NOT_CONNECTED_W4 = [[0, 0, 0, 0, 0],
                        [0, 1, 1, 0, 0],
                        [0, 1, 0, 1, 0],
                        [0, 1, 1, 1, 0],
                        [0, 0, 0, 0, 0]]

IMG_NOT_CONNECTED_B8 = [[0, 0, 0, 0, 0],
                        [0, 1, 1, 0, 0],
                        [0, 1, 0, 0, 0],
                        [0, 1, 0, 1, 0],
                        [0, 0, 0, 0, 0]]

IMG_NOT_CONNECTED_W8 = [[0, 0, 0, 0, 0],
                        [0, 1, 1, 1, 0],
                        [0, 1, 0, 1, 0],
                        [0, 1, 1, 1, 0],
                        [0, 0, 0, 0, 0]]

IMG_B4W4 = [[0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0]]

IMG_B4W8 = [[0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 1, 1, 1, 0],
            [0, 0, 0, 0, 0]]

IMG_B8W4 = [[0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0]]

IMG_B8W8 = [[0, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 0],
            [0, 1, 0, 1, 0, 0],
            [0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0]]

IMG_EXPAND_1 = [[1]]

IMG_EXPAND_2 = [[1, 1, 1],
                [0, 1, 0]]

IMG_REDUCE = [[0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 1, 1, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0]]

IMG_SWAP = [[0, 0, 0, 0],
            [0, 1, 1, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 0]]

IMG_SWAP_HOLE = [[0, 0, 0, 0, 0],
                 [1, 1, 1, 0, 0],
                 [1, 0, 0, 0, 1],
                 [1, 1, 1, 1, 1],
                 [0, 0, 0, 0, 0]]


IMG_ALGO_B4W4_ELEMENTS = [[0, 0, 0, 1, 1, 0, 0],
                          [0, 0, 0, 1, 0, 0, 1],
                          [0, 0, 1, 1, 1, 1, 1],
                          [0, 0, 1, 0, 0, 1, 0],
                          [0, 0, 1, 1, 0, 1, 1],
                          [0, 0, 1, 0, 0, 0, 1],
                          [0, 0, 0, 0, 0, 0, 0]]


class BinaryImageTests(unittest.TestCase):
    # Tests number of element = number of black pixel + white pixels
    def test_number_elements_img(self):
        binaryImage = BinaryImage(SIZE_IMAGE, BLACK_CONNEXITY, WHITE_CONNEXITY, SEED)
        total_pixels = binaryImage.width * binaryImage.height
        self.assertEqual(total_pixels, len(binaryImage.blackPixels) + len(binaryImage.whitePixels))

        binaryImage = BinaryImage(IMG_TEST_CASE_1, BLACK_CONNEXITY, WHITE_CONNEXITY)
        self.assertEqual(9, len(binaryImage.blackPixels) + len(binaryImage.whitePixels))

    # Tests hard entry image and generated image if they are connected
    def test_fct_image_connected(self):
        binaryImage = BinaryImage(IMG_NOT_CONNECTED_B4, 4, 4)
        self.assertEqual((False, [binaryImage.get_pixel(1, 2)], []), binaryImage.is_image_connected(),
                         "Wrong B4 connexity check")

        binaryImage = BinaryImage(IMG_NOT_CONNECTED_W4, 4, 4)
        self.assertEqual((False, [], [binaryImage.get_pixel(2, 2)]), binaryImage.is_image_connected(),
                         "Wrong W4 connexity check")

        binaryImage = BinaryImage(IMG_NOT_CONNECTED_B8, 8, 4)
        self.assertEqual((False, [binaryImage.get_pixel(1, 3)], []), binaryImage.is_image_connected(),
                         "Wrong B8 connexity check")

        binaryImage = BinaryImage(IMG_NOT_CONNECTED_W8, 4, 8)
        self.assertEqual((False, [], [binaryImage.get_pixel(2, 2)]), binaryImage.is_image_connected(),
                         "Wrong W8 connexity check")

        binaryImage = BinaryImage(IMG_B4W4, 4, 4)
        self.assertEqual((True, [], []), binaryImage.is_image_connected(), "B4W4-Image is valid ")

        binaryImage = BinaryImage(IMG_B4W8, 4, 8)
        self.assertEqual((True, [], []), binaryImage.is_image_connected(), "B4W8-Image is valid ")

        binaryImage = BinaryImage(IMG_B8W4, 8, 4)
        self.assertEqual((True, [], []), binaryImage.is_image_connected(), "B8W4-Image is valid ")

        binaryImage = BinaryImage(IMG_B8W8, 8, 8)
        self.assertEqual((True, [], []), binaryImage.is_image_connected(), "B8W8-Image is valid ")

        binaryImage = BinaryImage(SIZE_IMAGE, 4, 4, SEED)
        self.assertEqual((True, [], []), binaryImage.is_image_connected(), "Generated B4W4 image")

        binaryImage = BinaryImage(SIZE_IMAGE, 4, 8, SEED)
        self.assertEqual((True, [], []), binaryImage.is_image_connected(), "Generated B4W8 image")

        binaryImage = BinaryImage(SIZE_IMAGE, 8, 4, SEED)
        self.assertEqual((True, [], []), binaryImage.is_image_connected(), "Generated B8W4 image")

        binaryImage = BinaryImage(SIZE_IMAGE, 8, 8, SEED)
        self.assertEqual((True, [], []), binaryImage.is_image_connected(), "Generated B8W8 image")

    # Test the good resolution of expand
    def test_fct_image_expand(self):
        binaryImage = BinaryImage(IMG_EXPAND_1, BLACK_CONNEXITY, WHITE_CONNEXITY)
        self.assertEqual(8, len(binaryImage.whitePixels),
                         "[[1]] image should create 8 white pixels around the black pixel")
        self.assertEqual(1, len(binaryImage.blackPixels),
                         "[[1]] should keep exactly 1 black pixel in its image")
        self.assertEqual(binaryImage.get_pixel(1, 1).color, BinaryElement.Black,
                         "Pixel(1,1) should be black")

        binaryImage = BinaryImage(IMG_EXPAND_2, BLACK_CONNEXITY, WHITE_CONNEXITY)
        self.assertEqual(16, len(binaryImage.whitePixels),
                         "[[1, 1, 1],\
                           [0, 1, 0]] image should create 14 white pixels around the black (total = 16 because "
                         "already 2 white pixels in image)")
        self.assertEqual(4, len(binaryImage.blackPixels),
                         "[[1, 1, 1],\
                           [0, 1, 0]] should keep exactly 4 black pixel in its image")
        self.assertEqual(binaryImage.get_pixel(2, 1).color, BinaryElement.Black,
                         "Pixel(2,1) should be black")
        self.assertEqual(binaryImage.get_pixel(2, 2).color, BinaryElement.Black,
                         "Pixel(2,2) should be black")
        self.assertEqual(binaryImage.get_pixel(2, 3).color, BinaryElement.Black,
                         "Pixel(2,3) should be black")
        self.assertEqual(binaryImage.get_pixel(1, 2).color, BinaryElement.Black,
                         "Pixel(1,2) should be black")

    # Test the good application of reducing white pixels of an image
    def test_fct_img_reduce(self):
        binaryImage = BinaryImage(IMG_REDUCE, BLACK_CONNEXITY, WHITE_CONNEXITY)
        self.assertEqual(13, len(binaryImage.whitePixels),
                         "Image should reduce to 13 white pixels around the black pixels")
        self.assertEqual(3, len(binaryImage.blackPixels),
                         "Image should keep exactly 3 black pixel in its image")
        self.assertEqual(binaryImage.get_pixel(2, 1).color, BinaryElement.Black,
                         "Pixel(2,1) should be black")
        self.assertEqual(binaryImage.get_pixel(2, 2).color, BinaryElement.Black,
                         "Pixel(2,2) should be black")
        self.assertEqual(binaryImage.get_pixel(1, 2).color, BinaryElement.Black,
                         "Pixel(1,2) should be black")

    # Test the good computing of border image
    def test_fct_border_image(self):
        binaryImage = BinaryImage(IMG_TEST_CASE_1, BLACK_CONNEXITY, WHITE_CONNEXITY)
        border = binaryImage.get_border_image(binaryImage.blackPixels, 4)
        self.assertEqual(False, binaryImage.get_pixel(0, 0) in border,
                         "(0,0) shouldn't be in border for B4")
        self.assertEqual(True, binaryImage.get_pixel(0, 1) in border,
                         "(0,1) should be in border for B4")
        self.assertEqual(False, binaryImage.get_pixel(0, 2) in border,
                         "(0,2) shouldn't be in border for B4")
        self.assertEqual(True, binaryImage.get_pixel(1, 0) in border,
                         "(1,0) should be in border for B4")
        self.assertEqual(False, binaryImage.get_pixel(1, 1) in border,
                         "(1,1) shouldn't be in border for B4")
        self.assertEqual(True, binaryImage.get_pixel(1, 2) in border,
                         "(1,2) should be in border for B4")
        self.assertEqual(False, binaryImage.get_pixel(2, 0) in border,
                         "(2,0) shouldn't be in border for B4")
        self.assertEqual(True, binaryImage.get_pixel(2, 1) in border,
                         "(2,1) should be in border for B4")
        self.assertEqual(False, binaryImage.get_pixel(2, 2) in border,
                         "(2,2) shouldn't be in border for B4")

        binaryImage = BinaryImage(IMG_TEST_CASE_1, 8, WHITE_CONNEXITY)
        border = binaryImage.get_border_image(binaryImage.blackPixels, 8)
        self.assertEqual(True, binaryImage.get_pixel(0, 0) in border,
                         "(0,0) should be in border for B8")
        self.assertEqual(True, binaryImage.get_pixel(0, 1) in border,
                         "(0,1) should be in border for B8")
        self.assertEqual(True, binaryImage.get_pixel(0, 2) in border,
                         "(0,2) should be in border for B8")
        self.assertEqual(True, binaryImage.get_pixel(1, 0) in border,
                         "(1,0) should be in border for B8")
        self.assertEqual(False, binaryImage.get_pixel(1, 1) in border,
                         "(1,1) shouldn't be in border for B8")
        self.assertEqual(True, binaryImage.get_pixel(1, 2) in border,
                         "(1,2) should be in border for B8")
        self.assertEqual(True, binaryImage.get_pixel(2, 0) in border,
                         "(2,0) should be in border for B8")
        self.assertEqual(True, binaryImage.get_pixel(2, 1) in border,
                         "(2,1) should be in border for B8")
        self.assertEqual(True, binaryImage.get_pixel(2, 2) in border,
                         "(2,2) should be in border for B8")

    # Test the good working of changing a pixel
    # TODO Case for 4,8 8,4 8,8
    def test_fct_change_color_pixel(self):
        binaryImage = BinaryImage(IMG_B4W4, BLACK_CONNEXITY, WHITE_CONNEXITY)
        self.assertEqual(False, binaryImage.change_color_pixel(binaryImage.get_pixel(0, 0), BinaryElement.White),
                         "Changing same color of pixel should return False")
        self.assertEqual(False, binaryImage.change_color_pixel(binaryImage.get_pixel(0, 0), BinaryElement.Black),
                         "Not respecting connexity after change should return False")
        self.assertEqual(False, binaryImage.change_color_pixel(binaryImage.get_pixel(2, 3), BinaryElement.Black),
                         "Creating a hole in white connexity")
        self.assertEqual(True, binaryImage.change_color_pixel(binaryImage.get_pixel(1, 0), BinaryElement.Black),
                         "Respecting both connexity after change should return True")

    # Test the neighbours of a pixel
    def test_get_neighbours(self):
        binaryImage = BinaryImage(IMG_B4W4, BLACK_CONNEXITY, WHITE_CONNEXITY)
        neighbours = binaryImage.get_neighbours(binaryImage.get_pixel(1, 1), 8)

        # Both pixel verification
        verifNeighbours = binaryImage.get_pixel(0, 0) in neighbours \
                          and binaryImage.get_pixel(0, 1) in neighbours \
                          and binaryImage.get_pixel(0, 2) in neighbours \
                          and binaryImage.get_pixel(1, 0) in neighbours \
                          and binaryImage.get_pixel(1, 2) in neighbours \
                          and binaryImage.get_pixel(2, 0) in neighbours \
                          and binaryImage.get_pixel(2, 1) in neighbours \
                          and binaryImage.get_pixel(2, 2) in neighbours \

        self.assertEqual(True, verifNeighbours, "8-neighbours with black and white pixels not working ")

        # white pixels verification
        neighbours = binaryImage.get_neighbours(binaryImage.get_pixel(1, 1), 4, BinaryElement.White)
        verifNeighbours = binaryImage.get_pixel(1, 0) in neighbours \
                          and binaryImage.get_pixel(0, 1) in neighbours

        self.assertEqual(True, verifNeighbours, "4-neighbours with white pixels only not working")

        notNeighbours = binaryImage.get_pixel(0, 2) in neighbours \
                          and binaryImage.get_pixel(0, 0) in neighbours \
                          and binaryImage.get_pixel(1, 0) in neighbours \
                          and binaryImage.get_pixel(1, 2) in neighbours \
                          and binaryImage.get_pixel(2, 0) in neighbours \
                          and binaryImage.get_pixel(2, 1) in neighbours \
                          and binaryImage.get_pixel(2, 2) in neighbours \

        self.assertEqual(False, notNeighbours, "4-neighbours with white pixels only not working")

        # black pixels verification
        neighbours = binaryImage.get_neighbours(binaryImage.get_pixel(1, 1), 4, BinaryElement.Black)
        verifNeighbours = binaryImage.get_pixel(1, 2) in neighbours \
                          and binaryImage.get_pixel(2, 1) in neighbours

        self.assertEqual(True, verifNeighbours, "4-neighbours with white pixels only not working")

        notNeighbours = binaryImage.get_pixel(0, 2) in neighbours \
                        and binaryImage.get_pixel(0, 0) in neighbours \
                        and binaryImage.get_pixel(1, 0) in neighbours \
                        and binaryImage.get_pixel(1, 0) in neighbours \
                        and binaryImage.get_pixel(2, 0) in neighbours \
                        and binaryImage.get_pixel(0, 1) in neighbours \
                        and binaryImage.get_pixel(2, 2) in neighbours

        self.assertEqual(False, notNeighbours, "4-neighbours with white pixels only not working")

    # Test if the method return the good pixel
    def test_get_pixel(self):
        binaryImage = BinaryImage(IMG_B4W4, BLACK_CONNEXITY, WHITE_CONNEXITY)
        height = random.randint(0, binaryImage.height - 1)
        width = random.randint(0, binaryImage.width - 1)

        pixel = binaryImage.get_pixel(height, width)
        self.assertEqual(True, pixel.x == height and pixel.y == width, "GetPixel coordinates ("
                         + str(height) + ", " + str(width) + ")")

    # Test if the conversion to pixel is working
    def convert_pixels_to_img(self):
        binaryImage = BinaryImage(IMG_SWAP, BLACK_CONNEXITY, WHITE_CONNEXITY)
        self.assertEqual(IMG_SWAP,
                         binaryImage.convert_pixels_to_img(),
                         "error in the method convert_pixels_to_img")


class AlgoB4W4Tests(unittest.TestCase):
    # Tests for swap pixels without creating hole
    def test_swap_pixels_no_hole(self):
        binaryImage = BinaryImage(IMG_SWAP, BLACK_CONNEXITY, WHITE_CONNEXITY)
        algo = AlgoB4W4(binaryImage)

        # Not repescting B4W4 connexity
        self.assertEqual(False,
                         algo.swap_pixels(binaryImage.get_pixel(1, 2), binaryImage.get_pixel(1, 3), swap_active=True),
                         "The swap <(1,2), (1,3)> should return False (connexity not respected)")

        # Trying to swap the same pixel
        self.assertEqual(False,
                         algo.swap_pixels(binaryImage.get_pixel(1, 2), binaryImage.get_pixel(1, 2), swap_active=True),
                         "The swap <(1,2), (1,2)> should return False (Swapping the same pixel)")

        # Trying to swap the same 2 pixels with the same color
        self.assertEqual(False,
                         algo.swap_pixels(binaryImage.get_pixel(1, 2), binaryImage.get_pixel(2, 2), swap_active=True),
                         "The swap <(1,2), (2,2)> should return False (Swapping pixels with the same color)")

        # Testing if the image wasn't impacted by a wrong swaps
        self.assertEqual(IMG_SWAP,
                         algo.binaryImage.convert_pixels_to_img(),
                         "The previous swaps were False, the image shouldn't have changed")

        # Testing an authorized swap, without really swapping the pixels
        self.assertEqual(True,
                         algo.swap_pixels(binaryImage.get_pixel(1, 2), binaryImage.get_pixel(1, 1), swap_active=False),
                         "The swap <(1,2), (1,1)> should return True")

        # Testing if the swap_active parameter is working
        self.assertEqual(IMG_SWAP,
                         algo.binaryImage.convert_pixels_to_img(),
                         "The swap active was false, image shouldn't have change")

        # Testing an authorized swap and really swapping the pixels
        self.assertEqual(True,
                         algo.swap_pixels(binaryImage.get_pixel(1, 2), binaryImage.get_pixel(1, 1), swap_active=True),
                         "The swap <(1,2), (1,1)> should return True")

        # Testing if the swap is done correctly
        self.assertEqual([[0, 0, 0, 0],
                          [0, 1, 1, 0],
                          [0, 1, 0, 0],
                          [0, 0, 0, 0]],
                         algo.binaryImage.convert_pixels_to_img(),
                         "The swap should have been done (swap_active=True)")

    # Tests for swap pixels creating a hole
    def test_swap_pixels_creating_hole(self):
        binaryImage = BinaryImage(IMG_SWAP_HOLE, BLACK_CONNEXITY, WHITE_CONNEXITY)
        algo = AlgoB4W4(binaryImage)

        # Trying to swap the same 2 pixels with the same color
        self.assertEqual(False,
                         algo.swap_pixels(binaryImage.get_pixel(1, 2), binaryImage.get_pixel(2, 2), swap_active=True),
                         "The swap <(1,4), (2,3)> should return False (Swapping pixels create hole in whites)")

        # Testing if the image wasn't impacted by a wrong swaps
        self.assertEqual(IMG_SWAP_HOLE,
                         algo.binaryImage.convert_pixels_to_img(),
                         "The previous swaps were False, the image shouldn't have changed")

    # Test for compute frontier
    def test_compute_frontier(self):
        binaryImage = BinaryImage(IMG_ALGO_B4W4_ELEMENTS, BLACK_CONNEXITY, WHITE_CONNEXITY)
        algo = AlgoB4W4(binaryImage)

        frontierTest = [algo.binaryImage.get_pixel(1, 5),
                        algo.binaryImage.get_pixel(2, 5),
                        algo.binaryImage.get_pixel(4, 5),
                        algo.binaryImage.get_pixel(5, 5)]

        frontierAlgo, temp = algo.compute_frontier()

        self.assertEqual(frontierTest,
                         frontierAlgo,
                         "Pixels that should be in frontier [(1, 5), (2, 5), (4, 5), (5, 5)]")

    # Test compute anchor
    def test_compute_anchor(self):
        binaryImage = BinaryImage(IMG_ALGO_B4W4_ELEMENTS, BLACK_CONNEXITY, WHITE_CONNEXITY)
        algo = AlgoB4W4(binaryImage)

        self.assertEqual(algo.binaryImage.get_pixel(2, 4),
                         algo.compute_anchor(),
                         "Anchor should be (2, 4)")

        binaryImage = BinaryImage(IMG_TEST_CASE_1, BLACK_CONNEXITY, WHITE_CONNEXITY)
        algo = AlgoB4W4(binaryImage)
        self.assertEqual(None,
                         algo.compute_anchor(),
                         "Anchor should be None on vertical image")

    # Test compute lead_elbow
    def test_compute_lead_elbow(self):
        binaryImage = BinaryImage(IMG_ALGO_B4W4_ELEMENTS, BLACK_CONNEXITY, WHITE_CONNEXITY)
        algo = AlgoB4W4(binaryImage)

        self.assertEqual(algo.binaryImage.get_pixel(4, 5),
                         algo.compute_lead_elbow(),
                         "lead elbow should be (4, 5)")

    # Test compute height
    def test_compute_height(self):
        binaryImage = BinaryImage(IMG_ALGO_B4W4_ELEMENTS, BLACK_CONNEXITY, WHITE_CONNEXITY)
        algo = AlgoB4W4(binaryImage)

        self.assertEqual(2,
                         algo.height,
                         "height should be -1")

        binaryImage = BinaryImage(IMG_TEST_CASE_1, BLACK_CONNEXITY, WHITE_CONNEXITY)
        algo = AlgoB4W4(binaryImage)
        self.assertEqual(None,
                         algo.height,
                         "height should be 0 in vertical image")

    # Test compute top pixel
    def test_compute_top_pixel(self):
        binaryImage = BinaryImage(IMG_ALGO_B4W4_ELEMENTS, BLACK_CONNEXITY, WHITE_CONNEXITY)
        algo = AlgoB4W4(binaryImage)

        self.assertEqual(algo.binaryImage.get_pixel(5, 5),
                         algo.compute_top_pixel(),
                         "Anchor should be (5, 5)")

    # Test compute all elbows
    def test_compute_all_elbows(self):
        binaryImage = BinaryImage(IMG_ALGO_B4W4_ELEMENTS, BLACK_CONNEXITY, WHITE_CONNEXITY)
        algo = AlgoB4W4(binaryImage)

        elbowsTest = [algo.binaryImage.get_pixel(1, 1),
                        algo.binaryImage.get_pixel(1, 5),
                        algo.binaryImage.get_pixel(2, 2),
                        algo.binaryImage.get_pixel(4, 5),
                        algo.binaryImage.get_pixel(6, 3)]

        elbowsAlgo = algo.compute_all_elbows()

        self.assertEqual(elbowsTest,
                         elbowsAlgo,
                         "Pixels that should be in frontier [(1, 1), (1, 5), (2, 2), (4, 5), (6, 3)]")

    # Test is_eblow
    def test_is_elbow(self):
        binaryImage = BinaryImage(IMG_ALGO_B4W4_ELEMENTS, BLACK_CONNEXITY, WHITE_CONNEXITY)
        algo = AlgoB4W4(binaryImage)

        for pixel in algo.binaryImage.get_black_pixels():
            self.assertEqual(pixel in algo.compute_all_elbows(),
                             algo.is_elbow(pixel))


