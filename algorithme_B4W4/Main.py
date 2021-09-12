import Pixel
import BinaryImage


imageIsolatedWhite = [[1]]

imageIsolatedBlack = [[0,0,0,0,0],
					 [0,1,1,0,0],
					 [0,1,0,0,1],
					 [0,1,1,1,0],
					 [0,0,0,0,0]]

imageIsolatedBoth = [[1,0,0,0,0,0],
					 [0,0,1,1,0,0],
					 [0,0,1,0,1,0],
					 [0,0,1,1,1,0],
					 [0,1,0,1,0,1],
					 [0,0,0,0,0,0],
					 [0,0,0,0,0,1],]

# for pixel in pixels:
#     print(pixel)
binaryImage = BinaryImage.BinaryImage(imageIsolatedBoth)
binaryImage.show_image()
