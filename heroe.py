import pygame
from pygame.sprite import Sprite
from pygame import *
import util

class Heroe(Sprite):
	def __init__(self):
		Sprite.__init__(self)
		teclas = pygame.key.get_pressed()
		self.puntos = 0
		self.vida = 1000
		self.estado = "bajando"
		self.imagenes = [util.cargar_imagen('imagenes/auto.png'),
						util.cargar_imagen('imagenes/auto_chocado.png'),
						util.cargar_imagen('imagenes/auto.png'),
						util.cargar_imagen('imagenes/auto.png')]
		self.image = self.imagenes[0]
		self.rect = self.image.get_rect()
		self.rect.move_ip(520, 210)
        
	def update(self):
		teclas = pygame.key.get_pressed()
		if self.vida > 0:					
			if teclas[K_UP] and self.rect.y>=10:
				self.rect.y -= 10
				self.image = self.imagenes[2]
				
			elif teclas[K_DOWN] and self.rect.y<=480-self.rect.height:
				self.rect.y += 10
				self.image = self.imagenes[0]
				
		else:
			self.image = self.imagenes[1]
