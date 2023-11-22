# -*- coding: cp1252 -*-
import pygame
from pygame.locals import*
import os
import random
import pickle
import time

pygame.init()

l = 500
h = 500
mf = pygame.display.set_mode((l,h))


#mes couleurs
blanc = (255,255,255)
noir  = (0  ,  0,  0)
rouge = (255,  0,  0)
vert  = (0  ,255,  0)
bleu  = (0  ,0  ,255)

#Mes Images
carre   = pygame.image.load('carre rouge.png').convert_alpha()
accueil = pygame.image.load('clic here accueil.png').convert_alpha()

#FONT
font = 'segoeprb.ttf'
ma_font = pygame.font.Font(font,100)
#accueil
ACCUEIL = 1
boucle_du_jeu = 1
mode_U = 0
mode_T = 0
win = 0
continuer1 = 1
mf.fill(blanc)

                

while boucle_du_jeu:
    if ACCUEIL == 1:
        mf.blit(accueil,(0,0))
    for event1 in pygame.event.get():
        if event1.type == KEYDOWN:
            if event1.key == K_u:
                mode_U = 1
                mf.fill(blanc)
                ACCUEIL = 0
            if event1.key == K_t:
                mode_T = 1
                mf.fill(blanc)
                ACCUEIL = 0
                
    while mode_U:
        if continuer1 == 1:
            xcarre = random.randint(0,400)#position x
            ycarre = random.randint(0,400)#position y
            mf.blit(carre,(xcarre,ycarre))#blitage
            continuer1 = 0
                    
        for event in pygame.event.get():   
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:#evenment au clic
                    toucher = (event.pos[0]) - (xcarre)#def toucher (rayon)
                    if toucher > 0 and toucher < 100:#si on est dans le carre
                        continuer1 = 1
                        mf.fill(blanc)#on "nettoie"
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    ACCUEIL = 1
                    mode_U =0
        pygame.display.flip()
        

        
        
        
    pygame.display.flip()


        
