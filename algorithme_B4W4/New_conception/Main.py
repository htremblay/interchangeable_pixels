import BinaryImage
import AlgoB4W4
from Enumeration import Direction as d

imgTest = [[1], [1], [1]]

imageIsolatedBlack = [[0, 0, 0, 0, 0],
                      [0, 1, 1, 0, 0],
                      [0, 1, 0, 1, 0],
                      [0, 1, 1, 1, 0],
                      [0, 0, 0, 0, 0]]

imageIsolatedBoth = [[0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0],
                     [0, 0, 1, 1, 1, 0],
                     [0, 0, 1, 0, 1, 0],
                     [0, 0, 1, 1, 0, 0],
                     [0, 1, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0]]

showReduceAndExpand = [[0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 1, 1, 1, 1, 1],
                       [0, 0, 0, 1, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 0]]

showKDiag = [[0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 1, 0, 1, 0, 0, 0],
              [0, 1, 0, 0, 1, 0, 0, 0],
              [0, 1, 1, 1, 1, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0]]

showReduce = [[0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 1, 1, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0]]

showExpand = [[1], [1], [1]]

IMG_ALGO_B4W4_ELEMENTS = [[0, 0, 0, 1, 1, 0, 0],
                          [0, 0, 0, 1, 0, 0, 1],
                          [0, 0, 1, 1, 1, 1, 1],
                          [0, 0, 1, 0, 0, 1, 0],
                          [0, 0, 1, 1, 0, 1, 1],
                          [0, 0, 1, 0, 0, 0, 1],
                          [0, 0, 0, 0, 0, 0, 0]]

seed = 5
blackConnexity = 4
whiteConnexity = 4
sizeImage = 100
name_image_random = str(seed) + "_" + str(sizeImage) + "_B" + str(blackConnexity) + "_W" + str(whiteConnexity)


###############
#### MAIN #####
###############
binaryImage = BinaryImage.BinaryImage(IMG_ALGO_B4W4_ELEMENTS, blackConnexity, whiteConnexity, seed)
algo = AlgoB4W4.AlgoB4W4(binaryImage)

# p = binaryImage.get_pixel(1, 2)
# q = binaryImage.get_pixel_directionnal(p, [d.N, d.N, d.E, d.E])


binaryImage.show_image(title=name_image_random + " - Before", show_isolated=True, nb_figure=1)

# algo.swap_pixels(binaryImage.get_pixel(2, 4), binaryImage.get_pixel(1, 5), swap_active=True)

# test_dictionnary = {
#     'lightgreen': algo.frontier,
#     'dodgerblue': [algo.anchor],
#     'magenta': [algo.topPixel],
#     # 'gold': algo.allElbow,
#     'tomato': [algo.leadElbow]
# }

# algo.binaryImage.show_image(title=name_image_random + " - After",
#                             show_isolated=False, nb_figure=2)