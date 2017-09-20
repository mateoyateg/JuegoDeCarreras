import pygame
from pygame.sprite import Sprite
from pygame import *
from random import *
import util

class Villano(Sprite):
	def __init__(self,coord,vel):
		Sprite.__init__(self)
		teclas = pygame.key.get_pressed()
		self.image = util.cargar_imagen('imagenes/obstaculo.png')
		self.rect = self.image.get_rect()
		self.rect.move_ip(coord[0], coord[0])
		self.velocidad=vel
        
	def update(self):
		teclas = pygame.key.get_pressed()
		if self.velocidad == 0:
			self.velocidad=1
		if teclas[K_RIGHT]:
			self.velocidad=self.velocidad+1
		elif teclas[K_LEFT] and self.velocidad > 0:
			self.velocidad=self.velocidad-1
		self.rect.x += self.velocidad 
		self.rect.x = self.rect.x % 640
