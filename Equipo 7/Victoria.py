import pygame,sys,random,os
from Funciones import *
pygame.init()

def escribir_texto(pantalla,localizacion,texto,tamaño):
    fuente1=pygame.font.SysFont("Times New Roman",tamaño)
    ren2=fuente1.render(texto,True,(255,255,255))
    pantalla.blit(ren2,((localizacion[0]-(ren2.get_width()/2)),(localizacion[1]-(ren2.get_height()/2))))

def crear_boton(pantalla,boton,texto,tamaño):
    fuente1=pygame.font.SysFont("Times New Roman",tamaño)
    if boton.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(pantalla,[225, 38, 180],boton,0)
    else:
        pygame.draw.rect(pantalla,[174, 15, 135],boton,0)
    ren=fuente1.render(texto,True,(255,255,255))
    pantalla.blit(ren,(boton.x+(boton.width-ren.get_width())/2,boton.y+(boton.height-ren.get_height())/2))

def victoria(ventana,puntaje):
    fotograma = 0
    f_muro = 0
    continuar=pygame.Rect(960-200,800-100,170,70)
    pygame.mixer.music.load(os.path.dirname(os.path.abspath(__file__))+"\\Musica/VICTORIA.wav")
    pygame.mixer.music.play(1,0.0)
    pygame.mixer.music.set_volume(0.08)

    araña_feliz = [pygame.image.load(os.path.dirname(os.path.abspath(__file__))+"\\Sprites/Feliz_L.png").convert_alpha()
                ,pygame.image.load(os.path.dirname(os.path.abspath(__file__))+"\\Sprites/Feliz_R.png").convert_alpha()]
    araña_feliz[0] = pygame.transform.scale(araña_feliz[0],(570,380))
    araña_feliz[1] = pygame.transform.scale(araña_feliz[1],(570,380))
    araña_feliz[0] = pygame.transform.rotate(araña_feliz[0],-5)
    araña_feliz[1] = pygame.transform.rotate(araña_feliz[1],-5)

    run=True
    while run:
        ventana.fill((86, 18, 132))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
            if event.type==pygame.MOUSEBUTTONDOWN and event.button==1 and continuar.collidepoint(pygame.mouse.get_pos()):
                run=False
        f_muro+=1
        if(f_muro==60):
            fotograma+=1
            f_muro=0
        if(fotograma==2):
            fotograma=0
        
        escribir_texto(ventana,[960/2,150],"¡VICTORIA!",100)
        escribir_texto(ventana,[960/2+100,210],str(puntaje),50)
        escribir_texto(ventana,[960/2-30,210],"Puntaje: ",50)
        ventana.blit(araña_feliz[fotograma],(10,800-475))    
        crear_boton(ventana,continuar,"Continuar",40)
        pygame.display.flip()
