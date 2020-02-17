# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 15:11:40 2019

@author: nbarl
"""
#%% imports
from algo1 import ksingular, combineTowers, getBlocks, getTowers, towerize, getContacts, step2, step3, algo1
import BinImage
import Evolution
import generation
import time
import matplotlib.pyplot as plt

#%% definitions
"""
imageTest = [[0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,1,0,0,0,0,0],
			 [0,0,0,0,0,1,1,1,0,0,0,0],
			 [0,0,0,0,0,1,1,1,1,0,0,0],
			 [0,0,0,0,0,1,0,1,1,1,0,0],
			 [0,0,0,0,0,1,1,1,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0]]
"""

imageTest = [[0,0,0,0,0],
			 [0,1,1,0,0],
			 [0,1,0,1,0],
			 [0,1,1,1,0],
			 [0,0,0,0,0],]

"""
imageTest = [[0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,1,0,0,0,0],
			 [0,1,0,0,0,0,1,1,1,1,1,0],
			 [0,1,1,1,1,1,1,1,1,0,1,0],
			 [0,1,0,1,1,1,0,0,1,0,1,0],
			 [0,0,0,0,0,1,0,0,1,0,0,0],
			 [0,0,0,0,0,0,0,0,0,0,0,0]]


imageTest = [[0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0],
			 [1,0,0,0,0,0,0,0],
			 [1,0,1,0,1,0,0,0],
			 [1,1,1,0,1,1,1,1],
			 [1,0,1,1,1,1,0,1]]



imageTest = [[0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,0,0,0],
			 [0,0,0,0,0,1,0,0],
			 [0,0,1,0,0,1,0,0],
			 [1,1,1,1,1,1,0,0],
			 [0,0,1,0,1,1,1,0]]
"""
# %% application classique
"""

#image = BinImage.BinImage(imageTest, False, True)
image = generation.randomImage(20)
image.show()

evol = Evolution.Evolution(image)

evol.simplify()

algo1(evol)

#print(evol.getNbActions())


"""
#%% analyse complexité

nbIter = 3
ns = [5,10,20,30,50,65]
value = []

for n in ns :
	listOfValues = []
	for i in range(nbIter) :
		print("generating...")
		image = generation.randomImage(n)
		evol = Evolution.Evolution(image)
		print("solving")
		algo1(evol)
		listOfValues.append(evol.getNbActions())
		print(n, " pixels : ", evol.getNbActions(), " actions.\n")
	value.append(sum(listOfValues) / nbIter)

plt.figure()

plt.xlabel('nb of pixels')
plt.ylabel('nb of exchanges')
plt.title('complexity of the first algorithm') 

plt.plot(ns, value)
plt.show()


# %% test génération
"""
t = time.time()
image = generation.randomImage(50)
print ("temps de génération : ", time.time()-t)
image.show()
"""