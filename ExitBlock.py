#! /usr/bin/python

import pygame
from pygame import *
from Platform import *


class ExitBlock(Platform):
    def __init__(self, x, y):
        Platform.__init__(self, x, y, "E")



#if isinstance(p, ExitBlock):
