# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 15:11:51 2020

@author: nbarl
"""

import networkx as nx
import BinImage




image_test = [[0,0,0],
			  [0,1,1],
			  [0,0,1]]


im = BinImage.BinImage(image_test, False, True)


print(im.findOrigin())
print(im.pixelPotential(1,1))
print(im.pixelPotential(1,2))
print(im.pixelPotential(2,2))
print(im.potential())


"""
G = nx.Graph()

G.add_edge((0,0),(0,1))
G.add_edge((0,0),(1,0))
G.add_edge((1,0),(1,1))
G.add_edge((0,1),(1,1))

#G.remove_node((1,0))

print(list(nx.articulation_points(G)))
"""

