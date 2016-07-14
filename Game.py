#!/usr/bin/python3

from pygame import *
from Player import *
from Entity import *
from ExitBlock import *
from Platform import *
from InvisibleStone import *
from Menu import *
from Exceptions import *
from Seta import *

pygame.display.init()
window = pygame.display.Info()

WIN_WIDTH = int(window.current_w/32)*32
WIN_HEIGHT = int(window.current_h/32)*32 - 64
HALF_WIDTH = int(WIN_WIDTH / 2)
HALF_HEIGHT = int(WIN_HEIGHT / 2)

DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
DEPTH = 32
FLAGS = 0
CAMERA_SLACK = 30

def main():
	global cameraX, cameraY
	pygame.init()
	screen = pygame.display.set_mode(DISPLAY, FLAGS, DEPTH)
	pygame.display.set_caption("Use arrows to move!")
	timer = pygame.time.Clock()

	up = down = left = right = running = False
	bg = Surface((32,32))
	bg.convert()
	bg.fill(Color("#8888ff"))
	entities = pygame.sprite.Group()
	player = Player(32, 32)
	platforms = []

	x = y = 0
	
	#	Menu 1
	lt = []
	lt.append(menuItem(100, 100, 200, 50, "Jogar", 22, (255, 255, 255)))
	lt.append(menuItem(100, 100, 200, 50, "Tutorial", 22, (255, 255, 255)))
	lt.append(menuItem(100, 100, 200, 50, "Sair", 22, (255, 255, 255)))
	m = menu(lt, (30, 100), 20)
	op = 0
	
	fases = loadLevels("fases.txt")
	
	#	Menu 2
	lt = []
	for i in fases:
		lt.append(menuItem(100, 100, 200, 50, i[1], 22, (255, 255, 255)))
	m2 = menu(lt, (30, 100), 20)
	op2 = 0
	
	
	while True:
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
					op = m.selected
		
		screen.fill(Color("#8888ff"))
		m.draw(screen)
		pygame.display.update()
	
		while op == 1:
			while op == 1:
				for event in pygame.event.get():
					if event.type == QUIT:
						return
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_ESCAPE:
							op = 0
						
						if event.key == pygame.K_DOWN:
							m2.selected += 1
							if m2.selected > len(m2.itens):
								m2.selected = 1
						
						if event.key == pygame.K_UP:
							m2.selected -= 1
							if m2.selected < 1:
								m2.selected = len(m2.itens)
						
						if event.key == pygame.K_RETURN:
							op2 = m2.selected
				
				screen.fill(Color("#8888ff"))
				m2.draw(screen)
				pygame.display.update()
				
				if op2:
					c = 1
					for i in fases:
						if c == op2:
							level = i[0]
						c += 1
					
					x = 0
					y = 0
					# build the level
					for row in level:
						for col in row:
							if col == "J":
								player.rect.left = x
								player.rect.top = y
							
							elif col == "E":
								e = ExitBlock(x, y)
								platforms.append(e)
								entities.add(e)
							elif col == "I":
								e = InvisibleStone(x, y, col)
								platforms.append(e)
								entities.add(e)
							elif col in "<>^v[]-_":
								if col in "<>^v": move = False
								else: move = True
								
								if col in "<[":
									e = Seta(x, y, "left", move)
								elif col in ">]":
									e = Seta(x, y, "right", move)
								if col in "^-":
									e = Seta(x, y, "up", move)
								if col in "v_":
									e = Seta(x, y, "down", move)
								entities.add(e)
							
							elif not (col == " ") :
								p = Platform(x, y, col)
								platforms.append(p)
								entities.add(p)
							x += 32
						y += 32
						x = 0

					total_level_width  = len(level[0])*32
					total_level_height = len(level)*32
					camera = Camera(complex_camera, total_level_width, total_level_height)
					entities.add(player)
					
					jogando = True
					fase = zera = False
					while jogando:
						timer.tick(30)

						for e in pygame.event.get():
							if e.type == QUIT: 
								raise SystemExit
							if e.type == KEYDOWN and e.key == K_ESCAPE:
								zera = True
								break
								
							if e.type == KEYDOWN and e.key == K_UP:
								up = True
							if e.type == KEYDOWN and e.key == K_DOWN:
								down = True
							if e.type == KEYDOWN and e.key == K_LEFT:
								left = True
							if e.type == KEYDOWN and e.key == K_RIGHT:
								right = True
							if e.type == KEYDOWN and e.key == K_SPACE:
								running = True

							if e.type == KEYUP and e.key == K_UP:
								up = False
							if e.type == KEYUP and e.key == K_DOWN:
								down = False
							if e.type == KEYUP and e.key == K_RIGHT:
								right = False
							if e.type == KEYUP and e.key == K_LEFT:
								left = False

						# draw background
						for y in range(int(WIN_HEIGHT/32)):
							for x in range(int(WIN_WIDTH/32)):
								screen.blit(bg, (x * 32, y * 32))
						
						camera.update(player)
						
						# update player, draw everything else, end level
						try:
							player.update(up, down, left, right, running, platforms)
						except CompleteLevel as cl:
							fase = True
						
						for e in entities:
							if isinstance(e, Seta):
								e.update()
							if isinstance(e, Platform):
								e.draw(screen, camera.apply(e))
							else:
								screen.blit(e.image, camera.apply(e))
						
						#	Manter o player "por cima"
						screen.blit(player.image, camera.apply(player))
						
						pygame.display.update()
						
						if fase:
							pygame.draw.rect(screen, (0, 0, 0), Rect(HALF_WIDTH/2, HALF_HEIGHT/2, HALF_WIDTH, HALF_HEIGHT))
							font = pygame.font.Font(None, 40)
							text = font.render("Fase concluida", 1, (255, 255, 255))
							textpos = (HALF_WIDTH/2 + 50, HALF_HEIGHT/2 + 50)
							screen.blit(text, textpos)
							font = pygame.font.Font(None, 24)
							text = font.render("Pressione qualquer tecla para continuar", 1, (255, 255, 255))
							textpos = (HALF_WIDTH/2 + 50, HALF_HEIGHT/2 + 120)
							screen.blit(text, textpos)
							pygame.display.update()
							
							continuar = False
							while not continuar:
								for e in pygame.event.get():
									if e.type == KEYDOWN: 
										continuar = True
										zera = True				
						if zera:			
							jogando = False
							op2 = 0
							up = down = left = right = running = False
							entities = pygame.sprite.Group()
							player = Player(32, 32)
							platforms = []
							break

		#	Loop do tutorial	
		while op == 2:
			while op == 2:
				level = loadLevels("Tutorial.txt")[0][0]
				x = 0
				y = 0
				# build the level
				for row in level:
					for col in row:
						if col == "J":
							player.rect.left = x
							player.rect.top = y
						
						elif col == "E":
							e = ExitBlock(x, y)
							platforms.append(e)
							entities.add(e)
						elif col == "I":
							e = InvisibleStone(x, y, col)
							platforms.append(e)
							entities.add(e)
						elif col in "<>^v[]-_":
								if col in "<>^v": move = False
								else: move = True
								
								if col in "<[":
									e = Seta(x, y, "left", move)
								elif col in ">]":
									e = Seta(x, y, "right", move)
								if col in "^-":
									e = Seta(x, y, "up", move)
								if col in "v_":
									e = Seta(x, y, "down", move)
								entities.add(e)						
						elif not (col == " ") :
							p = Platform(x, y, col)
							platforms.append(p)
							entities.add(p)
						x += 32
					y += 32
					x = 0

				total_level_width  = len(level[0])*32
				total_level_height = len(level)*32
				camera = Camera(complex_camera, total_level_width, total_level_height)
				entities.add(player)
				
				jogando = True
				fase = zera = False
				
				c1 = Platform(64, 256, "caixa1.png")
				c2 = Platform(46*32, 256, "caixa2.png")
				
				while jogando:
					timer.tick(30)
					# (64, 256)
					
					
					for e in pygame.event.get():
						if e.type == QUIT: 
							raise SystemExit
						if e.type == KEYDOWN and e.key == K_ESCAPE:
							zera = True
							break
							
						if e.type == KEYDOWN and e.key == K_UP:
							up = True
						if e.type == KEYDOWN and e.key == K_DOWN:
							down = True
						if e.type == KEYDOWN and e.key == K_LEFT:
							left = True
						if e.type == KEYDOWN and e.key == K_RIGHT:
							right = True
						if e.type == KEYDOWN and e.key == K_SPACE:
							running = True

						if e.type == KEYUP and e.key == K_UP:
							up = False
						if e.type == KEYUP and e.key == K_DOWN:
							down = False
						if e.type == KEYUP and e.key == K_RIGHT:
							right = False
						if e.type == KEYUP and e.key == K_LEFT:
							left = False

					# draw background
					for y in range(int(WIN_HEIGHT/32)):
						for x in range(int(WIN_WIDTH/32)):
							screen.blit(bg, (x * 32, y * 32))
					
					camera.update(player)
					
					# update player, draw everything else, end level
					try:
						player.update(up, down, left, right, running, platforms)
					except CompleteLevel as cl:
						fase = True
					
					c1.draw(screen, camera.apply(c1))
					c2.draw(screen, camera.apply(c2)) 
					
					for e in entities:
						if isinstance(e, Seta):
							e.update()
						if isinstance(e, Platform):
							if camera.apply(e).colliderect(Rect(0, 0, WIN_WIDTH, WIN_HEIGHT)):
								e.draw(screen, camera.apply(e))
						else:
							screen.blit(e.image, camera.apply(e))
							
					screen.blit(player.image, camera.apply(player))
					pygame.display.update()
					
					if fase:
						pygame.draw.rect(screen, (0, 0, 0), Rect(HALF_WIDTH/2, HALF_HEIGHT/2, HALF_WIDTH, HALF_HEIGHT))
						font = pygame.font.Font(None, 40)
						text = font.render("Fase concluida", 1, (255, 255, 255))
						textpos = (HALF_WIDTH/2 + 50, HALF_HEIGHT/2 + 50)
						screen.blit(text, textpos)
						font = pygame.font.Font(None, 24)
						text = font.render("Pressione qualquer tecla para continuar", 1, (255, 255, 255))
						textpos = (HALF_WIDTH/2 + 50, HALF_HEIGHT/2 + 120)
						screen.blit(text, textpos)
						pygame.display.update()
						
						continuar = False
						while not continuar:
							for e in pygame.event.get():
								if e.type == KEYDOWN: 
									continuar = True
									zera = True
					
					if zera:			
						jogando = False
						op = 0
						up = down = left = right = running = False
						entities = pygame.sprite.Group()
						player = Player(32, 32)
						platforms = []
						break
	

class Camera(object):
	def __init__(self, camera_func, width, height):
		self.camera_func = camera_func
		self.state = Rect(0, 0, width, height)

	def apply(self, target):
		return target.rect.move(self.state.topleft)

	def update(self, target):
		self.state = self.camera_func(self.state, target.rect)

def simple_camera(camera, target_rect):
	l, t, _, _ = target_rect
	_, _, w, h = camera
	return Rect(-l+HALF_WIDTH, -t+HALF_HEIGHT, w, h)

def complex_camera(camera, target_rect):
	l, t, _, _ = target_rect
	_, _, w, h = camera
	l, t, _, _ = -l+HALF_WIDTH, -t+HALF_HEIGHT, w, h

	l = min(0, l)                           # stop scrolling at the left edge
	l = max(-(camera.width-WIN_WIDTH), l)   # stop scrolling at the right edge
	t = max(-(camera.height-WIN_HEIGHT), t) # stop scrolling at the bottom
	t = min(0, t)                           # stop scrolling at the top
	return Rect(l, t, w, h)
	
def loadLevels(arquivo):
	levels = []
	level = []
	arquivo = open(arquivo, "r")
	fases = arquivo.readlines()
	f = False
	nome = ""
	for i in fases:
		if i[0] == '#':
			continue
		if "nome" in i:
			nome = i[6:len(i)-1]
			f = True
			continue
		if	f:
			i = i[0:len(i)-1]
			if i != "":
				level.append(i)
			else:
				levels.append([level, nome])
				level = []
				f = False
	levels.append([level, nome])
	return levels

if __name__ == "__main__":
	main()
