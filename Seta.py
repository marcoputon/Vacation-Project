#! /usr/bin/python3

import pygame
from pygame import *
from Entity import *
import time

class Seta(Entity):
	def __init__(self, x, y, t, p):
		Entity.__init__(self)
		
		if t == "left":
			t = "Dir_left"
		elif t == "right":
			t = "Dir_right"
		elif t == "up":
			t = "Dir_up"
		elif t == "down":
			t = "Dir_down"
		self.p = p
		self.images = [pygame.image.load("_Imagens/teclas/" + t + ".png"), pygame.image.load("_Imagens/teclas/" + t + "0.png")]
		self.image = self.images[0]
		self.rect = Rect(x, y, 32, 32)
		self.TtB = time.clock()
		self.i = True

	def update(self):
		if self.p:
			if time.clock() - self.TtB >= 0.5:
				self.TtB = time.clock()
				self.i = not self.i
				if self.i:
					self.image = self.images[0]
				else:
					self.image = self.images[1]
				
	def draw(self, screen, camera):
		screen.blit(self.image, camera)
		
