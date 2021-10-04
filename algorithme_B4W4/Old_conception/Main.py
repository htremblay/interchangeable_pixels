import BinaryImage
import AlgoB4W4


imageTest = [[1]]


imageIsolatedBlack = [[0,0,0,0,0],
					 [0,1,1,0,0],
					 [0,1,0,0,1],
					 [0,1,1,1,0],
					 [0,0,0,0,0]]

imageIsolatedBoth = [[0,0,0,0,0,0],
					 [0,0,1,1,0,0],
					 [0,0,1,0,1,0],
					 [0,0,1,1,1,0],
					 [0,1,0,0,0,0],
					 [0,0,0,0,0,0]]

try:
	binaryImage = BinaryImage.BinaryImage(500)
	# algo = AlgoB4W4.AlgoB4W4(binaryImage)
	binaryImage.show_image(show_border=False, show_isolated=False)
except Exception as e:
	print(e)


