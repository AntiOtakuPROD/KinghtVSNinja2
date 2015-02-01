import pygame
from joueur import *
from boule import *
from niveau import *
from plateforme import *
from menu import *
from ninja import *
from shuriken import *
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
BLUE     = (   0,   0, 255)
RED      = ( 255,   0,   0)
GREEN    = (   0, 255,   0)
ECRAN_LARGEUR  = 800
ECRAN_HAUTEUR = 600
size = [ECRAN_LARGEUR, ECRAN_HAUTEUR]
screen = pygame.display.set_mode(size)

cases=[[250,350,50,150,False,pygame.image.load("art/carouj.png")],
       [500,600,20,120,False,pygame.image.load("art/caroz.png")]]
done = False
def clic(pos):
    global done
    for i in range(len(cases)):
        if cases[i][4]:
            done=True

def achatmenu():
    backpos = [0, 0]
    backimage = pygame.image.load("art/fondachat.png").convert()

    clock = pygame.time.Clock()
    global cases
    global done
    done = False
    while not done:
        pos = pygame.mouse.get_pos()
        
        for i in range(len(cases)):
            cases[i][4]=False
            cases[i][5]=pygame.image.load("art/carouj.png")
            if pos[0] >= cases[i][0] and pos[0] <= cases[i][1] and pos[1] >= cases[i][2] and pos[1] <= cases[i][3]:
                cases[i][4]=True
                cases[i][5]=pygame.image.load("art/caroz.png")
                
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                done = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    clic(pos)

        screen.blit(backimage, backpos)
        for i in range(len(cases)):
            screen.blit(cases[i][5], [cases[i][0],cases[i][2]])
        pygame.display.flip()
        clock.tick(60)

       
