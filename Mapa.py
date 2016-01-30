#!/usr/bin/python
import pygame
from pygame.locals import *

class Mapa():
	def __init__(self, m, n, blockSize, x, y):
		self.matriz = []
		self.bs = blockSize
		self.pos = (x, y)
		
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
			nl.append(v)
		self.matriz[l] = nl
	
	def pintaColuna(self, c, v):
		nc = []
		for i in range(len(self.matriz)):
			self.matriz[i][c] = v
				
	def pinta(self, l, c, v):
		self.matriz[l][c] = v
	
	
	def draw(self, surface):
		x = self.pos[0]
		y = self.pos[1]
		bs = self.bs
		m = 1
		
		for i in self.matriz:
			for j in i:
				pygame.draw.rect(surface, (255, 255, 255), (x, y, bs, bs))
				x += bs + m
			x = self.pos[0]
			y += bs + m

