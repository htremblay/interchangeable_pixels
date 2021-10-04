import matplotlib.pyplot as plt
from enum import Enum
import math
import random
import Pixel
from tqdm import tqdm


# Enum for cardinal directions
# N for North, E for East, S for South, W for West
class Direction(Enum):
    N = 1
    E = 2
    S = 3
    W = 4


# Class that'll handle all the image with its pixels.
class BinaryImage:

    # Constructor with a precreated image or a int to generate a random image
    def __init__(self, param,):
        if type(param) is list:
            self.image = param[::-1]                                # Reverse the elements of the array (better display)
        elif type(param) is int and param > 0:
            self.borderWhitePixels = []
            self.image = self.generate_random_B4W4img(param)  # If the param is an int, generating random image
        else:                                                       # If the param is not an image or int, show error
            raise ValueError("Error in parameter, please enter an image or an int > 0")

        self.height = len(self.image)                                   # Height of the image
        self.width = len(self.image[0])                                 # Width of the image
        self.arrayPixelsImage = self.create_pixel_array(self.image)     # From the image creating the pixels
        self.borderWhitePixels = self.get_white_border_image()          # All the white pixels 4-adjacent to the image

        self.n = self.get_n()                                           # Get the number of black pixels on the image
        self.whitePixels = self.get_white_pixels()                      # Get all the white pixels
        self.blackPixels = self.get_black_pixels()                      # Get all the black pixels
        self.expand_image()                                             # If black pixels are adjacent to the limit
                                                                        # Expand the white pixels

        self.connectedB4W4, \
        self.isolatedBlackPixels, \
        self.isolatedWhitePixels = self.is_image_connected_B4B4()       # Check if the image is fully B4,W4-connected

    # Return an image with n random black pixels that respect B4W4 connexity
    def generate_random_B4W4img(self, n):
        self.height = 3     # We fix it to 3 because the image is gonna expand with the
        self.width = 3      # creation of black pixels
        self.image = []     # Create empty array

        for line in range(0, self.height):      # Create a completly white image
            self.image.append([0]*self.width)

        self.image[1][1] = 1                        # Set the first middle pixel black
        self.arrayPixelsImage = self.create_pixel_array(self.image) # Create array of pixels
        self.blackPixels = self.get_black_pixels()  # Create array of black pixels
        self.whitePixels = self.get_white_pixels()  # Create array of white pixels

        i = 1  # i = 1 because already 1 pixel on the image
        self.borderWhitePixels = self.get_white_border_image()  # We create a temporary list
        pbar = tqdm(total=n)  # progress bar in print
        pbar.update(1)  # Adding the first pixel

        while i < n:
            borderPixel = random.choice(self.borderWhitePixels)         # Chosing randomly a while pixel in the border
            changeDone = self.change_color_pixel(borderPixel, True)     # Changing the white pixel to black

            if changeDone:                                              # If change has been done
                self.borderWhitePixels = self.get_white_border_image()  # Temporary list takes the new black pixel
                i += 1                                                  # +1 black pixel on the image

                pbar.set_description("Creating an image size n = " + str(n))  # Description for the loading bar
                pbar.update(1)  # Value to update the loading bar (No impact on the algorithm)
            else:
                self.borderWhitePixels.remove(borderPixel)  # Removing the black pixel of the list,
                                                            # so we don't try to pick it again

        pbar.close()                                        # Closing the progress when finished

        return self.image

    def get_white_border_image(self):
        blackPixels = self.get_black_pixels()
        whiteBorder = []
        for blackPixel in blackPixels:
            white_adjacent = self.get_4_white_neighbours(blackPixel)
            for white_pixel in white_adjacent:
                if white_pixel not in whiteBorder:
                    whiteBorder.append(white_pixel)

        return whiteBorder

    # Change the color of a pixel with its coordinates
    # Return a boolean if the change was done
    def change_color_pixel(self, pixel, color=False):
        currentColorPixel = pixel.black         # current color of pixel
        colorInt = 1 if color else 0            # wanted color int
        changeDone = False                      # True when the pixel changed its color

        if currentColorPixel != color:          # Current color needs to be different than the new one
            pixel.black = color                 # Change the color of the pixel with the new one
            isConnected, self.isolatedBlackPixels, self.isolatedWhitePixels = self.is_image_connected_B4B4()  # check B4W4 connexity
            if isConnected:
                # print("Connected really ? ", pixel)
                self.image[pixel.x][pixel.y] = colorInt
                self.blackPixels = self.get_black_pixels()
                self.whitePixels = self.get_white_pixels()
                self.expand_image()
                changeDone = True
            else:
                pixel.black = currentColorPixel
                changeDone = False

        return changeDone

    # Expand white pixel, to avoid black pixels on the border
    def expand_image(self):
        for pixel in self.blackPixels:
            if pixel.x == self.height - 1:
                temp = []
                for i in range(0, self.width):
                    temp.append(0)

                self.image.append(temp)
                self.height += 1

            if pixel.x == 0:
                temp = []
                for i in range(0, self.width):
                    temp.append(0)

                self.image.insert(0, temp)
                self.shift_pixels(Direction.N)
                self.height += 1

            if pixel.y == self.width - 1:
                for i in range(0, self.height):
                    self.image[i].append(0)

                self.width += 1

            if pixel.y == 0:
                for i in range(0, self.height):
                    self.image[i].insert(0, 0)
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

    # Rerturn a list of the 4_neighbours white pixels of a pixel
    def get_4_white_neighbours(self, pixel):
        neighbours = self.get_4_neighbours(pixel)
        temp = []
        for nb in neighbours:
            if not nb.black:
                temp.append(nb)

        return temp

    # Rerturn a list of the 4_neighbours black pixels of a pixel
    def get_4_black_neighbours(self, pixel):
        neighbours = self.get_4_neighbours(pixel)
        temp = []
        for nb in neighbours:
            if nb.black:
                temp.append(nb)

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
                elif pixel in self.arrayPixelsImage:
                    idx = self.arrayPixelsImage.index(pixel)
                    self.arrayPixelsImage[idx] = pixel

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
    def show_image(self, show_border=False, show_isolated=True, arrayPixelToShow=None, i=0):
        plt.figure(i)
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

        if show_isolated:
            # Filling the grid with isolated white pixels
            for pixel in self.isolatedWhitePixels:
                plt.gca().add_patch(plt.Rectangle((pixel.y, pixel.x), 1, 1, fc='orangered'))

            # Filling the grid with isolated black pixels
            for pixel in self.isolatedBlackPixels:
                plt.gca().add_patch(plt.Rectangle((pixel.y, pixel.x), 1, 1, fc='forestgreen'))

        # Filling the grid with isolated white pixels
        if show_border:
            for pixel in self.borderWhitePixels:
                plt.gca().add_patch(plt.Rectangle((pixel.y, pixel.x), 1, 1, fc='cyan'))

        # Filling the grid with pixels we want to show
        if arrayPixelToShow:
            for pixel in arrayPixelToShow:
                plt.gca().add_patch(plt.Rectangle((pixel.y, pixel.x), 1, 1, fc='blue'))

        plt.axis('scaled')
        plt.show()

    # Method to print all the informations of the pixels in text
    def print_array_pixels(self, arrayPixel):
        for pixel in arrayPixel:
            print(pixel, "\n")