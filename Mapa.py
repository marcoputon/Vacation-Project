#!/usr/bin/python
import pygame
from pygame.locals import *

class Mapa():
	def __init__(self, m, n, blockSize, x, y, bg):
		self.matriz = []
		self.bs = blockSize
		self.pos = (x, y)
		self.bg = bg
		
		linha = []
		for i in range(n):
			for j in range(m):
				linha.append(0)
			self.matriz.append(linha)
			linha = []
		
	def mostraMatriz(self):
		for i in self.matriz:
			for j in i:
				print(j, end="")
			print()
	
	def pintaLinha(self, l, v):
		nl = []
		for i in range(len(self.matriz[l])):
			nl.append(pygame.image.load("_Imagens/" + v))
		self.matriz[l] = nl
	
	def pintaColuna(self, c, v):
		nc = []
		for i in range(len(self.matriz)):
			self.matriz[i][c] = pygame.image.load("_Imagens/" + v)
				
	def pinta(self, l, c, v):
		self.matriz[l][c] = pygame.image.load("_Imagens/" + v)
	
	
	def draw(self, surface):
		x = self.pos[0]
		y = self.pos[1]
		bs = self.bs

		surface.blit(self.bg, (0, surface.get_size()[1] - self.bg.get_size()[1]))
		self.pintaLinha(len(self.matriz)-1, "terra.jpg")
		for i in self.matriz:
			for j in i:
				try:
					surface.blit(j, (x, y))
					x += bs
				except:
					pass
			x = self.pos[0]
			y += bs
