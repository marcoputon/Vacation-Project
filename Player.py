#! /usr/bin/python3

import pygame
from pygame import *
from Entity import *
from ExitBlock import *
from InvisibleStone import *
from Exceptions import *

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
			if self.onGround: self.yvel -= 23
		elif not self.onGround and self.yvel < 0:
			self.yvel += 1.6
		
		if down:
			pass
		if running:
			self.xvel = 20
		if left:
			self.xvel = -15
		if right:
			self.xvel = 15
		if not self.onGround:
			self.yvel += 1.6
			if self.yvel > 270: self.yvel = 270
		if not(left or right):
			self.xvel = 0
		
		self.rect.left += self.xvel
		self.collide(self.xvel, 0, platforms)
		self.rect.top += self.yvel
		self.onGround = False
		self.collide(0, self.yvel, platforms)

	def collide(self, xvel, yvel, platforms):
		for p in platforms:
			if pygame.sprite.collide_rect(self, p):				
				if isinstance(p, InvisibleStone):
					p.colidindo = True
					if self.rect.y + self.rect.h-1 == p.rect.y:
						p.colidindo = False
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
				
				if isinstance(p, ExitBlock):
					raise CompleteLevel()
