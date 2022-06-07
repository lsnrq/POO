import pygame 
from random import choice, randint
from ventana import *

class Obstaculo(pygame.sprite.Sprite):
	def __init__(self, grupos, escala):
		super().__init__(grupos)
		self.sprite_type = "obstaculo"
		orientacion = choice(('up','down'))
		self.enemy = pygame.image.load(f'../archivos/obstaculos/{choice((1,2))}.png').convert_alpha() #importar obsaculos en secuencia aleatoria
		self.image = pygame.transform.scale(self.enemy,pygame.math.Vector2(self.enemy.get_size()) * escala)
		x = WIDTH + randint(40,100) 
		if orientacion == 'up':
			y = HEIGHT + randint(10,50) #altura obstaculos
			self.rect = self.image.get_rect(midbottom = (x,y))
		else:
			y = randint(-50,-10) 
			self.image = pygame.transform.flip(self.image,False,True)
			self.rect = self.image.get_rect(midtop = (x,y))

		self.pos = pygame.math.Vector2(self.rect.topleft)
		self.mask = pygame.mask.from_surface(self.image) #anadir colisiones a los obstaculos

	def update(self,tiempo):
		self.pos.x -= 400 * tiempo
		self.rect.x = round(self.pos.x)
		if self.rect.right <= -100:
			self.kill()