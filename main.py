# Créé par isn1, le 05/01/2017 en Python 3.2
import pygame
import random
pygame.mixer.pre_init(44100,-16,2,2048) #Gestion du son
from pygame.locals import *
pygame.init()
clock=pygame.time.Clock()
cp=pygame.mixer.Sound("ressources/case pleine.wav")

fenetre=pygame.display.set_mode((800,600))

Red = pygame.image.load("ressources/RedDisc.png")
Redrect=Red.get_rect()
Redrectinit=Red.get_rect()
Yellow = pygame.image.load("ressources/YellowDisc.png")
Yellowrect=Yellow.get_rect()
Yellowrectinit=Yellow.get_rect()
fondnoir= pygame.image.load("ressources/fondnoir.png")
background=pygame.image.load("ressources/background.png")
Redwin=pygame.image.load("ressources/red_wins.png")
jaunewin=pygame.image.load("ressources/yellow_wins.png")
menuim= pygame.image.load("ressources/Title_Screen.png")
yRed=6



#gestion clics#
def menu():
    fenetre.blit(menuim, (0,0))
    pygame.display.flip()
    continuer= True
    commencer=False
    while continuer==True:
        for event in pygame.event.get():
            if event.type==QUIT:
                continuer == False
            if event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[1]< 395 and  event.pos[1] > 340 and event.pos[0] < 550 and  event.pos[0] > 250:
                commencer=True
                continuer=False
                choix=1
            if event.type == MOUSEBUTTONUP and event.button == 1 and event.pos[1]< 521 and  event.pos[1] > 468 and event.pos[0] < 550 and  event.pos[0] > 250:
                choix = 2
                commencer = False
                continuer=False

    return commencer,choix

def bougejeton(joueur,x,y,position,Redrect,Yellowrect):
    global taby,tabx
    if joueur==1 :
        Redrect=Redrect.move(x,y)
        fenetre.blit(Red,Redrect)
        pygame.display.flip()
        salejetonr=background.subsurface(Redrect)
        for i in range(taby[position]):
            fenetre.blit(salejetonr, Redrect)
            Redrect=Redrect.move(0,1)
            fenetre.blit(Red,Redrect)
            pygame.display.flip()
            salejetonr=background.subsurface(Redrect)
    if joueur==2 :
        Yellowrect=Yellowrect.move(x,y)
        fenetre.blit(Yellow,Yellowrect)
        pygame.display.flip()
        salejetonr=background.subsurface(Yellowrect)
        for i in range(taby[position]):
            fenetre.blit(salejetonr, Yellowrect)
            Yellowrect=Yellowrect.move(0,1)
            fenetre.blit(Yellow,Yellowrect)
            pygame.display.flip()
            salejetonr=background.subsurface(Yellowrect)

def test(col,couleur):
    li=5
    while (grille[col][li]!=0 ) and li>-1:
        li=li-1
    return(li)

def verif(grille,couleur):
    good=False
    for i in range (6): # test lignes
        if grille[0][i]==couleur and grille[1][i]==couleur and grille[2][i]==couleur and grille[3][i]==couleur :
            good=True
        if grille[1][i]==couleur and grille[2][i]==couleur and grille[3][i]==couleur and grille[4][i]==couleur :
            good=True
        if grille[2][i]==couleur and grille[3][i]==couleur and grille[4][i]==couleur and grille[5][i]==couleur :
            good=True
        if grille[3][i]==couleur and grille[4][i]==couleur and grille[5][i]==couleur and grille[6][i]==couleur :
            good=True

    for i in range (7):  # test colonnes
        if grille[i][0]==couleur and grille[i][1]==couleur and grille[i][2]==couleur and grille[i][3]==couleur  :
            good=True
        if grille[i][1]==couleur and grille[i][2]==couleur and grille[i][3]==couleur and grille[i][4]==couleur  :
            good=True
        if grille[i][2]==couleur and grille[i][3]==couleur and grille[i][4]==couleur and grille[i][5]==couleur  :
            good=True

    for i in range (4): # test diagonale gauche>droite
        if grille[i][5]==couleur and grille[i+1][4]==couleur and grille[i+2][3]==couleur and grille[i+3][2]==couleur  :
            good=True
        if grille[i][4]==couleur and grille[i+1][3]==couleur and grille[i+2][2]==couleur and grille[i+3][1]==couleur  :
            good=True
        if grille[i][3]==couleur and grille[i+1][2]==couleur and grille[i+2][1]==couleur and grille[i+3][0]==couleur  :
            good=True

    for i in range(4): # test diagonale droite>gauche
        if grille[i][0]==couleur and grille[i+1][1]==couleur and grille[i+2][2]==couleur and grille[i+3][3]==couleur  :
            good=True
        if grille[i][1]==couleur and grille[i+1][2]==couleur and grille[i+2][3]==couleur and grille[i+3][4]==couleur  :
            good=True
        if grille[i][2]==couleur and grille[i+1][3]==couleur and grille[i+2][4]==couleur and grille[i+3][5]==couleur  :
            good=True
    return good


def tombejeton(joueur,grille):              # joueur 1 --> Red / 2--> Yellow
        ok=False
        cont=True
        for event in pygame.event.get():
            if event.type==QUIT:
                cont=False #quitter#
            if event.type==MOUSEBUTTONUP and event.button==1:
                print ("clic effectué")
                if event.pos[1]<479:
                    Redrect=Redrectinit
                    Yellowrect=Yellowrectinit

            #première colonne
                if event.pos[0]<142:
                    position=test(0,joueur)
                    if position>-1:
                        grille[0][position]=joueur
                        ok=True
                        bougejeton(joueur,58, 107,position,Redrect,Yellowrect)
                        print(grille)

            #deuxième colonne

                if event.pos[0]<243 and event.pos[0]>158:
                    position=test(1,joueur)
                    if position>-1:
                        grille[1][position]=joueur
                        ok=True
                        bougejeton(joueur,158, 107,position,Redrect,Yellowrect)
                        print(grille)

            #troisième colonne

                if event.pos[0]<342 and event.pos[0]>257:
                    position=test(2,joueur)
                    if position>-1:
                        grille[2][position]=joueur
                        ok=True
                        bougejeton(joueur,257, 107,position,Redrect,Yellowrect)
                        print(grille)

            #quatrième colonne

                if event.pos[0]<444 and event.pos[0]>359:
                    position=test(3,joueur)
                    if position>-1:
                        grille[3][position]=joueur
                        ok=True
                        bougejeton(joueur,359, 107,position,Redrect,Yellowrect)
                        print(grille)

            #cinquième colonne

                if event.pos[0]<540 and event.pos[0]>458:
                    position=test(4,joueur)
                    if position>-1:
                        grille[4][position]=joueur
                        ok=True
                        bougejeton(joueur,458, 107,position,Redrect,Yellowrect)
                        print(grille)

            #sixième colonne

                if event.pos[0]<640 and event.pos[0]>557:
                    position=test(5,joueur)
                    if position>-1:
                        grille[5][position]=joueur
                        ok=True
                        bougejeton(joueur,558,107,position,Redrect,Yellowrect)
                        print(grille)

            #septième colonne

                if event.pos[0]>658:
                    position=test(6,joueur)
                    if position>-1:
                        grille[6][position]=joueur
                        ok=True
                        bougejeton(joueur,65, 107,position,Redrect,Yellowrect)
                        print(grille)

        ##        cp.play()

        return cont,ok
        #cont:Ferme la fenêtre ok:Position jeton

tabx=[57,158,195,257,359,458,557,65]
taby=[-10,0,100,200,300,400]
commencer,choix=menu()
#if commencer==False and choix==2:

if commencer==True and choix==1:
    fenetre.blit(background, (0,0))
    pygame.display.flip()
    grille=[[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
    jouer=False
    continuer=True
    joueur=1
    while continuer:

            continuer,bon=tombejeton(joueur,grille)
            if verif(grille,joueur)==True:
                if joueur==1:
                    fenetre.blit(Redwin, (300,250))
                    pygame.display.flip()
                if joueur==2:
                    fenetre.blit(jaunewin, (300,250))
                    pygame.display.flip()

            if bon :
                if joueur==1: joueur=2
                else : joueur=1
            jouer=True

pygame.quit()
