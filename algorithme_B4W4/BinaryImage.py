import matplotlib.pyplot as plt
from enum import Enum
import math
from matplotlib.patches import Rectangle
import numpy as np
import cv2
import Pixel


# Enum for cardinal directions
# N for North, E for East, S for South, W for West
class Direction(Enum):
    N = 1
    E = 2
    S = 3
    W = 4


# Class that'll handle all the image with its pixels.
class BinaryImage:

    # Constructor with a precreated image
    def __init__(self, image):
        self.image = image
        self.size = len(image)                              # WARNING image size must be perfectly squared (same number lines/columns)
        self.arrayPixelsImage = self.create_pixel_array() # From the image creating the pixels
        self.n = self.get_n(self.arrayPixelsImage)          # Get the number of black pixels on the image
        self.whitePixels = self.get_white_pixels()          # Get all the white pixels
        self.blackPixels = self.get_black_pixels()          # Get all the black pixels

    # Convert pixels array to image structure
    # Return arrays in an array
    def convert_pixels_to_img(self):
        img = []
        for i in range(0, self.size):
            line = []
            for j in range(0, self.size):
                if self.arrayPixelsImage[i * self.size + j].black:
                    line.append(1)
                else:
                    line.append(0)
            img.append(line)
        return img

    # Creating pixels array from image structure
    # Return an array of Pixel
    def create_pixel_array(self):
        pixels = []
        for line in range(0, self.size):
            for column in range(0, self.size):
                pixels.append(Pixel.Pixel(line, column, True if self.image[line][column] == 1 else False ))

        return pixels

    # Get the number of black pixels in the image
    def get_n(self, arrayPixelsImage):
        temp = 0
        for pixel in self.arrayPixelsImage:
            if pixel.black:
                temp += 1
        return temp

    # Return a Pixel array with all white pixels
    def get_white_pixels(self):
        temp = []
        for pixel in self.arrayPixelsImage:
            if not pixel.black:
                temp.append(pixel)
        return temp

    # Return a Pixel array with all black pixels
    def get_black_pixels(self):
        temp = []
        for pixel in self.arrayPixelsImage:
            if pixel.black:
                temp.append(pixel)
        return temp

    # Method that show the image at screen
    def show_image(self):
        plt.figure()
        lineWidth = 1
        print(self.size)

        # Creation of the lines of the grid
        for i in range(self.size + 1):
            plt.gca().add_line(plt.Line2D((0, self.size), (i, i), lw=lineWidth, color='dimgray'))

        # Creation of the columns of the grid
        for i in range(self.size + 1):
            plt.gca().add_line(plt.Line2D((i, i), (0, self.size ), lw=lineWidth, color='dimgray'))

        # Filling the grid with the black pixels
        for pixel in self.blackPixels:
            plt.gca().add_patch(plt.Rectangle((pixel.y, pixel.x), 1, 1, fc='#000000'))

        plt.axis('scaled')
        plt.show()
