
import pygame
import sys
import random

ANCHO_VENTANA=660
ALTO_VENTANA=660

#Listas para for de creación de restricción
RESTRICCION_VENTANAx=[55,110,165,220,275,330,385,440,495,550]
RESTRICCION_VENTANAy=[55,110,165,220,275,330,385,440,495,550]
RESTRICCION_JUGADOR=[]

#For para crear lista de listas de espacio posible por JUGADOR y ENEMIGO
for i in RESTRICCION_VENTANAx:
    for j in RESTRICCION_VENTANAy:
        llenar=[]
        llenar.append(i)
        llenar.append(j)
        RESTRICCION_JUGADOR.append(llenar)

#Listas para obstaculos(Z)
xOBSTACULO=[110,165,220,275,330,385,440,495,550]
yOBSTACULO=[110,165,220,275,330,385,440,495,550]

#Función que revisará si una lista esta dentro de otra(para restringir tablero) y para conocer estados
def restriccion(lista1,lista2):
    for i in range(len(lista1)-len(lista2)+1):
        c=0
        for j in range (len(lista2)):
            if lista2[j]==lista1[i+j]:
                c=c+1
            if(c==len(lista2)):
                return True, i+j
    return False

#Funcion que escogera un valor principal aleatorio para cada obstáculo
def OBS_iniciales():
    Z=[[0,0],[0,0],[0,0]]
    while Z[0]==Z[1] or Z[0]==Z[2] or Z[1]==Z[2]:
        Z=[]
        for i in range(3):
            b=[]
            for j in range(1):
                VALx_oBstaculo=random.choice(xOBSTACULO)
                b.append(VALx_oBstaculo)
                VALy_oBstaculo=random.choice(yOBSTACULO)
                b.append(VALy_oBstaculo)
            Z.append(b)
    return Z

#Función que creará coordenadas de todos los obstáculos de manera aleatoria
def obstaculos(Z):
    Z=[[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
    while Z[0]==Z[3] or Z[0]==Z[4] or Z[0]==Z[5] or Z[1]==Z[3] or Z[1]==Z[4] or Z[1]==Z[5] or Z[2]==Z[3] or Z[2]==Z[4] or Z[2]==Z[5] or Z[3]==Z[4] or Z[3]==Z[5] or Z[4]==Z[5] or Z[4][0]<55 or Z[4][0]>550 or Z[4][1]<55 or Z[4][1]>550 or Z[5][0]>550 or Z[5][1]>550 or Z[4][1]<55:
        Z=OBS_iniciales()
        b=[]
        if random.uniform(0, 1) <= 0.5:
            if random.uniform(0, 1) <= 0.5:
                x3_2OBS=Z[0][0]+55
                b.append(x3_2OBS)
                b.append(Z[0][1])
                Z.append(b)
                b=[]
                x3_3OBS=Z[3][0]+55
                b.append(x3_3OBS)
                b.append(Z[3][1])
            else:
                x3_2OBS=Z[0][0]-55
                b.append(x3_2OBS)
                b.append(Z[0][1])
                Z.append(b)
                b=[]
                x3_3OBS=Z[3][0]-55
                b.append(x3_3OBS)
                b.append(Z[3][1])
            Z.append(b)
        else:
            if random.uniform(0, 1) <= 0.5:
                b.append(Z[0][0])
                y3_2OBS=Z[0][1]+55
                b.append(y3_2OBS)
                Z.append(b)
                b=[]
                b.append(Z[3][0])
                y3_3OBS=Z[3][1]+55
                b.append(y3_3OBS)
            else:
                b.append(Z[0][0])
                y3_2OBS=Z[0][1]-55
                b.append(y3_2OBS)
                Z.append(b)
                b=[]
                b.append(Z[3][0])
                y3_3OBS=Z[3][1]-55
                b.append(y3_3OBS)
            Z.append(b)
        b=[]
        if random.uniform(0, 1) <= 0.5:
            if random.uniform(0, 1) <= 0.5:
                x2_2OBS=Z[1][0]+55
                b.append(x2_2OBS)
                b.append(Z[1][1])
            else:
                x2_2OBS=Z[1][0]-55
                b.append(x2_2OBS)
                b.append(Z[1][1])
            Z.append(b)
        else:
            if random.uniform(0, 1) <= 0.5:
                b.append(Z[1][0])
                y2_2OBS=Z[1][1]+55
                b.append(y2_2OBS)
            else:
                b.append(Z[1][0])
                y2_2OBS=Z[1][1]-55
                b.append(y2_2OBS)
            Z.append(b)
    return Z

#Función que crea aleatoriamente la posicion de los enemigos
def POSenemi(X):
    Z=[]
    b=[]
    VALx_enemigo=random.choice(xOBSTACULO)
    b.append(VALx_enemigo)
    VALy_enemigo=random.choice(yOBSTACULO)
    b.append(VALy_enemigo)
    Z.append(b)
    #Verificacion de que la posicion elegida no sea igual a la de un obstáculo
    while (restriccion(X,Z)):
        Z=[]
        b=[]
        VALx_enemigo=random.choice(xOBSTACULO)
        b.append(VALx_enemigo)
        VALy_enemigo=random.choice(yOBSTACULO)
        b.append(VALy_enemigo)
        Z.append(b)
    return Z

#Funcion que ejecuta pantalla de DERROTA
def derrota(score):
    #Cargar y correr música de derrota
    pygame.mixer.music.load('derrota.WAV')
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.05)
    #cargar imágenes de derrota
    fondo=pygame.image.load("DERROTADO.png")
    fondo2=pygame.image.load("marshmallow.png")
    #cargar fuentes de derrota
    fuente=pygame.font.SysFont("Showcard Gothic",50)
    fuente2=pygame.font.SysFont("Showcard Gothic",20)
    fuente3=pygame.font.SysFont("Showcard Gothic",23)
    #Cargar textos de derrota
    texto=fuente.render("DERROTA", True, (176, 7, 7))
    texto1=fuente2.render("PRESIONA 'R' PARA VOLVER AL MENU", True, (255,255,255))
    texto2=fuente3.render("Ve con mas precaucion", True, (222, 222, 2))
    texto3=fuente3.render("en tu próxima misión", True, (222, 222, 2))
    puntaje=fuente3.render("Puntaje:" + str(score), True, (255,255,255))
    #Dibujar toda imágen y texto de derrota
    ventana=pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
    ventana.blit(fondo,[-78,0])
    ventana.blit(fondo2,[400,20])
    ventana.blit(texto,[50,40])
    ventana.blit(texto1,[20,180])
    ventana.blit(texto2,[30,100])
    ventana.blit(texto3,[33,120])
    ventana.blit(puntaje,[460,350])
    pygame.display.flip()

#Funcion que ejecuta pantalla de VICTORIA
def victoria(score):
    #Cargar y correr música de victoria
    pygame.mixer.music.load('victoria.WAV')
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.05)
    #Cargar imágenes de victoria
    fondo=pygame.image.load("Victoria.png")
    #Cargar fuentes de victoria
    fuente=pygame.font.SysFont("Showcard Gothic",50)
    fuente3=pygame.font.SysFont("Showcard Gothic",38)
    fuente2=pygame.font.SysFont("Showcard Gothic",20)
    #Cargar textos de victoria
    texto=fuente.render("¡Lo has conseguido!", True, (222, 222, 2))
    texto1=fuente3.render("finalmente puedes descansar", True, (39, 60, 184))
    texto2=fuente2.render("PRESIONA 'R' PARA VOLVER", True, (255,255,255))
    puntaje=fuente.render("Puntaje:" + str(score), True, (255,255,255))
    #Dibujar toda imágen y texto
    ventana=pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
    ventana.blit(fondo,[-200,0])
    ventana.blit(texto,[30,34])
    ventana.blit(texto1,[30,130])
    ventana.blit(texto2,[350,450])
    ventana.blit(puntaje,[300,300])

    pygame.display.flip()

#Funcion que ejecuta instrucciones y todas sus imagenes
def instrucciones():
    #Cargar imágenes de instrucciones
    background2=pygame.image.load("Instrucciones.png")
    corazon=pygame.image.load("corazon menu.png")
    #Cargar fuente de instrucciones
    fuente1=pygame.font.SysFont("Showcard Gothic",50)
    fuente2=pygame.font.SysFont("Showcard Gothic",19)
    fuente3=pygame.font.SysFont("Showcard Gothic",15)
    #Cargar texto de instrucciones
    titulo=fuente1.render("CÓMO JUGAR", True, (222, 222, 2))
    texto1=fuente2.render("RECOGE TODOS LOS MALVAVISCOS QUE HAY POR EL ÁREA ESPACIAL", True, (222, 222, 2))
    texto2=fuente2.render("¡PERO CUIDADO! SI VUELVES A UN LUGAR DONDE YA AGARRASTE", True, (222, 222, 2))
    texto3=fuente2.render("UN MALVAVISCO LO DEJARAS CAER Y DEBERÁS RECOGERLO NUEVAMENTE", True, (222, 222, 2))
    texto4=fuente2.render("EVITA LOS ALIENS Y LOS OBSTACULOS", True, (222, 222, 2))
    texto5=fuente2.render("QUE SE INTERPONGAN EN TU CAMINO", True, (222, 222, 2))
    texto6=fuente2.render("SOLO TIENES 3             POR RONDA", True, (222, 222, 2))
    texto7=fuente2.render("MOVIMENTO", True, (40, 222, 198))
    texto8=fuente3.render("PRESIONA 'R' PARA VOLVER", True, (9, 237, 63))
    texto9=fuente3.render("PRESIONA 'C' PARA EMPERZAR", True, (9, 237, 63))
    #Dibujar toda imágen y texto de instrucciones
    ventana=pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
    ventana.blit(background2,[-15,0])
    ventana.blit(corazon,[167,292])
    ventana.blit(titulo,[20,20])
    ventana.blit(texto1,[33,90])
    ventana.blit(texto2,[35,122])
    ventana.blit(texto3,[8,144])
    ventana.blit(texto4,[20,205])
    ventana.blit(texto5,[20,233])
    ventana.blit(texto6,[30,300])
    ventana.blit(texto7,[60,370])
    ventana.blit(texto8,[440,580])
    ventana.blit(texto9,[430,610])
    pygame.display.flip()

#Función que ejecuta menu y todas sus imagenes
def mEnu():
    #Cargar imágenes de menú
    easter=pygame.image.load("easter.png")
    background=pygame.image.load("Menu.png")
    #Cargar fuentes de menú
    fuent=pygame.font.SysFont("Showcard Gothic",7)
    fuente=pygame.font.SysFont("Showcard Gothic",9)
    fuente2=pygame.font.SysFont("Showcard Gothic",30)
    #Cargar textos de menú
    texto2=fuente2.render("PRESIONA 'C' PARA COMENZAR", True, (113, 44, 148))
    texto3=fuente2.render("PRESIONA 'i' PARA SABER CÓMO JUGAR", True, (113, 44, 148))
    nombre=fuente.render("Benja", True, (0, 0, 0))
    nombre2=fuente.render("Seba", True, (0, 0, 0))
    nombre3=fuente.render("Javier", True, (0, 0, 0))
    nombre4=fuente.render("Isra", True, (0, 0, 0))
    neim=fuent.render("Nico",True, (0,0,0))
    #Dibujar toda imágen y texto de menú
    ventana=pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
    ventana.blit(background,[0,0])
    ventana.blit(neim,[5,5])
    ventana.blit(nombre,[5,15])
    ventana.blit(nombre2,[5,25])
    ventana.blit(nombre3,[5,35])
    ventana.blit(nombre4,[5,45])
    ventana.blit(easter,[645,0])
    ventana.blit(texto2,[50,500])
    ventana.blit(texto3,[50,550])
    pygame.display.flip()

#Funcion main
def main():
    pygame.init()

    ventana=pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))

    pygame.display.set_caption("AstromalV")

    pygame.display.flip()

    reloj=pygame.time.Clock()

    #Variable que rotará entre función del menú y de las instrucciones
    x=mEnu()

    corriendo=True

    #Si menu==True se mostrar la pantalla menu y la partida comenzará de 0
    menu=True
    victory=False
    lose=False

    #Lista que llama a obstaculos previo al dibujo de estos
    A=[]
    A=obstaculos(A)  

    #Posicion inicial de ENEMIGOS
    posEnemigo1=POSenemi(A)
    posEnemigo2=POSenemi(A)
    #Si la posicion de los enemigos son iguales, uno se crea nuevamente
    while posEnemigo1==posEnemigo2:
        posEnemigo2=POSenemi(A)

    #Cargar y correr música de menú
    pygame.mixer.music.load('menu.WAV')
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.2)   

    #While que inicia el juego
    while corriendo:

        while (corriendo and victory==True) or (corriendo and lose==True):
            for event in pygame.event.get():
                #If que cierra el juego
                if (event.type == pygame.QUIT):
                    corriendo=False
                #If que comienza una partida
                if event.type == pygame.KEYDOWN:
                    TECLA_PRESIONADA = pygame.key.name(event.key)
                    #Si se presiona la tecla c este while dejará de correr para darle paso al juego
                    if TECLA_PRESIONADA == 'r':
                        main()

        #While que ejecuta menu y crea todos los valores para el previo dibujo de cada situacion dentro del juego
        while corriendo and menu:

            #Variable x que se mueve entre instrucciones y menu
            x

            #Reinicio de contadores para un reinicio de partida
            contador_derrota=0
            contador_victoria=0

            #Contadores de puntaje para diferentes de estos en cuanto a velocidad de reacción
            CONTADOR_frame=0
            tiempo_uP=0
            PUNTAJE=0

            #Posición inicial del jugador
            pos_CUADRADO=[[55,55]]

            #Cargar la imagen del jugador
            jugador=pygame.image.load("jugador.png")

            #Contador de movimiento random de enemigos
            MOV_ENEMIGO = 0

            #For que crea lista ESTADOS
            ESTADOS=[1]
            for i in range(99):
                ESTADOS.append(0)  

            #For de eventos del menu
            for event in pygame.event.get():
                #If que cierra el juego
                if (event.type == pygame.QUIT):
                    corriendo=False
                #If que comienza una partida
                if event.type == pygame.KEYDOWN:
                    TECLA_PRESIONADA = pygame.key.name(event.key)
                    #Si se presiona la tecla c este while dejará de correr para darle paso al juego
                    if TECLA_PRESIONADA == 'c':
                        menu=False
                        #Música de una partida
                        pygame.mixer.music.load('main.WAV')
                        pygame.mixer.music.play()
                        pygame.mixer.music.set_volume(0.02)
                    #If que llama a instrucciones
                    if TECLA_PRESIONADA == 'i':
                        x=instrucciones()
                    #If que vuelve a menu
                    if TECLA_PRESIONADA == 'r':
                        x=mEnu()

        sonidoDaño=pygame.mixer.Sound("daño.WAV")

        reloj.tick(60)

        CONTADOR_frame+=1

        #Cargar fondo del juego
        espacio=pygame.image.load("espacio.jpg").convert()
        ventana.blit(espacio, [0,0])
        fuente=pygame.font.SysFont("Showcard Gothic",25)
        texto=fuente.render("Pulsa 'R' para reiniciar", True, (255,255,255))
        puntaje=fuente.render("Puntaje:" + str(PUNTAJE), True, (255,255,255))
        ventana.blit(texto,[275,630])
        ventana.blit(puntaje,[30,20])
        fondo=pygame.image.load("malva.png")
        alien=pygame.image.load("alien.png")   

        #For que dibuja las casillas dependiendo de su estado        
        for k in range(100):
            if ESTADOS[k]==1:
                #Si el estado es 1 dibujará un cuadrado gris
                pygame.draw.rect(ventana, (50,50,50), pygame.Rect(RESTRICCION_JUGADOR[k][0],RESTRICCION_JUGADOR[k][1], 50,50))
            else:
                #Si el estado es 0 dibujará una imagen con un 'malvavisco' de fondo gris
                ventana.blit(fondo,[RESTRICCION_JUGADOR[k][0],RESTRICCION_JUGADOR[k][1]]) 

        #Dibujo de obstáculo de 3 casillas
        pygame.draw.rect(ventana, (247, 165, 12), pygame.Rect(A[0][0],A[0][1], 50,50))
        pygame.draw.rect(ventana, (247, 165, 12), pygame.Rect(A[3][0],A[3][1], 50,50))
        pygame.draw.rect(ventana, (247, 165, 12), pygame.Rect(A[4][0],A[4][1], 50,50))

        #Dibujo de obstáculo de 2 casillas
        pygame.draw.rect(ventana, (247, 165, 12), pygame.Rect(A[1][0],A[1][1], 50,50))
        pygame.draw.rect(ventana, (247, 165, 12), pygame.Rect(A[5][0],A[5][1], 50,50))
            
        #Dibujo de obstáculo de 1 casilla
        pygame.draw.rect(ventana, (247, 165, 12), pygame.Rect(A[2][0],A[2][1], 50,50))
            
        #Dibujo de JUGADOR
        ventana.blit(jugador,[pos_CUADRADO[0][0],pos_CUADRADO[0][1]])

        #Dibujo de ENEMIGO1
        ventana.blit(alien,[posEnemigo1[0][0],posEnemigo1[0][1]])

        #Dibujo de ENEMIGO2
        ventana.blit(alien,[posEnemigo2[0][0],posEnemigo2[0][1]])

        #Dibujo de lineas separadoras de casillas
        for i in range(1,11):
            for j in range(1,11):
                pygame.draw.rect(ventana,(0, 0, 0), pygame.Rect((55*i),(55*j),10,50))
                pygame.draw.rect(ventana,(0, 0, 0), pygame.Rect((55*i),(55*j),50,10))
        for i in range(11,12):
            for j in range(1,11):                
                pygame.draw.rect(ventana,(0, 0, 0), pygame.Rect((55*i),(55*j),10,50))
        for i in range(1,11):
            for j in range(11,12):  
                pygame.draw.rect(ventana,(0, 0, 0), pygame.Rect((55*i),(55*j),50,10))

        #Movimiento random de ambos enemigos
        MOV_ENEMIGO = MOV_ENEMIGO + 1

        if MOV_ENEMIGO == 25:
            MOV_ENEMIGO = 0
            if random.uniform(0, 1) <= 0.5:
                if random.uniform(0, 1) <= 0.5 :
                    #Almacenamiento de posicion actual y su cambio mas if de restriccion ventana y obstaculos
                    posEnemigo1[0][0] += 55
                    if (restriccion(RESTRICCION_JUGADOR,posEnemigo1)==False) or (posEnemigo1[0][0],posEnemigo1[0][1])==(55,55) or (posEnemigo1[0][0],posEnemigo1[0][1])==(A[0][0],A[0][1]) or (posEnemigo1[0][0],posEnemigo1[0][1])==(A[3][0],A[3][1]) or (posEnemigo1[0][0],posEnemigo1[0][1])==(A[4][0],A[4][1]) or (posEnemigo1[0][0],posEnemigo1[0][1])==(A[1][0],A[1][1]) or (posEnemigo1[0][0],posEnemigo1[0][1])==(A[5][0],A[5][1]) or (posEnemigo1[0][0],posEnemigo1[0][1])==(A[2][0],A[2][1]):
                        posEnemigo1[0][0] -= 55
                else:
                    #Almacenamiento de posicion actual y su cambio mas if de restriccion ventana y obstaculos
                    posEnemigo1[0][0] -= 55
                    if (restriccion(RESTRICCION_JUGADOR,posEnemigo1)==False) or (posEnemigo1[0][0],posEnemigo1[0][1])==(55,55) or (posEnemigo1[0][0],posEnemigo1[0][1])==(A[0][0],A[0][1]) or (posEnemigo1[0][0],posEnemigo1[0][1])==(A[3][0],A[3][1]) or (posEnemigo1[0][0],posEnemigo1[0][1])==(A[4][0],A[4][1]) or (posEnemigo1[0][0],posEnemigo1[0][1])==(A[1][0],A[1][1]) or (posEnemigo1[0][0],posEnemigo1[0][1])==(A[5][0],A[5][1]) or (posEnemigo1[0][0],posEnemigo1[0][1])==(A[2][0],A[2][1]):
                        posEnemigo1[0][0] += 55
            else:
                if random.uniform(0, 1) <= 0.5:
                    #Almacenamiento de posicion actual y su cambio mas if de restriccion ventana y obstaculos
                    posEnemigo1[0][1] -= 55
                    if (restriccion(RESTRICCION_JUGADOR,posEnemigo1)==False) or (posEnemigo1[0][0],posEnemigo1[0][1])==(55,55) or (posEnemigo1[0][0],posEnemigo1[0][1])==(A[0][0],A[0][1]) or (posEnemigo1[0][0],posEnemigo1[0][1])==(A[3][0],A[3][1]) or (posEnemigo1[0][0],posEnemigo1[0][1])==(A[4][0],A[4][1]) or (posEnemigo1[0][0],posEnemigo1[0][1])==(A[1][0],A[1][1]) or (posEnemigo1[0][0],posEnemigo1[0][1])==(A[5][0],A[5][1]) or (posEnemigo1[0][0],posEnemigo1[0][1])==(A[2][0],A[2][1]):
                        posEnemigo1[0][1] += 55
                else:
                    #Almacenamiento de posicion actual y su cambio mas if de restriccion ventana y obstaculos
                    posEnemigo1[0][1] += 55
                    if (restriccion(RESTRICCION_JUGADOR,posEnemigo1)==False) or (posEnemigo1[0][0],posEnemigo1[0][1])==(55,55) or (posEnemigo1[0][0],posEnemigo1[0][1])==(A[0][0],A[0][1]) or (posEnemigo1[0][0],posEnemigo1[0][1])==(A[3][0],A[3][1]) or (posEnemigo1[0][0],posEnemigo1[0][1])==(A[4][0],A[4][1]) or (posEnemigo1[0][0],posEnemigo1[0][1])==(A[1][0],A[1][1]) or (posEnemigo1[0][0],posEnemigo1[0][1])==(A[5][0],A[5][1]) or (posEnemigo1[0][0],posEnemigo1[0][1])==(A[2][0],A[2][1]):
                        posEnemigo1[0][1] -= 55

            if random.uniform(0, 1) <= 0.5:
                if random.uniform(0, 1) <= 0.5 :
                    posEnemigo2[0][0] += 55
                    #If que retrocede al ENEMIGO2 si este tiene mismas coordenadas que ENEMIGO1
                    if ((posEnemigo1[0][0],posEnemigo1[0][1])==(posEnemigo2[0][0],posEnemigo2[0][1])):
                        posEnemigo2[0][0] -= 55
                    #If de restriccion ventana y obstaculos
                    if (restriccion(RESTRICCION_JUGADOR,posEnemigo2)==False) or (posEnemigo2[0][0],posEnemigo2[0][1])==(55,55) or (posEnemigo2[0][0],posEnemigo2[0][1])==(A[0][0],A[0][1]) or (posEnemigo2[0][0],posEnemigo2[0][1])==(A[3][0],A[3][1]) or (posEnemigo2[0][0],posEnemigo2[0][1])==(A[4][0],A[4][1]) or (posEnemigo2[0][0],posEnemigo2[0][1])==(A[1][0],A[1][1]) or (posEnemigo2[0][0],posEnemigo2[0][1])==(A[5][0],A[5][1]) or (posEnemigo2[0][0],posEnemigo2[0][1])==(A[2][0],A[2][1]):
                        posEnemigo2[0][0] -= 55                  
                else:
                    posEnemigo2[0][0] -= 55
                    #If que retrocede al ENEMIGO2 si este tiene mismas coordednads que ENEMIGO1
                    if ((posEnemigo1[0][0],posEnemigo1[0][1])==(posEnemigo2[0][0],posEnemigo2[0][1])):
                        posEnemigo2[0][0] += 55
                    #If de restriccion ventana y obstaculos
                    if (restriccion(RESTRICCION_JUGADOR,posEnemigo2)==False) or (posEnemigo2[0][0],posEnemigo2[0][1])==(55,55) or (posEnemigo2[0][0],posEnemigo2[0][1])==(A[0][0],A[0][1]) or (posEnemigo2[0][0],posEnemigo2[0][1])==(A[3][0],A[3][1]) or (posEnemigo2[0][0],posEnemigo2[0][1])==(A[4][0],A[4][1]) or (posEnemigo2[0][0],posEnemigo2[0][1])==(A[1][0],A[1][1]) or (posEnemigo2[0][0],posEnemigo2[0][1])==(A[5][0],A[5][1]) or (posEnemigo2[0][0],posEnemigo2[0][1])==(A[2][0],A[2][1]):
                        posEnemigo2[0][0] += 55                   
            else:
                if random.uniform(0, 1) <= 0.5:
                    posEnemigo2[0][1] -= 55
                    #If que retrocede al ENEMIGO2 si este tiene mismas coordednads que ENEMIGO1
                    if ((posEnemigo1[0][0],posEnemigo1[0][1])==(posEnemigo2[0][0],posEnemigo2[0][1])):
                        posEnemigo2[0][1] += 55
                    #If de restriccion ventana y obstaculos
                    if (restriccion(RESTRICCION_JUGADOR,posEnemigo2)==False) or (posEnemigo2[0][0],posEnemigo2[0][1])==(55,55) or (posEnemigo2[0][0],posEnemigo2[0][1])==(A[0][0],A[0][1]) or (posEnemigo2[0][0],posEnemigo2[0][1])==(A[3][0],A[3][1]) or (posEnemigo2[0][0],posEnemigo2[0][1])==(A[4][0],A[4][1]) or (posEnemigo2[0][0],posEnemigo2[0][1])==(A[1][0],A[1][1]) or (posEnemigo2[0][0],posEnemigo2[0][1])==(A[5][0],A[5][1]) or (posEnemigo2[0][0],posEnemigo2[0][1])==(A[2][0],A[2][1]):
                        posEnemigo2[0][1] += 55

                else:
                    posEnemigo2[0][1] += 55
                    #If que retrocede al ENEMIGO2 si este tiene mismas coordednads que ENEMIGO1
                    if ((posEnemigo1[0][0],posEnemigo1[0][1])==(posEnemigo2[0][0],posEnemigo2[0][1])):
                        posEnemigo2[0][1] -= 55
                    #If de restriccion ventana y obstaculos
                    if (restriccion(RESTRICCION_JUGADOR,posEnemigo2)==False) or (posEnemigo2[0][0],posEnemigo2[0][1])==(55,55) or (posEnemigo2[0][0],posEnemigo2[0][1])==(A[0][0],A[0][1]) or (posEnemigo2[0][0],posEnemigo2[0][1])==(A[3][0],A[3][1]) or (posEnemigo2[0][0],posEnemigo2[0][1])==(A[4][0],A[4][1]) or (posEnemigo2[0][0],posEnemigo2[0][1])==(A[1][0],A[1][1]) or (posEnemigo2[0][0],posEnemigo2[0][1])==(A[5][0],A[5][1]) or (posEnemigo2[0][0],posEnemigo2[0][1])==(A[2][0],A[2][1]):
                        posEnemigo2[0][1] -= 55

        #Corazones de vida llenos
        cor_oscuro=pygame.image.load("corazon oscuro.png")
        cor_claro=pygame.image.load("corazon claro.png")
        #Corazones de vida vacíos
        sincor_oscuro=pygame.image.load("sin corazon oscuro.png")
        sincor_claro=pygame.image.load("sin corazon claro.png")

        corazon1=ventana.blit(cor_claro,[600,10])
        corazon1=ventana.blit(cor_oscuro,[550,10])
        corazon2=ventana.blit(cor_oscuro,[500,10])

        #Detectar colision JUGADOR-ENEMIGOS
        if (pos_CUADRADO[0][0] == posEnemigo1[0][0] and pos_CUADRADO[0][1] == posEnemigo1[0][1]) or (pos_CUADRADO[0][0] == posEnemigo2[0][0] and pos_CUADRADO[0][1] == posEnemigo2[0][1]):
            pos_CUADRADO[0][0] = 55
            pos_CUADRADO[0][1] = 55
            contador_derrota += 1
            PUNTAJE-=int(1800/(CONTADOR_frame-tiempo_uP+1))
            if PUNTAJE<0:
                PUNTAJE=0
            daño = pygame.mixer.Sound('daño.WAV')
            daño.play()

        #If que cambia un corazon de vida lleno a uno vacío si un enemigo toca al jugador
        if contador_derrota==1:
            corazon1=ventana.blit(sincor_claro,[600,10])
        
        #If que cambia 2 corazones de vida llenos a unos vacíos si un enemigo toca al jugador
        if contador_derrota==2:
            corazon1=ventana.blit(sincor_claro,[600,10])
            corazon1=ventana.blit(sincor_oscuro,[550,10])

        #Llamar función DERROTA
        if (contador_derrota==3):
            derrota(PUNTAJE)
            lose=True      

        #For que revisa estados de casillas, al haber 94 estados en 1 (total de casillas donde el jugador puede moverse) llama función VICTORIA
        contador_victoria=0
        for j in range(100):
            if ESTADOS[j]==1:
                contador_victoria+=1   
            if contador_victoria==94:
                victoria(PUNTAJE)
                victory=True

        pygame.display.flip()
        
        #For de eventos
        for event in pygame.event.get():

            #Cierre de juego
            if (event.type == pygame.QUIT):
                corriendo=False

            #If evento teclas presionadas
            if event.type == pygame.KEYDOWN:
                TECLA_PRESIONADA = pygame.key.name(event.key)

                if TECLA_PRESIONADA == 'w':
                    pos_CUADRADO[0][1] -= 55
                    #Restricción con obstáculos y con tablero10x10
                    if (restriccion(RESTRICCION_JUGADOR,pos_CUADRADO)==False) or (pos_CUADRADO[0][0],pos_CUADRADO[0][1])==(A[0][0],A[0][1]) or (pos_CUADRADO[0][0],pos_CUADRADO[0][1])==(A[3][0],A[3][1]) or (pos_CUADRADO[0][0],pos_CUADRADO[0][1])==(A[4][0],A[4][1]) or (pos_CUADRADO[0][0],pos_CUADRADO[0][1])==(A[1][0],A[1][1]) or (pos_CUADRADO[0][0],pos_CUADRADO[0][1])==(A[5][0],A[5][1]) or (pos_CUADRADO[0][0],pos_CUADRADO[0][1])==(A[2][0],A[2][1]):
                        pos_CUADRADO[0][1] += 55
                    else:
                        #For que revisa que posición esta el jugador y el estado de su casilla, cambiandolo entre 1 y 0
                        for i in RESTRICCION_VENTANAx:
                            for j in RESTRICCION_VENTANAy:
                                a,b=(restriccion(RESTRICCION_JUGADOR,pos_CUADRADO))
                                if (i,j)==((pos_CUADRADO[0][0],pos_CUADRADO[0][1])):
                                    if ESTADOS[b]==0:
                                        ESTADOS[b]=1
                                        PUNTAJE+=int(1000/(CONTADOR_frame-tiempo_uP+1))
                                    else:
                                        ESTADOS[b]=0
                                        #Cálculo puntaje-tiempo de reacción
                                        PUNTAJE-=int(1500/(CONTADOR_frame-tiempo_uP+1))
                                        if PUNTAJE<0:
                                            PUNTAJE=0                                    
                    tiempo_uP=CONTADOR_frame     

                if TECLA_PRESIONADA == 'a':
                    #Cargar la imagen del jugador
                    jugador=pygame.image.load("jugadorv2.png")
                    pos_CUADRADO[0][0] -= 55
                    #Restricción con obstáculos y con tablero10x10
                    if (restriccion(RESTRICCION_JUGADOR,pos_CUADRADO)==False) or (pos_CUADRADO[0][0],pos_CUADRADO[0][1])==(A[0][0],A[0][1]) or (pos_CUADRADO[0][0],pos_CUADRADO[0][1])==(A[3][0],A[3][1]) or (pos_CUADRADO[0][0],pos_CUADRADO[0][1])==(A[4][0],A[4][1]) or (pos_CUADRADO[0][0],pos_CUADRADO[0][1])==(A[1][0],A[1][1]) or (pos_CUADRADO[0][0],pos_CUADRADO[0][1])==(A[5][0],A[5][1]) or (pos_CUADRADO[0][0],pos_CUADRADO[0][1])==(A[2][0],A[2][1]):
                        pos_CUADRADO[0][0] += 55
                    else:
                        #For que revisa que posición esta el jugador y el estado de su casilla, cambiandolo entre 1 y 0
                        for i in RESTRICCION_VENTANAx:
                            for j in RESTRICCION_VENTANAy:
                                a,b=(restriccion(RESTRICCION_JUGADOR,pos_CUADRADO))
                                if (i,j)==((pos_CUADRADO[0][0],pos_CUADRADO[0][1])):
                                    if ESTADOS[b]==0:
                                        ESTADOS[b]=1
                                        PUNTAJE+=int(1000/(CONTADOR_frame-tiempo_uP+1))
                                    else:
                                        ESTADOS[b]=0
                                        #Cálculo puntaje-tiempo de reacción
                                        PUNTAJE-=int(1500/(CONTADOR_frame-tiempo_uP+1))
                                        if PUNTAJE<0:
                                            PUNTAJE=0                                        
                    tiempo_uP=CONTADOR_frame

                if TECLA_PRESIONADA == 's':
                    pos_CUADRADO[0][1] += 55
                    #Restricción con obstáculos y con tablero10x10
                    if (restriccion(RESTRICCION_JUGADOR,pos_CUADRADO)==False) or (pos_CUADRADO[0][0],pos_CUADRADO[0][1])==(A[0][0],A[0][1]) or (pos_CUADRADO[0][0],pos_CUADRADO[0][1])==(A[3][0],A[3][1]) or (pos_CUADRADO[0][0],pos_CUADRADO[0][1])==(A[4][0],A[4][1]) or (pos_CUADRADO[0][0],pos_CUADRADO[0][1])==(A[1][0],A[1][1]) or (pos_CUADRADO[0][0],pos_CUADRADO[0][1])==(A[5][0],A[5][1]) or (pos_CUADRADO[0][0],pos_CUADRADO[0][1])==(A[2][0],A[2][1]):
                        pos_CUADRADO[0][1] -= 55
                    else:
                        #For que revisa que posición esta el jugador y el estado de su casilla, cambiandolo entre 1 y 0
                        for i in RESTRICCION_VENTANAx:
                            for j in RESTRICCION_VENTANAy:
                                a,b=(restriccion(RESTRICCION_JUGADOR,pos_CUADRADO))
                                if (i,j)==((pos_CUADRADO[0][0],pos_CUADRADO[0][1])):
                                    if ESTADOS[b]==0:
                                        ESTADOS[b]=1
                                        PUNTAJE+=int(1000/(CONTADOR_frame-tiempo_uP+1))
                                    else:
                                        ESTADOS[b]=0
                                        #Cálculo puntaje-tiempo de reacción
                                        PUNTAJE-=int(1500/(CONTADOR_frame-tiempo_uP+1))
                                        if PUNTAJE<0:
                                            PUNTAJE=0
                    tiempo_uP=CONTADOR_frame

                if TECLA_PRESIONADA == 'd':
                    #Cargar la imagen del jugador
                    jugador=pygame.image.load("jugador.png")
                    pos_CUADRADO[0][0] += 55
                    #Restricción con obstáculos y con tablero10x10                
                    if (restriccion(RESTRICCION_JUGADOR,pos_CUADRADO)==False) or (pos_CUADRADO[0][0],pos_CUADRADO[0][1])==(A[0][0],A[0][1]) or (pos_CUADRADO[0][0],pos_CUADRADO[0][1])==(A[3][0],A[3][1]) or (pos_CUADRADO[0][0],pos_CUADRADO[0][1])==(A[4][0],A[4][1]) or (pos_CUADRADO[0][0],pos_CUADRADO[0][1])==(A[1][0],A[1][1]) or (pos_CUADRADO[0][0],pos_CUADRADO[0][1])==(A[5][0],A[5][1]) or (pos_CUADRADO[0][0],pos_CUADRADO[0][1])==(A[2][0],A[2][1]):
                        pos_CUADRADO[0][0] -= 55
                    else:
                        #For que revisa que posición esta el jugador y el estado de su casilla, cambiandolo entre 1 y 0
                        for i in RESTRICCION_VENTANAx:
                            for j in RESTRICCION_VENTANAy:
                                a,b=(restriccion(RESTRICCION_JUGADOR,pos_CUADRADO))
                                if (i,j)==((pos_CUADRADO[0][0],pos_CUADRADO[0][1])):
                                    if ESTADOS[b]==0:
                                        ESTADOS[b]=1
                                        PUNTAJE+=int(1000/(CONTADOR_frame-tiempo_uP+1))
                                    else:
                                        ESTADOS[b]=0
                                        #Cálculo puntaje-tiempo de reacción
                                        PUNTAJE-=int(1500/(CONTADOR_frame-tiempo_uP+1))
                                        if PUNTAJE<0:
                                            PUNTAJE=0
                    tiempo_uP=CONTADOR_frame
                
                #Tecla para reiniciar partida
                if TECLA_PRESIONADA == 'r':
                    menu=True
                    main()
            
    pygame.quit()
    sys.exit()

main()
