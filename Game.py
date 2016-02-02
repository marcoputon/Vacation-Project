#! /usr/bin/python

import pygame
from pygame import *
from Player import *
from Entity import *
from ExitBlock import *
from Platform import *
from InvisibleStone import *

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
	level = [
		"PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP",
		"P       IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIP",
		"P       IIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIIP",
		"P       PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPIP",
		"P       PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPIP",
		"P                                                              P",
		"P                                                              P",
		"P                                                              P",
		"P    IIPPPPPP                                                  P",
		"P                                                              P",
		"P                IIIPPPPPPP                                    P",
		"P          PPPP                                                P",
		"P                                             PPPPPP           P",
		"P                                                              P",
		"P                  IIPPPPPPI                                   P",
		"P                                                    FFFF      P",
		"P                                    IIIII         FFFFFFFF    P",
		"P   PPPPPPPPPPP                                    FFFFFFFFF   P",
		"P                                                   FFFFFFF    P",
		"P                 PPPPPPPPPPP                          M       P",
		"P       IIIIII                                         M       P",
		"P       IIIIII                                         M       P",
		"P       IIIIII                                         M       P",
		"PGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGGG P",
		"PTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT P",
		"PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPEP",]
	# build the level
	for row in level:
		for col in row:
			if col == "E":
				e = ExitBlock(x, y)
				platforms.append(e)
				entities.add(e)
			elif col == "I":
				e = InvisibleStone(x, y, col)
				platforms.append(e)
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

	while 1:
		timer.tick(60)

		for e in pygame.event.get():
			if e.type == QUIT: 
				raise SystemExit
			if e.type == KEYDOWN and e.key == K_ESCAPE:
				raise SystemExit
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

		# update player, draw everything else
		player.update(up, down, left, right, running, platforms)
		for e in entities:
			if isinstance(e, Platform):
				e.draw(screen, camera.apply(e))
			else:
				screen.blit(e.image, camera.apply(e))

		pygame.display.update()

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


if __name__ == "__main__":
	main()
