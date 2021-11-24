

import pygame 
import random 
import sys 


#Tamaño de la ventana 
ancho_ventana = 1110
alto_ventana  = 555

#Colores 
Negro = (0, 0, 0)
Blanco = (255, 255, 255)
Verde = (0, 255, 0)
Rojo = (255, 0, 0)
Azul = (81, 209, 246)
NARANJO = (255, 81, 0)
Gris = (157, 157, 157)
Amarillo = (253, 253, 150)
Morado = (58, 20, 160)
#Tamaño casillas
Largo = 50
Alto  = 50

#Espacio entre las casillas
Margen = 5

#Tablero__Matriz
tablero = []
for fila in range (10):
    tablero.append([])
    for columna in range (10):
        tablero[fila].append(0)

#número random coordenada X (Obstaculo 1 casilla)
x1 = [5, 60, 115, 170, 225, 280, 335, 390, 445, 500]
indiceX1 = random.randint(0, len(x1)-1)
Xnumero_random1 = x1[indiceX1]
#número random coordenada y (Obstaculo 1 casilla)
y1 = [60, 115, 170, 225, 280, 335, 390, 445, 500]
indiceY1 = random.randint(0, len(y1)-1)
Ynumero_random1 = y1[indiceY1]


#número random coordenada X (obstaculo 2 casillas)
del x1[indiceX1], x1[8]
x2 = x1
indiceX2 = random.randint(0, len(x2)-1)
Xnumero_random2 = x2[indiceX2]
#número random coordenada y (enemigo2)
del y1[indiceY1]
y2 = y1
indiceY2 = random.randint(0, len(y2)-1)
Ynumero_random2 = y2[indiceY2]
#2°Cuadradito
xSegundocuadrado = Xnumero_random2 + 55
ySegundoCuadrado = Ynumero_random2

#número random coordenada X (obstaculo 3 casillas)
del x2[indiceX2]
if indiceX2 != len(x2):
    del x2[indiceX2]
x3 = x2
indiceX3 = random.randint(0, len(x3)-1)
Xnumero_random3 = x3[indiceX3]
#número random coordenada y (enemigo2)
del y2[indiceY2], y2[6]
y3 = y2
indiceY3 = random.randint(0, len(y3)-1)
Ynumero_random3 = y3[indiceY3]
#2° Cuadradito 2
xSegundocuadrado2 = Xnumero_random3 + 55
ySegundoCuadrado2 = Ynumero_random3
#3° Cuadradito 2
xTercercuadrado2 = Xnumero_random3
yTercercuadrado2 = Ynumero_random3 + 55

del x3[indiceX3]
x4= x3
del y3[indiceY3]
y4= y3

#Aparición enemigo 1 en x
xenem1= x4
indicexenem1= random.randint(0, len(xenem1)-1)
xaparenem1= xenem1[indicexenem1]
del xenem1[indicexenem1]
x5= x4

#Aparicion enemigo 1 en y
yenem1 = y4
indiceyenem1 = random.randint(0, len(yenem1)-1)
yaparenem1 = yenem1[indiceyenem1]
del y4[indiceyenem1]
y5 = y4
#Aparición enemigo 2 en x
xenem2= x5
indicexenem2= random.randint(0, len(xenem2)-1)
xaparenem2= xenem2[indicexenem2]
#Aparicion enemigo 2 en y
yenem2 = y5
indiceyenem2 = random.randint(0, len(yenem2)-1)
yaparenem2 = yenem2[indiceyenem2]

def movimientoEnemigo(x, y, Xnumero_random1,Ynumero_random1 , Xnumero_random2, Ynumero_random2, Xnumero_random3, Ynumero_random3, xSegundocuadrado, ySegundocuadrado, xSegundocuadrado2, ySegundoCuadrado2):
    #Mov. enemigo1 basado en jugador
    if random.uniform(0, 1) <= 0.5:
        if random.uniform(0, 1) <= 0.5:
            if x < 500:
                if (x == Xnumero_random1-55 and y==Ynumero_random1):
                    x += 0
                elif (x == Xnumero_random2-55 and y==Ynumero_random2):
                    x += 0
                elif (x == Xnumero_random3-55 and y == Ynumero_random3) or (x == xTercercuadrado2-55 and y == yTercercuadrado2):
                    x += 0
                else:
                    x += 55
        else:
            if x > 5:
                if (x == Xnumero_random1+55 and y==Ynumero_random1):
                    x -= 0
                elif (x == xSegundocuadrado+55 and y==ySegundoCuadrado):
                    x += 0
                elif (x == xSegundocuadrado2+55 and y == ySegundoCuadrado2):
                    x += 0
                elif (x == Xnumero_random3+55 and y == Ynumero_random3+55):
                    x += 0
                else:
                    x -= 55
    else:
        if random.uniform(0, 1) <= 0.5:
            if (y > 60):
                if (x == Xnumero_random1 and y==Ynumero_random1+55):
                    y += 0
                elif (x == Xnumero_random2 and y==Ynumero_random2+55) or (x == xSegundocuadrado and y==ySegundoCuadrado+55):
                    y += 0
                elif (x == xTercercuadrado2 and y == yTercercuadrado2+55):
                    y += 0
                elif (x == Xnumero_random3+55 and y == Ynumero_random3+55):
                    y += 0
                else:
                    y -= 55
        else:
            if y < 500:
                if (x == Xnumero_random1 and y==Ynumero_random1-55):
                    y += 0
                elif (x == Xnumero_random2 and y==Ynumero_random2-55) or (x == xSegundocuadrado and y==ySegundoCuadrado-55):
                    y += 0
                elif (x == Xnumero_random3 and y == Ynumero_random3-55) or (x == xSegundocuadrado2 and y == ySegundoCuadrado2-55):
                    y += 0
                else:
                    y += 55
    return x,y


def main():
    pygame.init()

    puntos = 0
    fuente1 = pygame.font.SysFont("Comicsans", 70)
    texto_puntos = fuente1.render("Puntaje: " +str(puntos),True, Blanco)


    vidas = 3

    #Fotos
    #fondo
    fondo = pygame.image.load("Space1.png")
    fondo1 = pygame.transform.scale(fondo, (1110, 800))


    #qberto 
    qberto = pygame.image.load("Sprite-0001.png")
    qberto1 = pygame.transform.scale(qberto, (50, 50))

    fotoqbert = pygame.image.load("Qberto.png")
    fotoqbert1 = pygame.transform.scale(fotoqbert, (500, 500))

    #Logos
    logo = pygame.image.load("Sprite-0004.png")
    logo1 = pygame.transform.scale(logo, (500, 150))
    logo2 = pygame.transform.scale(logo, (400, 120))

    #corazones
    corazon = pygame.image.load("Sprite-0006.png")
    corazonvacio = pygame.image.load("Sprite-0005.png")

    corazon1 = pygame.transform.scale(corazon, (70, 70))
    corazonvacio1 = pygame.transform.scale(corazonvacio, (70, 70))

    casilla1 = pygame.image.load("casilla1.png")
    casilla11 = pygame.transform.scale(casilla1, (50,50))

    casilla2 = pygame.image.load("casilla2.png") 
    casilla22 = pygame.transform.scale(casilla2, (50,50))

    casilla3 = pygame.image.load("casilla3.png")
    casilla33 = pygame.transform.scale(casilla3, (50,50))

    casilla4 = pygame.image.load("casilla4.png")
    casilla44 = pygame.transform.scale(casilla4, (50,50))
    
    #enemigos
    enemigo1 = pygame.image.load("Sprite-0007.png")
    enemigo11 = pygame.transform.scale(enemigo1, (50, 50))


    enemigo2= pygame.image.load("Sprite-0011.png")
    enemigo22 = pygame.transform.scale(enemigo2, (50, 50))


    #fotos teclas 
    w = pygame.image.load("TeclaW.png")
    w1 = pygame.transform.scale(w, (70, 70))

    a = pygame.image.load("TeclaA.png")
    a1 = pygame.transform.scale(a, (70, 70))

    s = pygame.image.load("TeclaS.png")
    s1 = pygame.transform.scale(s, (70, 70))

    d = pygame.image.load("TeclaD.png")
    d1 = pygame.transform.scale(d, (70, 70))

    r = pygame.image.load("TeclaR.png")
    r1 = pygame.transform.scale(r, (100, 100))

    

    #derrota
    derrota = pygame.image.load("Sprite-derrota.png")
    derrota1 = pygame.transform.scale(derrota, (500, 110))

    #victoria
    victoria = pygame.image.load("Sprite-victoria.png")
    victoria1 = pygame.transform.scale(victoria, (490, 100))
    fondovictoria = pygame.image.load("PantallaVictoria.png")
    fondovictoria1 = pygame.transform.scale(fondovictoria, (1150, 555))

    #menu
    pantallamenu = pygame.image.load("pantalla_principal.png")
    pantallamenu1 = pygame.transform.scale(pantallamenu, (1150, 555))


    #Audios
    salto = pygame.mixer.Sound("qbertsalto.wav")
    gameover = pygame.mixer.Sound("GameOver.wav")
    victory = pygame.mixer.Sound("Victoria.wav")



    #Ventana 
    ventana =  pygame.display.set_mode((ancho_ventana, alto_ventana))

    #Titulo de ventana 
    pygame.display.set_caption("Cuberto")

    #Color ventana
    ventana.fill((42, 84,92))
    
    #
    pygame.display.flip()
    
    #FPS
    reloj = pygame.time.Clock()

    #
    Funcionando = True
    menu = True
    perdiste = False

    #Creación de personaje 
    xPersonaje = Margen     # (5,5)
    yPersonaje = Margen     
    pygame.draw.rect(ventana, (255,255,0), pygame.Rect(xPersonaje,yPersonaje, 50,50)) 

    
    #Creación de enemigos
    xenemigo1= xaparenem1
    yenemigo1= yaparenem1

    xenemigo2= xaparenem2
    yenemigo2= yaparenem2
    
  
    menu = True
    perdiste = False
    ganar = 0
    ganaste = False
    
    while menu:

        reloj.tick(60)
                 
        ventana.fill((166, 166, 166))
        ventana.blit(pantallamenu1, [0,0])
        
        #ventana.blit(logo1, [300,50])
        #teclas
        ventana.blit(w1, [950, 370])
        ventana.blit(s1, [950, 450])
        ventana.blit(a1, [870, 450])
        ventana.blit(d1, [1030, 450])
        
        

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type==pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    menu = False

            if(event.type == pygame.QUIT):
                    menu = False
                    Funcionando = False
                    perdiste = False
 
    vidas = 3

    #While donde funciona el juego  산티아고 
    while Funcionando:
        reloj.tick(60)
        ventana.fill((38, 37, 37))
        ventana.blit(fondo1, [0,0])
        ventana.blit(fotoqbert1, [775, 205])
        texto_puntos = fuente1.render("Puntaje: " +str(puntos), True, Blanco)
        ventana.blit(texto_puntos, (700,300))

        #logo
        ventana.blit(logo2, [620, 30])

        #corazones
        if vidas == 3:        
            ventana.blit(corazon1, [700, 200])
            ventana.blit(corazon1, [800, 200])
            ventana.blit(corazon1, [900, 200])
        
        if vidas == 2:        
            ventana.blit(corazon1, [700, 200])
            ventana.blit(corazon1, [800, 200])
            ventana.blit(corazonvacio1, [900, 200])
        if vidas == 1:        
            ventana.blit(corazon1, [700, 200])
            ventana.blit(corazonvacio1, [800, 200])
            ventana.blit(corazonvacio1, [900, 200])
        if vidas == 0:
            gameover.play()
            Funcionando = False
            perdiste = True
            

        #Tablero
        tablero[0][0] = 2
        for fila in range(10):
            for columna in range(10):

                #Pintar tablero
                if tablero[fila][columna] == 1:
                    ventana.blit(casilla22, [(Margen+Largo) * columna +  Margen,(Margen+Alto) * fila + 5])


                if tablero[fila][columna] == 0:
                    ventana.blit(casilla11, [(Margen+Largo) * columna +  Margen,(Margen+Alto) * fila + 5])

                if tablero[fila][columna] == 2:
                    ventana.blit(casilla44, [(Margen+Largo) * columna +  Margen,(Margen+Alto) * fila + 5])
                

        #Obstaculo 1 casilla
        ventana.blit(casilla33, [Xnumero_random1,Ynumero_random1])

        #Obstaculo 2 casillas
        ventana.blit(casilla33, [Xnumero_random2,Ynumero_random2]) 
        ventana.blit(casilla33, [xSegundocuadrado,ySegundoCuadrado])

        #Obstaculo 3 casillas
        ventana.blit(casilla33, [Xnumero_random3,Ynumero_random3])
        ventana.blit(casilla33, [xSegundocuadrado2,ySegundoCuadrado2])
        ventana.blit(casilla33, [xTercercuadrado2, yTercercuadrado2])

        #Pintar casilla 0,0
        #tablero[0][0] = 2

        #Creacion de personaje
        ventana.blit(qberto1, [xPersonaje, yPersonaje]) 

        #Enemigo1
        ventana.blit(enemigo11, [xenemigo1, yenemigo1])
        
        #Enemigo2
        ventana.blit(enemigo22, [xenemigo2, yenemigo2])
        
        #Eventos de Pygame 
        for event in pygame.event.get():

            #cerrar ventana
            if(event.type == pygame.QUIT):
                Funcionando = False
            #Movimiento del personaje
            if event.type == pygame.KEYDOWN:
                tecla_presionada = pygame.key.name(event.key)

                #Movimiento hacia arriba
                if tecla_presionada == 'w':                       
                    if (yPersonaje > 5):
                        if (xPersonaje == Xnumero_random1 and yPersonaje==Ynumero_random1+55):
                            yPersonaje += 0
                        elif (xPersonaje == Xnumero_random2 and yPersonaje==Ynumero_random2+55) or (xPersonaje == xSegundocuadrado and yPersonaje==ySegundoCuadrado+55):
                            yPersonaje += 0
                        elif (xPersonaje == xTercercuadrado2 and yPersonaje == yTercercuadrado2+55):
                            yPersonaje += 0
                        elif (xPersonaje == Xnumero_random3+55 and yPersonaje == Ynumero_random3+55):
                                yPersonaje += 0
                        else:                           
                            yPersonaje -= 55
                            pos = xPersonaje, yPersonaje
                            columna = pos[0] // (Largo + Margen)
                            fila = pos[1] // (Alto + Margen)
                
                            #pintar casillas
                            salto.play()
                            if tablero[fila][columna] == 0:
                                ganar += 1
                                puntos += 25     
                                tablero[fila][columna] = 1
                            elif tablero[fila][columna]==1:
                                ganar -= 1
                                tablero[fila][columna]=0

                            xenemigo1,yenemigo1 = movimientoEnemigo(xenemigo1, yenemigo1, Xnumero_random1, Ynumero_random1 , Xnumero_random2, Ynumero_random2, Xnumero_random3, Ynumero_random3, xSegundocuadrado, ySegundoCuadrado, xSegundocuadrado2,ySegundoCuadrado2)
                            xenemigo2,yenemigo2 = movimientoEnemigo(xenemigo2, yenemigo2, Xnumero_random1, Ynumero_random1 , Xnumero_random2, Ynumero_random2, Xnumero_random3, Ynumero_random3, xSegundocuadrado, ySegundoCuadrado, xSegundocuadrado2,ySegundoCuadrado2)
                            
                #Movimiento hacia la izquierda
                if tecla_presionada == 'a':
                    if xPersonaje > 5:
                        if (xPersonaje == Xnumero_random1+55 and yPersonaje==Ynumero_random1):
                            xPersonaje -= 0
                        elif (xPersonaje == xSegundocuadrado+55 and yPersonaje==ySegundoCuadrado):
                            xPersonaje += 0
                        elif (xPersonaje == xSegundocuadrado2+55 and yPersonaje == ySegundoCuadrado2):
                            xPersonaje += 0
                        elif (xPersonaje == Xnumero_random3+55 and yPersonaje == Ynumero_random3+55):
                            xPersonaje += 0
                        else:
                            xPersonaje -= 55
                            pos = xPersonaje, yPersonaje
                            columna = pos[0] // (Largo + Margen)
                            fila = pos[1] // (Alto + Margen)
                            #pintar casillas
                            salto.play()
                            if tablero[fila][columna] == 0:
                                ganar += 1 
                                puntos += 25      
                                tablero[fila][columna] = 1
                            elif tablero[fila][columna]==1:
                                ganar -= 1
                                tablero[fila][columna]=0

                            xenemigo1,yenemigo1 = movimientoEnemigo(xenemigo1, yenemigo1, Xnumero_random1, Ynumero_random1 , Xnumero_random2, Ynumero_random2, Xnumero_random3, Ynumero_random3, xSegundocuadrado, ySegundoCuadrado, xSegundocuadrado2,ySegundoCuadrado2)
                            xenemigo2,yenemigo2 = movimientoEnemigo(xenemigo2, yenemigo2, Xnumero_random1, Ynumero_random1 , Xnumero_random2, Ynumero_random2, Xnumero_random3, Ynumero_random3, xSegundocuadrado, ySegundoCuadrado, xSegundocuadrado2,ySegundoCuadrado2)
                          
                #Movimiento hacia abajo
                if tecla_presionada == 's':                    
                    if yPersonaje < 500:
                        if (xPersonaje == Xnumero_random1 and yPersonaje==Ynumero_random1-55):
                            yPersonaje += 0
                        elif (xPersonaje == Xnumero_random2 and yPersonaje==Ynumero_random2-55) or (xPersonaje == xSegundocuadrado and yPersonaje==ySegundoCuadrado-55):
                            yPersonaje += 0
                        elif (xPersonaje == Xnumero_random3 and yPersonaje == Ynumero_random3-55) or (xPersonaje == xSegundocuadrado2 and yPersonaje == ySegundoCuadrado2-55):
                            yPersonaje += 0
                        else:
                            yPersonaje += 55
                            pos = xPersonaje, yPersonaje
                            columna = pos[0] // (Largo + Margen)
                            fila = pos[1] // (Alto + Margen)
                            #pintar casillas
                            salto.play()
                            if tablero[fila][columna] == 0:     
                                tablero[fila][columna] = 1
                                ganar += 1
                                puntos += 25  
                            elif tablero[fila][columna]==1:
                                tablero[fila][columna]=0
                                ganar -= 1
                          
                            xenemigo1,yenemigo1 = movimientoEnemigo(xenemigo1, yenemigo1, Xnumero_random1, Ynumero_random1 , Xnumero_random2, Ynumero_random2, Xnumero_random3, Ynumero_random3, xSegundocuadrado, ySegundoCuadrado, xSegundocuadrado2,ySegundoCuadrado2)
                            xenemigo2,yenemigo2 = movimientoEnemigo(xenemigo2, yenemigo2, Xnumero_random1, Ynumero_random1 , Xnumero_random2, Ynumero_random2, Xnumero_random3, Ynumero_random3, xSegundocuadrado, ySegundoCuadrado, xSegundocuadrado2,ySegundoCuadrado2)
                                                       
                #Movimiento hacia la derecha 
                if tecla_presionada == 'd':                      
                    if xPersonaje < 500:
                        if (xPersonaje == Xnumero_random1-55 and yPersonaje==Ynumero_random1):
                            xPersonaje += 0
                        elif (xPersonaje == Xnumero_random2-55 and yPersonaje==Ynumero_random2):
                            xPersonaje += 0
                        elif (xPersonaje == Xnumero_random3-55 and yPersonaje == Ynumero_random3) or (xPersonaje == xTercercuadrado2-55 and yPersonaje == yTercercuadrado2):
                            xPersonaje += 0
                        else:
                            xPersonaje += 55
                            pos = xPersonaje, yPersonaje
                            columna = pos[0] // (Largo + Margen)
                            fila = pos[1] // (Alto + Margen)
                            salto.play()
                            #pintar casillas
                            if tablero[fila][columna] == 0:     
                                tablero[fila][columna] = 1
                                ganar += 1
                                puntos += 25  
                            elif tablero[fila][columna]==1:
                                ganar -= 1
                                tablero[fila][columna]=0

                            xenemigo1,yenemigo1 = movimientoEnemigo(xenemigo1, yenemigo1, Xnumero_random1, Ynumero_random1 , Xnumero_random2, Ynumero_random2, Xnumero_random3, Ynumero_random3, xSegundocuadrado, ySegundoCuadrado, xSegundocuadrado2,ySegundoCuadrado2)
                            xenemigo2,yenemigo2 = movimientoEnemigo(xenemigo2, yenemigo2, Xnumero_random1, Ynumero_random1 , Xnumero_random2, Ynumero_random2, Xnumero_random3, Ynumero_random3, xSegundocuadrado, ySegundoCuadrado, xSegundocuadrado2,ySegundoCuadrado2)

                if (xPersonaje == xenemigo1 and yPersonaje == yenemigo1) or (xPersonaje == xenemigo2 and yPersonaje == yenemigo2):
                    vidas-=1
                    xPersonaje = 5
                    yPersonaje = 5
            
                if (xenemigo1 == xenemigo2) and (yenemigo1 == yenemigo2):
                    if random.uniform(0, 1) <= 0.5:
                        if random.uniform(0, 1) <= 0.5:
                            if xenemigo1 < 500:
                                if (xenemigo1 == Xnumero_random1-55 and yenemigo1==Ynumero_random1):
                                    xenemigo1 += 0
                                elif (xenemigo1 == Xnumero_random2-55 and yenemigo1==Ynumero_random2):
                                    xenemigo1 += 0
                                elif (xenemigo1 == Xnumero_random3-55 and yenemigo1 == Ynumero_random3) or (xenemigo1 == xTercercuadrado2-55 and yenemigo1 == yTercercuadrado2):
                                    xenemigo1 += 0
                                else:
                                    xenemigo1 += 55
                            else:
                                xenemigo1 -= 55
                        else:
                            if xenemigo1 > 5:
                                if (xenemigo1 == Xnumero_random1+55 and yenemigo1==Ynumero_random1):
                                    xenemigo1 -= 0
                                elif (xenemigo1 == xSegundocuadrado+55 and yenemigo1==ySegundoCuadrado):
                                    xenemigo1 += 0
                                elif (xenemigo1 == xSegundocuadrado2+55 and yenemigo1 == ySegundoCuadrado2):
                                    xenemigo1 += 0
                                elif (xenemigo1 == Xnumero_random3+55 and yenemigo1 == Ynumero_random3+55):
                                    xenemigo1 += 0
                                else:
                                    xenemigo1 -= 55
                            else:
                                xenemigo1+=55
                    else:
                        if random.uniform(0, 1) <= 0.5:
                            if (yenemigo1 > 60):
                                if (xenemigo1 == Xnumero_random1 and yenemigo1==Ynumero_random1+55):
                                    yenemigo1 += 0
                                elif (xenemigo1 == Xnumero_random2 and yenemigo1==Ynumero_random2+55) or (xenemigo1 == xSegundocuadrado and yenemigo1==ySegundoCuadrado+55):
                                    yenemigo1 += 0
                                elif (xenemigo1 == xTercercuadrado2 and yenemigo1 == yTercercuadrado2+55):
                                    yenemigo1 += 0
                                elif (xenemigo1 == Xnumero_random3+55 and yenemigo1 == Ynumero_random3+55):
                                    yenemigo1 += 0
                                else:
                                    yenemigo1 -= 55
                            else:
                                yenemigo1 += 55
                        else:
                            if yenemigo1 < 500:
                                if (xenemigo1 == Xnumero_random1 and yenemigo1==Ynumero_random1-55):
                                    yenemigo1 += 0
                                elif (xenemigo1 == Xnumero_random2 and yenemigo1==Ynumero_random2-55) or (xenemigo1 == xSegundocuadrado and yenemigo1==ySegundoCuadrado-55):
                                    yenemigo1 += 0
                                elif (xenemigo1 == Xnumero_random3 and yenemigo1 == Ynumero_random3-55) or (xenemigo1 == xSegundocuadrado2 and yenemigo1 == ySegundoCuadrado2-55):
                                    yenemigo1 += 0
                                else:
                                    yenemigo1 += 55
                            else:
                                yenemigo1 -= 55



        if ganar == 93:
            victory.play()
            Funcionando = False
            ganaste = True

        pygame.display.flip()

        while ganaste:
            reloj.tick(60)         
            ventana.fill((Negro))
            ventana.blit(fondovictoria1, [0,0])
            ventana.blit(victoria1, [310,180])
            ventana.blit(r1, [950, 400])
            texto_puntos = fuente1.render("Puntaje: " +str(puntos), True, Blanco)
            ventana.blit(texto_puntos, (400,450))




            for event in pygame.event.get():
                if(event.type == pygame.QUIT):
                        menu = False
                        Funcionando = False
                        perdiste = False
                        ganaste = False
                if event.type==pygame.KEYDOWN:
                    tecla_presionada = pygame.key.name(event.key)
                    if tecla_presionada == "r":
                        ganar = 0   
                        perdiste = False
                        menu = False
                        Funcionando = True
                        ganaste = False
                            
                        xPersonaje = 5
                        yPersonaje = 5
                        vidas = 3
                        puntos = 0 
                            
                        for i in range(10):
                            for j in range(10):
                                tablero[i][j]=0
                        #tablero[1][2]=0
                        pygame.display.flip()
                            
                    
                    #cerrar ventana
                if(event.type == pygame.QUIT):
                    menu = False
                    Funcionando = False
                    perdiste = False

            pygame.display.flip()

        while perdiste:

                
            reloj.tick(60)         
            ventana.fill((166, 166, 166))
            ventana.blit(fondo, [0,0])
            ventana.blit(derrota1, [310,50])
            ventana.blit(r1, [500, 300])
            texto_puntos = fuente1.render("Puntaje: " +str(puntos), True, Blanco)
            ventana.blit(texto_puntos, (400,200))

            for event in pygame.event.get():
                if event.type==pygame.KEYDOWN:
                    tecla_presionada = pygame.key.name(event.key)
                    if tecla_presionada == "r":
                        ganar = 0   
                        perdiste = False
                        menu = False
                        Funcionando = True
                            
                        xPersonaje = 5
                        yPersonaje = 5
                        vidas = 3
                        puntos = 0 
                            
                        for i in range(10):
                            for j in range(10):
                                tablero[i][j]=0
                        #tablero[1][2]=0
                        pygame.display.flip()
                            
                    
                    #cerrar ventana
                if(event.type == pygame.QUIT):
                    menu = False
                    Funcionando = False
                    perdiste = False

            pygame.display.flip()

    while ganaste:
        reloj.tick(60)         
        ventana.fill((166, 166, 166))

    pygame.quit()
    sys.exit()

   
main()



