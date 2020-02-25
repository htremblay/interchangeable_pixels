# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 15:11:51 2020

@author: nbarl
"""

import networkx as nx
import BinImage
from generation import randomImage




image_test = [[0,0,0],
			  [0,1,1],
			  [0,0,1]]


im = BinImage.BinImage(image_test, False, True)
#im = randomImage(10)

print(im.layoutDictionary)

im.drawGraphs()
"""
G = nx.Graph()

G.add_edge((0,0),(0,1))
G.add_edge((0,0),(1,0))
G.add_edge((1,0),(1,1))
G.add_edge((0,1),(1,1))

#G.remove_node((1,0))

print(list(nx.articulation_points(G)))
"""
