# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 14:59:26 2020

@author: nbarl
"""

import random
from math import sqrt
import BinImage

def randomImage(n) :
	height = (int) (n+sqrt(2*n/3.14)+3)
	width = (int) (2*sqrt(2*n/3.14)+6)
	im = []
	for i in range(height) :
		im.append([0]*width)
	im[n][width//2]=1
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