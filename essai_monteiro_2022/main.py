from algorithme_B4W4.New_Conception_v2.src.graphics.binary_image_displayer import BinaryImageDisplayer
from src.models.binary_image import BinaryImage
from algorithme_B4W4.New_Conception_v2.src.solvers.B4W4.b4w4_solver import B4W4_Solver
from algorithme_B4W4.New_Conception_v2.src.solvers.B4W8.b4w8_solver import B4W8_Solver
from algorithme_B4W4.New_Conception_v2.src.solvers.B8W4.b8w4_solver import B8W4_Solver
from algorithme_B4W4.New_Conception_v2.src.solvers.B8W8.b8w8_solver import B8W8_Solver
from algorithme_B4W4.New_Conception_v2.src.statistics.statistics_solver import Statistics
import matplotlib.pyplot as plt


def main_b4_w4() -> int:
    image = BinaryImage.create_img_spiral(50, 4, 4)
    image_final = BinaryImage.create_img_vertical(image.size, 4, 4)

    displayer = BinaryImageDisplayer(show_legend=True)

    solver = B4W4_Solver(image, image_final)

    displayer.show(image, subtitle="Image de départ")

    nb_interchange = solver.solve()

    print("Nb interchange = ", nb_interchange)
    print("len interchange = ", len(solver.array_interchange))

    displayer.show(image, subtitle="Image de fin")

    displayer.create_gif(image=solver.imageElementsStart.get_saved_img(),
                         array_interchage=solver.array_interchange, speed=1000, name="B4_W8.gif")

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


#Total average for solver B 4 W 8  is  {10: [[446967, 282006, 246098, 485400, 415473], 40.4], 20: [[471657, 420235, 336886, 252195, 400259], 185.2], 30: [[28792, 269945, 187536, 187289, 127483], 410.0], 40: [[191113, 221241, 37131, 382765, 245666], 676.4], 50: [[203153, 2675, 266197, 157744, 425949], 1277.0], 60: [[274428, 356235, 221797, 183902, 49609], 1783.2], 70: [[480643, 299171, 10936, 373083, 154123], 2457.8], 80: [[37431, 114774, 470418, 78827, 178029], 3123.2], 90: [[284974, 148131, 169071, 329126, 52714], 3927.8], 100: [[243247, 321259, 232955, 152799, 210337], 4681.0]}
#Total average for solver B 4 W 4  is  {10: [[275201, 467016, 2192, 38466, 352304], 48.0], 20: [[448638, 190762, 431594, 35348, 75824], 182.0], 30: [[408376, 51971, 401436, 162767, 277997], 402.0], 40: [[80511, 493136, 179278, 492002, 208013], 767.0], 50: [[98220, 254028, 366188, 12256, 412467], 1224.6], 60: [[114012, 474885, 53700, 134120, 132292], 1579.0], 70: [[218094, 349699, 302779, 160737, 295994], 2236.0], 80: [[159067, 91894, 245898, 65718, 127263], 2999.2], 90: [[160776, 203117, 336316, 223880, 42017], 3886.2], 100: [[280821, 232572, 214314, 480367, 431444], 4805.0]}
#Total average for solver B 8 W 4  is  {10: [[414621, 448708, 2996, 154158, 43386], 51.8], 20: [[461910, 299106, 167461, 27124, 214506], 256.2], 30: [[276527, 342957, 227843, 386169, 26864], 614.4], 40: [[244548, 107189, 305770, 47969, 353819], 920.2], 50: [[338487, 35367, 1632, 224307, 439580], 1417.8], 60: [[375019, 213240, 450165, 340715, 414813], 2060.0], 70: [[465601, 367519, 360491, 69208, 281430], 2823.4], 80: [[368613, 327664, 112300, 282483, 327378], 3734.6], 90: [[267408, 478, 445498, 103897, 383238], 4411.0], 100: [[164903, 185599, 405649, 443084, 301871], 5718.2]}
#Total average for solver B 8 W 8  is  {10: [[24229, 4101, 398504, 409116, 158201], 54.6], 20: [[129050, 491189, 268649, 417503, 485354], 255.0], 30: [[34844, 33260, 381857, 171564, 323629], 581.4], 40: [[89859, 29003, 378769, 474546, 90636], 1013.8], 50: [[157568, 398307, 17441, 311939, 227752], 1399.6], 60: [[26847, 283667, 381342, 267682, 113119], 1973.8], 70: [[91158, 107566, 451813, 410250, 38], 2829.8], 80: [[307719, 17016, 377851, 223983, 189945], 3556.2], 90: [[484075, 226018, 452040, 247526, 482984], 4582.4], 100: [[123339, 321890, 377992, 110073, 123710], 5663.8]}
def main_statistics():
    all_connexities = [[8, 8],
                       [8, 4],
                       [4, 8],
                       [4, 4]]

    for connexity in all_connexities:
        stats = Statistics()
        print(connexity)
        stats.statistics_from_random_images(black_connexity=connexity[0], white_connexity=connexity[1],
                                            nb_iter=10, nb_tick=5, initial_size_image=10, incr_size_image=10)
        plt.figure()

        plt.xlabel('nombre de pixels')
        plt.ylabel('nombre d\'échanges')
        title = 'Complexité de l\'algorithme B' + str(connexity[0]) + "W" + str(connexity[1])
        plt.title(title)
        x = []
        y = []
        for key, values in stats.dic_interchanges.items():
            x.append(key)
            y.append(values[1])

        plt.plot(x, y)
        plt.savefig('./'+str(connexity)+'_stats.svg', dpi=500)
        plt.show()



# Total average for solver B 4 W 4  is  {10: [0, 29], 20: [1, 151], 30: [2, 363], 40: [3, 648], 50: [4, 1120], 60: [5, 1583], 70: [6, 2145], 80: [7, 2793], 90: [8, 3589], 100: [9, 4627]}
# Total average for solver B 4 W 8  is  {10: [0, 29], 20: [1, 140], 30: [2, 350], 40: [3, 631], 50: [4, 1082], 60: [5, 1517], 70: [6, 2073], 80: [7, 2709], 90: [8, 3509], 100: [9, 4474]}
# Total average for solver B 8 W 4  is  {10: [0, 50], 20: [1, 196], 30: [2, 458], 40: [3, 819], 50: [4, 1392], 60: [5, 1905], 70: [6, 2479], 80: [7, 3220], 90: [8, 4160], 100: [9, 5306]}
# Total average for solver B 8 W 8  is  {10: [0, 42], 20: [1, 189], 30: [2, 451], 40: [3, 812], 50: [4, 1345], 60: [5, 1902], 70: [6, 2476], 80: [7, 3217], 90: [8, 4157], 100: [9, 5214]}
def main_statistics_spiral():
    all_connexities = [[8, 8],
                       [8, 4],
                       [4, 8],
                       [4, 4]]

    for connexity in all_connexities:
        stats = Statistics()
        print(connexity)
        stats.statistics_spiral(black_connexity=connexity[0], white_connexity=connexity[1],
                                    nb_iter=10, nb_tick=1, initial_size_image=10, incr_size_image=10)

        plt.figure()
        plt.xlabel('nombre de pixels')
        plt.ylabel('nombre d\'échanges')
        title = 'Complexité de l\'algorithme B' + str(connexity[0]) + "W" + str(connexity[1])
        plt.title(title)
        x = []
        y = []
        for key, values in dict.items():
            x.append(key)
            y.append(values[1])

        plt.plot(x, y)
        plt.savefig('./spiral_B4W4_stats.svg', dpi=500)
        plt.show()



if __name__ == "__main__":
    main_b4_w4()
    # main_b4_w8()
    # main_b8_w4()
    # main_b8_w8()
    # main_debug()
    # main_statistics()
    # main_statistics_spiral()









# Taille 50
# Total average for solver B 4 W 8  is  {5: [[235999, 148373, 202631], 7.0], 10: [[75960, 213758, 345888], 42.666666666666664], 15: [[29297, 51231, 321420], 113.66666666666667], 20: [[438003, 50316, 27994], 185.66666666666666], 25: [[481988, 409007, 22339], 268.6666666666667], 30: [[448365, 48116, 431951], 414.0], 35: [[182029, 184751, 475205], 561.0], 40: [[474483, 130499, 320600], 785.0], 45: [[305534, 432432, 269078], 918.0], 50: [[381713, 155404, 288378], 1105.3333333333333]}
# Total average for solver B 8 W 4  is  {5: [[113294, 398124, 464447], 20.333333333333332], 10: [[463190, 166874, 355065], 54.0], 15: [[308737, 203327, 437814], 145.33333333333334], 20: [[64383, 106521, 419514], 221.0], 25: [[139155, 460119, 436670], 388.0], 30: [[88476, 298922, 231609], 546.6666666666666], 35: [[4499, 338169, 431810], 761.6666666666666], 40: [[290605, 285740, 101669], 1041.0], 45: [[449875, 46362, 316450], 1270.0], 50: [[59855, 322571, 125284], 1537.6666666666667]}
# Total average for solver B 8 W 8  is  {5: [[86631, 267480, 17878], 16.0], 10: [[276331, 394143, 268103], 58.0], 15: [[244757, 250155, 265709], 116.0], 20: [[477921, 467021, 307654], 228.0], 25: [[371857, 245787, 484163], 430.3333333333333], 30: [[176932, 219330, 134947], 497.6666666666667], 35: [[373908, 81066, 312737], 680.3333333333334], 40: [[81198, 6304, 250306], 865.6666666666666], 45: [[379099, 200861, 423999], 1186.6666666666667], 50: [[159773, 71118, 482130], 1419.6666666666667]}
# Total average for solver B 4 W 4  is  {5: [[7315, 239720, 424945], 9.666666666666666], 10: [[88678, 385206, 228018], 40.333333333333336], 15: [[217388, 398285, 441501], 107.66666666666667], 20: [[214435, 39362, 310586], 169.0], 25: [[430391, 279359, 168519], 300.3333333333333], 30: [[143609, 128593, 244806], 393.3333333333333], 35: [[290438, 189132, 78319], 627.0], 40: [[161174, 287589, 71750], 727.6666666666666], 45: [[319089, 25908, 32505], 1051.6666666666667], 50: [[149040, 409611, 25654], 1289.0]}

