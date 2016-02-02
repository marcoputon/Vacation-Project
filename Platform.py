#! /usr/bin/python

import pygame
from pygame import *
from Entity import *


class Platform(Entity):
	def __init__(self, x, y, t):
		Entity.__init__(self)
		if t == "E":
			t = "Exit.jpg"
		elif t == "P":
			t = "Pedra.jpg"
		elif t == "T":
			t = "Terra.jpg"
		elif t == "M":
			t = "Madeira.jpg"
		elif t == "F":
			t = "Folha.jpg"
		elif t == "G":
			t = "Grama.jpg"
		elif t == "I":
			t = "Pedra.jpg"
		
		self.image = pygame.image.load("_Imagens/" + t)
		self.rect = Rect(x, y, 32, 32)

	def draw(self, screen, camera):
		screen.blit(self.image, camera)
		
