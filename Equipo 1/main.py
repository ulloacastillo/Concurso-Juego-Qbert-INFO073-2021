
import pygame
import sys
import random
from pygame.mixer import pause


#Funcion que reinicia el juego 
def Reiniciar(A,x,y,x1,y1,x2,y2,vivo,vidas,puntaje): 
    puntaje = 10000#Reiniciar Puntaje
    A = crearLista()#Volver a crear el tablero
    A = crearObstaculos(A)#Volver a generar obstaculos
    x = 10
    y = 0#Devolver jugador al principio
    (x1,y1) = randomEnemigo(A)
    (x2,y2) = randomEnemigo(A)#Volver a generar enemigos
    
    while((x1,y1) == (x2,y2)):#Ver si estan en la misma posicion
        (x2,y2)=randomEnemigo(A)#Generar de nuevo el otro enemigo
    
    vivo = True#Devolver variable de visa
    vidas = 3#Reinicar vidass
    
    return(A,x,y,x1,y1,x2,y2,vivo,vidas,puntaje)

#Funcion que carga la imagen y le cambia el tamaño       
def cargarImagen(a,x,y):
    Im = pygame.image.load(a)#Buscar la imagen
    Im = pygame.transform.scale(Im,(x,y))#Transformar la escala
    
    return(Im)

#Funcion que genera el tablero    
def crearLista():
    A = []
    B = []#Crear listas vacias
    
    for i in range(10):
        B = []#Reinica B
        
        for j in range(10):
            B.append(0)#Llenar lista con 0
        
        A.append(B)#Llenar lista A con lista B
    
    return(A)

#Funcion que crea obstaculos
def crearObstaculos(A):
    A[0][0]=1#Lista del tablero
    a,b=Obstaculos(A,1,8)
    A[a][b]=2#Crear primer obstaculo
    obstaculo2= True
    obstaculo31= True
    obstaculo32= True#Bucles infinitos
    
    while(obstaculo2 == True):
        c,d = Obstaculos(A,1,8)
        
        while(comparar(A,c,d)):
            c,d = Obstaculos(A,2,7)
        
        if(random.uniform(0,1) <= 0.5):
            
            if(d != 9):
                obstaculo2 = comparar(A,c,d+1)
                
                if(obstaculo2 == False):
                    A[c][d+1]=2
            else:
                
                obstaculo2 = comparar(A,c,d-1)
                
                if(obstaculo2 == False):
                    A[c][d-1]=2
        else:
            
            if(c != 9):
                obstaculo2 = comparar(A,c+1,d)
                
                if(obstaculo2 == False):
                    A[c+1][d]=2
            else:
                
                obstaculo2 = comparar(A,c-1,d)
                
                if(obstaculo2 == False):
                    A[c-1][d]=2
    A[c][d]=2

    if(random.uniform(0,1) <= 0.5):
        
        while(obstaculo32 == True):
            obstaculo31 = True
            
            while(obstaculo31 == True):
                e,f = Obstaculos(A,0,9)
                
                while(comparar(A,e,f)):
                    e,f = Obstaculos(A,0,9)
                
                if(f != 9)and(f != 8):
                    obstaculo31 = comparar(A,e,f+1) 
                
                else:
                
                    obstaculo31 = comparar(A,e,f-1)
            
            if(e != 9)and(e != 8):
                obstaculo32 = comparar(A,e+1,f)
                
                if(obstaculo32 == False):
                    A[e+1][f]=2
                    A[e][f]=2
                    
                    if(f != 9)and(f != 8):
                        A[e][f+1]=2
                    
                    else:
                    
                        A[e][f-1]=2
                    
                    return(A)
            else:
                
                obstaculo32 = comparar(A,e-1,f)
                
                if(obstaculo32 == False):
                    A[e-1][f]=2
                    A[e][f]=2
                    
                    if(f != 9)and(f != 8):
                        A[e][f+1]=2
                    
                    else:
                       
                        A[e][f-1]=2
                    
                    return(A)
    else:
        
        while(obstaculo32 == True):
            obstaculo31 = True
            
            while(obstaculo31 == True):
                e,f = Obstaculos(A,0,9)
                
                while(comparar(A,e,f)):
                    e,f = Obstaculos(A,0,9)
                
                if(e != 0)and(e != 1):
                    obstaculo31 = comparar(A,e-1,f)
                
                else:
                    
                    obstaculo31 = comparar(A,e+1,f)
            
            if(f != 0)and(f != 1):
                obstaculo32 = comparar(A,e,f-1)
                
                if(obstaculo32 == False):
                    A[e][f-1]=2
                    A[e][f]=2
                    
                    if(e != 0)and(e != 1):
                        A[e-1][f]=2
                    
                    else:
                    
                        A[e+1][f]=2
                    
                    return(A)
            else:
                
                obstaculo32 = comparar(A,e,f+1)
                
                if(obstaculo32 == False):
                    A[e][f+1]=2
                    A[e][f]=2
                    
                    if(e != 0)and(e != 1):
                        A[e-1][f]=2
                    
                    else:
                    
                        A[e+1][f]=2
                    
                    return(A)
    
    

    
    
#Funcion que genera posiciones aleatorias para los enemigos    
def randomEnemigo(A):
    x = random.randrange(10,451,60)
    y = random.randrange(0,451,60) #Posiciones enemigo
    
    while(comparar2(A,((x-10)//60),(y//60)) == True):#Ver si hay un obstaculo
        x = random.randrange(10,451,60)
        y = random.randrange(0,451,60)#Generar enemigo de nuevo
    
    return(x,y)

#Funcion que mira si el personaje choco con el enemigo   
def matar(v,x1,x2,y1,y2):
    
    if(((x1 == x2)and(y1 == y2))): #"Matar" al cuadradito cuando se posa encima
       
       return False
    
    return True

#Funcion que mira si todos el tablero esta pintado
def ganar(A):
    
    for i in range(10):
        
        for j in range(10):
            
            if(A[i][j] == 0):
                
                return False
    
    return True
            
#Funcion que hace que se muevan los enemigos y se cambien los estados del tablero cuando se mueve el jugador
def cambiarEstados(A,x,y,x1,y1,x2,y2,v,w1,s1,a1,d1,w2,s2,a2,d2,i1,i2):
    cambiarColores(x,y,A)
    v = ((matar(v,x,x1,y,y1))and(matar(v,x,x2,y,y2)))#Ver si el cuadradito sigue vivo
    
    if(v):#Cuando el cuadradito este vivo
        (x1,y1,i1) = moverEnemigo(A,x1,y1,i1,w1,s1,d1,a1)
        
        while(x1-10,y1) == (0,0):
            (x1,y1,i1) = moverEnemigo(A,x1,y1,i1,w1,s1,d1,a1)
        
        (x2,y2,i2) = moverEnemigo(A,x2,y2,i2,w2,s2,d2,a2)#Mover a los enemigos
        
        while(x2-10,y2) == (0,0):
            (x2,y2,i2) = moverEnemigo(A,x2,y2,i2,w2,s2,d2,a2)#Mover a los enemigos
        
        while((x1,y1) == (x2,y2)):#Ver si se chocan
            (x2,y2,i2) = moverEnemigo(A,x2,y2,i2,w2,s2,d2,a2)#Moverlo hacia otro lado
    
    return(A,x1,x2,y1,y2,i1,i2)

#Funcion que mueve al enemigo aleatoriamente 
def moverEnemigo(A,x,y,Im,w,s,d,a):
    EnEm = True
    
    while(EnEm == True):
        
        #Mover en horizontal
        if(random.uniform(0,1) <= 0.5):
            
            if(((x-10) < 590-50)and((x-10) > 0)):
                
                if random.uniform(0,1)<0.5:
                    
                    if((comparar3(A,(((x-10)//60)+1),(y//60)) == True) and (comparar4((((x-10)//60)+1),(y//60)) == True)):
                        x+=60
                        Im = pygame.image.load(d)
                        
                        return(x,y,Im)
                else:
                    
                    if((comparar3(A,(((x-10)//60)-1),(y//60)) == True) and (comparar4((((x-10)//60)-1),(y//60)) == True)):
                        x-=60 
                        Im = pygame.image.load(a)
                        
                        return(x,y,Im)
            
            if((x-10) == 590-50):#Evitar que salga del mapa
                
                if((comparar3(A,(((x-10)//60)-1),(y//60)) == True) and (comparar4((((x-10)//60)-1),(y//60)) == True)):
                    x-=60
                    Im = pygame.image.load(a)
                    
                    return(x,y,Im)
            
            if((x-10) == 0):
                
                if((comparar3(A,(((x-10)//60)+1),(y//60)) == True) and (comparar4((((x-10)//60)+1),(y//60)) == True)):
                    x+=60
                    Im = pygame.image.load(d)
                    
                    return(x,y,Im)
        #Mover en vertical
        
        else: 
            
            if((y < 590-50) and (y > 0)):
                
                if random.uniform(0,1) <= 0.5:
                    
                    if((comparar3(A,((x-10)//60),((y//60)-1)) == True) and (comparar4(((x-10)//60),((y//60)-1)) == True)):
                        y-=60
                        Im = pygame.image.load(s)
                        
                        return(x,y,Im)
                
                else:
                    
                    if((comparar3(A,((x-10)//60),((y//60)+1)) == True) and (comparar4(((x-10)//60),((y//60)+1)) == True)):
                        y+=60 
                        Im = pygame.image.load(w)
                        
                        return(x,y,Im)
            
            if(y == 590-50):#Evitar que salga del mapa
                
                if((comparar3(A,((x-10)//60),((y//60)-1)) == True) and (comparar4(((x-10)//60),((y//60)-1)) == True)):
                    y-=60
                    Im = pygame.image.load(s)
                    
                    return(x,y,Im)
            
            if(y == 0):
                
                if((comparar3(A,((x-10)//60),((y//60)+1)) == True) and (comparar4(((x-10)//60),((y//60)+1)) == True)):##Ver que no hayan obstaculos
                    y+=60 #Mover al enemigo
                    Im = pygame.image.load(w)#Cargar imagen
                    
                    return(x,y,Im)

#Funcion que mira si en la posicion estan las primeras posiciones del tablero para evitar loops infinitos de muerte
def comparar4(x,y):
    
    if(((x,y) == (0,0))or((x,y) == (1,0)) or ((x,y) == (0,1)) or ((x,y) == (1,1))):#Ver si esta en (0,0),(0,1),(1,0)o(1,1)
       
       return False
    
    return True

#Funcion que mira si no hay un obstaculo   
def comparar3(A,x,y):
    if(A[x][y] != 2):#Ver si no hay un obstacullo
        
        return True
    
    return False

#Funcion que mira si en la posicion hay un obstacolu o esta el personaje principal
def comparar2(A,a,b):
    if((A[a][b] == 2)or(A[a][b]==1)):#Ver si hay un obstaculo o es la posicion inicial del cuadradito
        
        return True
    
    return False

#Funcion que mira si en la posicion ya hay un obstaculo
def comparar(A,a,b):
    if(A[a][b] == 2):#Ver si hay un obstaculo
       
       return True
    
    return False

#Funcion que genera numeros aleatorios para los obstaculos   
def Obstaculos(A,x,y):
    a = random.randint(x,y)
    b = random.randint(x,y)#Generar posicones aleatorias
    
    while((a == 0) and (b == 1) or (( a== 1) and (b == 0)) or ((a == 0) and (b == 0)) or ((a == 1) and (b == 1))):#Ver si el obstaculo esta en la posicion inicial o bloquea al cuadradito
        a = random.randint(x,y)
        b = random.randint(x,y)#Generar de nuevo
        
        while(comparar(A,a,b)):#Ver si ya hay un obstaculo en la posicion
            a = random.randint(x,y)
            b = random.randint(x,y)#Generar de nuevo
            
            while((a == 0) and (b == 1) or ((a == 1) and (b == 0)) or ((a == 0) and (b == 0))):
                a = random.randint(x,y)
                b = random.randint(x,y)
    
    return(a,b)

#Funcion que cambia los estados del tablero
def cambiarColores(x,y,A):
    
    if(A[x//60][y//60] == 1):
        A[x//60][y//60] = 0#Pintar verde
    
    else:
        
        A[x//60][y//60] = 1#Pintar cafe
    
    return(A)

#Funcion principal del juego
def main():
    
    reloj = pygame.time.Clock() #Llamar a la funcion de velocidad
    pygame.font.init()
    pygame.mixer.init()
    
    #Cargar imagenes que se usaran
    principal = cargarImagen("Principal.png",1000,700)#Pantalla principañ
    Icono = pygame.image.load(icono)
    Fondo = cargarImagen(fondo,1000,700)#Fondo
    Vidas = cargarImagen(vida,110,110)#Vidas
    imagen1 = pygame.image.load(Front1)#Enemigo 1
    picture1 =pygame.transform.scale(imagen1,(30,50))#Ajustar tamaño
    imagen2 = pygame.image.load(Front2)#Enemigo 2
    picture2 = pygame.transform.scale(imagen2,(30,50))#Ajustar tamaño
    Victoria = cargarImagen(victoria,1000,700)#Pantalla de victoria
    Derrota = cargarImagen(derrota,1000,700)#Pantalla de derrota
    P_left = cargarImagen(p_left,30,50)
    P_right = cargarImagen(p_right,30,50)#Personaje Principal
    instrucciones = cargarImagen(Instrucciones,1000,700)#Instrucciones del juego
    controles = cargarImagen(Controles,1000,700)#Controles del juego
    control = cargarImagen(Control,370,113)
    instru = cargarImagen(Instru,370,113)
    Intro1 = cargarImagen(intro1,1000,700)
    Intro2 = cargarImagen(intro2,1000,700)
    Intro3 = cargarImagen(intro3,1000,700)
    Intro4 = cargarImagen(intro4,1000,700)
    Intro5 = cargarImagen(intro5,1000,700)#Introduccion
    puntos= cargarImagen(Puntos,300,75)
    intro0= cargarImagen(Intro0,1000,700)
    
    A = crearLista()#Crear un tablero vacio
    A = crearObstaculos(A)#Poner obstaculos en el tablero
    
    ventana = pygame.display.set_mode((ancho_ventana,alto_ventana))#Crear la ventana
    pygame.display.set_caption("Project Crossover")#Titulo
    pygame.display.set_icon(Icono)#Poner icono
    
    xCuadradito = 10 
    yCuadradito = 0 #Posiciones cuadradito
    
    (xEnemigo1,yEnemigo1) = randomEnemigo(A)#Posiciones primer enemigo
    (xEnemigo2,yEnemigo2) = randomEnemigo(A)#Posiciones segundo enemigo
    
    while((xEnemigo1,yEnemigo1) == (xEnemigo2,yEnemigo2)):#Ver si estan en la misma posicion
        (xEnemigo2,yEnemigo2) = randomEnemigo(A)#Generar de nuevo el otro enemigo
    
    Jugador = P_right#Imagen del jugador
    
    #Bucles infinitos
    corriendo = True#Para bucle infinito
    vivo = True#Mantener al cuadradito vivo
    jugar = False#Bucle infinito del juego
    vidas = 3#Vidas disponibles
    pausa = False#Bucle infinito de pausa
    
    puntaje = 10000#Puntaje Inicial
    
    
    #Sonidos
    movimiento = pygame.mixer.Sound('movimiento.mp3')
    muerte = pygame.mixer.Sound('muerte.mp3')
    siguiente = pygame.mixer.Sound('siguiente.mp3')
    wasted = pygame.mixer.Sound('Wasted.mp3')
    win = pygame.mixer.Sound('win.mp3')
    win.set_volume(0.04)
    wasted.set_volume(0.04)

    #Introduccion
    for event in pygame.event.get():
                
        if event.type == pygame.QUIT: 
            corriendo = False#Cerrar el programa
            pygame.quit()
            exit()
    reloj.tick(60)
    ventana.blit(intro0,(0,0,1000,700))
    for event in pygame.event.get():
                
        if event.type == pygame.QUIT: 
            corriendo = False#Cerrar el programa
            pygame.quit()
            exit()
    
    pygame.display.flip()
    reloj.tick(0.25)
    ventana.blit(Intro1,(0,0,1000,700))
    for event in pygame.event.get():
                
        if event.type == pygame.QUIT: 
            corriendo = False#Cerrar el programa
            pygame.quit()
            exit()
    
    pygame.display.flip()
    reloj.tick(0.25)
    ventana.blit(Intro2,(0,0,1000,700))
    for event in pygame.event.get():
                
        if event.type == pygame.QUIT: 
            corriendo = False#Cerrar el programa
            pygame.quit()
            exit()
    
    pygame.display.flip()
    reloj.tick(0.25)
    ventana.blit(Intro3,(0,0,1000,700))
    for event in pygame.event.get():
                
        if event.type == pygame.QUIT: 
            corriendo = False#Cerrar el programa
            pygame.quit()
            exit()
    
    pygame.display.flip()
    reloj.tick(0.25)
    ventana.blit(Intro4,(0,0,1000,700))
    for event in pygame.event.get():
                
        if event.type == pygame.QUIT: 
            corriendo = False#Cerrar el programa
            pygame.quit()
            exit()
    
    pygame.display.flip()
    reloj.tick(0.25)
    ventana.blit(Intro5,(0,0,1000,700))
    for event in pygame.event.get():
                
        if event.type == pygame.QUIT: 
            corriendo = False#Cerrar el programa
            pygame.quit()
            exit()
    
    pygame.display.flip()
    reloj.tick(0.25)


    while(corriendo == True):#Bucle infinito
        reloj.tick(60)
        if(vidas == 3)and(ganar(A) == False):#Generar la ventana de inicio si aun no se pierde ni gana
    
            ventana.blit(principal,(0,0,1000,700))
            
            pygame.display.flip()
            
        
        for event in pygame.event.get():
                
            if event.type == pygame.QUIT: #Cerrar el programa
                corriendo = False
                pygame.quit()
                
                exit()
            
            if event.type == pygame.KEYDOWN:#Activar el teclado
                tecla1 = pygame.key.name(event.key)
                
                if tecla1 == "return":#Empezar el juego
                    jugar = True
                    siguiente.play()
            
            pygame.display.flip()
        
        while(jugar == True):#El juego
            
            reloj.tick(7)
            
            if(puntaje > 0):#Evitar que el puntaje sea numeros negativos
                puntaje-=10#Descontar al puntaje
            
            p = str(puntaje)#Para ponerlo en pantalla
            letra = pygame.font.SysFont("Arial",130,10)#Tipo de letra
            Letra = letra.render(p,0,(150, 9, 9))#Variable que contiene al puntaje
            
            if(vidas == 0):
                jugar = False#Finalizar el juego cuando no quedan vidas
            
            reloj.tick(60) #Velocidad
            ventana.blit(Fondo,(0,0,1000,700)) #Pintar la ventana
            ventana.blit(instru,(619,250,370,113))#Poner imagen de instrucciones
            ventana.blit(control,(590,175,370,113))#Poner imagen de control
            ventana.blit(Letra,(650,400))#Poner el puntaje
            ventana.blit(puntos,(625,335,300,75))#Poner imagen de puntos

            pygame.init()#Iniciar programa
        
            Apagado = cargarImagen(pasto,50,50)
            Encendido = cargarImagen(tierra,50,50)
            Obstaculo = cargarImagen(caja,50,50)#Ajustar el tamaño de las cosas del tablero
            
            for i in range(10):
                
                for j in range(10):#Dibujar Tablero
                    
                    if(A[i][j]==0):
                        ventana.blit(Apagado,(0+60*i,(0+60*j)+20,50,50))#Pintar verde
                    
                    if(A[i][j]==1):
                        ventana.blit(Encendido,(0+60*i,(0+60*j)+20,50,50))#Pintar cafe
                    
                    if(A[i][j]==2):
                        ventana.blit(Obstaculo,(0+60*i,(0+60*j)+20,50,50))#Pintar gris
            
            if(vivo == True):#Mantener personaje mientras este vivo
                ventana.blit(Jugador,(xCuadradito,yCuadradito,30,50))#Dibujar personaje
            
            else:#Cuando el cuadradito ya no esta vivo
                
                xCuadradito =10 
                yCuadradito = 0#Devolver al cuadradito al inicio
                vidas-=1#Quitar una vida
                muerte.play()
                vivo = True#Devolver vida al cuadradito
            
            picture1 = pygame.transform.scale(imagen1,(30,50))
            ventana.blit(picture1,(xEnemigo1,yEnemigo1,30,50))
            picture2 = pygame.transform.scale(imagen2,(30,50))#Ajustar tamaño enemigo
            ventana.blit(picture2,(xEnemigo2,yEnemigo2,30,50))#Dibujar enemigo
            
            for i in range(vidas):
                xVidas = 610+130*i
                yVidas = 50#Posiciones de las vidas
                ventana.blit(Vidas,(xVidas,yVidas,110,110))#Dibujar vidas en la pantalla
            
            if(ganar(A) == True):#Ganar el juego
                jugar = False#Aqui termina el juego
                
            for event in pygame.event.get():
                
                if event.type == pygame.QUIT: #Cerrar el programa
                    corriendo = False
                    pygame.quit()
                    sys.exit()
                    
                    exit()
            
                if event.type == pygame.KEYDOWN:#Activar el teclado
                    tecla_presionada = pygame.key.name(event.key)#Mover con las teclas
                    
                        

                    if(tecla_presionada == "r"):#Reiniciar el juego
                        siguiente.play()
                        jugar = False#Aqui termina el juego
                        (A,xCuadradito,yCuadradito,xEnemigo1,yEnemigo1,xEnemigo2,yEnemigo2,vivo,vidas,puntaje)=Reiniciar(A,xCuadradito,yCuadradito,xEnemigo1,yEnemigo1,xEnemigo2,yEnemigo2,vivo,vidas,puntaje)
                    
                    if(tecla_presionada == "i"):#Mostrar instrucciones cuando aprietas i
                        pausa = True#Se pausa el juego
                        siguiente.play()
                        
                        while(pausa == True):
                            ventana.blit(instrucciones,(0,0,1000,700))#mostrar Instrucciones en pantalla
                            
                            for event in pygame.event.get():
                                
                                if event.type == pygame.KEYDOWN:
                                    teclapausa = pygame.key.name(event.key)
                                    
                                    if(teclapausa == "i"):#Cerrar instrucciones
                                        pausa = False#Continua el juego
                                        siguiente.play()
                            
                            pygame.display.flip()
                            
                    
                    if(tecla_presionada == "c"):#Mostrar instrucciones cuando aprietas i
                        pausa = True#Se pausa el juego
                        siguiente.play()
                        
                        while(pausa == True):
                            ventana.blit(controles,(0,0,1000,700))#mostrar Instrucciones en pantalla
                            
                            for event in pygame.event.get():
                                
                                if event.type == pygame.KEYDOWN:
                                    teclapausa = pygame.key.name(event.key)
                                    
                                    if(teclapausa == "c"):#Cerrar instrucciones
                                        pausa = False#Continua el juego
                                        siguiente.play()
                            
                            pygame.display.flip()
                    
                    
                    if(vivo):#Moverse mientras siga vivo el personaje
                        
                        if tecla_presionada == "up" or tecla_presionada == "w":#Mover hacia arriba
                            
                            if(yCuadradito>0):#No salir de los limites
                                
                                if(A[(xCuadradito-10)//60][(yCuadradito//60)-1]!=2):#No pisar obstaculos
                                    yCuadradito-=60
                                    movimiento.play()
                                    #Cambiar las cosas del tablero
                                    (A,xEnemigo1,xEnemigo2,yEnemigo1,yEnemigo2,imagen1,imagen2)=cambiarEstados(A,xCuadradito,yCuadradito,xEnemigo1,yEnemigo1,xEnemigo2,yEnemigo2,vivo,Front1,Backward1,Left1,Right1,Front2,Backward2,Left2,Right2,imagen1,imagen2)
                                    
                        if tecla_presionada == "left" or tecla_presionada == "a":#Mover hacia abajo
                            
                            if(xCuadradito-10>0):#No salir de los limites
                                
                                if(A[((xCuadradito-10)//60)-1][yCuadradito//60]!=2):#No pisar obstaculos
                                    xCuadradito-=60
                                    Jugador = P_left
                                    movimiento.play()
                                    (A,xEnemigo1,xEnemigo2,yEnemigo1,yEnemigo2,imagen1,imagen2) = cambiarEstados(A,xCuadradito,yCuadradito,xEnemigo1,yEnemigo1,xEnemigo2,yEnemigo2,vivo,Front1,Backward1,Left1,Right1,Front2,Backward2,Left2,Right2,imagen1,imagen2)
                                    
                        if tecla_presionada == "down" or tecla_presionada == "s":#Mover hacia la derecha
                            
                            if(yCuadradito<590-50):#No salir de los limites
                                
                                if(A[(xCuadradito-10)//60][(yCuadradito//60)+1]!=2):#No pisar obstaculos
                                    yCuadradito+=60
                                    movimiento.play()
                                    (A,xEnemigo1,xEnemigo2,yEnemigo1,yEnemigo2,imagen1,imagen2) = cambiarEstados(A,xCuadradito,yCuadradito,xEnemigo1,yEnemigo1,xEnemigo2,yEnemigo2,vivo,Front1,Backward1,Left1,Right1,Front2,Backward2,Left2,Right2,imagen1,imagen2)
                                    
                        if tecla_presionada == "right" or tecla_presionada == "d":#Las teclas que se pueden usar para moverla
                            
                            if(xCuadradito-10 < 590-50):#Mover hacia la izquerda
                                
                                if(A[((xCuadradito-10)//60)+1][yCuadradito//60] != 2):#No pisar obstaculos
                                    xCuadradito+=60
                                    Jugador = P_right
                                    movimiento.play()
                                    (A,xEnemigo1,xEnemigo2,yEnemigo1,yEnemigo2,imagen1,imagen2)=cambiarEstados(A,xCuadradito,yCuadradito,xEnemigo1,yEnemigo1,xEnemigo2,yEnemigo2,vivo,Front1,Backward1,Left1,Right1,Front2,Backward2,Left2,Right2,imagen1,imagen2)
                                    #Cambiar los colores y mover los enemigos               
            
            #Cambiar la variable vivo si chocas con un enemigo
            vivo = ((matar(vivo,xCuadradito,xEnemigo1,yCuadradito,yEnemigo1))and(matar(vivo,xCuadradito,xEnemigo2,yCuadradito,yEnemigo2)))
            
            #Quitar una vida cuando chocas con un enemigo
            pygame.display.flip()#Actualizar
        
        if(vidas == 0):#Cuando pierdes el juego
            musicaWasted= True
            ventana.blit(Derrota,(0,0,1000,700))#Pantalla de derrota
            ventana.blit(puntos,(355,437,300,75))
            ventana.blit(letra.render("0",0,(199, 179, 0)),(650,400))#Mostrar puntaje=0
            
            wasted.play()#Musica de derrota
            
        if((vidas != 0)and(ganar(A))):#Cuando ganas 
            ventana.blit(Victoria,(0,0,1000,700))#Mostrar pantalla de victoria
            ventana.blit(puntos,(355,475,300,75))
            ventana.blit(letra.render(p,0,(199, 179, 0)),(363,520))#Mostrar puntaje que quedo
            win.play()#Musica de victoria
        
        pygame.display.flip()#Actualizar
            
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT: #Cerrar el programa
                corriendo = False
                pygame.quit()
                sys.exit
                
                exit()
                
            if event.type == pygame.KEYDOWN:
                tecla = pygame.key.name(event.key)
                
                if(tecla == "r")or(tecla == "return"):#Teclas que se pueden usar para volver a jugar
                    wasted.stop()
                    win.stop()#Parar musica
                    #Reinicar tablero
                    (A,xCuadradito,yCuadradito,xEnemigo1,yEnemigo1,xEnemigo2,yEnemigo2,vivo,vidas,puntaje)=Reiniciar(A,xCuadradito,yCuadradito,xEnemigo1,yEnemigo1,xEnemigo2,yEnemigo2,vivo,vidas,puntaje)
                    
                    
        pygame.display.flip()#Actualizar
    pygame.quit()
    sys.exit()#Cerrar el programa
    
    exit()
    
#Programa Principal

ancho_ventana = 1000
alto_ventana = 700#Tamañp de la ventana

#Imagenes
Front1 = "Agent_Front.png"
Front2 = "Ingenier_Front.png"
Backward1 = "Agent_Backward.png"
Backward2 = "Ingenier_Backward.png"
Right1 = "Agent_Right.png"
Right2 = "Ingenier_Right.png"
Left1 = "Agent_Left.png"
Left2 = "Ingenier_Left.png"
pasto = "Pasto.png"
tierra = "Tierra.png"
caja = "Obstaculo.png"
vida = "corazones.png"
fondo = "fondo.png"
victoria = "Victoria.png"
icono = "icono.png"
p_left = "personaje_left.png"
p_right = "personaje_Right.png"
derrota = "derrota.png"
Instrucciones = "Instrucciones.png"
Controles = "controles.png"
Control = "control.png"
Instru = "instru.png"
intro1 = "1GG.png"
intro2 = "2GG.png"
intro3 = "3GG.png"
intro4 = "4GG.png"
intro5 = "5GG.png"
Intro0 = "0GG.png"
Puntos = "puntos.png"

main()
