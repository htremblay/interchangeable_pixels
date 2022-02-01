from tqdm import tqdm
import random
import copy
import networkx as nx

from algorithme_B4W4.New_Conception_v2.src.utils import Direction
from algorithme_B4W4.New_Conception_v2.src.models.pixel import Pixel, PixelColor

CONNEXITY_RESTRICTION = [4, 8]
INTERCHANGE_CONNEXITY = 8


# Class that'll handle all the image with its pixels.
class BinaryImage:

    # Constructor with a pre-created image or a int to generate a random image
    def __init__(self, black_connexity=4, white_connexity=4):
        self.seed = 0
        self.pixels = []

        self.black_connexity = black_connexity
        self.white_connexity = white_connexity
        self.height, self.width = (0, 0)  # Getting dimensions of image
        self.white_pixels = []  # Get all the white pixels
        self.black_pixels = []  # Get all the black pixels
        self.size = 0  # Get the number of black pixels on the image

        # All the white pixels 4-adjacent to black_pixels
        self.borderWhitePixels = []

        # Check if the image is fully B4,W4-connected
        self.connected, self.isolatedBlackPixels, self.isolatedWhitePixels = (False, [], [])

        # creating graph from pixel
        self.black_graph, self.white_graph = (0, 0)

    def __copy__(self):
        return self.create_img_from_array(self.convert_pixels_to_img(), self.black_connexity, self.white_connexity)

    def __str__(self):
        return ("Array : {" + self.print_array_pixels() + " }"
                + "\nheight : " + str(self.height) + " width : " + str(self.width)
                + "\nnb black pixels : " + str(len(self.black_pixels))
                + " & nb white pixels : " + str(len(self.white_pixels))
                + "\nimage connected : " + str(self.connected))

    ##############################
    # region instanciation

    # From a size of image b,w-connexity and a seed generate a random image
    @staticmethod
    def create_random_img(n: int, black_connexity=4, white_connexity=4, seed=1, show_p_bar=True):
        img = BinaryImage.create_img_from_array([[1]], black_connexity, white_connexity)
        i = 1  # i = 1 because already 1 pixel on the image
        p_bar = None

        if show_p_bar:
            p_bar = tqdm(total=n)  # progress bar in print
            p_bar.set_description("Creating B" + str(img.black_connexity) + "W" +
                                  str(img.white_connexity) + "connected; n="+str(n)+
                                  "; seed " + str(seed))  # Description for the loading bar
            p_bar.update(1)  # Adding the first pixel

        random.seed(seed)

        while i < n:
            border_pixel = random.choice(img.borderWhitePixels)  # Choosing randomly a while pixel in the border

            # Changing the white pixel to black
            has_change = img.change_color_pixel(border_pixel, PixelColor.BLACK)

            if has_change:  # If change has been done
                # Temporary list takes the new black pixel
                new_border_pixels = img.get_neighbours(border_pixel, black_connexity, PixelColor.WHITE)
                for pixel in new_border_pixels:
                    if pixel not in img.borderWhitePixels:
                        img.borderWhitePixels.append(pixel)
                i += 1  # +1 black pixel on the image

                img.expand_image()

                if show_p_bar:
                    p_bar.update(1)  # Value to update the loading bar (No impact on the algorithm)
            else:
                img.borderWhitePixels.remove(border_pixel)  # Removing the black pixel of the list,
                                                            # so we don't try to pick it again

        if show_p_bar:
            p_bar.close()                                       # Closing the progress when finished


        img.borderWhitePixels = img.get_border_image(img.black_connexity)
        img.seed = seed
        # creating graph from pixel
        # img.black_graph, img.white_graph = img.create_graphs(img.black_connexity, img.white_connexity)

        return img

    # From a 2D binary array (only 0-1 values) create a Binary Image
    @staticmethod
    def create_img_from_array(int_array: [[int]], black_connexity=4, white_connexity=4):
        img = BinaryImage(black_connexity, white_connexity)
        img.pixels = img.convert_img_to_pixels(int_array[::-1])
        img.update_img()

        return img

    # From a size create a vertical image
    @staticmethod
    def create_img_vertical(size_image: int, black_connexity=4, white_connexity=4):
        img = BinaryImage(black_connexity, white_connexity)
        for i in range(size_image):
            img.pixels.append(Pixel(i, 0, PixelColor.BLACK))

        img.update_img()

        return img

    # From a size create a spiral image
    @staticmethod
    def create_img_spiral(size_image: int, black_connexity=4, white_connexity=4):
        img = BinaryImage.create_img_from_array([[1]], black_connexity, white_connexity)

        current_pixel = img.black_pixels[0]

        nb_pixels_to_add = 1
        array_direction = [Direction.E, Direction.N, Direction.W, Direction.S]
        horaire = True
        if horaire:
            array_direction.reverse()


        choice_of_direction = 0
        direction = array_direction[choice_of_direction]

        nb_pixels = 1
        while nb_pixels < size_image:
            for d in range(nb_pixels_to_add):
                if nb_pixels >= size_image:
                    break
                current_pixel = img.get_pixel_directional(current_pixel, [direction])
                has_change = img.change_color_pixel(current_pixel, PixelColor.BLACK)

                if has_change:
                    nb_pixels += 1
                    img.expand_image()

            choice_of_direction += 1
            direction = array_direction[choice_of_direction % 4]
            nb_pixels_to_add += 1

        img.update_img()

        return img






    # endregion Instaciation
    ##############################

    ##############################
    # region get_informations

    # Return title of an image
    def get_title(self) -> str:
        """Returns the title of the image based on its specs"""
        return f'{self.seed}_{self.get_size()}_B{self.black_connexity}_W{self.white_connexity}'

    # Return size of an image
    def get_size(self) -> int:
        """Returns the size of the binary image (count of its black pixels)"""
        return len(self.black_pixels)

    # Get the border of all the black image. You can choose the connexity
    # Return an array of white pixels.
    def get_border_image(self, black_connexity=4):
        white_border = []
        for blackPixel in self.black_pixels.copy():
            white_adjacent = self.get_neighbours(blackPixel, black_connexity, PixelColor.WHITE)
            for white_pixel in white_adjacent:
                if white_pixel not in white_border:
                    white_border.append(white_pixel)

        return white_border

    # Return an array of Pixels
    # You can chose connexity and the color of pixel you want
    def get_neighbours(self, pixel: Pixel, connexity=4, color=PixelColor.BOTH) -> [Pixel]:
        neighbours = []

        if (connexity not in CONNEXITY_RESTRICTION) or color not in PixelColor:
            print("Error in color [Enum.PixelColor] choice or connexity in ", CONNEXITY_RESTRICTION)
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

        wanted_neighbours = neighbours
        if color != PixelColor.BOTH:
            wanted_neighbours = []
            for n in neighbours:
                if n.color == color:
                    wanted_neighbours.append(n)

        return wanted_neighbours

    # Give the pixel from coordinates
    def get_pixel(self, x: int, y: int) -> Pixel or None:
        if x * self.width + y < len(self.pixels):
            return self.pixels[x * self.width + y]
        else:
            return Pixel(x, y, PixelColor.WHITE)

    # Return a pixel with a direction
    def get_pixel_adjacent(self, pixel: Pixel, direction: Direction) -> Pixel or None:
        p = pixel
        temp = None
        if p is not None:
            if direction == Direction.N:
                temp = self.get_pixel(p.x + 1, p.y)
            elif direction == Direction.NE:
                temp = self.get_pixel(p.x + 1, p.y + 1)
            elif direction == Direction.E:
                temp = self.get_pixel(p.x, p.y + 1)
            elif direction == Direction.SE:
                temp = self.get_pixel(p.x - 1, p.y + 1)
            elif direction == Direction.S:
                temp = self.get_pixel(p.x - 1, p.y)
            elif direction == Direction.SW:
                temp = self.get_pixel(p.x - 1, p.y - 1)
            elif direction == Direction.W:
                temp = self.get_pixel(p.x, p.y - 1)
            elif direction == Direction.NW:
                temp = self.get_pixel(p.x + 1, p.y - 1)
            else:
                print("Wrong choice of direction or pixel doesn't exist")

        return temp

    # Return a pixel with multiple directions
    def get_pixel_directional(self, pixel: Pixel, array_direction: [Direction]) -> Pixel or None:
        p = copy.deepcopy(pixel)
        for d in array_direction:
            p = self.get_pixel_adjacent(p, d)

        return p

    # endregion get_informations
    ##############################

    ##############################
    # region main_methods

    def create_graphs(self, black_connexity=4, white_connexity=4) -> (nx.Graph(), nx.Graph()):
        white_graph = self.create_nodes(PixelColor.WHITE)
        black_graph = self.create_nodes(PixelColor.BLACK)

        for p in self.black_pixels:
            neighbours = self.get_neighbours(p, connexity=black_connexity, color=PixelColor.BLACK)
            for n in neighbours:
                black_graph.add_edge((p.x, p.y), (n.x, n.y))

        for p in self.white_pixels:
            neighbours = self.get_neighbours(p, connexity=white_connexity, color=PixelColor.BLACK)
            for n in neighbours:
                white_graph.add_edge((p.x, p.y), (n.x, n.y))

        return black_graph, white_graph

    def create_nodes(self, color:PixelColor) -> nx.Graph():
        nodes = nx.Graph()
        if color == PixelColor.BLACK:
            for p in self.black_pixels:
                nodes.add_node((p.x, p.y))
        elif color == PixelColor.WHITE:
            for p in self.white_pixels:
                nodes.add_node((p.x, p.y))
        return nodes

    # Return a boolean if the swap of 2 pixels is possible
    def swap_pixels(self, p: (int, int), q: (int, int), swap_active=True) -> bool:
        imgTemp = copy.copy(self)
        swap_pixel = False

        # We always want pTemp as the black pixel
        if imgTemp.get_pixel(p[0], p[1]).color == PixelColor.BLACK:
            pTemp = imgTemp.get_pixel(p[0], p[1])
            qTemp = imgTemp.get_pixel(q[0], q[1])
        else:
            pTemp = imgTemp.get_pixel(q[0], q[1])
            qTemp = imgTemp.get_pixel(p[0], p[1])

        if Pixel.is_adjacent(pTemp, qTemp, INTERCHANGE_CONNEXITY) and pTemp.color != qTemp.color:
            pTemp.color, qTemp.color = qTemp.color, pTemp.color

            imgTemp.update_black_white([pTemp, qTemp])

            connected, b, w = imgTemp.is_image_connected(qTemp, pTemp)

            if connected:
                if swap_active:
                    p = self.get_pixel(pTemp.x, pTemp.y)
                    q = self.get_pixel(qTemp.x, qTemp.y)
                    self.pixels[self.pixels.index(p)] = pTemp
                    self.pixels[self.pixels.index(q)] = qTemp
                    self.update_black_white([p, q])
                    self.expand_image()
                    self.reduce_image()
                swap_pixel = True

        else:
            print("Trying to swap same pixel, same color pixels or non 8-adjacent pixels <", p, ", ", q, ">")

        return swap_pixel


    def is_vertical(self):
        y = self.black_pixels[0].y
        for p in self.black_pixels:
            if p.y != y:
                return False

        return True

    # Use an array of tuple of Pixel to do multiple swap at once
    def multiple_swap_pixels(self, array_swap: [((int, int), (int, int))]) -> int or None:
        interchange = 0
        pix_array_temp = copy.copy(self.pixels)
        for p, q in array_swap:
            swap = self.swap_pixels(p, q)
            if not swap:
                self.pixels = pix_array_temp
                self.update_img()
                interchange = None
                break
            else:
                interchange += 1

        return interchange

    # Change the color of a pixel with its coordinates
    # Return a boolean if the change was done
    def change_color_pixel(self, pixel: Pixel, color: PixelColor) -> bool:
        idx = self.pixels.index(pixel)
        current_color_pixel = pixel.color  # current color of pixel
        change_done = False  # True when the pixel changed its color

        if current_color_pixel != color:  # Current color needs to be different than the new one
            self.pixels[idx].color = color  # Change the color of the pixel with the new one
            self.update_black_white([pixel])
            # connected = self.respect_white_connexity(pixel)
            connected, b, w = self.is_image_connected()
            if connected:
                change_done = True
            else:
                self.pixels[idx].color = current_color_pixel  # Change the color of the pixel with the old one
                self.update_black_white([pixel])
                change_done = False

        return change_done

    # Check if the image respect the Black & White connexity restrictions
    # Return True or False, array of not visited black pixels, array of not visited white pixels
    def is_image_connected(self, blackPixelToStrart=None, whitePixelToStart=None) -> (bool, [int], [int]):
        notVisitedBlack = self.black_pixels.copy()
        blackVisited = []
        blackWaitingList = []
        if notVisitedBlack:
            if blackPixelToStrart is None:
                blackWaitingList = [notVisitedBlack.pop()]
            else:
                blackWaitingList = [blackPixelToStrart]

        notVisitedWhite = self.white_pixels.copy()
        whiteVisited = []
        whiteWaitingList = []
        if notVisitedWhite:
            if whitePixelToStart is None:
                whiteWaitingList = [notVisitedWhite.pop()]
            else:
                whiteWaitingList = [whitePixelToStart]

        while len(blackWaitingList) > 0:
            pixel = blackWaitingList.pop()
            for neighbour in self.get_neighbours(pixel, self.black_connexity, PixelColor.BLACK):
                if neighbour in notVisitedBlack:
                    blackWaitingList.append(neighbour)
                    notVisitedBlack.remove(neighbour)

            blackVisited.append(pixel)

        while len(whiteWaitingList) > 0:
            pixel = whiteWaitingList.pop()
            for neighbour in self.get_neighbours(pixel, self.white_connexity, PixelColor.WHITE):
                if neighbour in notVisitedWhite:
                    whiteWaitingList.append(neighbour)
                    notVisitedWhite.remove(neighbour)

            whiteVisited.append(pixel)

        return len(notVisitedBlack) == 0 and len(notVisitedWhite) == 0, notVisitedBlack, notVisitedWhite

    # Expand white pixel, to avoid black pixels on the border
    def expand_image(self) -> None:
        for pixel in self.black_pixels:
            if pixel.x == self.height - 1:
                for i in range(0, self.width):
                    self.pixels.append(Pixel(self.height, i, PixelColor.WHITE))
                self.height += 1

            if pixel.x == 0:
                self.shift_pixels(Direction.N)
                for i in range(0, self.width):
                    self.pixels.append(Pixel(0, i, PixelColor.WHITE))

                self.height += 1

            if pixel.y == self.width - 1:
                for i in range(0, self.height):
                    self.pixels.append(Pixel(i, self.width, PixelColor.WHITE))
                self.width += 1

            if pixel.y == 0:
                self.shift_pixels(Direction.E)
                for i in range(0, self.height):
                    self.pixels.append(Pixel(i, 0, PixelColor.WHITE))
                self.width += 1

        self.pixels.sort(key=lambda k: [k.x, k.y])
        self.black_pixels = self.get_black_pixels()
        self.white_pixels = self.get_white_pixels()

    # reduces white pixel, to avoid multiples lines or column of white pixels
    def reduce_image(self) -> None:
        min_x, max_x, min_y, max_y = self.get_extreme_pixels()
        pixel_to_remove = []
        height_temp = self.height
        width_temp = self.width
        for pixel in self.white_pixels:
            if pixel not in pixel_to_remove:
                if pixel.x > max_x + 1:
                    for i in range(0, self.width):
                        pixel_to_remove.append(self.get_pixel(pixel.x, i))
                    height_temp -= 1

                # if pixel.x < min_x - 1:
                #     for i in range(0, self.width):
                #         pixel_to_remove.append(self.get_pixel(pixel.x, i))
                #     height_temp -= 1

            if pixel not in pixel_to_remove:
                if pixel.y > max_y + 1:
                    for i in range(0, self.height):
                        pixel_to_remove.append(self.get_pixel(i, pixel.y))
                    width_temp -= 1

                if pixel.y < min_y - 1:
                    for i in range(0, self.height):
                        pixel_to_remove.append(self.get_pixel(i, pixel.y))
                    width_temp -= 1

        pixel_to_remove = list(dict.fromkeys(pixel_to_remove))
        for pixel in pixel_to_remove:
            self.pixels.remove(pixel)

        # self.shift_pixels(Direction.S, min_x - 1)
        self.shift_pixels(Direction.W, min_y - 1)

        self.height = height_temp
        self.width = width_temp

        self.pixels.sort(key=lambda k: [k.x, k.y])
        self.black_pixels = self.get_black_pixels()
        self.white_pixels = self.get_white_pixels()

    # To change connexity of an image
    def change_connexity(self, black_connexity: int, white_connexity: int) -> None:
        if (black_connexity in CONNEXITY_RESTRICTION) \
                and (white_connexity in CONNEXITY_RESTRICTION):
            self.black_connexity = black_connexity
            self.white_connexity = white_connexity
        else:
            print("Connexity must be in ", CONNEXITY_RESTRICTION, " !")

        # Update isolated pixels
        self.connected, self.isolatedBlackPixels, self.isolatedWhitePixels = self.is_image_connected()

    # Return if a pixel is a cut vertex
    def is_cut_vertex(self, pixel: Pixel) -> bool:
        color = PixelColor.BLACK if pixel.color == PixelColor.WHITE else PixelColor.WHITE
        img_temp = self.__copy__()
        p = img_temp.get_pixel(pixel.x, pixel.y)
        return not img_temp.change_color_pixel(p, color)

    def black_pixels_width(self):
        min = float("inf")
        max = float("-inf")
        for p in self.black_pixels:
            if p.y < min:
                min = p.y
            if p.y > max:
                max = p.y

        return max - min + 1

    # endregion main_methods
    ##############################

    ##############################
    # region Utils



    # For the expand, when you add a line of white pixels under or on the left of the figure,
    # We move all the pixel upward or on the right
    def shift_pixels(self, direction, number=1) -> None:
        if number >= 1:
            if direction == Direction.N:
                for pixel in self.pixels:
                    pixel.x += number
            elif direction == Direction.E:
                for pixel in self.pixels:
                    pixel.y += number
            elif direction == Direction.S:
                for pixel in self.pixels:
                    pixel.x -= number
            elif direction == Direction.W:
                for pixel in self.pixels:
                    pixel.y -= number

    # Convert image structure to Pixels array
    # Return arrays in an array
    @staticmethod
    def convert_img_to_pixels(image) -> [Pixel]:
        img_pixels = []
        for i in range(0, len(image)):
            for j in range(0, len(image[0])):
                color = PixelColor.BLACK if image[i][j] == 1 else PixelColor.WHITE
                img_pixels.append(Pixel(i, j, color))

        return img_pixels

    # Convert pixels array to image structure
    # Return arrays in an array
    def convert_pixels_to_img(self) -> [[int]]:
        img = []
        for i in range(0, self.height):
            line = []
            for j in range(0, self.width):
                if self.pixels[i * self.width + j].color == PixelColor.BLACK:
                    line.append(1)
                else:
                    line.append(0)
            img.append(line)
        return img[::-1]

    # Return height and width of image
    def get_dimensions(self) -> (int, int):
        max_x = float("-inf")  # set to smallest number
        max_y = float("-inf")  # set to smallest number
        for pixel in self.pixels:
            if pixel.y > max_y:
                max_y = pixel.y
            if pixel.x > max_x:
                max_x = pixel.x

        return max_x + 1, max_y + 1

    # Return a Pixel array with all white pixels
    def get_white_pixels(self) -> [Pixel]:
        temp = []
        for pixel in self.pixels:
            if pixel.color == PixelColor.WHITE:
                temp.append(pixel)

        return temp

    # Update every attribute of the BinaryImage
    def update_img(self) -> None:
        self.height, self.width = self.get_dimensions()   # Getting dimensions of image



        self.white_pixels = self.get_white_pixels()       # Get all the white pixels
        self.black_pixels = self.get_black_pixels()       # Get all the black pixels
        self.size = len(self.black_pixels)                # size = number of black pixels

        # self.height = self.size + 2
        # self.width = self.black_pixels_width() + 2

        # self.expand_img()

        self.expand_image()                                # If black pixels are adjacent to the limit
        self.reduce_image()                              # Collapse white pixels collumn or lines

        # All the white pixels 4-adjacent to black_pixels
        self.borderWhitePixels = self.get_border_image(self.black_connexity)

        # Check if the image is fully B4,W4-connected
        self.connected, self.isolatedBlackPixels, self.isolatedWhitePixels = self.is_image_connected()

        # creating graph from pixel
        # self.black_graph, self.white_graph = self.create_graphs(self.black_connexity, self.white_connexity)

    # def expand_img(self):
    #     return None

    # Return a Pixel array with all black pixels
    def get_black_pixels(self) -> [Pixel]:
        temp = []
        for pixel in self.pixels:
            if pixel.color == PixelColor.BLACK:
                temp.append(pixel)

        return temp

    def update_black_white(self, array_pixel=None) -> None:
        if array_pixel is None:
            self.black_pixels = self.get_black_pixels()
            self.white_pixels = self.get_white_pixels()
        else:
            for p in array_pixel:
                if p.color == PixelColor.BLACK and p not in self.black_pixels:
                    self.black_pixels.append(p)
                    self.white_pixels.remove(p)
                elif p.color == PixelColor.WHITE and p not in self.white_pixels:
                    self.black_pixels.remove(p)
                    self.white_pixels.append(p)

    # Method to print all the infos of the pixels in text
    def print_array_pixels(self) -> str:
        tmp = ""
        for pixel in self.pixels:
            tmp += str(pixel) + " "
            # print(pixel)

        return tmp

    # Return min_x, max_x, min_y, max_y of black pixels
    def get_extreme_pixels(self) -> (int, int, int, int):
        min_x = self.black_pixels[0].x
        max_x = self.black_pixels[0].x
        min_y = self.black_pixels[0].y
        max_y = self.black_pixels[0].y
        for pixel in self.black_pixels:
            min_x = pixel.x if pixel.x < min_x else min_x
            max_x = pixel.x if pixel.x > max_x else max_x
            min_y = pixel.y if pixel.y < min_y else min_y
            max_y = pixel.y if pixel.y > max_y else max_y

        return min_x, max_x, min_y, max_y

    # Return the density of an image
    def compute_density(self) -> float:
        nbEdges = 0
        for pixel in self.black_pixels:
            # note : nbEdges is in reallity 2 times the real number of edges
            nbEdges += len(self.get_neighbours(pixel, self.black_connexity, PixelColor.BLACK))

        density = nbEdges / (self.size * (self.size - 1))
        return density

    # endregion Utils
    ##############################

    # region test
    # Add all new pixels from an expand
    # Return array of new image, whitePixels, blackPixels
    # def update_new_pixels_array(self, img):
    #     image = self.pixels.copy()
    #     blackPixels = self.blackPixels.copy()
    #     whitePixels = self.whitePixels.copy()
    #
    #     for line in range(0, self.height):
    #         for column in range(0, self.width):
    #             pixel = Pixel(line,
    #                           column,
    #                           PixelColor.BLACK if img[line][column] == 1 else PixelColor.WHITE)
    #             if pixel not in image:
    #                 image.append(pixel)
    #             elif pixel in image:
    #                 idx = image.index(pixel)
    #                 image[idx] = pixel
    #
    #             if pixel not in blackPixels and pixel.color == PixelColor.BLACK:
    #                 blackPixels.append(pixel)
    #             elif pixel in blackPixels and pixel.color == PixelColor.BLACK:
    #                 idxBlack = blackPixels.index(pixel)
    #                 blackPixels[idxBlack] = pixel
    #             elif pixel not in whitePixels and pixel.color == PixelColor.WHITE:
    #                 whitePixels.append(pixel)
    #             elif pixel not in whitePixels and pixel.color == PixelColor.WHITE:
    #                 idxWhite = whitePixels.index(pixel)
    #                 whitePixels[idxWhite] = pixel
    #
    #
    #     image.sort(key=lambda k: [k.x, k.y])
    #     blackPixels.sort(key=lambda k: [k.x, k.y])
    #     whitePixels.sort(key=lambda k: [k.x, k.y])
    #
    #     return image, blackPixels, whitePixels

    # def respect_white_connexity(self, pixel):
    #     respected = False
    #     # récupérer tous les pixels blancs
    #     whiteAdjacent = self.get_neighbours(pixel, self.whiteConnexity, Enum.PixelColor.WHITE)
    #     visited = []
    #     exploreWhite = []
    #
    #     for p in whiteAdjacent:
    #         visited.append(p)
    #         neighbours = self.get_neighbours(p, self.whiteConnexity, Enum.PixelColor.WHITE)
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
    # isConnect = self.get_neighbours(p, self.whiteConnexity, Enum.PixelColor.WHITE)
    # if not isConnect:
    #     respected = False
    #     break

    # return respected

    # def change_color_pixel_temp(self, pixel, color):
    #     copy_pixel = copy.copy(pixel)
    #     current_color_pixel = copy_pixel.color  # current color of pixel
    #     change_done = False                     # True when the pixel changed its color
    #
    #     if current_color_pixel != color:  # Current color needs to be different than the new one
    #         pixel = color  # Change the color of the pixel with the new one
    #         self.update_black_white([pixel])
    #
    #         connected, b, w = self.is_image_connected()
    #         if connected:
    #             change_done = True
    #         else:
    #             self.pixels[idx].color = current_color_pixel  # Change the color of the pixel with the old one
    #             self.update_black_white([pixel])
    #             change_done = False
    #
    #     return change_done

    # endregion test

