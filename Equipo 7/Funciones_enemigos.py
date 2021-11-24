import pygame,sys,random,os

#colores
blanco=[255,255,255]
negro=[0,0,0]
rojo=[255,0,0]
verde=[0,255,0]
azul=[0,0,255]
verdeazul=[0, 200, 70]

#detecta colision
def detectar_colision(tecla,movx,movy,lista1):
    if tecla=="w":
        if movy==0 or lista1[movx][movy-1][2]==1:
            return 0
        else:
            return "w"
    if tecla=="a":
        if movx==0 or lista1[movx-1][movy][2]==1:
            return 0
        else:
            return "a"
    if tecla=="s":
        if movy==9 or lista1[movx][movy+1][2]==1:
            return 0
        else:
            return "s"
    if tecla=="d":
        if movx==9 or lista1[movx+1][movy][2]==1:
            return 0
        else:
            return "d"

#colision_entre_enemigos
def colision_entre_enemigos(direccion,moex_inicial,moey_inicial,moex_secundario,moey_secundario):
    
    if direccion=="w":
        if (moex_inicial==moex_secundario and moey_inicial-1==moey_secundario) or (moex_inicial<3 and moey_inicial<3):
            return False
        else:
            return True
    if direccion=="a":
        if moex_inicial-1==moex_secundario and moey_inicial==moey_secundario or (moex_inicial<3 and moey_inicial<3):
            return False
        else:
            return True
    if direccion=="s":
        if moex_inicial==moex_secundario and moey_inicial+1==moey_secundario:
            return False
        else:
            return True
    if direccion=="d":
        if moex_inicial+1==moex_secundario and moey_inicial==moey_secundario:
            return False
        else:
            return True


#movimiento enemigo
def movimiento_enemigo(moex_inicial,moey_inicial,moex_secundario,moey_secundario,lista1,xd):
    direccion=direccion_alea_enemigo()
    if direccion=="arriba":
        if detectar_colision("w",moex_inicial,moey_inicial,lista1)=="w" and colision_entre_enemigos("w",moex_inicial,moey_inicial,moex_secundario,moey_secundario):
            moey_inicial-=1
        else:
            moey_inicial+=0
    if direccion=="izquierda":
        if detectar_colision("a",moex_inicial,moey_inicial,lista1)=="a" and colision_entre_enemigos("a",moex_inicial,moey_inicial,moex_secundario,moey_secundario):
            moex_inicial-=1
            xd=0
        else:
            moex_inicial+=0
    if direccion=="abajo":
        if detectar_colision("s",moex_inicial,moey_inicial,lista1)=="s" and colision_entre_enemigos("s",moex_inicial,moey_inicial,moex_secundario,moey_secundario):
            moey_inicial+=1
        else:
            moey_inicial+=0
    if direccion=="derecha":
        if detectar_colision("d",moex_inicial,moey_inicial,lista1)=="d" and colision_entre_enemigos("d",moex_inicial,moey_inicial,moex_secundario,moey_secundario):
            moex_inicial+=1
            xd=1
        else:
            moex_inicial+=0
    if direccion=="quieto":
            moex_inicial+=0
        
    return [moex_inicial,moey_inicial,xd]

#generacion de enemigos
def generacion_enemigos(lista):
    bachelet_onu=True
    moex=random.randint(4,9)
    moey=random.randint(4,9)
    while bachelet_onu:
        if lista[moex][moey][2]==1:
            moex=random.randint(4,9)
            moey=random.randint(4,9)
        else:
            bachelet_onu=False
    return [moex,moey]

#direccion enemigo
def direccion_alea_enemigo():
    direccion=random.randint(0,4)
    if direccion==0:
        return "arriba"
    if direccion==1:
        return "izquierda"
    if direccion==2:
        return "abajo"
    if direccion==3:
        return "derecha"
    if direccion==4:
        return "quieto"

#detectar colision jugador-enemigo
def detectar_jugadorenemigo(enemigox,enemigoy,jugadorx,jugadory,lista):
    ex1=lista[enemigox][enemigoy][0]
    ey1=lista[enemigox][enemigoy][1]
    jx1=lista[jugadorx][jugadory][0]
    jy1=lista[jugadorx][jugadory][1]
    if ex1==jx1 and ey1==jy1:
        return True
