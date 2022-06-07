import pygame, sys, time
from ventana import *
from aeroplano import Aeronave
from fondo import Fondo
from obstaculo import Obstaculo
from suelo import Suelo




class Juego():
	def __init__(self):
		pygame.init()
		self.interfazMenu = pygame.display.set_mode((WIDTH,HEIGHT))
		pygame.display.set_caption('La historia de México')#titulo del juego
		self.clock = pygame.time.Clock()#agregando reloj para el contador
		self.activo = True #estado activo depende de la vida del personaje
		#sprite en grupos
		self.fullSprites = pygame.sprite.Group()
		self.spritesColisiones = pygame.sprite.Group()
		alturaFondo = pygame.image.load('../archivos/visual/fondo.png').get_height()
		self.escala = HEIGHT / alturaFondo
		#Instanciar subclases
		Fondo(self.fullSprites,self.escala) #pasar grupos de sprites al fondo
		Suelo([self.fullSprites,self.spritesColisiones],self.escala)
		self.nave = Aeronave(self.fullSprites,self.escala / 1)  #se divide entre n para definir el tamano del objeto aeroplano
		self.obstacle_timer = pygame.USEREVENT+1
		pygame.time.set_timer(self.obstacle_timer,2500) #Generar un obstaculo cada 2.5 segundos 
        #fuente
		self.font = pygame.font.Font('../archivos/font/8_BIT.ttf',30) #importar fuente y definir su tamano
		self.puntos = 0 #contador comienza en 0 
		self.inicio = 0
		#Menu
		self.menu_surf = pygame.image.load('../archivos/visual/menu.png').convert_alpha()
		self.menu_rect = self.menu_surf.get_rect(center = (WIDTH/2, HEIGHT/2)) #colocar menu de continuar justo en medio
		#Himno nacional 
		self.music = pygame.mixer.Sound('../archivos/sfx/himno.wav')
		self.music.play(loops=-1) # el himno se mantendra en un loop infinito
        

	def Colision(self):
		if pygame.sprite.spritecollide(self.nave, self.spritesColisiones, False, pygame.sprite.collide_mask)\
		or self.nave.rect.top <= 0:  #si el aeroplano toca el techo pierdes
			for sprite in self.spritesColisiones.sprites():
				if sprite.sprite_type == "obstaculo":
					sprite.kill()  #desaparece todo tipo de colision mientras se encuentra el menu abierto
			self.activo = False
			self.nave.kill() #el aeroplano desaparece si el usuario pierde con el metodo kill de pygame


	def Puntaje(self): #marcador 
		if self.activo: # si el usuario se mantiene activo seguira corriendo el puntaje
			self.puntos = (pygame.time.get_ticks() - self.inicio)//100 #definir cantidad de puntos por milisegundo (10 puntos cada segundo)
			y = HEIGHT/10
		else:
			y = HEIGHT/2 + (self.menu_rect.height / 1.5)

		puntajeInterfaz = self.font.render(str(self.puntos),True,'black') #color blanco de fuente 
		puntaje_rect = puntajeInterfaz.get_rect(midtop = (WIDTH/2, y)) #definir donde estara colocado el marcador
		self.interfazMenu.blit(puntajeInterfaz, puntaje_rect)


	def Ejecutar(self): #metodo para ejecutar el juego
		fin_tiempo = time.time()
		while True:
			tiempo = time.time() - fin_tiempo
			fin_tiempo = time.time()
			for evento in pygame.event.get():        #controlar los eventos
				if evento.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
                    
				if evento.type == pygame.MOUSEBUTTONDOWN:
					if self.activo:    #si el usuario se encuentra activo podra ejecutar el metodo del impulso del aeroplano
						self.nave.Impulso() #cada vez que se haga click, se activara el metodo salto
					else:
						self.nave = Aeronave(self.fullSprites,self.escala) #se puede dividir entre n para que el personaje principal cambie de tamaño
						self.activo = True
						self.inicio = pygame.time.get_ticks() #metodo get_ticks (pygame) para obtener milisegundos

				if evento.type == self.obstacle_timer and self.activo:
					Obstaculo([self.fullSprites,self.spritesColisiones],self.escala*1)
			
			#logica
			self.interfazMenu.fill('white') #llenar superficie con color blanco
			self.fullSprites.update(tiempo)
			self.fullSprites.draw(self.interfazMenu) #todos los sprites esten en la superficie
			self.Puntaje() #ejecutar contador

			if self.activo: 
				self.Colision() #si el usuario esta con vida le afectan las colisiones.
			else:
				self.interfazMenu.blit(self.menu_surf,self.menu_rect) #si el usuario no tiene vida, se desplega el menu.
			pygame.display.update()


a = Juego() #Instancia de la clase Juego 
a.Ejecutar() #Ejecutar el juego