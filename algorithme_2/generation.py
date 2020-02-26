# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 14:59:26 2020

@author: nbarl
"""

import random
from math import sqrt
import BinImage

def separated(l) :
	change = 0
	lastVal = l[0]
	for x in l[1:] :
		if x!=lastVal :
			change += 1
			lastVal = x
			if change > 2 :
				return False
	return True

def randomImage(n) :
	height = (int) (n+2*sqrt(n)+3)
	width = (int) (2*sqrt(n)+6)
	im = []
	for i in range(height) :
		im.append([0]*width)
	im[(int)(n+sqrt(n))][width//2]=1
	image = BinImage.BinImage(im, False, True)
	
	generateContour = True
	i=1
	while i<n :
		if generateContour :
			contour = image.getContour()
			generateContour = False
		newPix = random.choice(contour)
		image.addPixel(newPix)
		
		if separated(image.get8Neighbours(newPix)) :
			connected = True
		else :
			connected= image.isConnected(True)
		
		if connected :
			i+=1
			generateContour = True
		else :
			image.removePixel(newPix)
			contour.remove(newPix)
			
	image.findOrigin()
	image.computeLayout()
	return image