#! /usr/bin/python

import pygame
from pygame import *


class Entity(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)