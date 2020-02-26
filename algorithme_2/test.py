# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 15:11:51 2020

@author: nbarl
"""

import BinImage
import Evolution
from generation import randomImage
from algo2 import findP, B4W8kinterchange, algoB4W8





image_test = [[0,0,0,0],
			  [0,0,0,0],
			  [0,1,1,0]]


#im = BinImage.BinImage(image_test, False, True)
im = randomImage(40)
evol = Evolution.Evolution(im)

algoB4W8(evol)

evol.createGif("B4W8.gif", 100)
print(evol.getNbActions())
