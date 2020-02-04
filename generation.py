# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 14:59:26 2020

@author: nbarl
"""

import random
import BinImage

def randomImage(n) :
	height = (int) (n*1.3+5)
	width = (int) (n*0.5+5)
	im = []
	for i in range(height) :
		im.append([0]*width)
	im[(height*3)//4][width//2]=1
	image = BinImage.BinImage(im, False, True)
	i=0
	while i<n-1 :
		contour = image.getContour()
		newPix = random.choice(contour)
		image.addPixel(newPix)
		if image.isConnected(whiteMode = True) :
			i+=1
		else :
			image.removePixel(newPix)
	return image