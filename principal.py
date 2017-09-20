import sys, pygame, util
from pygame.locals import *
from heroe import *
from villano import *
from random import *

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

def game():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode( (SCREEN_WIDTH,SCREEN_HEIGHT) )
    pygame.display.set_caption( "Autos - Juego" )
    background_image = util.cargar_imagen('imagenes/fondo.jpg');
    pierde_vida = util.cargar_sonido('sonidos/pierde_vida.wav')
    pygame.mouse.set_visible( False )
    temporizador = pygame.time.Clock()
    heroe = Heroe()
    villano = [Villano((30,150),randint(1,5)),
			   Villano((100,150),randint(1,5)),
               Villano((200,220),randint(1,5)),
               Villano((300,350),randint(1,5)),
               Villano((370,350),randint(1,5)),
               ]
	
    while True:
        fuente = pygame.font.Font(None,25)
        texto_puntos = fuente.render("Puntos: "+str(heroe.puntos),1,(246,246,246))
        texto_vida = fuente.render("Vida: "+str(heroe.vida),1,(246,246,246))
        texto_banner = fuente.render("Esquiva al auto",1,(246,246,246))
        
        heroe.update()
        for n in villano:
            n.update()
            
        for n in villano:
			if n.rect.x == heroe.rect.x and heroe.rect.colliderect(n.rect) == 0 and heroe.vida > 0:
				heroe.puntos=heroe.puntos+1

        for n in villano:
            if heroe.rect.colliderect(n.rect):
                heroe.image = heroe.imagenes[1]
                pierde_vida.play()
                if heroe.vida > 0:
                    heroe.vida=heroe.vida-1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
                
        screen.blit(background_image, (0,0))
        screen.blit(heroe.image, heroe.rect)
        screen.blit(texto_vida,(430,455))
        screen.blit(texto_puntos,(120,455))
        screen.blit(texto_banner, (240,10))
        for n in villano:
            screen.blit(n.image, n.rect)
        pygame.display.update()
        pygame.time.delay(10)

if __name__ == '__main__':
    game();
