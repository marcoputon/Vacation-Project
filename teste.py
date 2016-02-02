#! /usr/bin/python

import pygame
from pygame import *
from Platform import *
from ExitBlock import *


a = Platform(0, 0, "G")
b = ExitBlock(19, 8)

if isinstance(a, Platform):
	print("1")
	
if isinstance(a, ExitBlock):
	print("2")

if isinstance(b, Platform):
	print("3")
	
if isinstance(b, ExitBlock):
	print("4")
