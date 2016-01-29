#!/usr/bin/python
import pygame
from pygame.locals import *

class menuItem():
	def __init__(self, x, y, w, h, text, size, color):
		self.t = text
		self.c = color
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.s = size
		self.ret = pygame.Rect(x, y, w, h)
		
	def draw(self, surface):
		pygame.draw.rect(surface, (0, 0, 0), self.ret)
		font = pygame.font.Font(None, self.s)
		text = font.render(self.t, 1, self.c)
		textpos = (self.x + 15, (self.y + (self.h / 2) - (self.s / 2)))
		surface.blit(text, textpos)
		
	def update(self, x, y):
		self.x = x
		self.y = y
		self.ret = pygame.Rect(self.x, self.y, self.w, self.h)


class menu():
	def __init__(self, itens, posFirst, intervalo):
		self.selected = 1
		self.itens = itens
		a = 0
		for i in self.itens:
			i.update(posFirst[0], i.y + a + intervalo)
			a += posFirst[1]
		
	def draw(self, surface):
		for i in self.itens:
			i.draw(surface)
			
		r = self.itens[self.selected - 1]
		pygame.draw.rect(surface, (255, 255, 255), (r.x-5, r.y-5, r.w+10, r.h+10), 5)
		
		
		
		
		
