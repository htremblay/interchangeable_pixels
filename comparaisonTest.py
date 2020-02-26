# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 11:29:41 2020

@author: nbarl
"""
import time

import sys
sys.path.append('algorithme_1/')
sys.path.append('algorithme_2/')

import generation2 as gen2
from copy import deepcopy
import BinImage as Image1
import Evolution as Evol1
import Evolution2 as Evol2
import algo1
import algo2

n=150

#generte the BinImages from the same random image

def compare(n) :
	t = time.time()
	im2 = gen2.randomImage(n)
	im1 = Image1.BinImage(deepcopy(im2.image), False, True)
	
	evol1 = Evol1.Evolution(im1)
	evol2 = Evol2.Evolution(im2)
	
	t1 = time.time()
	print("generation of an image with ",n," pixels : ", t1-t, " seconds")
	
	algo1.algo1(evol1)
	t2 = time.time()
	print("first algorithm : ", (t2-t1), " seconds")
	print("                  ", (evol1.getNbActions()), " actions")
	
	algo2.algoB4W8(evol2)
	print("second algorithm : ", (time.time()-t2), " seconds")
	print("                   ", (evol2.getNbActions()), " actions")
	
	return (evol1.getNbActions(), evol2.getNbActions())
