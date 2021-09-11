import Pixel
import BinaryImage


imageTest = [[0,0,0,0,0],
			 [0,0,0,1,0],
			[0,0,0,0,0],
			[0,0,0,0,0],
			[0,0,0,0,0]]

# for pixel in pixels:
#     print(pixel)

binaryImage = BinaryImage.BinaryImage(imageTest)
binaryImage.show_image()
