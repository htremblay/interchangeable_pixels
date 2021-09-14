import BinaryImage
import AlgoB4W4


imageTest = [[0,0,0,0,0],
			 [0,0,0,0,0],
			 [0,0,0,0,0],
			 [0,1,0,0,0],
			 [0,0,0,0,0]]


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
	binaryImage = BinaryImage.BinaryImage(imageTest)
	algo = AlgoB4W4.AlgoB4W4(binaryImage)
	binaryImage.show_image()
except Exception as e:
	print(e)


