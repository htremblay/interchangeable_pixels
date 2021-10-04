import matplotlib.pyplot as plt
from tqdm import tqdm
import random

from algorithme_B4W4.New_conception.Enumeration import Direction
from algorithme_B4W4.New_conception.Enumeration import BinaryElement
from algorithme_B4W4.New_conception.Pixel import Pixel


CONNEXITY_RESTRICTION = [4, 8]


# Class that'll handle all the image with its pixels.
class BinaryImage:

    # Constructor with a precreated image or a int to generate a random image
    def __init__(self, param, blackConnexity=4, whiteConnexity=4, seed=1):
        self.seed = seed

        if type(param) is list:
            self.image = param[::-1]             # Reverse the elements of the array (better display)
            self.image = self.convert_img_to_pixels(self.image)
        elif type(param) is int and param > 0:   # If the param is an int, generating random image
            self.image = self.generate_random_img(param, blackConnexity, whiteConnexity, seed)

        else:                                                       # If the param is not an image or int, show error
            raise ValueError("Error in parameter, please enter an image or an int > 0")


        self.blackConnexity = blackConnexity
        self.whiteConnexity = whiteConnexity
        self.height, self.width = self.get_dimensions()   # Getting dimensions of image
        self.whitePixels = self.get_white_pixels()                  # Get all the white pixels
        self.blackPixels = self.get_black_pixels()                  # Get all the black pixels
        self.size = len(self.blackPixels)                           # Get the number of black pixels on the image

        self.expand_image()  # If black pixels are adjacent to the limit
        self.reduce_image()

        # All the white pixels 4-adjacent to black_pixels
        self.borderWhitePixels = self.get_border_image(self.blackPixels, self.blackConnexity)

        # Check if the image is fully B4,W4-connected
        connected, \
        self.isolatedBlackPixels, \
        self.isolatedWhitePixels = self.is_image_connected()


    def __copy__(self):
        return type(self)(self.convert_pixels_to_img(), self.blackConnexity, self.whiteConnexity, self.seed)

    def __str__(self):
        return ("Array : {" + self.print_array_pixels() + " }"
                + "\nheigt : " + str(self.height) + " width : " + str(self.width)
                + "\nnb black pixels : " + str(len(self.blackPixels))
                + " & nb white pixels : " + str(len(self.whitePixels))
                + "\nimage connected : " + str(self.connected))

    # From a size of image b,w-connexity and a seed generate a ranom image
    def generate_random_img(self, n, blackConnexity=4, whiteConnexity=4, seed=1):
        img = BinaryImage([[1]], blackConnexity, whiteConnexity)

        i = 1                   # i = 1 because already 1 pixel on the image
        pbar = tqdm(total=n)    # progress bar in print
        pbar.update(1)          # Adding the first pixel

        random.seed(seed)

        while i < n:
            # img.show_image(title=str(i) + " IMAGE")
            # print("len ", len(img.borderWhitePixels))
            borderPixel = random.choice(img.borderWhitePixels)  # Chosing randomly a while pixel in the border
            # img.show_image(show_border=True)
            # print("len ", len(img.borderWhitePixels))

            # Changing the white pixel to black
            # img.show_image()
            # print("\nNouveau tour : ", img.print_array_pixels(), "\nPixel choisi : ", borderPixel)
            changeDone = img.change_color_pixel(borderPixel, BinaryElement.Black)

            if changeDone:                                              # If change has been done
                # Temporary list takes the new black pixel
                newBorderPixels = img.get_neighbours(borderPixel, blackConnexity, BinaryElement.White)
                for pixel in newBorderPixels:
                    if pixel not in img.borderWhitePixels:
                        img.borderWhitePixels.append(pixel)
                # img.show_image()
                # print("changeDoned  ", len(img.borderWhitePixels))
                i += 1                                                  # +1 black pixel on the image

                img.expand_image()

                pbar.set_description("Creating an image size n = " + str(n))  # Description for the loading bar
                pbar.update(1)  # Value to update the loading bar (No impact on the algorithm)
            else:
                img.borderWhitePixels.remove(borderPixel)  # Removing the black pixel of the list,
                                                            # so we don't try to pick it again

        pbar.close()                                        # Closing the progress when finished

        # img.show_image(title="Juste avant return")

        return img.image

    # Change the color of a pixel with its coordinates
    # Return a boolean if the change was done
    def change_color_pixel(self, pixel, color):
        idx = self.image.index(pixel)
        currentColorPixel = pixel.color     # current color of pixel
        changeDone = False                  # True when the pixel changed its color

        if currentColorPixel != color:      # Current color needs to be different than the new one
            self.image[idx].color = color   # Change the color of the pixel with the new one
            self.update_black_white([pixel])
            # connected = self.respect_white_connexity(pixel)
            connected, b, w = self.is_image_connected()
            if connected:
                changeDone = True
            else:
                self.image[idx].color = currentColorPixel  # Change the color of the pixel with the old one
                self.update_black_white([pixel])
                changeDone = False

        return changeDone

    # Check if the image respect the Black & White connexity restrictions
    # Return True or False, array of not visited black pixels, array of not visited white pixels
    def is_image_connected(self):
        notVisitedBlack = self.blackPixels.copy()
        blackVisited = []
        blackWaitingList = []
        if notVisitedBlack:
            blackWaitingList = [notVisitedBlack.pop()]

        notVisitedWhite = self.whitePixels.copy()
        whiteVisited = []
        whiteWaitingList = []
        if notVisitedWhite:
            whiteWaitingList = [notVisitedWhite.pop()]

        while len(blackWaitingList) > 0:
            pixel = blackWaitingList.pop()
            for neighbour in self.get_neighbours(pixel, self.blackConnexity, BinaryElement.Black):
                if neighbour in notVisitedBlack:
                    blackWaitingList.append(neighbour)
                    notVisitedBlack.remove(neighbour)

            blackVisited.append(pixel)

        while len(whiteWaitingList) > 0:
            pixel = whiteWaitingList.pop()
            for neighbour in self.get_neighbours(pixel, self.whiteConnexity, BinaryElement.White):
                if neighbour in notVisitedWhite:
                    whiteWaitingList.append(neighbour)
                    notVisitedWhite.remove(neighbour)

            whiteVisited.append(pixel)

        return len(notVisitedBlack) == 0 and len(notVisitedWhite) == 0, notVisitedBlack, notVisitedWhite

    # Get the border of all the black image. You can choose the connexity
    # Return an array of white pixels.
    def get_border_image(self, blackPixels, blackConnexity=4):
        whiteBorder = []
        for blackPixel in blackPixels.copy():
            white_adjacent = self.get_neighbours(blackPixel, blackConnexity, BinaryElement.White)
            for white_pixel in white_adjacent:
                if white_pixel not in whiteBorder:
                    whiteBorder.append(white_pixel)

        return whiteBorder

    # Return an array of Pixels
    # You can chose connexity and the color of pixel you want
    def get_neighbours(self, pixel, connexity=4, color=BinaryElement.Both):
        neighbours = []

        if (connexity not in CONNEXITY_RESTRICTION) or color not in BinaryElement:
            print("Error in color [Enum.BinaryElement] choice or connexity in ", CONNEXITY_RESTRICTION)
        else:
            if pixel.x + 1 < self.height:
                neighbours.append(self.get_pixel(pixel.x + 1, pixel.y))
            if pixel.y + 1 < self.width:
                neighbours.append(self.get_pixel(pixel.x, pixel.y + 1))
            if pixel.x - 1 >= 0:
                neighbours.append(self.get_pixel(pixel.x - 1, pixel.y))
            if pixel.y - 1 >= 0:
                neighbours.append(self.get_pixel(pixel.x, pixel.y - 1))

            if connexity == 8:
                if pixel.x + 1 < self.height and pixel.y + 1 < self.width:
                    neighbours.append(self.get_pixel(pixel.x + 1, pixel.y + 1))
                if pixel.x + 1 < self.height and pixel.y - 1 >= 0:
                    neighbours.append(self.get_pixel(pixel.x + 1, pixel.y - 1))
                if pixel.x - 1 >= 0 and pixel.y + 1 < self.width:
                    neighbours.append(self.get_pixel(pixel.x - 1, pixel.y + 1))
                if pixel.x - 1 >= 0 and pixel.y - 1 >= 0:
                    neighbours.append(self.get_pixel(pixel.x - 1, pixel.y - 1))

        wantedNeighbours = neighbours
        if color != BinaryElement.Both:
            wantedNeighbours = []
            for n in neighbours:
                if n.color == color:
                    wantedNeighbours.append(n)

        return wantedNeighbours

    # Give the pixel from coordinates
    def get_pixel(self, x, y):
        return self.image[x * self.width + y]

    # Method that show the image at screen
    def show_image(self, title="", show_border=False, show_isolated=True, dict_array_pixels=None, nb_figure=0):
        plt.figure(nb_figure)
        plt.title(title)
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
        if dict_array_pixels:
            for color, arrayPixel in dict_array_pixels.items():
                for pixel in arrayPixel:
                    plt.gca().add_patch(plt.Rectangle((pixel.y, pixel.x), 1, 1, fc=str(color)))

        plt.axis('scaled')
        plt.show()

    # Expand white pixel, to avoid black pixels on the border
    def expand_image(self):
        for pixel in self.blackPixels:
            if pixel.x == self.height - 1:
                for i in range(0, self.width):
                    self.image.append(Pixel(self.height, i, BinaryElement.White))
                self.height += 1

            if pixel.x == 0:
                self.shift_pixels(Direction.N)
                for i in range(0, self.width):
                    self.image.append(Pixel(0, i, BinaryElement.White))

                self.height += 1

            if pixel.y == self.width - 1:
                for i in range(0, self.height):
                    self.image.append(Pixel(i, self.width, BinaryElement.White))
                self.width += 1

            if pixel.y == 0:
                self.shift_pixels(Direction.E)
                for i in range(0, self.height):
                    self.image.append(Pixel(i, 0, BinaryElement.White))
                self.width += 1

        self.image.sort(key=lambda k: [k.x, k.y])
        self.blackPixels = self.get_black_pixels()
        self.whitePixels = self.get_white_pixels()

    # Expand white pixel, to avoid multiples lines or column of white pixels
    def reduce_image(self):
        min_x, max_x, min_y, max_y = self.get_extreme_pixels()
        pixel_to_remove = []
        heighTemp = self.height
        widthTemp = self.width
        for pixel in self.whitePixels:
            if pixel not in pixel_to_remove:
                if pixel.x > max_x + 1:
                    for i in range(0, self.width):
                        pixel_to_remove.append(self.get_pixel(pixel.x, i))
                    heighTemp -= 1

                if pixel.x < min_x - 1:
                    for i in range(0, self.width):
                        pixel_to_remove.append(self.get_pixel(pixel.x, i))
                    heighTemp -= 1

            if pixel not in pixel_to_remove:
                if pixel.y > max_y + 1:
                    for i in range(0, self.height):
                        pixel_to_remove.append(self.get_pixel(i, pixel.y))
                    widthTemp -= 1

                if pixel.y < min_y - 1:
                    for i in range(0, self.height):
                        pixel_to_remove.append(self.get_pixel(i, pixel.y))
                    widthTemp -= 1

        pixel_to_remove = list(dict.fromkeys(pixel_to_remove))
        for pixel in pixel_to_remove:
            self.image.remove(pixel)

        self.shift_pixels(Direction.S, min_x - 1)
        self.shift_pixels(Direction.W, min_y - 1)

        self.height = heighTemp
        self.width = widthTemp

        self.image.sort(key=lambda k: [k.x, k.y])
        self.blackPixels = self.get_black_pixels()
        self.whitePixels = self.get_white_pixels()

    # To change connexity of an image
    def change_connexity(self, blackConnexity, whiteConnexity):
        if (blackConnexity in CONNEXITY_RESTRICTION)\
        and (whiteConnexity in CONNEXITY_RESTRICTION):
            self.blackConnexity = blackConnexity
            self.whiteConnexity = whiteConnexity
        else:
            print("Connexity must be in ", CONNEXITY_RESTRICTION, " !")

        # Update isolated pixels
        self.connected, \
        self.isolatedBlackPixels, \
        self.isolatedWhitePixels = self.is_image_connected()

    # Return boolean if p and q are adjacent depending on connexity
    def is_adjacent(self, p, q, connexity=4):
        tmp = False
        if connexity == 4:
            tmp = (pow(p.x - q.x, 2) + pow(p.y - q.y, 2) <= 1)
        elif connexity == 8:
            tmp = (pow(p.x - q.x, 2) + pow(p.y - q.y, 2) <= 2)
        else:
            print("Error in connexity, please choose in ", CONNEXITY_RESTRICTION)

        return tmp

    # Return a pixel with a direction
    def get_pixel_adjacent(self, pixel: Pixel, direction: Direction):
        p = pixel
        if direction == Direction.N:
            p = self.get_pixel(p.x + 1, p.y)
        elif direction == Direction.NE:
            p = self.get_pixel(p.x + 1, p.y + 1)
        elif direction == Direction.E:
            p = self.get_pixel(p.x, p.y + 1)
        elif direction == Direction.SE:
            p = self.get_pixel(p.x - 1, p.y + 1)
        elif direction == Direction.S:
            p = self.get_pixel(p.x - 1, p.y)
        elif direction == Direction.SW:
            p = self.get_pixel(p.x - 1, p.y - 1)
        elif direction == Direction.W:
            p = self.get_pixel(p.x, p.y - 1)
        elif direction == Direction.NW:
            p = self.get_pixel(p.x + 1, p.y - 1)
        else:
            print("Wrong choice of direction or pixel doesn't exist")

        return p

    # Return a pixel with multiple directions
    def get_pixel_directionnal(self, pixel: Pixel, array_direction):
        q = pixel
        for d in array_direction:
            q = self.get_pixel_adjacent(q, d)

        return q

    # Return if a pixel is a cut vertex
    def is_cut_vertex(self, pixel):
        color = BinaryElement.Black if pixel.color == BinaryElement.White else BinaryElement.White
        imgTemp = self.__copy__()
        p = imgTemp.get_pixel(pixel.x, pixel.y)
        return not imgTemp.change_color_pixel(p, color)

    ################################
    #####        Utils         #####
    ################################

    # Add all new pixels from an expand
    # Return array of new image, whitePixels, blackPixels
    # def update_new_pixels_array(self, img):
    #     image = self.image.copy()
    #     blackPixels = self.blackPixels.copy()
    #     whitePixels = self.whitePixels.copy()
    #
    #     for line in range(0, self.height):
    #         for column in range(0, self.width):
    #             pixel = Pixel(line,
    #                           column,
    #                           BinaryElement.Black if img[line][column] == 1 else BinaryElement.White)
    #             if pixel not in image:
    #                 image.append(pixel)
    #             elif pixel in image:
    #                 idx = image.index(pixel)
    #                 image[idx] = pixel
    #
    #             if pixel not in blackPixels and pixel.color == BinaryElement.Black:
    #                 blackPixels.append(pixel)
    #             elif pixel in blackPixels and pixel.color == BinaryElement.Black:
    #                 idxBlack = blackPixels.index(pixel)
    #                 blackPixels[idxBlack] = pixel
    #             elif pixel not in whitePixels and pixel.color == BinaryElement.White:
    #                 whitePixels.append(pixel)
    #             elif pixel not in whitePixels and pixel.color == BinaryElement.White:
    #                 idxWhite = whitePixels.index(pixel)
    #                 whitePixels[idxWhite] = pixel
    #
    #
    #     image.sort(key=lambda k: [k.x, k.y])
    #     blackPixels.sort(key=lambda k: [k.x, k.y])
    #     whitePixels.sort(key=lambda k: [k.x, k.y])
    #
    #     return image, blackPixels, whitePixels

    # For the expand, when you add a line of white pixels under or on the left of the figure,
    # We move all the pixel upward or on the right
    def shift_pixels(self, direction, number=1):
        if number >= 1:
            if direction == Direction.N:
                for pixel in self.image:
                    pixel.x += number
            elif direction == Direction.E:
                for pixel in self.image:
                    pixel.y += number
            elif direction == Direction.S:
                for pixel in self.image:
                    pixel.x -= number
            elif direction == Direction.W:
                for pixel in self.image:
                    pixel.y -= number

    # Convert image structure to Pixels array
    # Return arrays in an array
    def convert_img_to_pixels(self, image):
        imgPixels = []
        for i in range(0, len(image)):
            for j in range(0, len(image[0])):
                color = BinaryElement.Black if image[i][j] == 1 else BinaryElement.White
                imgPixels.append(Pixel(i, j, color))

        return imgPixels

    # Convert pixels array to image structure
    # Return arrays in an array
    def convert_pixels_to_img(self):
        img = []
        for i in range(0, self.height):
            line = []
            for j in range(0, self.width):
                if self.image[i * self.width + j].color == BinaryElement.Black:
                    line.append(1)
                else:
                    line.append(0)
            img.append(line)
        return img[::-1]

    # Return heigh and width of image
    def get_dimensions(self):
        max_x = float("-inf")       # set to smallest number
        max_y = float("-inf")       # set to smallest number
        for pixel in self.image:
            if pixel.y > max_y:
                max_y = pixel.y
            if pixel.x > max_x:
                max_x = pixel.x

        return max_x + 1, max_y + 1

    # Return a Pixel array with all white pixels
    def get_white_pixels(self):
        temp = []
        for pixel in self.image:
            if pixel.color == BinaryElement.White:
                temp.append(pixel)

        return temp

    # Update every attribute of the BinaryImage
    def update_img(self):
        self.height, self.width = self.get_dimensions()  # Getting dimensions of image
        self.whitePixels = self.get_white_pixels()                 # Get all the white pixels
        self.blackPixels = self.get_black_pixels()                 # Get all the black pixels
        self.size = len(self.blackPixels)                          # size = number of black pixels

        self.expand_image()  # If black pixels are adjacent to the limit

        # All the white pixels 4-adjacent to black_pixels
        self.borderWhitePixels = self.get_border_image(self.blackPixels, self.blackConnexity)

        # Check if the image is fully B4,W4-connected
        self.connected, \
        self.isolatedBlackPixels, \
        self.isolatedWhitePixels = self.is_image_connected()

    # Return a Pixel array with all black pixels
    def get_black_pixels(self):
        temp = []
        for pixel in self.image:
            if pixel.color == BinaryElement.Black:
                temp.append(pixel)

        return temp

    def update_black_white(self, arrayPixel=None):
        if arrayPixel is None:
            self.blackPixels = self.get_black_pixels()
            self.whitePixels = self.get_white_pixels()
        else:
            for p in arrayPixel:
                if p.color == BinaryElement.Black and p not in self.blackPixels:
                    self.blackPixels.append(p)
                    self.whitePixels.remove(p)
                elif p.color == BinaryElement.White and p not in self.whitePixels:
                    self.blackPixels.remove(p)
                    self.whitePixels.append(p)
    # Method to print all the informations of the pixels in text
    def print_array_pixels(self):
        tmp = ""
        for pixel in self.image:
            tmp += str(pixel) + " "
            # print(pixel)

        return tmp

    # Return min_x, max_x, min_y, max_y of black pixels
    def get_extreme_pixels(self):
        min_x = self.blackPixels[0].x
        max_x = self.blackPixels[0].x
        min_y = self.blackPixels[0].y
        max_y = self.blackPixels[0].y
        for pixel in self.blackPixels:
            min_x = pixel.x if pixel.x < min_x else min_x
            max_x = pixel.x if pixel.x > max_x else max_x
            min_y = pixel.y if pixel.y < min_y else min_y
            max_y = pixel.y if pixel.y > max_y else max_y

        return min_x, max_x, min_y, max_y

    # def respect_white_connexity(self, pixel):
    #     respected = False
    #     # récupérer tous les pixels blancs
    #     whiteAdjacent = self.get_neighbours(pixel, self.whiteConnexity, Enum.BinaryElement.White)
    #     visited = []
    #     exploreWhite = []
    #
    #     for p in whiteAdjacent:
    #         visited.append(p)
    #         neighbours = self.get_neighbours(p, self.whiteConnexity, Enum.BinaryElement.White)
    #         print(len(neighbours))
    #         for n in neighbours:
    #             if n not in visited:
    #                 exploreWhite.append(n)
    #
    #         temp = exploreWhite
    #         for q in temp:
    #             visited.append(q)
    #             if len(self.get_black_pixels()) > 18:
    #                 self.show_image(dict_array_pixels={"red":[p]})
    #             if q.x == 0 or q.x == self.height - 1 or q.y == 0 or q.y == self.width - 1:
    #                 return True
    #             else:
    #                 exploreWhite.remove(q)

            # exploreWhite = [result for result in exploreWhite if result not in visited]



            # Vérifier que chaque pixel blanc est encore connecté à un autre
            # isConnect = self.get_neighbours(p, self.whiteConnexity, Enum.BinaryElement.White)
            # if not isConnect:
            #     respected = False
            #     break

        # return respected
