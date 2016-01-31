#!/usr/bin/python
import pygame
from pygame.locals import *
from Colidivel import *


class Bloco(Colidivel):
	def __init__(self, x, y, size, img):
		Colidivel.__init__(self, x, y, size, size)
		self.img = img
		self.tipo = 0
		self.size = size

	def draw(self, surface):
		surface.blit(self.img, (self.x, self.y))
