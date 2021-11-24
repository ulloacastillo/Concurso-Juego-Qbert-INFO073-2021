import pygame,sys,random,os
from Funciones import *

pygame.init()

#ventana
resolucion=[960,800]
ventana=pygame.display.set_mode(resolucion)
fondo=pygame.image.load(os.path.dirname(os.path.abspath(__file__))+"\\Background/Cueva.jpg").convert()
fondo=pygame.transform.scale(fondo,resolucion)
titulo=pygame.image.load(os.path.dirname(os.path.abspath(__file__))+"\\Sprites/Titulo_Juego.png").convert_alpha()
titulo=pygame.transform.scale(titulo,[503,206])

pygame.display.set_caption("SeVen Telarañas")
icono=pygame.image.load(os.path.dirname(os.path.abspath(__file__))+"\\Sprites/cabeza_araña2.png").convert_alpha()
pygame.display.set_icon(icono)

#colores
blanco=[255,255,255]
negro=[0,0,0]
rojo=[255,0,0]
verde=[0,255,0]
azul=[0,0,255]

jugar=pygame.Rect(resolucion[0]/2-75,resolucion[1]/4+120,150,50)
opciones=pygame.Rect(resolucion[0]/2-75,resolucion[1]/4+195,150,50)
extras=pygame.Rect(resolucion[0]/2-75,resolucion[1]/4+270,150,50)
salir=pygame.Rect(resolucion[0]/2-75,resolucion[1]/4+345,150,50)

run=True
while run:  
    ventana.blit(fondo,[0,0])
    ventana.blit(titulo,[resolucion[0]/2-245,resolucion[1]/4-150])
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type==pygame.MOUSEBUTTONDOWN and event.button==1 and jugar.collidepoint(pygame.mouse.get_pos()):
            ejecucion_juego(ventana)
        if event.type==pygame.MOUSEBUTTONDOWN and event.button==1 and opciones.collidepoint(pygame.mouse.get_pos()):
            print("click2")
        if event.type==pygame.MOUSEBUTTONDOWN and event.button==1 and extras.collidepoint(pygame.mouse.get_pos()):
            print("click3")
        if event.type==pygame.MOUSEBUTTONDOWN and event.button==1 and salir.collidepoint(pygame.mouse.get_pos()):
            run=False
            
    #dibujar pantalla
    crear_boton(ventana,jugar,"Jugar",30)
    crear_boton(ventana,opciones,"Opciones",30)
    crear_boton(ventana,extras,"Extras",30)
    crear_boton(ventana,salir,"Salir",30)
    
    pygame.display.flip()
