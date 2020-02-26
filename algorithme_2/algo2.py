# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 22:42:19 2020

@author: nbarl
"""

def findP(image) :
	columnPos = -1
	for i in range(image.n) :
		for j in range(image.m-1, -1,-1):
			if image.getPixel(i,j)==1 :
				columnPos=j
				break
			else :
				if j==columnPos : #we are under the wanted column
					return (i-1, j)
	return (image.n-1, columnPos)