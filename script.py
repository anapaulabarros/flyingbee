#coding:utf-8
import pygame, sys, pygame.mixer
from pygame.locals import *
from random import randint
import reinicio

wind_size = 568,500
space = 200
back = pygame.image.load("image/back-bee.png")
chao = pygame.image.load("image/chao.jpg")
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


#funcao para desenhar a abelha na tela na posicao x,y
def bee(x,y,screen):
    screen.blit(abelha, [x,y])

#funcao para informar fim de jogo
def gameover(screen):
    reinicio.reinicio()    

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


#funcao para blitar o pote de mel
def bonus_extras(x,y,screen):
    screen.blit(pote_mel, [x,y])
    #pygame.draw.rect(screen, green, [xloc, yloc, xsize, ysize])   

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
    ground = 425
    localizacao_x = 460
    localizacao_y = 0
    velo_obsctaculo = 0
    tamanho_x = 70
    tamanho_y = randint(0,300)
    ponto = 0
    grava_pontos = ''

    #inicializa o pygame
    pygame.init()
    click_mouse = pygame.mouse.get_pressed()
    som_abelha = pygame.mixer.Sound('sons/jump.wav')
    som_ponto = pygame.mixer.Sound('sons/yay.wav')
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
            if event.key == pygame.K_DOWN:
                velocidade_y = -10
                velo_obsctaculo = 2.5
                #som_abelha.play()                
        if event.type == pygame.KEYUP: #incrementa a posicao para bola subir
            if event.key == pygame.K_DOWN:
                velocidade_y = 5
        for i in (0, 568 / 2): #carrega o background e repete a imagem até completar o tamanho da tela
            screen.blit(back, (i,0))
        obstaculos(localizacao_x, localizacao_y, tamanho_x, tamanho_y, screen) #carrega os obstaculos na tela    
        bee(x,y,screen) #carrega a abelha
        screen.blit(chao, (0,450)) #blita o chao do cenário
        pontuacao(ponto, screen) #pontuacao
        
        
        if y >= ground or y <= 0: #verifica se a posicao Y da bola atingiu o chao
            gameover(screen)
            velocidade_y = 0
            velo_obsctaculo = 0
            
        #verifica se a abelha bateu nos obstaculos 
        if x + 20 > localizacao_x and y - 20 < tamanho_y and x - 15 < tamanho_x + localizacao_x:
            gameover(screen)
            velocidade_y = 0
            velo_obsctaculo = 0
            
        #verifica se a abelha bateu nos obstaculos
        if x + 20 > localizacao_x and y + 20 > tamanho_y + space and x - 15 < tamanho_x + localizacao_x:
            gameover(screen)
            velo_obsctaculo = 0
            velocidade_y = 0
        if localizacao_x < -80:
            localizacao_x = 400 #era 700
            tamanho_y = randint(0,300)    

        #print localizacao_x, localizacao_y
        if x > localizacao_x and x < localizacao_x + 4: # atualiza o contador de pontos a cada obstaculo ultrapassado        
            ponto += 1
            som_ponto.play()
            grava_pontos = open("pontos.txt","w").write(str(ponto)) #grava pontuação da partida no arquivo

        y += velocidade_y # atualiza a posicao da bola
        localizacao_x -= velo_obsctaculo
        
        pygame.display.flip()
        clock.tick(60)
        pygame.display.update()                
        
    pygame.quit()
    

# executa a funcao principal ao executar o programa
if __name__ == '__main__':
    main()
