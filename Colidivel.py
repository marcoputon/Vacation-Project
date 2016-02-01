#!/usr/bin/python
import pygame
from pygame.locals import *

'''
	A funcao update foi baseada no codigo encontrado no link:
		http://stackoverflow.com/questions/14354171/add-scrolling-to-a-platformer-in-pygame
	que eu encontrei no video:
		https://www.youtube.com/watch?v=bxibfL4TjWo&list=PL2K8-kPw3uPOTpfk-LJM-yvzSQB88hFYf
'''

class Colidivel():
	def __init__(self, x, y, w, h):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.xvel = 0
		self.yvel = 0
		self.onGround = False
		
	def colide(self, c):
		eu = Rect(self.x, self.y, self.w, self.h)
		ele = Rect(c.x, c.y, c.w, c.h)
		return eu.colliderect(ele) 
	
	def collide(self, xvel, yvel, platforms):
		for p in platforms:
			if self.colide(p):
				#	Aqui acontece umas magias negras das trevas e do ocultismo iluminati
				
				if xvel > 0:
					#self.rect.right = p.rect.left
					self.x += p.x - (self.x + self.w)
				if xvel < 0:
					#self.rect.left = p.rect.right
					self.x += (p.x + p.w) - self.x
				if yvel > 0:
					#self.rect.bottom = p.rect.top
					self.y += p.y - (self.y + self.h)
					self.onGround = True
					self.yvel = 0
				if yvel < 0:
					#self.rect.top = p.rect.bottom
					self.y += (p.y + p.h) - self.y
					
	
	def update(self, direction, platforms):
		
		
		if direction['up']:
			# only jump if on the ground
			if self.onGround:
				self.yvel -= 10
		if direction['down']:
			pass
		if direction['left']:
			self.xvel = -8
		if direction['right']:
			self.xvel = 8
		
		if not(direction['left'] or direction['right']):
			self.xvel = 0
		
		if not self.onGround:
			self.yvel += 0.3
			if self.yvel > 100:
				self.yvel = 100
		
		
		self.x += self.xvel
		
		# do x-axis collisions
		self.collide(self.xvel, 0, platforms)
        
		self.y += self.yvel
		self.onGround = False;
        
        # do y-axis collisions
		self.collide(0, self.yvel, platforms)
		
		
		
		
		
		
		
		
	
	def setPos(self, x, y):
		self.x = x
		self.y = y
	
	def draw(self, surface):
		pass
