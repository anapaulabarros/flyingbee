#coding:utf-8
import pygame, sys, pygame.mixer
from pygame.locals import *
from random import randint

wind_size = 568,500
space = 220
back = pygame.image.load("image/back-bee.png")
abelha = pygame.image.load("image/bee.png")


#----------- CORES
green = (35, 232, 61)
blue = (37,241,245)
black = (0,0,0)
grey = (9,105,16)
grey2 = (24,168,33)
grey3 = (220,220,220)
green2 = (161,255,167)
green3 = (87,255,98)
yellow = (246,255,0)
white = (255,255,255)
orange = (255,187,0)
brown = (143,71,0)


#funcao para desenhar a bola na tela na posicao x,y
def bee(x,y,screen):
    screen.blit(abelha, [x,y])

#funcao para informar fim de jogo
def gameover(screen):
    font = pygame.font.Font("fonts/font2.ttf", 30)
    mensagem = font.render('PERDEU  PLAYBOY!!!', True, (0,0,0))
    screen.blit(mensagem, [120,200])

#funcao para desenhar e inserir os obstaculos na tela
def obstaculos(xloc, yloc, xsize, ysize, screen):
    
    pygame.draw.rect(screen, green, [xloc, yloc, xsize, ysize])
    pygame.draw.rect(screen, green, [xloc, yloc+ysize+space, xsize, ysize+500])
    pygame.draw.rect(screen, black, [xloc+63, yloc, 7, ysize])
    pygame.draw.rect(screen, grey, [xloc+56, yloc, 7, ysize])
    pygame.draw.rect(screen, grey2, [xloc+49, yloc, 7, ysize])
    pygame.draw.rect(screen, green2, [xloc, yloc, 7, ysize])
    pygame.draw.rect(screen, green3, [xloc+7, yloc, 7, ysize])

    pygame.draw.rect(screen, black, [xloc+63, yloc+ysize+space, 7, ysize+500])
    pygame.draw.rect(screen, grey, [xloc+56, yloc+ysize+space, 7, ysize+500])
    pygame.draw.rect(screen, grey2, [xloc+49, yloc+ysize+space, 7, ysize+500])
    pygame.draw.rect(screen, green2, [xloc, yloc+ysize+space, 7, ysize+500])
    pygame.draw.rect(screen, green3, [xloc+7, yloc+ysize+space, 7, ysize+500])
   

#funcao para marcar a pontuacao
def pontuacao(ponto, screen):
    font = pygame.font.Font("fonts/font2.ttf", 30)
    text = font.render(str(ponto), True, (0,0,0))
    screen.blit(text, [284,50])
    
        
#funcao principal
def main():
    
    #seta as variaveis de inicializacao
    done = False
    x = 200
    y = 230
    velocidade_x = 0
    velocidade_y = 0
    ground = 400
    localizacao_x = 460
    localizacao_y = 0
    tamanho_x = 70
    tamanho_y = randint(0,300)
    velo_obsctaculo = 2.5
    ponto = 0

    #inicializa o pygame
    pygame.init()
    som_abelha = pygame.mixer.Sound('click.wav')
    clock = pygame.time.Clock()

    
    #configura o tamanho da tela do jogo
    screen = pygame.display.set_mode(wind_size)
    pygame.display.set_caption('Flying Bee')

    #contole de execucao
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        if event.type == pygame.KEYDOWN: #decrementa a posicao para bola cair
            if event.key == pygame.K_UP:
                velocidade_y = -10
                #som_abelha.play()                
        if event.type == pygame.KEYUP: #incrementa a posicao para bola subir
            if event.key == pygame.K_UP:
                velocidade_y = 5
        for i in (0, 568 / 2): #carrega o background e repete a imagem até completar o tamanho da tela
            screen.blit(back, (i,0))
        obstaculos(localizacao_x, localizacao_y, tamanho_x, tamanho_y, screen) #carrega os obstaculos na tela    
        bee(x,y,screen) #carrega a bola
        pontuacao(ponto, screen) #pontuacao

        if y >= ground or y <= 0: #verifica se a posicao Y da bola atingiu o chao
            gameover(screen)
            velocidade_y = 0
            velo_obsctaculo = 0
            
        #verifica se a bola bateu nos obstaculos 
        if x + 20 > localizacao_x and y - 20 < tamanho_y and x - 15 < tamanho_x + localizacao_x:
            gameover(screen)
            velocidade_y = 0
            velo_obsctaculo = 0
            
        #verifica se a bola bateu nos obstaculos
        if x + 20 > localizacao_x and y + 20 > tamanho_y + space and x - 15 < tamanho_x + localizacao_x:
            gameover(screen)
            velo_obsctaculo = 0
            velocidade_y = 0
        if localizacao_x < -80:
            localizacao_x = 400 #era 700
            tamanho_y = randint(0,300)    

        if x > localizacao_x and x < localizacao_x + 4: # atualiza o contador de pontos a cada obstaculo ultrapassado        
            ponto += 1

        y += velocidade_y # atualiza a posicao da bola
        localizacao_x -= velo_obsctaculo
        
        pygame.display.flip()
        clock.tick(60)
        pygame.display.update()                
        
    pygame.quit()
    

# executa a funcao principal ao executar o programa
if __name__ == '__main__':
    main()
