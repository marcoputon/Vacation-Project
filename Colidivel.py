#!/usr/bin/python
import pygame
from pygame.locals import *


class Colidivel():
	def __init__(self, x, y, w, h):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		
	def colide(self, c):
		try:
			eu = Rect(self.x, self.y, self.w, self.h)
			ele = Rect(c.x, c.y, c.w, c.h)
			if eu.colliderect(ele):
				print("Colidiu")
			else:
				print("Nao colidiu")
		except:
			print("A funcao 'colide' da classe 'colidivel' nao funcionou")