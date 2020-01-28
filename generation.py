# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 14:59:26 2020

@author: nbarl
"""

import random
import BinImage

def randomImage(n) :
	height = (int) (n*1.5+5)
	width = (int) (n*0.7+5)
	im = []
	for i in range(height) :
		im.append([0]*width)
	im[(height*3)//4][width//2]=1
	image = BinImage.BinImage(im, False, True)
	for i in range(n-1) :
		contour = image.getContour()
		newPix = random.choice(contour)
		image.addPixel(newPix)
	return image