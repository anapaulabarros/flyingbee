# coding: utf-8
import pygame, sys
from pygame.locals import *
import script
 
wind_size = 568,500
back = pygame.image.load('image/tela_menu.png')
btn_iniciar = pygame.image.load('image/botoes/iniciar.jpg')
btn_iniciar_h = pygame.image.load('image/botoes/iniciar_hover.jpg')
btn_ajuda = pygame.image.load('image/botoes/ajuda.jpg')
btn_ajuda_h = pygame.image.load('image/botoes/ajuda_hover.jpg')
btn_sobre = pygame.image.load('image/botoes/sobre.jpg')
btn_sobre_h = pygame.image.load('image/botoes/sobre_hover.jpg')
btn_sair = pygame.image.load('image/botoes/sair.jpg')
btn_sair_h = pygame.image.load('image/botoes/sair_hover.jpg')
tela_sobre = pygame.image.load('image/tela-sobre.jpg')

 
def main():
    done = False
    pos2 = [] #posicao do mouse
    pygame.init()
    clock = pygame.time.Clock()


    screen = pygame.display.set_mode(wind_size)
    pygame.display.set_caption('Flying Bee')
    screen.blit(back,(0,0))
    screen.blit(btn_iniciar,(330,140))
    screen.blit(btn_ajuda,(325,185))
    screen.blit(btn_sobre,(320,232))
    screen.blit(btn_sair,(320,275))
    
    while not done:
        pos2 = list((pygame.mouse.get_pos()))
        click_mouse = pygame.mouse.get_pressed()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        if pos2[0] >= 365 and pos2[0] <= 483 and pos2[1] >= 146 and pos2[1] <= 171:
            if click_mouse[0] == 1:
                script.main()    
                sys.exit()
            screen.blit(btn_iniciar_h,(330,140))
        else:
            screen.blit(btn_iniciar,(330,140))

        if pos2[0] >= 372 and pos2[0] <= 475 and pos2[1] >= 195 and pos2[1] <= 216:
            screen.blit(btn_ajuda_h,(325,185))
        else:
            screen.blit(btn_ajuda,(325,185))
            
        if pos2[0] >= 373 and pos2[0] <= 472 and pos2[1] >= 240 and pos2[1] <= 273:
            screen.blit(btn_sobre_h,(320,232))
            if click_mouse[0] == 1:
                screen.blit(tela_sobre,(315,120))
        else:
            screen.blit(btn_sobre,(320,232))

        if pos2[0] >= 387 and pos2[0] <= 451 and pos2[1] >= 286 and pos2[1] <= 308:
            if click_mouse[0] == 1:
                    done = True #sai do jogo
            screen.blit(btn_sair_h,(320,275))
        else:
            screen.blit(btn_sair,(320,275))    
          

        pygame.display.flip()
        clock.tick(60)
        pygame.display.update()

        
    pygame.quit()
    

# executa a funcao principal ao executar o programa
if __name__ == '__main__':
    main()
