from ventana import *
import pygame

class Fondo(pygame.sprite.Sprite):#determina la escala
	def __init__(self, grupos, escala):
		super().__init__(grupos) #grupos de la clase padre Juego
		self.mapa = pygame.image.load('../archivos/visual/fondo.png').convert()

		alturaTotal = self.mapa.get_height()*escala #multiplicar escalas para el fondo
		anchoTotal = self.mapa.get_width()*escala
		fondoCompleto = pygame.transform.scale(self.mapa,(anchoTotal, alturaTotal))#determinar el tamano de la superficie
		
		self.image = pygame.Surface((anchoTotal*2, alturaTotal)) 
		self.image.blit(fondoCompleto, (0,0))
		self.image.blit(fondoCompleto, (anchoTotal,0))

		self.rect = self.image.get_rect(topleft=(0,0)) #rect para ajustar areas rectangulares
		self.pos = pygame.math.Vector2(self.rect.topleft) #se obtiene una posicion en el vector 0 y 0

	def update(self, tiempo):
		self.pos.x -= 150 * tiempo #velocidad en la que avanza el fondo del juego
		if self.rect.centerx <= 0:
			self.pos.x = 0
		self.rect.x = round(self.pos.x)
