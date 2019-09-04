import pygame
from pygame.locals import *
import sys

class Game():

    corredores = []

    # Constructor por defecto
    def __init__(self, width, height):
        self.__size = (width, height)
        #Titulo de la pantalla
        self.__title = "Carrera de bichos"

        #Inicializamos el display
        self.__screen = pygame.display.set_mode((640,480))
        
        #Cargamos la imagen de fondo del display
        self.background = pygame.image.load("images/background.png")

    def competir(self):
        pygame.font.init()
        pygame.init()
        self.__screen = pygame.display.set_mode(self.__size, pygame.HWSURFACE)
        pygame.display.set_caption(self.__title)
        
        ganador = False

        while not ganador:
            #Comprobacion de los eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            #Renderizado de la pantalla
            #Nos pinta la pantalla con el background
            self.__screen.blit(self.background, (0,0))
            #refresco de pantalla
            pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    game = Game(640, 480)
    game.competir()