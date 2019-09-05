import pygame
from pygame.locals import *
import sys
import random

class Runner():
    #tupla de personajes (imagenes) de los runners
    __custome =('turtle', 'fish', 'prawn', 'moray', 'octopus')

    def __init__(self, x = 0, y = 0, custome = None):
        
        '''
        #coloco imagen del corredor
        for i in range (len(self.__custome)):

            self.custome = pygame.image.load("images/{}.png".format(self.__custome[i]))
        '''
        '''
        #coloco imagen del corredor
        ixCustome = random.randint(0,4)    
        self.custome = pygame.image.load("images/{}.png".format(self.__custome[ixCustome]))
        '''

        self.position = [x,y]
        self.name = custome

    def avanzar(self):
        self.position[0] += random.randint(1,3)

class Game():

    runners = []
    __posY = (160,200,240,280)
    __names = ('Speedy', 'Lucera', 'Alonso', 'Torcuata')
    __startLine = 20
    __finishLine = 600


    # Constructor por defecto
    def __init__(self, width, height, custome=None):
        self.__size = (width, height)
        #Titulo de la pantalla
        self.__title = "Carrera de bichos"

        #Inicializamos el display
        self.__screen = pygame.display.set_mode((640,480))
        
        #Cargamos la imagen de fondo del display
        self.background = pygame.image.load("images/background.png")

        for i in range(4):
            theRunner = Runner(self.__startLine, self.__posY[i])
            theRunner.name = self.__names[i]
            theRunner.custome = self.__custome[i]
            self.runners.append(theRunner)


    def close(self):
        pygame.quit()
        sys.exit()

    def competir(self):
        pygame.font.init()
        pygame.init()
        self.__screen = pygame.display.set_mode(self.__size, pygame.HWSURFACE)
        pygame.display.set_caption(self.__title)
        
        hayGanador = False
        x = 0        

        while not hayGanador:
            #Comprobacion de los eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            
            for activeRunner in self.runners:
                activeRunner.avanzar()

                if activeRunner.position[0] >= self.__finishLine:
                    print("{} Ha ganado".format(activeRunner.name))
                    hayGanador = True
                


            #Renderizado de la pantalla
            #Nos pinta la pantalla con el background
            self.__screen.blit(self.background, (0,0))

            for runner in self.runners:
                self.__screen.blit(runner.custome, runner.position)
            
            #refresco de pantalla
            pygame.display.flip()
            
        while True:    
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close()



if __name__ == '__main__':
    pygame.font.init()
    game = Game(640, 480,'turtle')
    game.competir()
