from ventana import *
import pygame


class Aeronave(pygame.sprite.Sprite):
	def __init__(self, grupos, escala):
		super().__init__(grupos)
		self.volar(escala)
		self.fotogramas = 0
		self.image = self.frames[self.fotogramas]
        #acomodar el aeroplano en una posicion
		self.rect = self.image.get_rect(midleft = (WIDTH/50, HEIGHT/2))#posicion
		self.pos = pygame.math.Vector2(self.rect.topleft)
		self.grav = 300 #asignar gravitacion al aeroplano
		self.direccion = 0
		self.mask = pygame.mask.from_surface(self.image) #asignar mask(hitbox)

		# sound
		self.impulso_sound = pygame.mixer.Sound('../archivos/sfx/impulso.wav')
		self.impulso_sound.set_volume(5)

	def volar(self, escala): #metodo volar
		self.frames = []
		for i in range(3):
			airplane = pygame.image.load(f'../archivos/airplane/nave{i}.png').convert_alpha()
			escalaAirplane = pygame.transform.scale(airplane ,pygame.math.Vector2(airplane.get_size())* escala)
			self.frames.append(escalaAirplane)

	def Gravedad(self, tiempo): #metodo gravedad
		self.direccion += self.grav * tiempo
		self.pos.y += self.direccion * tiempo
		self.rect.y = round(self.pos.y)

	def Impulso(self):    #metodo salto
		self.impulso_sound.play()
		self.direccion = -200 #asignar una fuerza de impulso al aeroplano

	def Animacion(self, tiempo):
		self.fotogramas += 15 * tiempo #velocidad de fotogramas a la animacion de las helices del aeroplano
		if self.fotogramas >= len(self.frames):
			self.fotogramas = 0
		self.image = self.frames[int(self.fotogramas)]

	def update(self,tiempo):
		self.Gravedad(tiempo)
		self.Animacion(tiempo)
