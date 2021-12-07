from algorithme_B4W4.New_Conception_v2.src.graphics.binary_image_displayer import BinaryImageDisplayer
from src.models.binary_image import BinaryImage
from algorithme_B4W4.New_Conception_v2.src.utils import Direction as d
from algorithme_B4W4.New_Conception_v2.src.solvers.B4W4.b4w4_elements import B4W4_Elements
from algorithme_B4W4.New_Conception_v2.src.solvers.B4W4.b4w4_solver import B4W4_Solver
from algorithme_B4W4.New_Conception_v2.src.solvers.B4W8.b4w8_solver import B4W8_Solver

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

test_get_p = [[ 1, 1, 0 ,0],
              [ 1, 0, 1, 1],
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

    print(binary_img.size)
    print(binary_img_vertical.size)

    solver = B4W4_Solver(binary_img, binary_img_vertical)

    nb_echange = solver.solve()
    print("Nombre d'échange total : ", nb_echange)

    displayer.create_gif(image=solver.imageElementsStart.get_saved_img(),
                         array_interchage=solver.array_interchange, speed=1000, name="B4_W4_Spirale.gif")

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
    image_saved = BinaryImage.create_random_img(image_size, 4, 8, seed)
    image = BinaryImage.create_random_img(image_size, 4, 8, seed)

    image = BinaryImage.create_img_spiral(50, 4, 8)
    # image = BinaryImage.create_img_from_array(test_get_p, 4, 8)
    # image_saved = BinaryImage.create_img_from_array(test_get_p, 4, 8)
    image_final = BinaryImage.create_img_vertical(image.size, 4, 8)

    displayer = BinaryImageDisplayer(show_legend=True)

    solver = B4W8_Solver(image, image_final)

    displayer.show(solver.imageStart, subtitle="Begined")

    nb_interchange = solver.solve()


    print("Nb interchange = ", nb_interchange)
    print("len interchange = ", len(solver.array_interchange))

    displayer.show(solver.imageStart, subtitle="Finished")

    displayer.create_gif(image=solver.get_image_save(),
                         array_interchage=solver.array_interchange, speed=1000, name="B4_W8.gif")

    return 0



if __name__ == "__main__":
    # main()
    main_test_spiral()
    # main_fonctionnel()
    # main_b4_w8()