#!/usr/bin/python
import pygame
from pygame.locals import *
from Colidivel import *
from Bloco import *

class Mapa():
	def __init__(self, m, n, blockSize, x, y, bg):
		self.matriz = []
		self.bs = blockSize
		self.pos = (x, y)
		self.bg = bg
		
		linha = []
		for i in range(n):
			for j in range(m):
				linha.append(Colidivel(-100, -100, 50, 50))
			self.matriz.append(linha)
			linha = []
		
	def mostraMatriz(self):
		for i in self.matriz:
			for j in i:
				print(j, end="")
			print()
	
	def pintaLinha(self, l, v):
		nl = []
		t = 0
		for i in range(len(self.matriz[l])):
			nl.append(Bloco(t * 50, l * 50, 50, pygame.image.load("_Imagens/" + v)))
			t += 1
		self.matriz[l] = nl
	
	def pintaColuna(self, c, v):
		nc = []
		t = 0
		for i in range(len(self.matriz)):
			self.matriz[i][c] = Bloco(c * 50, t * 50, 50, pygame.image.load("_Imagens/" + v))
			t += 1
			
	def pinta(self, l, c, v):
		self.matriz[l][c] = pygame.image.load("_Imagens/" + v)
	
	
	def draw(self, surface):
		x = self.pos[0]
		y = self.pos[1]
		bs = self.bs

		surface.blit(self.bg, (0, surface.get_size()[1] - self.bg.get_size()[1]))
		self.pintaLinha(len(self.matriz)-1, "terra.jpg")
		self.pintaColuna(0, "terra.jpg")
		for i in self.matriz:
			for j in i:
				j.draw(surface)
	def getBlocos(self):
		l = []
		for i in self.matriz:
			for j in i:
				l.append(j)
		return l
