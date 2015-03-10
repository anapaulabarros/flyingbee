# coding: utf-8
import pygame, sys
from pygame.locals import *
import script
import menu

wind_size = 568,500
back = pygame.image.load('image/tela_game_over.jpg')
reiniciar = pygame.image.load('image/botoes/reiniciar.png')
voltar = pygame.image.load('image/botoes/voltar.png')
screen = pygame.display.set_mode(wind_size)
pos2 = []
pygame.init()

def reinicio():
    zera_pontos = ''
    pos2 = list((pygame.mouse.get_pos()))
    click_mouse = pygame.mouse.get_pressed()
    screen.blit(back, (0,0))
    screen.blit(reiniciar, (340, 185))
    screen.blit(voltar, (340, 279))

    #exibe a pontuacao da ultima partida
    pontuacao = open("pontos.txt","r").read()
    font = pygame.font.Font("fonts/font2.ttf", 30)
    mensagem = font.render(pontuacao, True, (0,0,0))
    screen.blit(mensagem, [450,110])

    if pos2[0] >= 281 and pos2[0] <= 437 and pos2[1] >= 187 and pos2[1] <= 269:
        if click_mouse[0] == 1:
            zera_pontos = open("pontos.txt","w").write(str(0)) #zera a ultima pontuação
            script.main()
            sys.exit()

    if pos2[0] >= 282 and pos2[0] <= 438 and pos2[1] >= 282 and pos2[1] <= 368:
        if click_mouse[0] == 1:
            menu.main()
            sys.exit()
    
    pygame.display.flip()
