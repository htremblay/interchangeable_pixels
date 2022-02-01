from algorithme_B4W4.New_Conception_v2.src.graphics.binary_image_displayer import BinaryImageDisplayer
from src.models.binary_image import BinaryImage
from algorithme_B4W4.New_Conception_v2.src.utils import Direction as d
from algorithme_B4W4.New_Conception_v2.src.solvers.B4W4.b4w4_elements import B4W4_Elements
from algorithme_B4W4.New_Conception_v2.src.solvers.B4W4.b4w4_solver import B4W4_Solver
from algorithme_B4W4.New_Conception_v2.src.solvers.B4W8.b4w8_solver import B4W8_Solver
from algorithme_B4W4.New_Conception_v2.src.solvers.B8W4.b8w4_solver import B8W4_Solver
from algorithme_B4W4.New_Conception_v2.src.solvers.B8W8.b8w8_solver import B8W8_Solver
from algorithme_B4W4.New_Conception_v2.src.statistics.statistics_solver import Statistics

# region Context

img_test = [[1]]

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

showReduce = [[0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 1, 1, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0]]

showExpand = [[1, 1, 1]]

IMG_ALGO_B4W4_ELEMENTS = [[0, 0, 0, 1, 1, 0, 0],
                          [0, 0, 0, 1, 0, 0, 1],
                          [0, 0, 1, 1, 1, 1, 1],
                          [0, 0, 1, 0, 0, 1, 0],
                          [0, 0, 1, 1, 0, 1, 1],
                          [0, 0, 1, 0, 0, 0, 1],
                          [0, 0, 0, 0, 0, 0, 0]]

showKDiag_simple = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 0, 1, 0, 0, 0, 0],
                    [0, 1, 0, 0, 1, 0, 0, 0, 0],
                    [0, 1, 1, 1, 1, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0],
                    [0, 0, 0, 0, 0, 0, 0, 0, 0]]

showKDiag_case_not_cut = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 1, 1, 0, 0, 0, 0, 0, 0, 0],
                          [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 1, 1, 1, 1, 0, 0, 0, 0, 0],
                          [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
                          [0, 0, 0, 1, 1, 1, 1, 0, 1, 0],
                          [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
                          [0, 0, 0, 1, 1, 1, 1, 1, 1, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

showKDiag_case_cut = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 1, 1, 0, 0, 0, 0, 0, 0],
                      [0, 1, 0, 0, 1, 0, 0, 0, 0],
                      [0, 1, 1, 1, 1, 0, 0, 0, 0],
                      [0, 0, 0, 1, 0, 0, 1, 0, 0],
                      [0, 0, 0, 1, 1, 1, 1, 0, 1],
                      [0, 0, 0, 1, 0, 0, 0, 0, 1],
                      [0, 0, 0, 1, 1, 1, 1, 1, 1],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0, 0, 0]]

showKDiag_case_cut_2 = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 1, 0, 0, 0, 0, 0, 0, 0],
                        [0, 1, 0, 0, 1, 0, 0, 0, 0],
                        [0, 1, 1, 1, 1, 0, 0, 0, 0],
                        [0, 0, 0, 1, 0, 0, 1, 0, 0],
                        [0, 0, 0, 1, 1, 1, 1, 0, 1],
                        [0, 0, 0, 1, 0, 0, 0, 0, 1],
                        [0, 0, 0, 1, 1, 1, 1, 1, 1],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0, 0, 0, 0, 0]]

showKDiag = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 1, 1, 1, 0, 0, 0, 0],
             [0, 1, 1, 0, 1, 0, 1, 0, 1],
             [0, 1, 0, 0, 1, 0, 1, 0, 1],
             [0, 1, 0, 0, 0, 0, 1, 0, 1],
             [0, 1, 0, 0, 0, 1, 1, 0, 1],
             [0, 1, 1, 1, 1, 1, 0, 0, 1],
             [0, 0, 0, 0, 0, 1, 1, 1, 1],
             [0, 0, 0, 0, 0, 1, 1, 1, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0], ]

weirdKDiag = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 1, 1, 1, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 1, 0, 0, 0, 0],
              [0, 0, 0, 1, 1, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0], ]

test_get_p = [[1, 1, 0, 0],
              [1, 0, 1, 1],
              [1, 1, 1, 0],
              [0, 1, 0, 0]]

seed = 345
black_connexity = 4
white_connexity = 4
image_size = 50


# endregion

# region density
#### 250 ####
###### low_density : {147: 0.012433734939759036, 155: 0.012369477911646587, 222: 0.012176706827309237,
# 345: 0.01240160642570281, 573: 0.012433734939759036, 625: 0.01240160642570281,
# 713: 0.012273092369477911, 715: 0.012433734939759036, 791: 0.012433734939759036,
# 818: 0.01233734939759036}

###### high_density : {80: 0.013911646586345382, 96: 0.013815261044176706, 214: 0.013718875502008033,
# 328: 0.013815261044176706, 347: 0.013783132530120482, 500: 0.013718875502008033,
# 581: 0.013783132530120482, 686: 0.013718875502008033, 723: 0.013718875502008033,
# 864: 0.013815261044176706}
###### medium_density : {1: 0.013172690763052209, 3: 0.013269076305220883, 5: 0.012947791164658634,
# 6: 0.01278714859437751, 9: 0.013236947791164659, 11: 0.013012048192771084,
# 14: 0.01310843373493976, 63: 0.013140562248995983, 227: 0.01310843373493976,
# 629: 0.013076305220883534}

####  1000 ####
# low_density : {1788: 0.02727272727272727, 2195: 0.028282828282828285, 2318: 0.028282828282828285,
# 3060: 0.028282828282828285, 3873: 0.028282828282828285, 3984: 0.027676767676767678,
# 4490: 0.028282828282828285, 4567: 0.027676767676767678, 4639: 0.02727272727272727,
# 4753: 0.02808080808080808}
# high_density : {1210: 0.03414141414141414, 1464: 0.03414141414141414, 2289: 0.03393939393939394,
# 2629: 0.03393939393939394, 2652: 0.03434343434343434, 2798: 0.03393939393939394,
# 2971: 0.03414141414141414, 3135: 0.03414141414141414, 3585: 0.03414141414141414,
# 4178: 0.03434343434343434}
# medium_density : {1015: 0.03171717171717172, 1018: 0.03151515151515152, 1026: 0.03171717171717172,
# 1028: 0.03151515151515152, 1038: 0.03171717171717172, 1067: 0.03151515151515152,
# 1121: 0.031313131313131314, 1354: 0.03111111111111111, 2975: 0.031313131313131314,
# 3063: 0.03111111111111111}
# endregion density

def main() -> int:
    # dict_img = {
    #             # "ex_simple": showKDiag_simple,
    #             "ex_p_1_not_cut": showKDiag_case_not_cut,
    #             # "ex_p1_cut": showKDiag_case_cut,
    #             # "ex_p1_cut_2": showKDiag_case_cut_2,
    #             # "revese k_diag": weirdKDiag
    #             }

    #
    # for key, img in dict_img.items():
    #     binary_image_start = BinaryImage.create_img_from_array(img, black_connexity, white_connexity)
    #     binary_image_final = BinaryImage.create_img_vertical(binary_image_start.size, black_connexity, white_connexity)
    #     solver = B4W4_Solver(binary_image_start, binary_image_final)

    # print("\n----- Image binary ", key, " -----")
    # for p in solver.imageElementsStart.all_elbows:
    #     k, p_1 = solver.imageElementsStart.lemme_5(p)
    #     print(k, "-diagonal avec on pixel p ", p, " et mon p1 ", p_1)

    # p = solver.imageElementsStart.binary_image.get_pixel(1, 4)
    # p = solver.imageElementsStart.binary_image.get_pixel(1, 8)
    # k, p_1 = solver.imageElementsStart.lemme_5(p)
    #
    # nb_echange = solver.imageElementsStart.k_diagonal_interchange(p, p_1)
    # print(nb_echange)

    binary_image_start = BinaryImage.create_random_img(image_size, black_connexity, white_connexity, seed=seed)
    binary_image_final = BinaryImage.create_random_img(image_size, black_connexity,
                                                       white_connexity, seed=seed * 2)
    solver = B4W4_Solver(binary_image_start, binary_image_final)

    ###### Affichage ######
    binary_image_displayer = BinaryImageDisplayer(show_border=False, show_isolated=False, show_legend=True)
    binary_image_displayer.show(image=binary_image_start, subtitle="Depart")
    # binary_image_displayer.show(image=binary_image_final, subtitle="Arrivée")

    # Solver
    nb_echange = solver.solve()

    binary_image_displayer.create_gif(image=solver.imageElementsStart.get_saved_img(),
                                      array_interchage=solver.array_interchange, speed=1500)

    binary_image_displayer.show(image=solver.imageElementsFinal.binary_image,
                                subtitle="AFTER Solve")

    print("Nombre d'échange total :", nb_echange)

    return 0


def main_test_spiral() -> int:
    displayer = BinaryImageDisplayer()

    binary_img = BinaryImage.create_img_spiral(50, 4, 4)
    binary_img_vertical = binary_img.create_img_vertical(binary_img.size, 4, 4)

    displayer.show(binary_img, subtitle="Image de départ")

    solver = B4W4_Solver(binary_img, binary_img_vertical)

    nb_echange = solver.solve()
    print("Nombre d'échange total : ", nb_echange)

    # displayer.create_gif(image=solver.imageElementsStart.get_saved_img(),
    #                      array_interchage=solver.array_interchange, speed=1000, name="B4_W4_Spirale.gif")

    displayer.show(binary_img, subtitle="Image Résultante")

    return 0


def main_fonctionnel() -> int:
    binary_image_start = BinaryImage.create_img_from_array(showKDiag_case_cut_2, black_connexity, white_connexity)
    binary_image_final = BinaryImage.create_img_vertical(binary_image_start.size, black_connexity, white_connexity)

    displayer = BinaryImageDisplayer()
    displayer.show(binary_image_start, subtitle="image de départ")

    solver = B4W4_Solver(binary_image_start, binary_image_final)

    nb_echange = solver.solve()

    print("Nombre d'échange total :", nb_echange)

    # displayer.create_gif(image=solver.imageElementsStart.get_saved_img(),
    #                      array_interchage=solver.array_interchange, speed=500)

    displayer.show(image=solver.imageElementsFinal.binary_image,
                   subtitle="AFTER Solve")

    return 0


def main_b4_w8() -> int:
    image = BinaryImage.create_img_spiral(50, 4, 8)
    image_final = BinaryImage.create_img_vertical(image.size, 4, 8)

    displayer = BinaryImageDisplayer(show_legend=True)

    solver = B4W8_Solver(image, image_final)

    displayer.show(solver.imageStart, subtitle="Image de départ")

    nb_interchange = solver.solve()

    print("Nb interchange = ", nb_interchange)
    print("len interchange = ", len(solver.array_interchange))

    displayer.show(solver.imageStart, subtitle="Image de fin")

    displayer.create_gif(image=solver.get_image_save(),
                         array_interchage=solver.array_interchange, speed=1000, name="B4_W8.gif")

    return 0


def main_b8_w4() -> int:
    image = BinaryImage.create_img_spiral(50, 8, 4)
    image_final = BinaryImage.create_img_vertical(image.size, 8, 4)

    displayer = BinaryImageDisplayer(show_legend=True)

    solver = B8W4_Solver(image, image_final)

    displayer.show(solver.imageStart, subtitle="Image de départ")

    nb_interchange = solver.solve()

    print("Nb interchange = ", nb_interchange)
    print("len interchange = ", len(solver.array_interchange))

    displayer.show(solver.imageStart, subtitle="Image de fin")

    displayer.create_gif(image=solver.get_image_save(),
                         array_interchage=solver.array_interchange, speed=1000, name="B8_W4.gif")

    return 0


def main_b8_w8() -> int:
    image = BinaryImage.create_img_spiral(50, 8, 8)
    image_final = BinaryImage.create_img_vertical(image.size, 8, 8)

    displayer = BinaryImageDisplayer(show_legend=True)

    solver = B8W8_Solver(image, image_final)

    displayer.show(solver.imageStart, subtitle="Image de départ")

    nb_interchange = solver.solve()

    print("Nb interchange = ", nb_interchange)
    print("len interchange = ", len(solver.array_interchange))

    displayer.show(solver.imageStart, subtitle="Image de fin")

    displayer.create_gif(image=solver.get_image_save(),
                         array_interchage=solver.array_interchange, speed=1000, name="B8_W8.gif")

    return 0


def main_debug():
    img_depart = [[0, 0, 0, 0, 0, 0, 0],
                  [0, 1, 1, 1, 0, 0, 0],
                  [0, 1, 0, 0, 0, 1, 0],
                  [0, 1, 1, 1, 1, 1, 0],
                  [0, 0, 0, 0, 0, 0, 0]]

    binary_image = BinaryImage.create_random_img(n=50, black_connexity=4,
                                                 white_connexity=8, seed=432432)

    displayer = BinaryImageDisplayer()
    displayer.show(binary_image, subtitle="Départ")
    solver = B4W8_Solver(binary_image, BinaryImage.create_img_vertical(binary_image.size))

    solver.solve()

    displayer.show(binary_image, subtitle="After resolver")


import matplotlib.pyplot as plt

# Total average for solver B 4 W 8  is  {5: [[235999, 148373, 202631], 7.0], 10: [[75960, 213758, 345888], 42.666666666666664], 15: [[29297, 51231, 321420], 113.66666666666667], 20: [[438003, 50316, 27994], 185.66666666666666], 25: [[481988, 409007, 22339], 268.6666666666667], 30: [[448365, 48116, 431951], 414.0], 35: [[182029, 184751, 475205], 561.0], 40: [[474483, 130499, 320600], 785.0], 45: [[305534, 432432, 269078], 918.0], 50: [[381713, 155404, 288378], 1105.3333333333333]}
# Total average for solver B 8 W 4  is  {5: [[113294, 398124, 464447], 20.333333333333332], 10: [[463190, 166874, 355065], 54.0], 15: [[308737, 203327, 437814], 145.33333333333334], 20: [[64383, 106521, 419514], 221.0], 25: [[139155, 460119, 436670], 388.0], 30: [[88476, 298922, 231609], 546.6666666666666], 35: [[4499, 338169, 431810], 761.6666666666666], 40: [[290605, 285740, 101669], 1041.0], 45: [[449875, 46362, 316450], 1270.0], 50: [[59855, 322571, 125284], 1537.6666666666667]}
# Total average for solver B 8 W 8  is  {5: [[86631, 267480, 17878], 16.0], 10: [[276331, 394143, 268103], 58.0], 15: [[244757, 250155, 265709], 116.0], 20: [[477921, 467021, 307654], 228.0], 25: [[371857, 245787, 484163], 430.3333333333333], 30: [[176932, 219330, 134947], 497.6666666666667], 35: [[373908, 81066, 312737], 680.3333333333334], 40: [[81198, 6304, 250306], 865.6666666666666], 45: [[379099, 200861, 423999], 1186.6666666666667], 50: [[159773, 71118, 482130], 1419.6666666666667]}
# Total average for solver B 4 W 4  is  {5: [[7315, 239720, 424945], 9.666666666666666], 10: [[88678, 385206, 228018], 40.333333333333336], 15: [[217388, 398285, 441501], 107.66666666666667], 20: [[214435, 39362, 310586], 169.0], 25: [[430391, 279359, 168519], 300.3333333333333], 30: [[143609, 128593, 244806], 393.3333333333333], 35: [[290438, 189132, 78319], 627.0], 40: [[161174, 287589, 71750], 727.6666666666666], 45: [[319089, 25908, 32505], 1051.6666666666667], 50: [[149040, 409611, 25654], 1289.0]}
def main_statistics():
    all_connexities = [#[4, 8],
                       # [8, 4],
                       # [8, 8],
                       [4, 4]
                            ]

    for connexity in all_connexities:
        stats = Statistics()
        print(connexity)
        # stats.statistics_from_random_images(black_connexity=connexity[0], white_connexity=connexity[1],
        #                                     nb_iter=10, nb_tick=3, size_image=5, incr_size_image=5)


        stats.dic_interchanges = {5: [[7315, 239720, 424945], 9.666666666666666], 10: [[88678, 385206, 228018], 40.333333333333336], 15: [[217388, 398285, 441501], 107.66666666666667], 20: [[214435, 39362, 310586], 169.0], 25: [[430391, 279359, 168519], 300.3333333333333], 30: [[143609, 128593, 244806], 393.3333333333333], 35: [[290438, 189132, 78319], 627.0], 40: [[161174, 287589, 71750], 727.6666666666666], 45: [[319089, 25908, 32505], 1051.6666666666667], 50: [[149040, 409611, 25654], 1289.0]}
        plt.figure()

        plt.xlabel('nb of pixels')
        plt.ylabel('nb of exchanges')
        title = 'complexity of the B' + str(connexity[0]) + "W" + str(connexity[1]) + " algorithm"
        plt.title(title)
        x = []
        y = []
        for key, values in stats.dic_interchanges.items():
            x.append(key)
            y.append(values[1])

        plt.plot(x, y)
        plt.show()


if __name__ == "__main__":
    # main()
    # main_test_spiral()
    # main_fonctionnel()
    # main_b4_w8()
    # main_b8_w4()
    # main_b8_w8()
    # main_debug()
    main_statistics()
