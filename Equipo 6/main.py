

import pygame
import sys
from random import *
from pygame.locals import *
import random

def escribir_pantalla(surface, text, size, x, y):               #muestra mensajes en pantalla
    font = pygame.font.SysFont("arial", size)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surface.blit(text_surface, text_rect)

def puntuacion(score):
    score += 25         #suma 25 por cada cuadrado pintado
    return score

def enemigos(e_x, e_y, e_x2, e_y2, tablero):  # enemigos
    if random.uniform(0, 1) <= 0.5:             # enemigo 1
        if random.uniform(0, 1) <= 0.5:         #probabilidad derecha o izquierda
            if e_x != 9:                        #limite
                e_x += 1
                if tablero[e_x][e_y] == -1:     #si toca obstaculo
                    e_x -= 1
        else:                                  #movimiento derecha o izquierda
            if e_x != 0:                       #limite
                e_x -= 1
                if tablero[e_x][e_y] == -1:    #si toca enemigo
                    e_x += 1
    else:
        if random.uniform(0, 1) <= 0.5:        #probabilidad arriba o abajo
            if e_y != 0:                       #limite
                e_y -=1
                if tablero[e_x][e_y] == -1:    #si toca obstaculo
                    e_y += 1
        else:                                  #probabilidad arriba o abajo
            if e_y != 9:                       #limite
                e_y += 1
                if tablero[e_x][e_y] == -1:    #si toca obstaculo
                    e_y -= 1

    if random.uniform(0, 1) <= 0.5:            #enemigo 2
        if random.uniform(0, 1) <= 0.5:        #probabilidad izquiera o derecha
            if e_x2 != 9:                      #limite
                e_x2 += 1
                if tablero[e_x2][e_y2] == -1:  #si toca obstaculo
                    e_x2 -= 1
                if e_x == e_x2:                #que sea diferente de enemigo 1
                    e_x2 -= 1
        else:                                 #probabilidad izquiera o derecha
            if e_x2 != 0:                     #limite
                e_x2 -= 1
                if tablero[e_x2][e_y2] == -1: #si toca obstacuo
                    e_x2 += 1
                if e_x == e_x2:
                    e_x2 += 1                   #que sea diferente de enemigo 1
    else:
        if random.uniform(0, 1) <= 0.5:     #probabilidad arriba o abajo
            if e_y2 != 0:                       #limite
                e_y2 -= 1
                if tablero[e_x2][e_y2] == -1:   #si toca obstaculo
                    e_y2 += 1
                if e_y == e_y2:                 #que sea diferente de enemigo 1
                    e_y2 += 1
        else:                                 #probabilidad arriba o abajo
            if e_y2 != 9:                     #limite
                e_y2 += 1
                if tablero[e_x2][e_y2] == -1:   #si toca obstaculo
                    e_y2 -= 1
                if e_y == e_y2:                 #que sea diferente de enemigo 1
                    e_y2 -= 1

    return e_x, e_y, e_x2, e_y2

def ganar(tablero):                     #funcion ganar
    for i in range(len(tablero)):
        for j in range(len(tablero[i])):
            if tablero[i][j] == 0:         #si todos los cuadrados estan pintados
                return True
    else:
        return False

def pantalla_inicio(ventana):               #primera pantalla
    escribir_pantalla(ventana, "Para empezar la partida aprete ENTER", 40, 500, 100)
    escribir_pantalla(ventana, "Para ver las instrucciones aprete i", 40, 500, 150)
    pygame.display.flip()

def instrucciones(ventana):         #instrucciones en la primera pantalla
    escribir_pantalla(ventana, "Usted se mueve con las teclas", 40, 500, 250)
    escribir_pantalla(ventana, "W", 50, 500, 300)
    escribir_pantalla(ventana, "S", 50, 500, 350)
    escribir_pantalla(ventana, "A", 50, 450, 350)
    escribir_pantalla(ventana, "D", 50, 550, 350)
    escribir_pantalla(ventana, "Cuenta con 3 vidas cada vez que pierda una", 40, 500, 450)
    escribir_pantalla(ventana, "Regresará al lugar de inicio sin reiniciar el progreso", 40, 500, 500)
    escribir_pantalla(ventana, "Por cada cuadrito pintado = 25pts, si colisionas con un cuadrado amarillo = -500 pts ", 30 , 500, 550)
    pygame.display.flip()

def perder(v):
    if v == 1:          #vida minima
        return False
    else:
        return True

def pantalla_perder(ventana):
    escribir_pantalla(ventana, "Perdiste", 50, 800, 250)
    pygame.display.flip
    waiting = True
    reloj = pygame.time.Clock()
    while waiting:
        reloj.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False

def pantalla_ganar(ventana):
    escribir_pantalla(ventana, "Victory Royale", 40, 800, 250)
    pygame.display.flip()
    waiting = True
    reloj = pygame.time.Clock()
    while waiting:
        reloj.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False

def colision(c_x, c_y, e_x, e_y, e_x2, e_y2, score, v):  # Choque enemigo1
    if c_x == e_x and c_y == e_y:
        c_x = 0
        c_y = 0
        e_x = 5
        e_y = 5
        score -= 500
        v -= 33
    if c_x == e_x2 and c_y == e_y2:
        c_x = 0
        c_y = 0
        e_x2 = 4
        e_y2 = 4
        score -= 500
        v -= 33
    return c_x, c_y, e_x, e_y, e_x2, e_y2, score, v

def vida(surface, x, y, life):
    Ancho = 100    #ancho barra
    Largo = 10     #largo barra
    fill = (life / 100) * Ancho
    border = pygame.Rect(x, y, Ancho, Largo)
    fill = pygame.Rect(x, y, fill, Largo)
    pygame.draw.rect(surface, (0, 255, 0), fill)
    pygame.draw.rect(surface, (255, 255, 255), border, 2)
    pygame.display.flip()

def main():
    ancho = 700  # tamaño
    alto = 1000  # tamaño
    pygame.init()
    ventana = pygame.display.set_mode((alto, ancho))
    pygame.display.set_caption("Qbert")  # nombre del juego
    pygame.display.flip()

    c_x = 0             #cordenada x del jugador
    c_y = 0             #cordenada y del jugador
    e_x = 0             #cordenada x del enemigo
    e_y = 9             #cordenada y del enemigo
    e_x2 = 9            #cordenada x del enemigo 2
    e_y2 = 0            #cordenada y del enemigo 2
    v = 100             #vida maxima
    score = 0           #puntaje inicial

    pygame.display.flip()
    reloj = pygame.time.Clock()

    run = True                  # juego iniciado

    tablero = []                # matriz del tablero
    for i in range(10):
        tablero.append([])
        for j in range(10):
            tablero[i].append(0)
    tablero[0][0] = 1

    a = randint(2, 9)      #cordenada obstaculos
    b = randint(2, 9)      #cordenada obstaculos
    for k in range(1, 3):  # obstaculos
        for i in range(3):
            tablero[b][k] = -1
            tablero[i][a] = -1
            tablero[b][a] = -1

    inicio = True                           #pantalla inicio
     # puntaje
    game_over = True
    while inicio:
        pantalla_inicio(ventana)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # cierre de ventana
                run = False                #no corre el juego
                inicio = False             #no corre la pantalla principal
            if event.type == pygame.KEYDOWN:
                tecla = pygame.key.name(event.key)
                if tecla == "return":           #si presiona enter
                    inicio = False              #paso a pantalla juego
                if tecla == "i":
                    instrucciones(ventana)      # si presiona i muestra instrucciones

    while run:
        reloj.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # cierre de ventana
                run = False                #no corre el juego
            if event.type == pygame.KEYDOWN:
                tecla = pygame.key.name(event.key)
                if game_over:
                    if tecla == "w":  # mover arriba
                        if c_y != 0:  # limite
                            c_y -= 1
                            if tablero[c_x][c_y] == -1:  # si pisa obstaculo
                                c_y += 1
                            else:
                                e_x, e_y, e_x2, e_y2 = enemigos(e_x, e_y, e_x2, e_y2, tablero)  # mover enemigos
                                c_x, c_y, e_x, e_y, e_x2, e_y2, score, v = colision(c_x, c_y, e_x, e_y, e_x2, e_y2,score, v)  # colision con enemigos
                        if tablero[c_x][c_y] == 1:  # cambio a sin color
                            tablero[c_x][c_y] = 0
                        else:
                            tablero[c_x][c_y] = 1  # cambio a color
                            score = puntuacion(score)  # puntuacion

                    if tecla == "s":  # mover abajo
                        if c_y != 9:  # limite
                            c_y += 1
                            if tablero[c_x][c_y] == -1:  # si pisa obstaculo
                                c_y -= 1
                            else:
                                e_x, e_y, e_x2, e_y2 = enemigos(e_x, e_y, e_x2, e_y2, tablero)  # mover enemigos
                                c_x, c_y, e_x, e_y, e_x2, e_y2, score, v = colision(c_x, c_y, e_x, e_y, e_x2, e_y2,score, v)  # colision con enemigos
                        if tablero[c_x][c_y] == 1:  # cambio a sin color
                            tablero[c_x][c_y] = 0
                        else:
                            tablero[c_x][c_y] = 1  # cambio a color
                            score = puntuacion(score)  # puntuacion

                    if tecla == "d":  # mover derecha
                        if c_x != 9:  # limite
                            c_x += 1
                            if tablero[c_x][c_y] == -1:  # si pisa obstaculo
                                c_x -= 1
                            else:
                                e_x, e_y, e_x2, e_y2 = enemigos(e_x, e_y, e_x2, e_y2, tablero)  # mover enemigos
                                c_x, c_y, e_x, e_y, e_x2, e_y2, score, v = colision(c_x, c_y, e_x, e_y, e_x2, e_y2,score, v)  # colision con enemigos
                        if tablero[c_x][c_y] == 1:  # cambio a sin color
                            tablero[c_x][c_y] = 0
                        else:
                            tablero[c_x][c_y] = 1  # cambio a color
                            score = puntuacion(score)  # puntuacion

                    if tecla == "a":  # mover izquierda
                        if c_x != 0:  # limite
                            c_x -= 1
                            if tablero[c_x][c_y] == -1:  # pisa obstaculoa
                                c_x +=1
                            else:
                                e_x, e_y, e_x2, e_y2 = enemigos(e_x, e_y, e_x2, e_y2, tablero)  # mover enemigos
                                c_x, c_y, e_x, e_y, e_x2, e_y2, score, v = colision(c_x, c_y, e_x, e_y, e_x2, e_y2,score, v)  # colision con enemigos
                        if tablero[c_x][c_y] == 1:  # cambio a sin color
                            tablero[c_x][c_y] = 0
                        else:
                            tablero[c_x][c_y] = 1  # cambio a color
                            score = puntuacion(score)  # puntuacion

            ventana.fill((0, 0, 0))  # fondo

            for i in range(len(tablero)):  # estados
                for j in range(len(tablero[i])):
                    if tablero[i][j] == 0:
                        pygame.draw.rect(ventana, (255, 255, 255), pygame.Rect(10 + 60 * i, 10 + 60 * j, 30, 30))   #cuadro sin pintar
                    if tablero[i][j] == 1:
                        pygame.draw.rect(ventana, (255, 0, 0), pygame.Rect(10 + 60 * i, 10 + 60 * j, 30, 30))   #cuadro pintado
                    if tablero[i][j] == -1:
                        pygame.draw.rect(ventana, (0, 0, 255), pygame.Rect(10 + 60 * i, 10 + 60 * j, 30, 30))   #obstaculo

            pygame.draw.rect(ventana, (0, 255, 0), pygame.Rect(60 * c_x, 60 * c_y, 50, 50))  # jugador

            pygame.draw.rect(ventana, (255, 255, 0), pygame.Rect(60 * e_x, 60 * e_y, 50, 50))  # enemigo

            pygame.draw.rect(ventana, (255, 255, 0), pygame.Rect(60 * e_x2, 60 * e_y2, 50, 50))  # enemigo 2

            escribir_pantalla(ventana, str(score), 30, 800, 0)      #muestra puntaje
            escribir_pantalla(ventana, "score:", 30, 700, 0)        #muestra puntaje
            vida(ventana, 650, 50, v)           #llama a la funcion vida
            pygame.display.flip()

        if perder(v):
            game_over = True                    #cierra juego
        else:
            pantalla_perder(ventana)            #muestra mensaje perder
            game_over = False                   #cierra el juego

        if ganar(tablero):
            game_over = True
        else:
            pantalla_ganar(ventana)             #muestra mensaje ganar
            game_over = False                   #cierra el juego
        pygame.display.flip()
    sys.exit()

main()
