#!/usr/bin/python
import pygame
from pygame.locals import *
from Personagem import *

class Player(Personagem):
	def __init__(self, x, y, w, h, img):
		Personagem.__init__(self, x, y, w, h, img)
		
