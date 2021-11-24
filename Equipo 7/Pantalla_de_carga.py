import pygame,sys,random,os
from pygame import mixer

pygame.init()

def Pantalla_carga(ventana):
    ventana=pygame.display.set_mode([960,800])
    fotograma = 0
    f_muro = 0
    tiempo=0
    background=pygame.image.load((os.path.dirname(os.path.abspath(__file__))+"\\Background\P_CARGA.png"))
    background = pygame.transform.scale(background,(960,600))
    cabeza=[pygame.image.load(os.path.dirname(os.path.abspath(__file__))+"\\Sprites\C1.png").convert_alpha(),
            pygame.image.load(os.path.dirname(os.path.abspath(__file__))+"\\Sprites\C2.png").convert_alpha(),
            pygame.image.load(os.path.dirname(os.path.abspath(__file__))+"\\Sprites\C3.png").convert_alpha(),
            pygame.image.load(os.path.dirname(os.path.abspath(__file__))+"\\Sprites\C4.png").convert_alpha(),
            pygame.image.load(os.path.dirname(os.path.abspath(__file__))+"\\Sprites\C5.png").convert_alpha(),
            pygame.image.load(os.path.dirname(os.path.abspath(__file__))+"\\Sprites\C6.png").convert_alpha(),
            pygame.image.load(os.path.dirname(os.path.abspath(__file__))+"\\Sprites\C7.png").convert_alpha(),
            pygame.image.load(os.path.dirname(os.path.abspath(__file__))+"\\Sprites\C8.png").convert_alpha()]
    run=True
    while run:
        tiempo+=1
        ventana.fill((0,0,0))
        ventana.blit(background,[0,100])
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
        f_muro+=1
        if(f_muro==60):
            fotograma+=1
            f_muro=0
        if(fotograma==7):
            fotograma=0
        ventana.blit(cabeza[fotograma],[960-100,800-200])
        pygame.display.flip()
        if tiempo==600:
            run=False
