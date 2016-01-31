#!/usr/bin/python
import pygame
from pygame.locals import *


class Colidivel():
	def __init__(self, x, y, w, h):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.c = [0, 0, 0, 0]
		
	def colide(self, c):
		eu = Rect(self.x, self.y, self.w, self.h)
		ele = Rect(c.x, c.y, c.w, c.h)
		if not eu.colliderect(ele):
			return False
		
		if ele.collidepoint((eu.x, eu.y + eu.h)):
			self.c[3] = 1
		if ele.collidepoint((eu.x + eu.w, eu.y + eu.h)):
			self.c[2] = 1
		if ele.collidepoint((eu.x + w, eu.y)):
			self.c[1] = 1
		if ele.collidepoint((eu.x, eu.y)):
			self.c[0] = 1
		return True
	
	def update(self, x, y):
		self.x += x
		self.y += y
	
	def setpPos(self, x, y):
		self.x = x
		self.y = y
	
	def draw(self, surface):
		pass

	def resetColisao(self):
		self.c = [0, 0, 0, 0]
