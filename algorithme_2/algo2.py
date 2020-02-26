# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 22:42:19 2020

@author: nbarl
"""
import Evolution2
from BinImage2 import Direction
import networkx as nx


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

def B4W8kinterchange(evol):
	im = evol.currentImage
	p = findP(im)
	if not im.isCutVertex(p) :
		if im.getPixel(*im.N(p))==1 :
			evol.addAction(*p, Direction.UpRight)
		elif im.getPixel(*im.N(im.W(p)))==1 :
			evol.addAction(*p, Direction.Up)
		else :
			evol.addAction(*p, Direction.UpLeft)
			
	else :
		if not im.isCutVertex(im.N(im.W(p))) :
			evol.addAction(*p, Direction.UpLeft)
		else :
			g = im.N(im.W(im.W(p)))
			if im.W(p) in list(nx.shortest_path(im.blackGraph, p, g)) :
				evol.addAction(*im.W(p), Direction.Up)
			else :
				if im.getPixel(*im.N(im.N(im.W(p))))==0 :
					evol.addAction(*im.N(p), Direction.Left)
				else :
					evol.addAction(*g, Direction.Right)
					evol.addAction(*im.N(p), Direction.UpRight)
					
def algoB4W8(evol) :
	while not evol.currentImage.isVertical() :
		B4W8kinterchange(evol)
	evol.simplify()