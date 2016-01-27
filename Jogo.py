#!/usr/bin/python

import pygame
from Classes import *
from pygame.locals import *

def main():
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
	
	lt = []
	lt.append(menuItem(100, 100, 200, 50, "Jogar", 22, (255, 255, 255)))
	lt.append(menuItem(100, 100, 200, 50, "Tutorial", 22, (255, 255, 255)))
	lt.append(menuItem(100, 100, 200, 50, "Configurar", 22, (255, 255, 255)))
	lt.append(menuItem(100, 100, 200, 50, "Sair", 22, (255, 255, 255)))
	m = menu(lt, (30, 100), 20)
	op = 0
	
	# Loop do menu
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
		while op == 3:
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
		
			background.fill((150, 0, 0))
			screen.blit(background, (0, 0))
			pygame.display.flip()


if __name__ == '__main__': main()
