import matplotlib.pyplot as plt
from enum import Enum
import math
import random
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
    def __init__(self, param):
        if type(param) is list:
            self.image = param[::-1]                                    # On inverse les éléments du tableau
                                                                        # pour un affichage cohérent
        elif type(param) is int:
            self.image = self.generate_random_B4W4img(param)
        else:
            print("Error in parameter, please enter an image or an int")
            exit()

        self.height = len(self.image)                                   # Hauteur de l'image
        self.width = len(self.image[0])                                 # Largeur de l'image
        self.arrayPixelsImage = self.create_pixel_array(self.image)     # From the image creating the pixels

        self.n = self.get_n()                                           # Get the number of black pixels on the image
        self.whitePixels = self.get_white_pixels()                      # Get all the white pixels
        self.blackPixels = self.get_black_pixels()                      # Get all the black pixels
        print(len(self.blackPixels))
        print("taille pixels", self.arrayPixelsImage)
        self.expand_image()                                             # If black pixels are adjacent to the limit
                                                                        # Expand the white pixels

        self.connectedB4W4, \
        self.isolatedBlackPixels, \
        self.isolatedWhitePixels = self.is_image_connected_B4B4()       # Check if the image is fully B4,W4-connected

    # Return an image with n random black pixels that respect B4W4 connexity
    def generate_random_B4W4img(self, n):
        self.height = n
        self.width = n
        self.image = []
        for line in range(0, self.height):
            self.image.append([0]*self.width)

        self.image[1][1] = 1
        self.arrayPixelsImage = self.create_pixel_array(self.image)
        self.blackPixels = self.get_black_pixels()
        self.whitePixels = self.get_white_pixels()

        i = 1
        while i < n:
            blackPixel = random.choice(self.blackPixels)
            randomDirection = random.choice(list(Direction))
            changeDone = False

            if randomDirection == Direction.N:
                changeDone = self.change_color_pixel(blackPixel.x + 1, blackPixel.y, True)
            elif randomDirection == Direction.E:
                changeDone = self.change_color_pixel(blackPixel.x, blackPixel.y+1, True)
            elif randomDirection == Direction.S:
                changeDone = self.change_color_pixel(blackPixel.x - 1, blackPixel.y, True)
            elif randomDirection == Direction.W:
                changeDone = self.change_color_pixel(blackPixel.x, blackPixel.y-1, True)

            if changeDone:
                i += 1

        return self.image

    def change_color_pixel(self, x, y, color=False):
        pixel = self.get_pixel(x, y)
        tempColor = pixel.black
        colorInt = 1 if color else 0
        changeDone = False

        if not pixel.black == color:
            pixel.black = color
            if self.is_image_connected_B4B4():
                self.image[pixel.x][pixel.y] = colorInt
                self.blackPixels.append(pixel)
                self.expand_image()
                changeDone = True
            else:
                pixel.black = tempColor
                changeDone = False

        return changeDone

    # Expand white pixel, to avoid black pixels on the border
    def expand_image(self):
        for pixel in self.blackPixels:
            if pixel.x == self.height - 1:
                print("passe x == max hauteur -1")
                temp = []
                for i in range(0, self.width):
                    temp.append(0)

                self.image.append(temp)
                self.height += 1

            if pixel.x == 0:
                print("passe x == 0")
                temp = []
                for i in range(0, self.width):
                    temp.append(0)

                self.image.insert(0, temp)
                self.shift_pixels(Direction.N)
                self.height += 1

            if pixel.y == self.width - 1:
                print("Passage ici")
                for i in range(0, self.height):
                    self.image[i].append(0)

                self.width += 1

            if pixel.y == 0:
                print(self.image)
                for i in range(0, self.height):
                    print("i = ", i)
                    self.image[i].insert(0, 0)

                print(self.image)
                self.shift_pixels(Direction.E)
                self.width += 1

        self.update_pixel_array(self.image)
        self.whitePixels = self.get_white_pixels()  # updating all the white pixels
        self.blackPixels = self.get_black_pixels()  # updating all the black pixels

    # For the expand, when you add a line of white pixels under or on the left of the figure,
    # We move all the pixel upward or on the right
    def shift_pixels(self, direction):
        if direction == Direction.N:
            for pixel in self.arrayPixelsImage:
                pixel.x += 1
        elif direction == Direction.E:
            for pixel in self.arrayPixelsImage:
                pixel.y += 1

    # Check if the image respect the B4W4 restrictions
    # Return True or False, array of not visited black pixels, array of not visited white pixels
    def is_image_connected_B4B4(self):
        notVisitedBlack = self.get_black_pixels()
        blackVisited = []
        blackWaitingList = []
        if notVisitedBlack:
            blackWaitingList = [notVisitedBlack.pop()]

        notVisitedWhite = self.get_white_pixels()
        whiteVisited = []
        whiteWaitingList = []
        if notVisitedWhite:
            whiteWaitingList = [notVisitedWhite.pop()]

        while len(blackWaitingList) > 0:
            pixel = blackWaitingList.pop()
            for neighbour in self.get_4_neighbours(pixel):
                if neighbour in notVisitedBlack:
                    blackWaitingList.append(neighbour)
                    notVisitedBlack.remove(neighbour)

            blackVisited.append(pixel)

        while len(whiteWaitingList) > 0:
            pixel = whiteWaitingList.pop()
            for neighbour in self.get_4_neighbours(pixel):
                if neighbour in notVisitedWhite:
                    whiteWaitingList.append(neighbour)
                    notVisitedWhite.remove(neighbour)

            whiteVisited.append(pixel)

        return len(notVisitedBlack) == 0 and len(notVisitedWhite) == 0, notVisitedBlack, notVisitedWhite

    # Return a list of the 4_neighbours of a pixel
    def get_4_neighbours(self, pixel):
        temp = []

        if pixel.x + 1 < self.height:
            temp.append(self.get_pixel(pixel.x + 1, pixel.y))
        if pixel.y + 1 < self.width:
            temp.append(self.get_pixel(pixel.x, pixel.y + 1))
        if pixel.x - 1 >= 0:
            temp.append(self.get_pixel(pixel.x - 1, pixel.y))
        if pixel.y - 1 >= 0:
            temp.append(self.get_pixel(pixel.x, pixel.y - 1))

        return temp

    # Give the pixel from coordinates
    def get_pixel(self, x, y):
        return self.arrayPixelsImage[x * self.width + y]

    # Convert pixels array to image structure
    # Return arrays in an array
    def convert_pixels_to_img(self, arrayPixels):
        img = []
        for i in range(0, self.height):
            line = []
            for j in range(0, self.width):
                if arrayPixels[i * self.height + j].black:
                    line.append(1)
                else:
                    line.append(0)
            img.append(line)
        return img

    # Creating pixels array from image structure
    # Return an array of Pixel
    def create_pixel_array(self, img):
        pixels = []
        for line in range(0, self.height):
            for column in range(0, self.width):
                pixel = Pixel.Pixel(line, column, True if img[line][column] == 1 else False)
                pixels.append(pixel)

        return pixels

    # Add all new pixels from an expand to self.arrayPixelsImage
    def update_pixel_array(self, img):
        for line in range(0, self.height):
            for column in range(0, self.width):
                pixel = Pixel.Pixel(line, column, True if img[line][column] == 1 else False)
                if pixel not in self.arrayPixelsImage:
                    self.arrayPixelsImage.append(pixel)

        self.arrayPixelsImage.sort(key=lambda k: [k.x, k.y])

    # Get the number of black pixels in the image
    def get_n(self):
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

        # Creation of the lines of the grid
        for i in range(self.height + 1):
            plt.gca().add_line(plt.Line2D((0, self.width), (i, i), lw=lineWidth, color='dimgray'))

        # Creation of the columns of the grid
        for i in range(self.width + 1):
            plt.gca().add_line(plt.Line2D((i, i), (0, self.height), lw=lineWidth, color='dimgray'))

        # Filling the grid with the black pixels
        for pixel in self.blackPixels:
            plt.gca().add_patch(plt.Rectangle((pixel.y, pixel.x), 1, 1, fc='#000000'))

        # Filling the grid with isolated white pixels
        for pixel in self.isolatedWhitePixels:
            plt.gca().add_patch(plt.Rectangle((pixel.y, pixel.x), 1, 1, fc='red'))

        # Filling the grid with isolated black pixels
        for pixel in self.isolatedBlackPixels:
            plt.gca().add_patch(plt.Rectangle((pixel.y, pixel.x), 1, 1, fc='green'))

        plt.axis('scaled')
        plt.show()

    # Method to print all the informations of the pixels in text
    def print_array_pixels(self):
        for pixel in self.arrayPixelsImage:
            print(pixel, "\n\n")