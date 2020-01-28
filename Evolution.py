# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 08:19:16 2019

@author: nbarl
"""
from math import sqrt
from BinImage import BinImage
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from copy import deepcopy

class Evolution :
    """class representing the evolution of a binary image"""
    
    def __init__(self, image, actions=[]) :
        self.firstImage = deepcopy(image)
        self.currentImage = image
        self.actions = actions
        self.nbAction = 0
        for x in actions :
            self.currentImage.movePixel(x)
            self.nbAction += 1
            
    def addAction(self, i, j, direction) :
        self.actions.append((i,j,direction))
        self.currentImage.movePixel((i,j,direction))
        self.nbAction += 1
        
    def popAction(self) :
        if self.nbAction > 0 :
            act = self.actions.pop()
            self.currentImage.movePixel(act)
            self.nbAction -=1
            
    def createGif(self, name = 'dynamic_images.gif', speed = 500) :
        image = deepcopy(self.firstImage)
        M=image.image 
        
        def update(i):
            image.movePixel(self.actions[i-1])
            matrice.set_array(image.image)
            
        fig, ax = plt.subplots()
        matrice = ax.matshow(M, cmap=plt.cm.gray_r)
        
        ani = animation.FuncAnimation(fig, update, frames=len(self.actions)+1, interval=speed)
        ani.save(name)
        
    def dist(p1, p2) :
        return sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)
        
    def simplify(self) :
        if len(self.actions)==0 :
            return
        newList = [self.actions[0]]
        i = 1
        while i<len(self.actions) :
            lastAction = newList[-1]
            currentAction = self.actions[i]
            lastExchange = ( (lastAction[0],lastAction[1]) , self.currentImage.getNeighbourCoord(lastAction[0],lastAction[1],lastAction[2]) )
            currentExchange = ( (currentAction[0],currentAction[1]) , self.currentImage.getNeighbourCoord(currentAction[0],currentAction[1],currentAction[2]) )
            
            b1=-1
            if lastExchange[1]==currentExchange[0] :
               b1=0
               b2=1
            elif lastExchange[0]==currentExchange[0] :
                b1=1
                b2=1
            elif lastExchange[1]==currentExchange[1] :
                b1=0
                b2=0
            elif lastExchange[0]==currentExchange[1] :
                b1=1
                b2=0
                
            if b1!=-1 and Evolution.dist(lastExchange[b1], currentExchange[b2])<=sqrt(2) :
                newList.pop()
                newList.append((lastExchange[b1][0], lastExchange[b1][1], BinImage.getDirection(lastExchange[b1], currentExchange[b2])))
            else :
                newList.append(currentAction)
            i+=1
        self.actions = newList
        
    def getNbActions(self) :
        return len(self.actions)