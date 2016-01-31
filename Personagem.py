#!/usr/bin/python
import pygame
from pygame.locals import *
from Colidivel import *

G = 1
MAXa = 25
timer = 2

class Personagem(Colidivel):
	def __init__(self, x, y, w, h, img):
		Colidivel.__init__(self, x, y, w, h)
		self.img = img
		self.acel = 1
		self.t = 1
		self.direction = [0, 0]

	def draw(self, surface):
		pygame.draw.rect(surface, (255, 100, 0), (self.x, self.y, self.w, self.h))
		print(self.direction)
		
	def update(self, x, y):
		#	Seta a direcao que o personagem esta se movimentando
		if y + self.acel > 0:
			self.direction[1] = 1
		elif y + self.acel == 0:
			self.direction[1] = 0
		else:
			self.direction[1] = -1
			
		self.x += x
		self.y += y + self.acel
		self.t += 1
		
		if self.t == timer:	
			self.acel += G
			self.t = 1
		if self.acel > MAXa:
			self.acel = MAXa
