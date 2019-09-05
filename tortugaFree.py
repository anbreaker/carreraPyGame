import pygame
from pygame.locals import *
import sys
import random

class Runner():
    #tupla de personajes (imagenes) de los runners
    __custome =('turtle', 'fish', 'prawn', 'moray', 'octopus')

    def __init__(self, x = 0, y = 0, custome = None):
        
        #coloco imagen del corredor
        ixCustome = random.randint(0,4)    
        self.custome = pygame.image.load("images/{}.png".format(self.__custome[ixCustome]))

        self.position = [x,y]
        self.name = custome

    def avanzar(self):
        self.position[0] += random.randint(1,3)

class Game():

    # Constructor por defecto
    def __init__(self, width, height):
        #Inicializamos el display
        self.__screen = pygame.display.set_mode((640,480))
        #Cargamos la imagen de fondo del display
        self.background = pygame.image.load("images/background.png")
        #Titulo de la pantalla
        self.__title = "Carrera de bichos"


        self.runner = Runner (320,240)
    
    def start(self):
        gameOver = False

        while not gameOver:
            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event == KEYDOWN:
                        if event.key() == K_UP:
                            # Mover Arriba
                            self.runner.position[1] -= 5
                        elif event.key() == K_DOWN:
                            # Mover Abajo 
                            self.runner.position[1] += 5
                        elif event.key() == K_LEFT:
                            # Mover Izquierda 
                            self.runner.position[0] -= 5
                        elif event.key() == K_RIGHT:                  
                            # Mover Derecha 
                            self.runner.position[0] += 5
                        else:
                            pass

            #Renderizado de la pantalla
            #Nos pinta la pantalla con el background
            self.__screen.blit(self.background, (0,0))
            self.__screen.blit(self.runner.custome, self.runner.position)
            
            #refresco de pantalla
            pygame.display.flip()

if __name__ == '__main__':
    pygame.font.init()
    game = Game(640, 480)
    game.start()