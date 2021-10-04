import copy

from algorithme_B4W4.New_conception.Enumeration import Direction as d
from algorithme_B4W4.New_conception.Enumeration import BinaryElement
from algorithme_B4W4.New_conception.Pixel import Pixel
from algorithme_B4W4.New_conception.BinaryImage import BinaryImage


BLACK_CONNEXITY = 4
WHITE_CONNEXITY = 4
INTERCHANGE_CONNEXITY = 8

# Class that will resolve B4W4 binary images
class AlgoB4W4:

    # Constructor with a BinaryImage
    def __init__(self, binaryImage: BinaryImage):
        self.binaryImage = binaryImage
        self.interchange = 0


        self.width = binaryImage.width - 2
        self.frontier, self.adj_black_pixels_frontier = self.compute_frontier()
        self.anchor = self.compute_anchor()
        self.topPixel = self.compute_top_pixel()
        self.allElbow = self.compute_all_elbows()
        self.leadElbow = self.compute_lead_elbow()
        if self.anchor is None:
            self.height = None
        else:
            self.height = self.leadElbow.x - self.anchor.x


    def k_diagonal_interchange(self):
        imgTemp = copy.deepcopy(self.binaryImage)
        array_k_diag = []
        for p in self.allElbow:
            loop = True
            cut_elbow = imgTemp.is_cut_vertex(p)
            pi = p
            i = 0
            while loop:
                nnww = imgTemp.get_pixel_directionnal(pi, [d.N, d.N, d.W, d.W])
                if pi.color == nnww.color:
                    nw = imgTemp.get_pixel_directionnal(pi, [d.N, d.W])
                    se = imgTemp.get_pixel_directionnal(pi, [d.S, d.E])
                    if cut_elbow and self.swap_pixels(pi, nw, swap_active=False):
                        i += 1
                        pi = nw
                    elif not cut_elbow and self.swap_pixels(pi, se, swap_active=False):
                        i += 1
                        pi = se
                    else:
                        if i > 0:
                            array_k_diag.append(pi)
                        loop = False

        return array_k_diag

    # Return list of black pixels in the frontier
    def compute_frontier(self):
        max_y = self.binaryImage.blackPixels[0].y
        frontier = []
        adj_frontier = []

        for p in self.binaryImage.blackPixels:
            if max_y == p.y:
                frontier.append(p)
            elif max_y < p.y:
                max_y = p.y
                if p.y == max_y - 1:
                    adj_frontier = frontier
                frontier = [p]
            elif p.y == max_y - 1:
                adj_frontier.append(p)

        return frontier, adj_frontier

    # Return the pixel that is the anchor
    def compute_anchor(self):
        anchor = None
        if self.adj_black_pixels_frontier:
            anchor = self.adj_black_pixels_frontier[0]
            min_x = anchor.x

            for p in self.adj_black_pixels_frontier:
                if min_x > p.x:
                    min_x = p.x
                    anchor = p

        return anchor

    # Return the top pixel
    def compute_top_pixel(self):
        topPixel = self.frontier[0]
        max_x = topPixel.x

        for p in self.frontier:
            if max_x < p.x:
                max_x = p.x
                topPixel = p

        return topPixel

    # Return an array of all elbows
    def compute_all_elbows(self):
        elbows = []
        for p in self.binaryImage.blackPixels:
            if self.is_elbow(p):
                elbows.append(p)

        return elbows

    # Return a boolean if a pixel is an elbow
    def is_elbow(self, pixel):
        pE = self.binaryImage.get_pixel_adjacent(pixel, d.E)
        pSE = self.binaryImage.get_pixel_adjacent(pixel, d.SE)
        pS = self.binaryImage.get_pixel_adjacent(pixel, d.S)
        return pE.color == BinaryElement.White and pSE.color == BinaryElement.White \
               and pS.color == BinaryElement.White

    # Return the lead elbow
    def compute_lead_elbow(self):
        max_x = float('-inf')
        leadElbow = None
        for p in self.frontier:
            if self.is_elbow(p) and max_x < p.x:
                leadElbow = p

        return leadElbow

    # Return a boolean if the swap of 2 pixels is possible
    def swap_pixels(self, p: Pixel, q: Pixel, swap_active=True):
        imgTemp = copy.deepcopy(self.binaryImage)
        pTemp = imgTemp.get_pixel(p.x, p.y)
        qTemp = imgTemp.get_pixel(q.x, q.y)
        swap_pixel = False

        if imgTemp.is_adjacent(pTemp, qTemp, INTERCHANGE_CONNEXITY) and pTemp.color != qTemp.color:
            colorTemp = pTemp.color
            pTemp.color = qTemp.color
            qTemp.color = colorTemp

            # if not imgTemp.is_cut_vertex(pTemp) and not imgTemp.is_cut_vertex(qTemp):
            pNeighbours = imgTemp.get_neighbours(pTemp, BLACK_CONNEXITY, pTemp.color)
            qNeighbours = imgTemp.get_neighbours(qTemp, WHITE_CONNEXITY, qTemp.color)

            if pNeighbours and qNeighbours:
                if swap_active:
                    self.binaryImage = imgTemp
                    self.binaryImage.update_black_white([pTemp, qTemp])
                    self.interchange += 1
                    self.update_elements()
                swap_pixel = True

        else:
            print("Trying to swap same pixel or same color pixels")

        return swap_pixel

    # Update all attributes of the Algorithm
    def update_elements(self):
        self.width = self.binaryImage.width - 2
        self.frontier, adj_black_pixels = self.compute_frontier()
        self.anchor = self.compute_anchor()
        self.topPixel = self.compute_top_pixel()
        self.allElbow = self.compute_all_elbows()
        self.leadElbow = self.compute_lead_elbow()
        if self.anchor is None:
            self.height = None
        else:
            self.height = self.leadElbow.x - self.anchor.x