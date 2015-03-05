# coding: utf-8
import pygame, sys
from pygame.locals import *

pos2 = []
pygame.init()
wind_size = 568,500
screen = pygame.display.set_mode(wind_size)
back = pygame.image.load('image/tela_menu.png')
tela_ajuda = pygame.image.load('image/tela-ajuda.jpg')
tela_sobre = pygame.image.load('image/tela-sobre.jpg')

def ajuda():
    done = False
    while not done:
        pos2 = list((pygame.mouse.get_pos()))
        click_mouse = pygame.mouse.get_pressed()
        screen.blit(back, (0,0))
        screen.blit(tela_ajuda, (330,140))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
        if pos2[0] >= 518 and pos2[0] <= 536 and pos2[1] >= 148 and pos2[1] <= 166:
            if click_mouse[0] == 1:
                done = True
       
        pygame.display.flip() 


def sobre():
    done = False
    while not done:
        pos2 = list((pygame.mouse.get_pos()))
        click_mouse = pygame.mouse.get_pressed()
        screen.blit(back, (0,0))
        screen.blit(tela_sobre, (330,140))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
        if pos2[0] >= 518 and pos2[0] <= 536 and pos2[1] >= 148 and pos2[1] <= 166:
            if click_mouse[0] == 1:
                done = True
       
        pygame.display.flip() 


