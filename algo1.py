# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 15:36:20 2020

@author: nbarl
"""

from BinImage import Direction
from Evolution import Evolution
import time

def ksingular(image) :
	"""gives the max k so that the image is k-singular"""
	towers = [0]*image.m
	k=0
	while k<image.n :
		
		#get ligne k
		l = image.image[k]
		
		empty = True
		isTowers = False
		for i in range(image.m) :
			if l[i]==1 :
				empty = False
				break
			if towers[i]==1:
				isTowers = True
		
		if empty and  isTowers :
			return -1
			
		for i in range(image.m) :
			if towers[i]==1 and l[i]==0 :
				return k-1
			if l[i]==1 :
				if i<image.m-1 and l[i+1]==1 :
					return k-1
				towers[i]=1
				
		k+=1
		

def combineTowers(evol,k,a,b) :
	"""combine tower in a with tower in b in the same bloc row k, at position a and b"""
	if a==b :
		return
	
	#get summits
	sa=k
	while sa-1>=0 and evol.currentImage.getPixel(sa-1,a)==1 :
		sa-=1
	sb=k
	while sb-1>=0 and evol.currentImage.getPixel(sb-1,b)==1 :
		sb-=1
	
	
	if a<b : #if we bo right throught left
		if b-a==1 : #if the towers touch each other
			while sa<sb-1 :
				evol.addAction(sa,a,Direction.DownRight)
				for i in range(1, sb-sa-1) :
					evol.addAction(sa+i,a+1, Direction.Down)
				sa+=1
				sb-=1
			if sa==sb-1 :
				evol.addAction(sa,a,Direction.Right)
				sa+=1
				sb-=1
			while sa<k :
				for i in range(sa-sb) :
					evol.addAction(sa-i,a, Direction.Up)
				evol.addAction(sb,a, Direction.UpRight)
				sa+=1
				sb-=1
				
		elif b-a==2 : #if just one space
			while sa<sb-1 :
				evol.addAction(sa,a,Direction.DownRight)
				for i in range(1, sb-sa-1) :
					evol.addAction(sa+i,a+1, Direction.Down)
				evol.addAction(sb-1,a+1, Direction.Right)
				sa+=1
				sb-=1
			if sa==sb-1 :
				evol.addAction(sa,a,Direction.Right)
				evol.addAction(sa,a+1,Direction.Right)
				sa+=1
				sb-=1
			while sa<k :
				evol.addAction(sa,a,Direction.Right)
				for i in range(sa-sb) :
					evol.addAction(sa-i,a+1, Direction.Up)
				evol.addAction(sb,a+1, Direction.UpRight)
				sa+=1
				sb-=1
				
		else : #general case
			while sa<k :
				#first move
				if sa==k-1 : evol.addAction(sa,a,Direction.Right)
				else : evol.addAction(sa,a,Direction.DownRight)
				#the middle moves
				for i in range(1, k-sa-1) :
					evol.addAction(sa+i,a+1, Direction.Down)
				for i in range(b-a-2) :
					evol.addAction(k-1,a+1+i, Direction.Right)
				for i in range(k-sb-1) :
					evol.addAction(k-1-i,b-1, Direction.Up)
				#last move
				if sb==k : evol.addAction(sb-1,b-1, Direction.Right)
				else : evol.addAction(sb,b-1, Direction.UpRight)
				sa+=1
				sb-=1
			
	else : #if we go left throught right
		if a-b==1 : #if the towers touch each other
			while sa<sb-1 :
				evol.addAction(sa,a,Direction.DownLeft)
				for i in range(1, sb-sa-1) :
					evol.addAction(sa+i,a-1, Direction.Down)
				sa+=1
				sb-=1
			if sa==sb-1 :
				evol.addAction(sa,a,Direction.Left)
				sa+=1
				sb-=1
			while sa<k :
				for i in range(sa-sb) :
					evol.addAction(sa-i,a, Direction.Up)
				evol.addAction(sb,a, Direction.UpLeft)
				sa+=1
				sb-=1
				
		elif a-b==2 : #if just one space
			while sa<sb-1 :
				evol.addAction(sa,a,Direction.DownLeft)
				for i in range(1, sb-sa-1) :
					evol.addAction(sa+i,a-1, Direction.Down)
				evol.addAction(sb-1,a-1, Direction.Left)
				sa+=1
				sb-=1
			if sa==sb-1 :
				evol.addAction(sa,a,Direction.Left)
				evol.addAction(sa,a-1,Direction.Left)
				sa+=1
				sb-=1
			while sa<k :
				evol.addAction(sa,a,Direction.Left)
				for i in range(sa-sb) :
					evol.addAction(sa-i,a-1, Direction.Up)
				evol.addAction(sb,a-1, Direction.UpLeft)
				sa+=1
				sb-=1
				
		else : #general case
			while sa<k :
				#first move
				if sa==k-1 : evol.addAction(sa,a,Direction.Left)
				else : evol.addAction(sa,a,Direction.DownLeft)
				#the middle moves
				for i in range(1, k-sa-1) :
					evol.addAction(sa+i,a-1, Direction.Down)
				for i in range(a-b-2) :
					evol.addAction(k-1,a-1-i, Direction.Left)
				for i in range(k-sb-1) :
					evol.addAction(k-1-i,b+1, Direction.Up)
				#last move
				if sb==k : evol.addAction(sb-1,b+1, Direction.Left)
				else : evol.addAction(sb,b+1, Direction.UpLeft)
				sa+=1
				sb-=1
	

def getBlocks(evol, k) :
	"""get the list of blocks (a start and an end) from row k"""
	row = evol.currentImage.image[k]
	inBlock = False
	result = []
	startIndex = 0
	for i in range(len(row)) :
		if (not inBlock) and row[i]==1 : #enter a block
			startIndex = i
			inBlock = True
		elif inBlock and row[i]==0 : #exit a block
			result.append((startIndex, i))
			inBlock = False
		# if in the midle of a block or between two blocks, do nothing
		
	if inBlock : #a block reaches the end
		result.append((startIndex, len(row)))
		inBlock = False
	return result


def getTowers(evol, k) :
	"""get the list of blocks of towers on row k"""
	row = evol.currentImage.image[k]
	towers = evol.currentImage.image[k-1]
	inBlock = False
	result = []
	currentBlock = []
	for i in range(len(row)) :
		if (not inBlock) and row[i]==1 : #enter a block
			inBlock = True
		elif inBlock and row[i]==0 : #exit a block
			inBlock = False
			result.append(currentBlock)
			currentBlock = []
		
		if towers[i]==1:
			currentBlock.append(i)
		
	if inBlock : #a block reaches the end
		inBlock = False
		result.append(currentBlock)
	return result


def combineBlockTowers(evol, k, block) :
	"""combine all the towers in block, at row k"""
	for i in range(len(block)-1) :
		combineTowers(evol, k, block[i], block[i+1])
		
def towerize(evol, k) :
	"""combine the towers on a row, so there is at most one tower per block. Returns the runs on row k+1, and the position of the tower. If no tower, position -1."""
	res = []
	towers = getTowers(evol, k+1)
	runs = getBlocks(evol, k+1)
	for i in range(len(runs)) :
		if len(towers[i])>0 :
			combineBlockTowers(evol, k+1, towers[i])
			res.append((runs[i][0], runs[i][1], towers[i][-1]))
		else :
			res.append((runs[i][0], runs[i][1], runs[i][1]-1))
	return res


def getContacts(evol, runs1, runs2) :
	"""create a list telling wich run of runs2 is in contact with each run of runs1"""
	res = []
	for r in runs1 :
		l = []
		start = r[0]
		end = r[1]
		for i in range(len(runs2)) :
			s=runs2[i]
			if s[0]<=end and s[1]>=start : #contact with r
				l.append(i)
		res.append(l)
	return res


def step2(evol,k) :
	"""proposition 2 of the article"""
	runs1 = towerize(evol, k)
	runs2 = getBlocks(evol, k+2)
	contacts = getContacts(evol, runs1, runs2)
	for i in range(len(runs1)) :
		r = runs1[i]
		contactsR = contacts[i]
		towerPos = r[2]
		
		if len(contactsR)==0 :
			combineTowers(evol, k+1, towerPos, r[1]-1)
			for j in range(r[0], r[1]-1) :
				evol.addAction(k+1, j, Direction.Up)
				combineTowers(evol, k+1, j, r[1]-1)
			
		elif len(contactsR)==1 :
			s = runs2[contactsR[0]]
			#move the tower above s
			for ind in range(s[0], s[1]) :
				if ind>=r[0] and ind<r[1] :
					break
			combineTowers(evol, k+1, towerPos, ind)
			for j in range(r[0], ind) :
				evol.addAction(k+1, j, Direction.Up)
				combineTowers(evol, k+1, j, ind)
			for j in range(r[1]-1, ind, -1) :
				evol.addAction(k+1, j, Direction.Up)
				combineTowers(evol, k+1, j, ind)
				
		else :
			#combine the ends of r whith the tower, so that there is only one pixel of connection left
			s1 = runs2[contactsR[0]]
			sm = runs2[contactsR[-1]]
			#move the tower if necessary
			combineTowers(evol, k+1, towerPos, sm[0])
			towerPos = sm[0]
				
			for j in range(r[0], s1[1]-1) :
				evol.addAction(k+1, j, Direction.Up)
				combineTowers(evol, k+1, j, towerPos)
			for j in range(r[1]-1, sm[0], -1) :
				evol.addAction(k+1, j, Direction.Up)
				combineTowers(evol, k+1, j, towerPos)
			
			
			#parcours des s en contact avec r
			for ind in contactsR[1:-1] : #remove the ends
				si = runs2[ind]
				
				if si[1]-si[0] >= 3 :
					#separate s in 2
					for j in range(si[0]+1, si[1]-1) :
						evol.addAction(k+1, j, Direction.Up)
						combineTowers(evol, k+1, j, towerPos)
			
				elif si[1]-si[0] ==2 :
					#2 cas, si espace de 1 avant ou non
					sinf = runs2[ind-1]
					ssup = runs2[ind+1]
					print("non fini")
					"""
					if si[0]-sinf[1] == 1 :
						evol.addAction(k+1, si[0]-1, Direction.Down)
					elif ssup[0]-si[1] == 1 :
						evol.addAction(k+1, si[1], Direction.Down)
					else :"""
	

def createHole(evol, i, j) :
	"""tesls if moving the pixel (i,j) to the down right creates a hole (necessary for step3)"""
	return False


def step3(evol, k) :
	"""proposition 3 of the article"""
	runs1 = towerize(evol, k)
	for i in range(len(runs1)) :
		r = runs1[i]
		if r[1]-r[0]>1 : #if r is a singleton, we have nothing to do
			ris = []
			for j in range(r[0], r[1]) :
				if evol.currentImage.getPixel(k+2, j)==1 :
					ris.append(j);
			#here, ris contains the pixels of r that are in contact with row k+2
			#now we move the tower to the extrem right
			combineTowers(evol, k+1, r[2], r[1]-1)
			#we consider the sub-run from ri to ri+1 (excluded)
			for a in range(len(ris)-1) :
				for j in range(ris[a], ris[a+1]) :
					if not createHole(evol, k+1, j) : #if no hole is created 
						if evol.currentImage.getPixel(k+2, j+1)==0 :
							evol.addAction(k+1, j, Direction.DownRight)
						else :
							evol.addAction(k+1, j, Direction.Up)
							combineTowers(evol, k+1, j, r[1]-1)
	

def algo1(evol, name="algo1.gif", frame = 150) :
	t1 = time.time()
	k = ksingular(evol.currentImage)
	while k>0 :
		step2(evol, k)
		step3(evol, k)
		k = ksingular(evol.currentImage)
	
	t2 = time.time()
	print("algo : %f s" % (t2-t1))
	
	evol.simplify()
	t3 = time.time()
	print("simplify : %f s" % (t3-t2))
	
	evol.createGif(name, frame)
	t4 = time.time()
	print("gif creation : %f s" % (t4-t3))
				