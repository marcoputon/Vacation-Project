#! /usr/bin/python

import pygame
from pygame import *
from Entity import *
from Platform import *


class InvisibleStone(Platform):
	def __init__(self, x, y, t):
		Platform.__init__(self, x, y, t)
		self.colidindo = False
		
	def draw(self, screen, camera):
		
		
		if self.colidindo:
			pass
		else:
			screen.blit(self.image, camera)
			
		self.colidindo = False
