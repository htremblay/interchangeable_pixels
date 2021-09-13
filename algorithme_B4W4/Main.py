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

try:
	binaryImage = BinaryImage.BinaryImage("600")
	binaryImage.show_image()
except Exception as e:
	print(e)


