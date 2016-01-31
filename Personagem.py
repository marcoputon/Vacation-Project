#!/usr/bin/python
import pygame
from pygame.locals import *
from Colidivel import *

MAXa = 25
timer = 2

class Personagem(Colidivel):
	def __init__(self, x, y, w, h, img):
		Colidivel.__init__(self, x, y, w, h)
		self.img = img
		
		
	def draw(self, surface):
		pygame.draw.rect(surface, (255, 100, 0), (self.x, self.y, self.w, self.h))
