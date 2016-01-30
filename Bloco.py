#!/usr/bin/python
import pygame
from pygame.locals import *
from Colidivel import *


class Bloco(Colidivel):
	def __init__(self, x, y, size, img):
		Colidivel.__init__(self, x, y, size, size)
		self.img = img
		self.tipo = 0

	def draw(self, surface):
		pygame.draw.rect(surface, (255, 100, 0), (self.x, self.y, self.size, self.size))
		
	def update(self, x, y):
		self.x = x
		self.y = y
