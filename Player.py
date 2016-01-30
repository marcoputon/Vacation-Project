#!/usr/bin/python
import pygame
from pygame.locals import *
from Personagem import *

class player(Personagem):
	def __init__(self, x, y, w, h, img):
		Personagem.__init__(self, x, y, w, h, img)
		
	def update(self, colidiveis):
		pass
