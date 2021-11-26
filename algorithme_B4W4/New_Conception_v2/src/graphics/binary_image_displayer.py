from __future__ import annotations
from algorithme_B4W4.New_Conception_v2.src.models.binary_image import BinaryImage
from algorithme_B4W4.New_Conception_v2.src.models.pixel import Pixel
from matplotlib.animation import FuncAnimation
from tqdm import tqdm

from matplotlib import pyplot
from matplotlib import patches


class BinaryImageDisplayer:
    """Defines a class whose role is to display a binary image"""

    LINE_WIDTH = 1
    LINE_COLOR = "dimgray"

    PIXEL_SIZE = 1
    BLACK_PIXEL_COLOR = "#000000"
    ISOLATED_WHITE_PIXEL_COLOR = "orangered"
    ISOLATED_BLACK_PIXEL_COLOR = "forestgreen"
    BORDER_PIXEL_COLOR = "cyan"

    def __init__(self, show_border=False, show_isolated=True, show_legend=True):
        self.show_border = show_border
        self.show_isolated = show_isolated
        self.show_legend = show_legend

    def show(self, image: BinaryImage, subtitle: None | str = None, custom_pixels_lists=None) -> None:
        """Displays the given binary image on screen"""

        pyplot.figure()

        title = image.get_title()

        if subtitle is not None:
            title = f'{title} - {subtitle}'

        pyplot.title(title)

        # Creates the lines of the grid
        for i in range(image.height + 1):
            BinaryImageDisplayer.__draw_line(0, image.width, i, i)

        # Creates the columns of the grid
        for i in range(image.width + 1):
            BinaryImageDisplayer.__draw_line(i, i, 0, image.height)

        # Fills the grid with the black pixels
        for pixel in image.black_pixels:
            BinaryImageDisplayer.__draw_pixel(x=pixel.x, y=pixel.y, color=BinaryImageDisplayer.BLACK_PIXEL_COLOR)

        # Displays the white and black isolated pixels (optional)
        if self.show_isolated:
            for pixel in image.isolatedWhitePixels:
                BinaryImageDisplayer.__draw_pixel(x=pixel.x, y=pixel.y,
                                                  color=BinaryImageDisplayer.ISOLATED_WHITE_PIXEL_COLOR)

            for pixel in image.isolatedBlackPixels:
                BinaryImageDisplayer.__draw_pixel(x=pixel.x, y=pixel.y,
                                                  color=BinaryImageDisplayer.ISOLATED_BLACK_PIXEL_COLOR)

        # Displays border (optional)
        if self.show_border:
            for pixel in image.borderWhitePixels:
                BinaryImageDisplayer.__draw_pixel(x=pixel.x, y=pixel.y, color=BinaryImageDisplayer.BORDER_PIXEL_COLOR)

        # Displays optional pixels that we want to highlight
        if custom_pixels_lists is not None:
            for (color, arrayPixel, _) in custom_pixels_lists:
                for pixel in arrayPixel:
                    pyplot.gca().add_patch(pyplot.Rectangle((pixel.y, pixel.x), 1, 1, fc=str(color)))

        # Displays legend (optional)
        if self.show_legend:
            self._show_legend(custom_pixels_lists)

        pyplot.axis('scaled')
        pyplot.show()

    def _show_legend(self, custom_pixels_lists=None) -> None:
        """Displays legends next to the plot (reduces its size to fit hte screen)"""
        legends = []

        black_pixels_label = 'Pixels'
        legends.append(patches.Patch(color=BinaryImageDisplayer.BLACK_PIXEL_COLOR, label=black_pixels_label))

        if self.show_border:
            border_pixels_label = 'Pixel border'
            legends.append(patches.Patch(color=BinaryImageDisplayer.BORDER_PIXEL_COLOR, label=border_pixels_label))

        if self.show_isolated:
            isolated_white_pixels_label = 'Isolated white pixels'
            isolated_black_pixels_label = 'Isolated black pixels'
            legends.append(patches.Patch(color=BinaryImageDisplayer.ISOLATED_WHITE_PIXEL_COLOR,
                                         label=isolated_white_pixels_label))
            legends.append(patches.Patch(color=BinaryImageDisplayer.ISOLATED_BLACK_PIXEL_COLOR,
                                         label=isolated_black_pixels_label))

        if custom_pixels_lists is not None:
            for (color, _, label) in custom_pixels_lists:
                legends.append(patches.Patch(color=color, label=label))

        pyplot.legend(handles=legends, bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.)  # show legends
        pyplot.tight_layout(rect=[0, 0, 1, 1])  # reduce plot size so that the legend can fit

    @staticmethod
    def create_gif(image: BinaryImage, array_interchage: [(Pixel, Pixel)],
                   name="GifInterchange.gif", speed=2000) -> None:

        fig, ax = pyplot.subplots()

        M = image.convert_pixels_to_img()
        matrice = ax.matshow(M, cmap='Greys')
        # width = image.width
        # height = image.height

        p_bar = tqdm(total=len(array_interchage))  # progress bar in print
        p_bar.set_description("Creating gif nb_interchange n = " + str(len(array_interchage)))  # Description for the loading bar



        def init():

            # Creates the lines of the grid
            for i in range(image.height + 1):
                BinaryImageDisplayer.__draw_line(-0.5, image.width-0.5, i-0.5, i-0.5)

            # Creates the columns of the grid
            for i in range(image.width + 1):
                BinaryImageDisplayer.__draw_line(i-0.5, i-0.5, -0.5, image.height-0.5)

        def update(i):
            p, q = array_interchage[i-1]
            swap = image.swap_pixels(p, q)

            if swap:
                p_bar.update(1)  # Adding the first pixel

                M = image.convert_pixels_to_img()
                matrice = ax.matshow(M, cmap='Greys')

                matrice.set_array(image.convert_pixels_to_img())

        ani = FuncAnimation(fig, update, frames=len(array_interchage) + 1, interval=speed)
        ani.save(name)

        #
        #
        # def update():
        #     for p, q in array_interchage:
        #         image.swap_pixels(p, q)
        #         BinaryImageDisplayer.__draw_pixel(x=p.x, y=p.y, color="#FFFFFF")
        #         BinaryImageDisplayer.__draw_pixel(x=q.x, y=q.y, color=BinaryImageDisplayer.BLACK_PIXEL_COLOR)

        return None


    @staticmethod
    def __draw_line(x_start, y_start, x_end, y_end) -> None:
        """Draw a line from with start and end 2D-coordinates"""
        pyplot.gca().add_line(pyplot.Line2D((x_start, y_start), (x_end, y_end), lw=BinaryImageDisplayer.LINE_WIDTH,
                                            color=BinaryImageDisplayer.LINE_COLOR))

    @staticmethod
    def __draw_pixel(x, y, color) -> None:
        """Draw a pixel (rectangle of "pixel_size" size) at the given coordinates with the given color"""
        pyplot.gca().add_patch(
            pyplot.Rectangle((y, x), BinaryImageDisplayer.PIXEL_SIZE, BinaryImageDisplayer.PIXEL_SIZE, fc=color))
