#!/usr/bin/python

import pygame
from Classes import *
from pygame.locals import *


#	Variaveis globais
vol = 50

class configMenuItem(menuItem):
	def __init__(self, x, y, w, h, text, size, color, value):
		menuItem.__init__(self, x, y, w, h, text, size, color)
		self.value = value
		
	def draw(self, surface):
		pygame.draw.rect(surface, (0, 0, 0), self.ret)
		font = pygame.font.Font(None, self.s)
		text = font.render(self.t + str(self.value), 1, self.c)
		textpos = (self.x + 15, (self.y + (self.h / 2) - (self.s / 2)))
		surface.blit(text, textpos)
			
	def update(self, x, y, value):
		self.x = x
		self.y = y
		self.ret = pygame.Rect(self.x, self.y, self.w, self.h)
		self.value = value
		
class configMenu():
	def __init__(self, itens, posFirst, intervalo):
		
		global vol
		self.selected = 1
		self.itens = itens
		a = 0
		for i in self.itens:
			i.update(posFirst[0], i.y + a + intervalo, "")
			a += posFirst[1]
		
	def draw(self, surface):
		for i in self.itens:
			i.draw(surface)
			
		r = self.itens[self.selected - 1]
		pygame.draw.rect(surface, (255, 255, 255), (r.x-5, r.y-5, r.w+10, r.h+10), 5)


def main():
	global vol
	direction = {"up":False, "down":False, "left":False, "right":False}
	
	# Initialise screen
	pygame.init()
	screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
	pygame.display.set_caption('Game')

	# Fill background
	background = pygame.Surface(screen.get_size())
	background = background.convert()
	background.fill((0, 0, 0))
	
	'''
	# Display some text
	font = pygame.font.Font(None, 36)
	text = font.render("Hello There", 1, (10, 10, 10))
	textpos = text.get_rect()
	textpos.centerx = background.get_rect().centerx
	background.blit(text, textpos)
	'''
	
	# Blit everything to the screen
	screen.blit(background, (0, 0))
	pygame.display.flip()
	
	#	Menu principal
	lt = []
	lt.append(menuItem(100, 100, 200, 50, "Jogar", 22, (255, 255, 255)))
	lt.append(menuItem(100, 100, 200, 50, "Tutorial", 22, (255, 255, 255)))
	lt.append(menuItem(100, 100, 200, 50, "Configurar", 22, (255, 255, 255)))
	lt.append(menuItem(100, 100, 200, 50, "Sair", 22, (255, 255, 255)))
	m = menu(lt, (30, 100), 20)
	op = 0
	
	#	Menu de configuracoes
	lt = []
	lt.append(configMenuItem(100, 100, 200, 50, "Volume", 22, (255, 255, 255), ": " + str(vol)))
	cm = configMenu(lt, (30, 100), 10)
	#cop = 0
	
	
	#	Loop do menu
	while 1:
		for event in pygame.event.get():
			if event.type == QUIT:
				return
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					return
					
				if event.key == pygame.K_DOWN:
					m.selected += 1
					if m.selected > len(m.itens):
						m.selected = 1
						
				if event.key == pygame.K_UP:
					m.selected -= 1
					if m.selected < 1:
						m.selected = len(m.itens)
				
				if event.key == pygame.K_RETURN:
					if m.selected == len(m.itens):
						return
					if m.selected == 1:
						op = 1
					elif m.selected == 2:
						op = 2
					elif m.selected == 3:
						op = 3
					
			if event.type == pygame.KEYUP:
				pass
		
		background.fill((0, 0, 0))
		m.draw(background)
		screen.blit(background, (0, 0))
		pygame.display.flip()
		
		#	Loop do jogo
		while op == 1:
			for event in pygame.event.get():
				if event.type == QUIT:
					return
					
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						op = 0
						break
					if event.key == pygame.K_DOWN:
						pass
					if event.key == pygame.K_UP:
						pass
					if event.key == pygame.K_RETURN:
						pass				
				if event.type == pygame.KEYUP:
					pass
		
			background.fill((0, 150, 0))
			screen.blit(background, (0, 0))
			pygame.display.flip()
		
		#	Loop do tutorial
		while op == 2:
			for event in pygame.event.get():
				if event.type == QUIT:
					return
					
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						op = 0
						break
					if event.key == pygame.K_DOWN:
						pass
					if event.key == pygame.K_UP:
						pass
					if event.key == pygame.K_RETURN:
						pass				
				if event.type == pygame.KEYUP:
					pass
		
			background.fill((0, 0, 200))
			screen.blit(background, (0, 0))
			pygame.display.flip()
		
		
		#	Loop de configuracoes
		v = 0
		while op == 3:
			for event in pygame.event.get():
				if event.type == QUIT:
					return
					
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_ESCAPE:
						op = 0
						break
						
					if event.key == pygame.K_DOWN:
						cm.selected += 1
						if cm.selected > len(cm.itens):
							cm.selected = 1		
					if event.key == pygame.K_UP:
						cm.selected -= 1
						if cm.selected < 1:
							cm.selected = len(cm.itens)
							
					if event.key == pygame.K_LEFT:
						if cm.selected == 1:
							v = -1
					
					if event.key == pygame.K_RIGHT:
						if cm.selected == 1:
							v = 1
								
				if event.type == pygame.KEYUP:
					if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
						v = 0
			
			vol += v
			if vol > 100:
				vol = 100
			elif vol < 0:
				vol = 0
				
			cm.itens[0].update(cm.itens[0].x, cm.itens[0].y, ": " + str(vol) + "%")
		
			background.fill((150, 0, 0))
			cm.draw(background)
			screen.blit(background, (0, 0))
			pygame.display.flip()


if __name__ == '__main__': main()
