from ventana import *
import pygame

class Suelo(pygame.sprite.Sprite):
	def __init__(self, grupos, escala):
		super().__init__(grupos)
		self.sprite_type = "suelo"
		self.tierra = pygame.image.load('../archivos/visual/suelo.png').convert_alpha()
		self.image = pygame.transform.scale(self.tierra,pygame.math.Vector2(self.tierra.get_size())*escala)
		self.rect = self.image.get_rect(bottomleft = (0,HEIGHT))  #acomodar el suelo en la parte de abajo al ejecutar el programa
		self.pos = pygame.math.Vector2(self.rect.topleft)
		self.mask = pygame.mask.from_surface(self.image) #anadir una colision al suelo

	def update(self,tiempo):
		self.pos.x -= 360 * tiempo  #el suelo se mueve a otra velocidad que el mapa
		if self.rect.centerx <= 0:
			self.pos.x = 0

		self.rect.x = round(self.pos.x)
