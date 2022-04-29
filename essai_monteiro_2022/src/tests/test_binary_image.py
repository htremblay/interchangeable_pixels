import unittest
import random

from algorithme_B4W4.New_Conception_v2.src.models.binary_image import BinaryImage
from algorithme_B4W4.New_Conception_v2.src.models.pixel import PixelColor

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

IMG_SWAP_HOLE = [[0, 0, 0, 0, 0, 0, 0],
                 [0, 1, 1, 1, 0, 0, 0],
                 [0, 1, 0, 0, 0, 1, 0],
                 [0, 1, 1, 1, 1, 1, 0],
                 [0, 0, 0, 0, 0, 0, 0]]


class BinaryImageTests(unittest.TestCase):
    # Tests number of element = number of black pixel + white pixels
    def test_number_elements_img(self):
        binary_image = BinaryImage.create_random_img(SIZE_IMAGE, BLACK_CONNEXITY, WHITE_CONNEXITY, SEED)
        total_pixels = binary_image.width * binary_image.height
        self.assertEqual(total_pixels, len(binary_image.black_pixels) + len(binary_image.white_pixels))

        binary_image = BinaryImage.create_img_from_array(IMG_TEST_CASE_1, BLACK_CONNEXITY, WHITE_CONNEXITY)
        self.assertEqual(9, len(binary_image.black_pixels) + len(binary_image.white_pixels))

    # Tests hard entry image and generated image if they are connected
    def test_fct_image_connected(self):
        binary_image = BinaryImage.create_img_from_array(IMG_NOT_CONNECTED_B4, 4, 4)
        self.assertEqual((False, [binary_image.get_pixel(1, 2)], []), binary_image.is_image_connected(),
                         "Wrong B4 connexity check")

        binary_image = BinaryImage.create_img_from_array(IMG_NOT_CONNECTED_W4, 4, 4)
        self.assertEqual((False, [], [binary_image.get_pixel(2, 2)]), binary_image.is_image_connected(),
                         "Wrong W4 connexity check")

        binary_image = BinaryImage.create_img_from_array(IMG_NOT_CONNECTED_B8, 8, 4)
        self.assertEqual((False, [binary_image.get_pixel(1, 3)], []), binary_image.is_image_connected(),
                         "Wrong B8 connexity check")

        binary_image = BinaryImage.create_img_from_array(IMG_NOT_CONNECTED_W8, 4, 8)
        self.assertEqual((False, [], [binary_image.get_pixel(2, 2)]), binary_image.is_image_connected(),
                         "Wrong W8 connexity check")

        binary_image = BinaryImage.create_img_from_array(IMG_B4W4, 4, 4)
        self.assertEqual((True, [], []), binary_image.is_image_connected(), "B4W4-Image is valid ")

        binary_image = BinaryImage.create_img_from_array(IMG_B4W8, 4, 8)
        self.assertEqual((True, [], []), binary_image.is_image_connected(), "B4W8-Image is valid ")

        binary_image = BinaryImage.create_img_from_array(IMG_B8W4, 8, 4)
        self.assertEqual((True, [], []), binary_image.is_image_connected(), "B8W4-Image is valid ")

        binary_image = BinaryImage.create_img_from_array(IMG_B8W8, 8, 8)
        self.assertEqual((True, [], []), binary_image.is_image_connected(), "B8W8-Image is valid ")

        binary_image = BinaryImage.create_random_img(SIZE_IMAGE, 4, 4, SEED)
        self.assertEqual((True, [], []), binary_image.is_image_connected(), "Generated B4W4 image")

        binary_image = BinaryImage.create_random_img(SIZE_IMAGE, 4, 8, SEED)
        self.assertEqual((True, [], []), binary_image.is_image_connected(), "Generated B4W8 image")

        binary_image = BinaryImage.create_random_img(SIZE_IMAGE, 8, 4, SEED)
        self.assertEqual((True, [], []), binary_image.is_image_connected(), "Generated B8W4 image")

        binary_image = BinaryImage.create_random_img(SIZE_IMAGE, 8, 8, SEED)
        self.assertEqual((True, [], []), binary_image.is_image_connected(), "Generated B8W8 image")

    # Test the good resolution of expand
    def test_fct_image_expand(self):
        binary_image = BinaryImage.create_img_from_array(IMG_EXPAND_1, BLACK_CONNEXITY, WHITE_CONNEXITY)
        self.assertEqual(8, len(binary_image.white_pixels),
                         "[[1]] image should create 8 white pixels around the black pixel")
        self.assertEqual(1, len(binary_image.black_pixels),
                         "[[1]] should keep exactly 1 black pixel in its image")
        self.assertEqual(binary_image.get_pixel(1, 1).color, PixelColor.BLACK,
                         "Pixel(1,1) should be black")

        binary_image = BinaryImage.create_img_from_array(IMG_EXPAND_2, BLACK_CONNEXITY, WHITE_CONNEXITY)
        self.assertEqual(16, len(binary_image.white_pixels),
                         "[[1, 1, 1],\
                           [0, 1, 0]] image should create 14 white pixels around the black (total = 16 because "
                         "already 2 white pixels in image)")
        self.assertEqual(4, len(binary_image.black_pixels),
                         "[[1, 1, 1],\
                           [0, 1, 0]] should keep exactly 4 black pixel in its image")
        self.assertEqual(binary_image.get_pixel(2, 1).color, PixelColor.BLACK,
                         "Pixel(2,1) should be black")
        self.assertEqual(binary_image.get_pixel(2, 2).color, PixelColor.BLACK,
                         "Pixel(2,2) should be black")
        self.assertEqual(binary_image.get_pixel(2, 3).color, PixelColor.BLACK,
                         "Pixel(2,3) should be black")
        self.assertEqual(binary_image.get_pixel(1, 2).color, PixelColor.BLACK,
                         "Pixel(1,2) should be black")

    # Test the good application of reducing white pixels of an image
    # def test_fct_img_reduce(self):
    #     binary_image = BinaryImage.create_img_from_array(IMG_REDUCE, BLACK_CONNEXITY, WHITE_CONNEXITY)
    #     self.assertEqual(13, len(binary_image.white_pixels),
    #                      "Image should reduce to 13 white pixels around the black pixels")
    #     self.assertEqual(3, len(binary_image.black_pixels),
    #                      "Image should keep exactly 3 black pixel in its image")
    #     self.assertEqual(binary_image.get_pixel(2, 1).color, PixelColor.BLACK,
    #                      "Pixel(2,1) should be black")
    #     self.assertEqual(binary_image.get_pixel(2, 2).color, PixelColor.BLACK,
    #                      "Pixel(2,2) should be black")
    #     self.assertEqual(binary_image.get_pixel(1, 2).color, PixelColor.BLACK,
    #                      "Pixel(1,2) should be black")

    # Test the good computing of border image
    def test_fct_border_image(self):
        binary_image = BinaryImage.create_img_from_array(IMG_TEST_CASE_1, BLACK_CONNEXITY, WHITE_CONNEXITY)
        border = binary_image.get_border_image(BLACK_CONNEXITY)
        self.assertEqual(False, binary_image.get_pixel(0, 0) in border,
                         "(0,0) shouldn't be in border for B4")
        self.assertEqual(True, binary_image.get_pixel(0, 1) in border,
                         "(0,1) should be in border for B4")
        self.assertEqual(False, binary_image.get_pixel(0, 2) in border,
                         "(0,2) shouldn't be in border for B4")
        self.assertEqual(True, binary_image.get_pixel(1, 0) in border,
                         "(1,0) should be in border for B4")
        self.assertEqual(False, binary_image.get_pixel(1, 1) in border,
                         "(1,1) shouldn't be in border for B4")
        self.assertEqual(True, binary_image.get_pixel(1, 2) in border,
                         "(1,2) should be in border for B4")
        self.assertEqual(False, binary_image.get_pixel(2, 0) in border,
                         "(2,0) shouldn't be in border for B4")
        self.assertEqual(True, binary_image.get_pixel(2, 1) in border,
                         "(2,1) should be in border for B4")
        self.assertEqual(False, binary_image.get_pixel(2, 2) in border,
                         "(2,2) shouldn't be in border for B4")

        binary_image = BinaryImage.create_img_from_array(IMG_TEST_CASE_1, 8, WHITE_CONNEXITY)
        border = binary_image.get_border_image(8)
        self.assertEqual(True, binary_image.get_pixel(0, 0) in border,
                         "(0,0) should be in border for B8")
        self.assertEqual(True, binary_image.get_pixel(0, 1) in border,
                         "(0,1) should be in border for B8")
        self.assertEqual(True, binary_image.get_pixel(0, 2) in border,
                         "(0,2) should be in border for B8")
        self.assertEqual(True, binary_image.get_pixel(1, 0) in border,
                         "(1,0) should be in border for B8")
        self.assertEqual(False, binary_image.get_pixel(1, 1) in border,
                         "(1,1) shouldn't be in border for B8")
        self.assertEqual(True, binary_image.get_pixel(1, 2) in border,
                         "(1,2) should be in border for B8")
        self.assertEqual(True, binary_image.get_pixel(2, 0) in border,
                         "(2,0) should be in border for B8")
        self.assertEqual(True, binary_image.get_pixel(2, 1) in border,
                         "(2,1) should be in border for B8")
        self.assertEqual(True, binary_image.get_pixel(2, 2) in border,
                         "(2,2) should be in border for B8")

    # Test the good working of changing a pixel
    # TODO Case for 4,8 8,4 8,8
    def test_fct_change_color_pixel(self):
        binary_image = BinaryImage.create_img_from_array(IMG_B4W4, BLACK_CONNEXITY, WHITE_CONNEXITY)
        self.assertEqual(False, binary_image.change_color_pixel(binary_image.get_pixel(0, 0), PixelColor.WHITE),
                         "Changing same color of pixel should return False")
        self.assertEqual(False, binary_image.change_color_pixel(binary_image.get_pixel(0, 0), PixelColor.BLACK),
                         "Not respecting connexity after change should return False")
        self.assertEqual(False, binary_image.change_color_pixel(binary_image.get_pixel(2, 3), PixelColor.BLACK),
                         "Creating a hole in white connexity")
        self.assertEqual(True, binary_image.change_color_pixel(binary_image.get_pixel(1, 0), PixelColor.BLACK),
                         "Respecting both connexity after change should return True")

    # Test the neighbours of a pixel
    def test_get_neighbours(self):
        binary_image = BinaryImage.create_img_from_array(IMG_B4W4, BLACK_CONNEXITY, WHITE_CONNEXITY)
        neighbours = binary_image.get_neighbours(binary_image.get_pixel(1, 1), 8)

        # Both pixel verification
        verify_neighbours = binary_image.get_pixel(0, 0) in neighbours \
                          and binary_image.get_pixel(0, 1) in neighbours \
                          and binary_image.get_pixel(0, 2) in neighbours \
                          and binary_image.get_pixel(1, 0) in neighbours \
                          and binary_image.get_pixel(1, 2) in neighbours \
                          and binary_image.get_pixel(2, 0) in neighbours \
                          and binary_image.get_pixel(2, 1) in neighbours \
                          and binary_image.get_pixel(2, 2) in neighbours \

        self.assertEqual(True, verify_neighbours, "8-neighbours with black and white pixels not working ")

        # white pixels verification
        neighbours = binary_image.get_neighbours(binary_image.get_pixel(1, 1), 4, PixelColor.WHITE)
        verify_neighbours = binary_image.get_pixel(1, 0) in neighbours \
                          and binary_image.get_pixel(0, 1) in neighbours

        self.assertEqual(True, verify_neighbours, "4-neighbours with white pixels only not working")

        not_neighbours = binary_image.get_pixel(0, 2) in neighbours and binary_image.get_pixel(0, 0) in neighbours \
                        and binary_image.get_pixel(1, 0) in neighbours \
                        and binary_image.get_pixel(1, 2) in neighbours \
                        and binary_image.get_pixel(2, 0) in neighbours \
                        and binary_image.get_pixel(2, 1) in neighbours \
                        and binary_image.get_pixel(2, 2) in neighbours \

        self.assertEqual(False, not_neighbours, "4-neighbours with white pixels only not working")

        # black pixels verification
        neighbours = binary_image.get_neighbours(binary_image.get_pixel(1, 1), 4, PixelColor.BLACK)
        verify_neighbours = binary_image.get_pixel(1, 2) in neighbours \
                          and binary_image.get_pixel(2, 1) in neighbours

        self.assertEqual(True, verify_neighbours, "4-neighbours with white pixels only not working")

        not_neighbours = binary_image.get_pixel(0, 2) in neighbours \
                        and binary_image.get_pixel(0, 0) in neighbours \
                        and binary_image.get_pixel(1, 0) in neighbours \
                        and binary_image.get_pixel(1, 0) in neighbours \
                        and binary_image.get_pixel(2, 0) in neighbours \
                        and binary_image.get_pixel(0, 1) in neighbours \
                        and binary_image.get_pixel(2, 2) in neighbours

        self.assertEqual(False, not_neighbours, "4-neighbours with white pixels only not working")

    # Test if the method return the good pixel
    def test_get_pixel(self):
        binary_image = BinaryImage.create_img_from_array(IMG_B4W4, BLACK_CONNEXITY, WHITE_CONNEXITY)
        height = random.randint(0, binary_image.height - 1)
        width = random.randint(0, binary_image.width - 1)

        pixel = binary_image.get_pixel(height, width)
        self.assertEqual(True, pixel.x == height and pixel.y == width, "GetPixel coordinates ("
                         + str(height) + ", " + str(width) + ")")

    # Test if the conversion to pixel is working
    def convert_pixels_to_img(self):
        binary_image = BinaryImage.create_img_from_array(IMG_SWAP, BLACK_CONNEXITY, WHITE_CONNEXITY)
        self.assertEqual(IMG_SWAP,
                         binary_image.convert_pixels_to_img(),
                         "error in the method convert_pixels_to_img")

    # Tests for swap pixels without creating hole
    def test_swap_pixels_no_hole(self):
        binary_image = BinaryImage.create_img_from_array(IMG_SWAP, BLACK_CONNEXITY, WHITE_CONNEXITY)

        # Not respecting B4W4 connexity
        self.assertEqual(False,
                         binary_image.swap_pixels(binary_image.get_pixel(1, 2).get_coords(),
                                                  binary_image.get_pixel(1, 3).get_coords(),
                                          swap_active=True),
                         "The swap <(1,2), (1,3)> should return False (connexity not respected)")

        # Trying to swap the same pixel
        self.assertEqual(False,
                         binary_image.swap_pixels(binary_image.get_pixel(1, 2).get_coords(),
                                                  binary_image.get_pixel(1, 2).get_coords(),
                                          swap_active=True),
                         "The swap <(1,2), (1,2)> should return False (Swapping the same pixel)")

        # Trying to swap the same 2 pixels with the same color
        self.assertEqual(False,
                         binary_image.swap_pixels(binary_image.get_pixel(1, 2).get_coords(),
                                                  binary_image.get_pixel(2, 2).get_coords(),
                                          swap_active=True),
                         "The swap <(1,2), (2,2)> should return False (Swapping pixels with the same color)")

        # Testing if the image wasn't impacted by a wrong swaps
        self.assertEqual(IMG_SWAP,
                         binary_image.convert_pixels_to_img(),
                         "The previous swaps were False, the image shouldn't have changed")

        # Testing an authorized swap, without really swapping the pixels
        self.assertEqual(True,
                         binary_image.swap_pixels(binary_image.get_pixel(1, 2).get_coords(),
                                                  binary_image.get_pixel(1, 1).get_coords(),
                                          swap_active=False),
                         "The swap <(1,2), (1,1)> should return True")

        # Testing if the swap_active parameter is working
        self.assertEqual(IMG_SWAP,
                         binary_image.convert_pixels_to_img(),
                         "The swap active was false, image shouldn't have change")

        # Testing an authorized swap and really swapping the pixels
        self.assertEqual(True,
                         binary_image.swap_pixels(binary_image.get_pixel(1, 2).get_coords(),
                                                  binary_image.get_pixel(1, 1).get_coords(),
                                          swap_active=True),
                         "The swap <(1,2), (1,1)> should return True")

        # Testing if the swap is done correctly
        self.assertEqual([[0, 0, 0, 0],
                          [0, 1, 1, 0],
                          [0, 1, 0, 0],
                          [0, 0, 0, 0]],
                         binary_image.convert_pixels_to_img(),
                         "The swap should have been done (swap_active=True)")

    # Tests for swap pixels creating a hole
    def test_swap_pixels_creating_hole(self):
        binary_image = BinaryImage.create_img_from_array(IMG_SWAP_HOLE, BLACK_CONNEXITY, WHITE_CONNEXITY)

        # Trying to swap the same 2 pixels with the same color
        self.assertEqual(False,
                         binary_image.swap_pixels(binary_image.get_pixel(1, 5).get_coords(),
                                                  binary_image.get_pixel(2, 4).get_coords(),
                                          swap_active=True),
                         "The swap <(1,5), (2,4)> should return False (Swapping pixels create hole in whites)")

        # Testing if the image wasn't impacted by a wrong swaps
        self.assertEqual([[0, 0, 0, 0, 0, 0, 0],
                          [0, 1, 1, 1, 0, 0, 0],
                          [0, 1, 0, 0, 0, 1, 0],
                          [0, 1, 1, 1, 1, 1, 0],
                          [0, 0, 0, 0, 0, 0, 0]],
                         binary_image.convert_pixels_to_img(),
                         "The previous swaps weren't autorised (returned False), the image shouldn't have changed")
