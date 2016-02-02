#! /usr/bin/python

import pygame
from pygame import *
from Entity import *
from ExitBlock import *
from InvisibleStone import *


class Player(Entity):
	def __init__(self, x, y):
		Entity.__init__(self)
		self.xvel = 0
		self.yvel = 0
		self.onGround = False
		self.image = Surface((32,64))
		self.image.fill(Color("#0000FF"))
		self.image.convert()
		self.rect = Rect(x, y, 32, 64)

	def update(self, up, down, left, right, running, platforms):
		if up:
			# only jump if on the ground
			if self.onGround: self.yvel -= 15
		elif not self.onGround and self.yvel < 0:
			self.yvel += 0.6
		
		if down:
			pass
		if running:
			self.xvel = 12
		if left:
			self.xvel = -8
		if right:
			self.xvel = 8
		if not self.onGround:
			self.yvel += 0.6
			if self.yvel > 90: self.yvel = 90
		if not(left or right):
			self.xvel = 0
		
		# increment in x direction
		self.rect.left += self.xvel
		# do x-axis collisions
		self.collide(self.xvel, 0, platforms)
		# increment in y direction
		self.rect.top += self.yvel
		# assuming we're in the air
		self.onGround = False;
		# do y-axis collisions
		self.collide(0, self.yvel, platforms)

	def collide(self, xvel, yvel, platforms):
		for p in platforms:
			if pygame.sprite.collide_rect(self, p):
				if isinstance(p, ExitBlock):
					pygame.event.post(pygame.event.Event(QUIT))
					print("Voce achou a saida!")
				
				if isinstance(p, InvisibleStone):
					p.colidindo = True
					continue
				
				if xvel > 0:
					self.rect.right = p.rect.left
				if xvel < 0:
					self.rect.left = p.rect.right
				if yvel > 0:
					self.rect.bottom = p.rect.top
					self.onGround = True
					self.yvel = 0
				if yvel < 0:
					self.rect.top = p.rect.bottom
					self.yvel = 0