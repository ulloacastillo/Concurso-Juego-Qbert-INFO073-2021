
import pygame
import sys
import random

ANCHO_VENTANA=1280
ALTO_VENTANA=720

def cambio_de_estado(a):     #Funcion que cambia el estado del tablero de 0 a 1 y viceversa para llamar dejar rastro
    if a == 1:
        a = 0
    else:
        a = 1
    return a

def mov_negativo(a, b ,c):   #Funcion que controla el limite, la posicion y moviemento del personaje al presionar "a" y "w"
    a -= 60
    b -= 1
    c -= 60
    return(a,b,c)

def mov_positivo(a,b,c):    #Funcion que controla el limite, la posicion y moviemento del personaje al presionar "s" y "d"
    a += 60
    b += 1
    c += 60
    return (a,b,c)

def colision(a,b,c,d,e,f,g,h): #Funcion que reinicia las variables del personaje y detiene los enemigos al morir
    a = 60
    b = 60
    c = 0
    d = 0
    e = 50
    f = 50
    g = False
    h -= 1

    return(a,b,c,d,e,f,g,h)

def victoria(lista):   #Funcion que recorre el tablero de estados y define si existe la victoria
    contador = 0
    for i in range (10):
        for j in range(10):
            if lista [i][j] == 1:
                contador += 1
    if contador == 94:
        return True
    else:
        return False

def main():
    pygame.init()
    
    ventana= pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    pygame.display.set_caption("The Indigenous Resistance")
    ventana.fill((0,255,0))

    fuentemedia = pygame.font.SysFont("arial black",60)
    fuentechica = pygame.font.SysFont("arial black",30)
    #-----------------------Texturas-----------------------
    personaje1=pygame.image.load("Personaje1.png")
    enemigo1=pygame.image.load("Enemy.png")
    enemigo2=pygame.image.load("Enemy2.png")
    obstaculo=pygame.image.load("Obstaculo1.png")
    tierra=pygame.image.load("Tierra1.png")
    trigo=pygame.image.load("Trigo.png")
    vida=pygame.image.load("corazon.png")
    vidaN=pygame.image.load("VidaN.png")
    fondo=pygame.image.load("Portada.jpg")
    fondoj=pygame.image.load("FondoJ.png")
    instrucciones=pygame.image.load("Instrucciones.jpg")
    encima = pygame.image.load("encima.png")
    victorioso = pygame.image.load("Victoria.jpg")
    perdedor = pygame.image.load("Perdiste1.jpg")
    
    #-----------------------Sonidos-----------------------
    pygame.mixer.music.load("Intro.mp3")

    #---------------Posiciones en ventana del personaje------------------------
    
    xCuadrado=60 
    yCuadrado=60

    #---------------Posiciones aleatorias de los obstaculos-----------------------

    x_uno_Obstaculo = random.randrange(1,9)
    y_uno_Obstaculo = random.randrange (1,9)
    
    x_dos_Obstaculo = random.randrange(1,9)
    y_dos_Obstaculo = random.randrange (1,8)

    x_tres_Obstaculo = random.randrange (1,7)
    y_tres_Obstaculo = random.randrange (1,9)    

    #--------------validaciones para que los obstaculos no se sobrepongan--------------------------------

    while y_uno_Obstaculo == y_tres_Obstaculo and (abs(x_tres_Obstaculo - x_uno_Obstaculo)) <= 3:  #En caso de caer en una misma posicion los obstaculos, se vuelve a generar una coordenad aleatoria.
        x_uno_Obstaculo = random.randrange(1,9)

    while x_uno_Obstaculo == x_dos_Obstaculo and (abs(y_dos_Obstaculo - y_uno_Obstaculo)) < 2:
        y_uno_Obstaculo = random.randrange (1,9)

    while y_dos_Obstaculo == y_tres_Obstaculo and (abs(x_tres_Obstaculo - x_dos_Obstaculo)) < 3:
        y_tres_Obstaculo = random.randrange (1,9)
            

    while ((abs(x_tres_Obstaculo - x_dos_Obstaculo)) < 3) and ((abs(y_tres_Obstaculo - y_dos_Obstaculo) < 3)):
        x_dos_Obstaculo = random.randrange(1,9)     
        y_dos_Obstaculo = random.randrange (1,8)

    
    #------------------Listas de estados del tablero-----------------------------------------------------

      #posiciones no recorridas en estado 0, ya pisadas en estado 1 y obstaculos en estado -1

    estado = []

    for i in range(10):
        mini_estado = []
        estado.append(mini_estado)
        for j in range (10):
            estado[i].append(0)
            
    #----------estados de obstaculos---------------------------------------------------------------------
    estado [y_uno_Obstaculo][x_uno_Obstaculo] = -1
    estado [y_dos_Obstaculo][x_dos_Obstaculo] = -1
    estado [y_dos_Obstaculo + 1][x_dos_Obstaculo] = -1
    estado [y_tres_Obstaculo][x_tres_Obstaculo] = -1
    estado [y_tres_Obstaculo][x_tres_Obstaculo + 1] = -1
    estado [y_tres_Obstaculo][x_tres_Obstaculo + 2] = -1
    
    estado [0][0] = 1 #Lugar de inicio del personaje (estado: pisado)

    pygame.display.flip() #actualizar
    
    reloj=pygame.time.Clock()

    corriendo=True
    contadorMovimiento=0

    limite_horizontal = 50 #limite personaje eje x
    limite_vertical = 50 #limite personaje eje y

    personaje_x = 0 #coordenadas personaje eje x
    personaje_y = 0 #coordenadas personaje eje y

    xlimite_enemigo1 = 0 #limite enemigo eje x
    ylimite_enemigo1 = 9 #limite enemigo eje y

    xEnemigo1 = 100 #Pixeles de aparicion del enemigo 1 eje x
    yEnemigo1 = 640 #Pixeles de aparicion del enemigo 1 eje y

    x_coor_enemigo1 = 0 #Coordenadas eje x enemigo 1
    y_coor_enemigo1 = 9 #Coordenadas eje y enemigo 1

    xlimite_enemigo2 = 9 #limite enemigo eje x
    ylimite_enemigo2 = 0 #limite enemigo eje y

    xEnemigo2 = 640 #Pixeles de aparicion del enemigo 2 eje x
    yEnemigo2 = 100 #Pixeles de aparicion del enemigo 2 eje y

    x_coor_enemigo2 = 9 #Coordenadas eje x enemigo 2
    y_coor_enemigo2 = 0 #Coordenadas eje y enemigo 2

    mov_enemigo = False #Variable que define si el enemigo tiene la capacidad de moverse
    
    vidas = 3 #Contador de vidas

    teclas = True #Variable que define si el personaje se puede moover al presionar la teclas

    contador_movimiento = 0

    #--------------------------------------Pantalla Inicio-----------------------------------------     
    com=True
    if com==True:
        while com:
            ventana.blit(fondo,(0,0))
            for event in pygame.event.get():
                if(event.type==pygame.QUIT):
                    corriendo=False
                    pygame.display.flip()
                if event.type==pygame.KEYDOWN:
                    tecla_presion=pygame.key.name(event.key)
                    if tecla_presion=="e":
                        com=False
                        ventana.blit(fondoj,(0,0))
                        pygame.display.flip()
            pygame.display.flip()

    #--------------------------------------Pantalla Instrucciones-----------------------------------------    
    com=True
    if com==True:
        while com:
            ventana.blit(instrucciones,(0,0))
            for event in pygame.event.get():
                if(event.type==pygame.QUIT):
                    corriendo=False
                    pygame.display.flip()
                if event.type==pygame.KEYDOWN:
                    tecla_presion=pygame.key.name(event.key)
                    if tecla_presion=="e":
                        com=False
                        ventana.blit(fondoj,(0,0))
                        pygame.display.flip()
            pygame.display.flip()
    pygame.mixer.music.play(20)

    marcador=5000
    
    while corriendo:
        reloj.tick(60)
        ventana.fill((25,166,194))
        contador_movimiento += 1

        #--------------Tablero de texturas 10x10-----------------------------------------------------------------------

        tablero = []

        for i in range(10):
            minitablero = []
            tablero.append(minitablero)
            for j in range (10):
                tablero[i].append(j)
                pygame.draw.rect(ventana, (100,100,100), pygame.Rect(60*j + 100, 60*i + 100, 50, 50))

        ventana.blit(fondoj,(0,0))
        ventana.blit(encima,(320,180))


        #-------------------Obstaculos de 1, 2 y 3 casillas generados con los numeros aleatorios-----------------------------------------------------------------

        ventana.blit(obstaculo, (x_uno_Obstaculo * 60 + 100,y_uno_Obstaculo * 60 + 100))
        for obs in range (2):
            ventana.blit(obstaculo, (x_dos_Obstaculo * 60 + 100,(y_dos_Obstaculo+ obs) * 60 + 100))
        for obs in range (3):
            pygame.draw.rect(ventana,(202, 25, 212),pygame.Rect((x_tres_Obstaculo+obs) * 60 +100,(y_tres_Obstaculo) * 60+100,50,50))
            ventana.blit(obstaculo, ((x_tres_Obstaculo+obs) * 60 + 100,y_tres_Obstaculo * 60 + 100))

        #-------------------Rastro del personaje----------------------------------------------------------------------------

        for i in range(10):
            for j in range (10):
                if estado[i][j] == 0:
                    ventana.blit(tierra,(60*j + 100, 60*i + 100))     #estado 0 = No pisado
                if estado[i][j] == 1:
                    ventana.blit(trigo, (60*j + 100, 60*i + 100))     #estado 1 = Pisado

        #-------------------Vidas------------------------------------------------------------------------------------------

        for i in range (3):
            ventana.blit(vidaN,(i*120 + 800, 200)) #Vidas perdidas (se encuentran detras de las vidas restantes)

        for i in range (vidas):
            ventana.blit(vida,(i*120 + 800, 200)) #Vidas restantes

        #-------------------Enemigos----------------------------------------------------------------------------------------

        ventana.blit(enemigo1,(xEnemigo1, yEnemigo1)) #Enemigo 1
        ventana.blit(enemigo2,(xEnemigo2, yEnemigo2)) #Enemigo 2

        #--------------------Movimientos del enemigo-------------------------------------------------------------------------

        if contador_movimiento == 15:
            contador_movimiento = 0
            
            if mov_enemigo:

                if random.uniform(0,1) <= 0.6 :
                    if random.uniform(0,1) <= 0.5 and x_coor_enemigo1 < 9 and estado[y_coor_enemigo1][x_coor_enemigo1 + 1] != -1: #Contiene los limites y el choque con los obstaculo en estado -1
                        xEnemigo1 += 60
                        x_coor_enemigo1 += 1
                        if personaje_x == x_coor_enemigo1 and personaje_y == y_coor_enemigo1: #Si el obstaculo colisiona con el personaje se reincian todas las variables del personaje
                            xCuadrado, yCuadrado, personaje_y, personaje_x, limite_horizontal, limite_vertical, mov_enemigo, vidas = colision(xCuadrado, yCuadrado, personaje_y, personaje_x, limite_horizontal, limite_vertical, mov_enemigo, vidas)           
                            #Llamada a la funcion colision(linea superior)
                                
                    elif x_coor_enemigo1 >0 and estado[y_coor_enemigo1][x_coor_enemigo1 - 1] != -1 and x_coor_enemigo1 !=1 and y_coor_enemigo1 != 0:
                        xEnemigo1 -= 60
                        x_coor_enemigo1 -=1
                        if personaje_x == x_coor_enemigo1 and personaje_y == y_coor_enemigo1:
                            xCuadrado, yCuadrado, personaje_y, personaje_x, limite_horizontal, limite_vertical, mov_enemigo, vidas = colision(xCuadrado, yCuadrado, personaje_y, personaje_x, limite_horizontal, limite_vertical, mov_enemigo, vidas)
                                
                    elif random.uniform(0,1) >= 0.6 and y_coor_enemigo1 < 9 and estado[y_coor_enemigo1 + 1][x_coor_enemigo1] != -1:
                        yEnemigo1 += 60
                        y_coor_enemigo1 += 1
                        if personaje_x == x_coor_enemigo1 and personaje_y == y_coor_enemigo1:
                            xCuadrado, yCuadrado, personaje_y, personaje_x, limite_horizontal, limite_vertical, mov_enemigo, vidas = colision(xCuadrado, yCuadrado, personaje_y, personaje_x, limite_horizontal, limite_vertical, mov_enemigo, vidas)
                                
                            
                    elif y_coor_enemigo1 > 0 and estado[y_coor_enemigo1 - 1][x_coor_enemigo1] != -1 and x_coor_enemigo1 !=0 and y_coor_enemigo1 != 1:
                        yEnemigo1 -= 60
                        y_coor_enemigo1 -= 1
                        if personaje_x == x_coor_enemigo1 and personaje_y == y_coor_enemigo1:
                            xCuadrado, yCuadrado, personaje_y, personaje_x, limite_horizontal, limite_vertical, mov_enemigo, vidas = colision(xCuadrado, yCuadrado, personaje_y, personaje_x, limite_horizontal, limite_vertical, mov_enemigo, vidas)
                #enemigo 2

                if random.uniform(0,1) <= 0.4 :
                    if random.uniform(0,1) <= 0.5 and x_coor_enemigo2 < 9 and estado[y_coor_enemigo2][x_coor_enemigo2 + 1] != -1:
                        xEnemigo2 += 60
                        x_coor_enemigo2 += 1
                        if personaje_x == x_coor_enemigo2 and personaje_y == y_coor_enemigo2:
                            xCuadrado, yCuadrado, personaje_y, personaje_x, limite_horizontal, limite_vertical, mov_enemigo, vidas = colision(xCuadrado, yCuadrado, personaje_y, personaje_x, limite_horizontal, limite_vertical, mov_enemigo, vidas)
                                
                                
                    elif x_coor_enemigo2 >0 and estado[y_coor_enemigo2][x_coor_enemigo2 - 1] != -1 and x_coor_enemigo2 !=1 and y_coor_enemigo2 != 0:
                        xEnemigo2 -= 60
                        x_coor_enemigo2 -=1
                        if personaje_x == x_coor_enemigo2 and personaje_y == y_coor_enemigo2:
                            xCuadrado, yCuadrado, personaje_y, personaje_x, limite_horizontal, limite_vertical, mov_enemigo, vidas = colision(xCuadrado, yCuadrado, personaje_y, personaje_x, limite_horizontal, limite_vertical, mov_enemigo, vidas)
                                
                    elif random.uniform(0,1) >= 0.4 and y_coor_enemigo2 < 9 and estado[y_coor_enemigo2 + 1][x_coor_enemigo2] != -1:
                        yEnemigo2 += 60
                        y_coor_enemigo2 += 1
                        if personaje_x == x_coor_enemigo2 and personaje_y == y_coor_enemigo2:
                            xCuadrado, yCuadrado, personaje_y, personaje_x, limite_horizontal, limite_vertical, mov_enemigo, vidas = colision(xCuadrado, yCuadrado, personaje_y, personaje_x, limite_horizontal, limite_vertical, mov_enemigo, vidas)
                                
                            
                    elif y_coor_enemigo2 > 0 and estado[y_coor_enemigo2 - 1][x_coor_enemigo2] != -1 and x_coor_enemigo2 !=0 and y_coor_enemigo2 != 1:
                        yEnemigo2 -= 60
                        y_coor_enemigo2 -= 1
                        if personaje_x == x_coor_enemigo2 and personaje_y == y_coor_enemigo2:
                            xCuadrado, yCuadrado, personaje_y, personaje_x, limite_horizontal, limite_vertical, mov_enemigo, vidas = colision(xCuadrado, yCuadrado, personaje_y, personaje_x, limite_horizontal, limite_vertical, mov_enemigo, vidas)
                        
            
                
        

        #---------------------------Personaje--------------------------------------------------------------------------------
        
        ventana.blit(personaje1,(xCuadrado,yCuadrado,))

        #-------------------Movimientos del personaje----------------------------------------------------------------------

        
        
        for event in pygame.event.get():
            if(event.type==pygame.QUIT):
                corriendo=False
                    
            if event.type==pygame.KEYDOWN:
                tecla_presion=pygame.key.name(event.key)

                if teclas:
                    
                    #Los comentarios al presionar la letra "w" son similares a presionar "a","s","d".

                    if tecla_presion=="w":
                        mov_enemigo = True #Permite que los enemigos se comiencen a mover
                        if personaje_x == x_uno_Obstaculo and personaje_y - 1 == y_uno_Obstaculo:    #Validaciones para que el personaje sobrepase los obstaculo
                            print("Obstaculo")                                                       #Si el personaje se encuentra en una posicion (x,y) y el obstaculo
                                                                                                         #en una poscion cercana colindante, nuestro personaje no avanza.
                        elif personaje_x == x_dos_Obstaculo and personaje_y - 1 == y_dos_Obstaculo:
                            print("Obstaculo")

                        elif personaje_x == x_dos_Obstaculo and personaje_y - 2 == y_dos_Obstaculo:
                            print("Obstaculo")

                        elif personaje_x == x_tres_Obstaculo and personaje_y - 1 == y_tres_Obstaculo:
                            print("Obstaculo")

                        elif personaje_x - 1 == x_tres_Obstaculo and personaje_y -1 == y_tres_Obstaculo:
                            print("Obstaculo")

                        elif personaje_x - 2 == x_tres_Obstaculo and personaje_y -1 == y_tres_Obstaculo:
                            print("Obstaculo") #Muestra en el shell cuando el personaje se topa con un obstaculo
                                
                    
                        elif limite_vertical > 50:         #limites dentro del tablero, entre 50 y 590 pixeles por eje
                            limite_vertical, personaje_y, yCuadrado = mov_negativo (limite_vertical, personaje_y, yCuadrado) # Llamado a funcion mov_negativo
                            estado [personaje_y][personaje_x] = cambio_de_estado(estado[personaje_y][personaje_x])           # Llamado a funcion cambio_de_estado
                            marcador-=10
                                
                            if personaje_x == x_coor_enemigo1 and personaje_y == y_coor_enemigo1: #Si el personje se encuentra en la misma coordenada del enemigo 1 se reinician las varibles del personaje
                                xCuadrado, yCuadrado, personaje_y, personaje_x, limite_horizontal, limite_vertical, mov_enemigo, vidas = colision(xCuadrado, yCuadrado, personaje_y, personaje_x, limite_horizontal, limite_vertical, mov_enemigo, vidas)
                            if personaje_x == x_coor_enemigo2 and personaje_y == y_coor_enemigo2: #Si el personje se encuentra en la misma coordenada del enemigo 2 se reinician las varibles del personaje
                                xCuadrado, yCuadrado, personaje_y, personaje_x, limite_horizontal, limite_vertical, mov_enemigo, vidas = colision(xCuadrado, yCuadrado, personaje_y, personaje_x, limite_horizontal, limite_vertical, mov_enemigo, vidas)
                                
                                
                                


                    if tecla_presion=="a":
                        mov_enemigo = True
                        if personaje_x - 1 == x_uno_Obstaculo and personaje_y == y_uno_Obstaculo:
                            print("Obstaculo")
                                
                        elif personaje_x - 1 == x_dos_Obstaculo and personaje_y == y_dos_Obstaculo:
                            print("Obstaculo")
                                
                        elif personaje_x - 1 == x_dos_Obstaculo and personaje_y - 1 == y_dos_Obstaculo:
                            print("Obstaculo")

                        elif personaje_x - 3 == x_tres_Obstaculo and personaje_y == y_tres_Obstaculo:
                            print("Obstaculo")

                        elif limite_horizontal > 50:
                            limite_horizontal, personaje_x, xCuadrado = mov_negativo (limite_horizontal, personaje_x, xCuadrado)
                            estado [personaje_y][personaje_x] = cambio_de_estado(estado[personaje_y][personaje_x])
                            marcador-=10
                                
                            if personaje_x == x_coor_enemigo1 and personaje_y == y_coor_enemigo1:
                                xCuadrado, yCuadrado, personaje_y, personaje_x, limite_horizontal, limite_vertical, mov_enemigo, vidas = colision(xCuadrado, yCuadrado, personaje_y, personaje_x, limite_horizontal, limite_vertical, mov_enemigo, vidas)

                            if personaje_x == x_coor_enemigo2 and personaje_y == y_coor_enemigo2:
                                xCuadrado, yCuadrado, personaje_y, personaje_x, limite_horizontal, limite_vertical, mov_enemigo, vidas = colision(xCuadrado, yCuadrado, personaje_y, personaje_x, limite_horizontal, limite_vertical, mov_enemigo, vidas)
                                
                                
                                
                                

                    if tecla_presion=="s":
                        mov_enemigo = True
                        if personaje_x == x_uno_Obstaculo and personaje_y + 1 == y_uno_Obstaculo:
                            print("Obstaculo")

                        elif personaje_x == x_dos_Obstaculo and personaje_y + 1 == y_dos_Obstaculo:
                            print("Obstaculo")

                        elif personaje_x == x_tres_Obstaculo and personaje_y + 1 == y_tres_Obstaculo:
                            print("Obstaculo")

                        elif personaje_x - 1 == x_tres_Obstaculo and personaje_y + 1 == y_tres_Obstaculo:
                            print("Obstaculo")

                        elif personaje_x - 2 == x_tres_Obstaculo and personaje_y + 1 == y_tres_Obstaculo:
                            print("Obstaculo")
                              
                        elif limite_vertical < 590:
                            limite_vertical, personaje_y, yCuadrado = mov_positivo (limite_vertical, personaje_y, yCuadrado)
                            estado [personaje_y][personaje_x] = cambio_de_estado(estado[personaje_y][personaje_x])
                            marcador-=10
                                
                            if personaje_x == x_coor_enemigo1 and personaje_y == y_coor_enemigo1:
                                xCuadrado, yCuadrado, personaje_y, personaje_x, limite_horizontal, limite_vertical, mov_enemigo, vidas = colision(xCuadrado, yCuadrado, personaje_y, personaje_x, limite_horizontal, limite_vertical, mov_enemigo, vidas)
                            if personaje_x == x_coor_enemigo2 and personaje_y == y_coor_enemigo2:
                                xCuadrado, yCuadrado, personaje_y, personaje_x, limite_horizontal, limite_vertical, mov_enemigo, vidas = colision(xCuadrado, yCuadrado, personaje_y, personaje_x, limite_horizontal, limite_vertical, mov_enemigo, vidas)
                            


                    if tecla_presion=="d":
                        mov_enemigo = True
                        if personaje_x + 1 == x_uno_Obstaculo and personaje_y == y_uno_Obstaculo:
                            print("Obstaculo")

                        elif personaje_x + 1 == x_dos_Obstaculo and personaje_y == y_dos_Obstaculo:
                            print("Obstaculo")

                        elif personaje_x + 1 == x_dos_Obstaculo and personaje_y - 1 == y_dos_Obstaculo:
                            print("Obstaculo")

                        elif personaje_x + 1 == x_tres_Obstaculo and personaje_y == y_tres_Obstaculo:
                            print("Obstaculo")
                                    
                        elif limite_horizontal < 590:
                            limite_horizontal, personaje_x, xCuadrado = mov_positivo (limite_horizontal, personaje_x, xCuadrado)
                            estado [personaje_y][personaje_x] = cambio_de_estado(estado[personaje_y][personaje_x])
                            marcador-=10
                                
                            if personaje_x == x_coor_enemigo1 and personaje_y == y_coor_enemigo1:
                                xCuadrado, yCuadrado, personaje_y, personaje_x, limite_horizontal, limite_vertical, mov_enemigo, vidas = colision(xCuadrado, yCuadrado, personaje_y, personaje_x, limite_horizontal, limite_vertical, mov_enemigo, vidas)
                            if personaje_x == x_coor_enemigo2 and personaje_y == y_coor_enemigo2:
                                xCuadrado, yCuadrado, personaje_y, personaje_x, limite_horizontal, limite_vertical, mov_enemigo, vidas = colision(xCuadrado, yCuadrado, personaje_y, personaje_x, limite_horizontal, limite_vertical, mov_enemigo, vidas)


        #---------------------Textos dentro del juego------------------------------------------------------------------
        mensaje2=fuentemedia.render("Puntos: "+ str(marcador), True,(0,0,0))
        ventana.blit(mensaje2,(770,385))
        mensaje=fuentemedia.render("Puntos: "+ str(marcador), True,(227, 174, 16))
        puntaje_final = fuentemedia.render(str(marcador), True,(78, 212, 25))
        puntaje_final2 = fuentemedia.render(str(marcador), True,(0, 0, 0))
        puntaje_final3 = fuentemedia.render(str(marcador-2500), True,(255, 0, 0))
        ventana.blit(mensaje,(765,380))
        victoriareset=fuentechica.render("Presiona R para reiniciar",True,(78, 212, 25))
        derrotareset=fuentechica.render("Presiona R para reiniciar",True,(255,0,0))
        sombrareset=fuentechica.render("Presiona R para reiniciar",True,(0, 0, 0))
        
        #----------------------Pantallas de victoria------------------------------------------------------------------------------
        ganador = victoria(estado)#Llamado a la funcion victoria(retorna True o False)

        if ganador == True: 
            ventana.blit(victorioso,(0,0))
            ventana.blit(puntaje_final2,(505,215))
            ventana.blit(puntaje_final,(500,210))
            ventana.blit(sombrareset,(215,305))
            ventana.blit(victoriareset,(210,300))
            teclas = False                  #Bloquea el movimientos de las teclas "a" "w" "s" "d"
            mov_enemigo = False             #Bloquea el movimiento de los enemigos
            pygame.display.flip()
            tecla = pygame.key.get_pressed() #Reinicia el juego una vez ganado al presionar "r"
            if tecla[pygame.K_r]:
                main()

        #--------------------Pantalla de derrota----------------------------------------------------------------------------------
            
        if vidas == 0:
            ventana.blit(perdedor,(0,0))
            ventana.blit(puntaje_final3,(725,595))
            ventana.blit(derrotareset,(400,150))
            teclas = False                 #Bloquea el movimientos de las teclas "a" "w" "s" "d"
            mov_enemigo = False            #Bloquea el movimiento de los enemigos
            pygame.display.flip()
            tecla = pygame.key.get_pressed() #Reinicia el juego una vez ganado al presionar "r"
            if tecla[pygame.K_r]:
                main()
        
        pygame.display.flip()
    pygame.quit()
    sys.exit()



#Llamada a la funcion 
main()
