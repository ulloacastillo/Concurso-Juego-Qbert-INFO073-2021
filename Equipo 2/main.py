
import pygame
import sys
import random
#Constantes
ANCHO = 1300
ALTO = 720
SIZE_BLOCK = 70
PORTE=70
MORADO = (121, 50, 168)
BLANCO = (255,255,255)
VERDE = (50, 168, 149)
NEGRO=(0,0,0)
ROJO = (252, 3, 3)
AZUL = (0,0, 255,)
reloj = pygame.time.Clock()
imagen_sumi = pygame.image.load("sumi.png")
fondo_principal = pygame.image.load("fondo.jpg")
fondo_juego= pygame.image.load("fondo_neon.png")
historia = pygame.image.load("historia.png")
instrucciones = pygame.image.load("instrucciones.png")
obstaculo= pygame.image.load("obstaculo.jpg")
vidas_imagen= pygame.image.load("vida.png")
personaje= pygame.image.load("elsus.jpg")
moneda = pygame.image.load("bitcoin.png")
enemigo_chino= pygame.image.load("enemigo1.png")
enemigo_bitcoin=pygame.image.load("enemigo2.png")
piso=pygame.image.load("ladrillo.png")
victoria_imagen= pygame.image.load("victoria.png")
derrota_imagen= pygame.image.load("derrota.jpg")



#Sonidos
def sonido_fondo():
    pygame.mixer.music.load("drip_amongos.mp3")
    pygame.mixer.music.play(-1)
def sonido_colision():
    colision=pygame.mixer.Sound("colision.mp3")
    pygame.mixer.Sound.play(colision)
def sonido_derrota():
    derrota=pygame.mixer.Sound("burla.mp3")
    pygame.mixer.Sound.play(derrota)
    
def sonido_pasos():
    pasos=pygame.mixer.Sound("pasos_1.wav")
    pygame.mixer.Sound.play(pasos)
def sonido_victoria():
    victoria=pygame.mixer.Sound("sonido_victoria.mp3")
    pygame.mixer.Sound.play(victoria)
    
#funcion cerrado
def cerrar_juego():
    pygame.quit()
    sys.exit()
    quit()
            
#Funcion Colisiones   
def colisiones(xCuadr, yCuadr,xEne, yEne):
    if xEne + 70 >xCuadr and xEne < xCuadr + 70 and yEne +70 > yCuadr and yEne < yCuadr +70:
        return True
    return False

#Funcion posicion inicial
def monito_choca():
    xCuadradito=0
    yCuadradito=0
    xP=0
    yP=0
    return xCuadradito,yCuadradito,xP,yP

#Función Para Cambiar los Estados de la matriz
def Estado(matriz,yP,xP):
    if matriz [yP][xP]==0:
        matriz [yP][xP]=1            
    else:
        matriz [yP][xP]=0
    return matriz    


#Función Movimiento Enemigo
def mov(a,b,yEnemigo,xEnemigo,yE2,xE2,matriz):
    lista_enemigo=[]
    for i in range(10):
        lista_enemigo.append([])
        for j in range(10):
            lista_enemigo[i].append(0)
    lista_enemigo[a][b]=1
    lista_enemigo[yE2][xE2]=1
    
    if random.uniform(0,1)<= 0.5:
        if random.uniform(0,1)<=0.5 :
            if b<9 and matriz [a][b+1]!=-1 and lista_enemigo[a][b+1]!=lista_enemigo[yE2][xE2] and a!=0 and b!=0:
                xEnemigo += 70
                b+=1
        else:
            if b > 1 and matriz [a][b-1]!=-1 and lista_enemigo[a][b-1]!=lista_enemigo[yE2][xE2] and a!=0 and b!=0:
                xEnemigo -= 70
                b-=1    
    else:
        if random.uniform(0,1)<=0.5 :
            if a>1 and matriz [a-1][b]!=-1 and lista_enemigo[a-1][b]!=lista_enemigo[yE2][xE2] and a!=0 and b!=0:               
                yEnemigo-= 70
                a-=1       
        else:
            if a<9 and matriz [a+1][b]!=-1 and lista_enemigo[a+1][b]!=lista_enemigo[yE2][xE2] and a!=0 and b!=0:               
                yEnemigo+= 70
                a+=1            
    return a,b,yEnemigo,xEnemigo

#Funcion Victoria
def victoria(matriz):
    cont=0
    for i in range(len(matriz)):
            for j in range(len(matriz)):
                if matriz [i][j]==0:
                    cont+=1
    if cont==0:
        jugando1= False
        pantalla_victoria= True
        
    else:
        jugando1= True
        pantalla_victoria= False
        
                  
    return pantalla_victoria, jugando1,cont

#Funcion derrota
def derrota(vidas):
    if vidas==1 or vidas ==2 or vidas==3:
        jugando2= True
        pantalla_derrota= False
    if vidas==0:
        jugando2= False
        pantalla_derrota= True
    return pantalla_derrota,jugando2   


def main():
    #Iniciar Ventana de juego
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO,ALTO))
    pygame.display.set_caption("AmongBert")
    sonido_fondo()
    contador_puntaje=0
    
    #Personaje
    xCuadradito = 0
    yCuadradito = 0

    #Coordenada en La matriz
    xP=0
    yP=0 
    
    pygame.display.flip()

     
    #Creación de Matriz
    a=0
    matriz = []
    for i in range(10):
        matriz.append([])
        for j in range(10):
            matriz[i].append(a)
            
    #Definir el estado de la posicion inicial 
    matriz[0][0]=1
    #Creación de Obstáculo
    for i in range (3):
        x = random.randrange(2,9)
        y = random.randrange(2,9)
        if i!=0:
            #Validar que no se superpongan
            while matriz[y][x]==matriz[k][j] or matriz[y+1][x]==matriz[k][j] or matriz[y-1][x]==matriz[k][j] or matriz[y+1][x+1]==matriz[k][j] or matriz[y+1][x-1]==matriz[k][j] or matriz[y-1][x+1]==matriz[k][j] or matriz[y][x+1]==matriz[k][j] or matriz[y][x-1]==matriz[k][j] or matriz[y-1][x-1]==matriz[k][j]: 
                x = random.randrange(2,9)
                y = random.randrange(2,9)
        matriz [y][x]=-1
        if i !=0 :
            if x==9 :
                matriz [y][x-1]=-1

            else:    
                matriz [y][x+1]=-1
        if i == 2:
            #Validar que el obstáculo este dentro del tablero
            if x == 9 and y == 9:
                matriz [y-1][x-1]=-1
                
            if x==9 and y!=9:
                matriz [y+1][x-1]=-1
            if x!=9 and y==9:
                matriz [y-1][x+1]=-1
            if x!=9  and y !=9 :
                matriz [y+1][x+1] = -1
        #Controlar la posición de mis obstaculos para validarlas
        j=x
        k=y   
            
    #Enemigos
    lista_validar=[]
    for i in range(10):
        lista_validar.append([])
        for j in range(10):
            lista_validar[i].append(0)    

    x_ene = random.randrange(4,9)
    y_ene = random.randrange(4,9)
    x_ene2 = random.randrange(4,9)
    y_ene2 = random.randrange(4,9)
    lista_validar[y_ene][x_ene]=1
    lista_validar[y_ene2][x_ene2]=2
    
    #Enemigo1
    while lista_validar[y_ene][x_ene] == 2:
        x_ene = random.randrange(4,9)
        y_ene = random.randrange(4,9)
    while matriz[y_ene][x_ene] == -1:   
        if matriz[y_ene][x_ene] == -1:
            x_ene = random.randrange(4,9)
            y_ene = random.randrange(4,9)
    xEnemigo=x_ene*70
    yEnemigo=y_ene*70

    #Coordenada matriz (Enemigo1)
    xE=x_ene
    yE=y_ene

    #Enemigo 2
    while matriz[y_ene2][x_ene2] == -1:
        if matriz[y_ene2][x_ene2] == -1:
            x_ene2 = random.randrange(4,9)
            y_ene2 = random.randrange(4,9)
    xEnemigo2=x_ene2*70
    yEnemigo2=y_ene2*70
    #Coordenada matriz(Enemigo2)
    xE2=x_ene2
    yE2=y_ene2
    
    #vidas, puntaje , colisiones
    vidas = 3
    puntaje = 0
    colision= 0
    #hace que inicie la primera pantalla
    pantalla_intro= True
    #pantalla de inicio
    while pantalla_intro:
        reloj.tick(60)
        texto_salir= pygame.font.SysFont("console", 30, True)
        texto_intro = pygame.font.SysFont("console",40, True)
        ventana.blit(pygame.transform.scale(fondo_principal,(1300,720)), (0,0))
        click_continuar= texto_salir.render("Presione [ENTER] para jugar", 1,BLANCO)
        salir=texto_salir.render("[ESC]=SALIR",1,BLANCO)
        ventana.blit(salir,[10,10])
        ventana.blit(click_continuar,((ANCHO//2)-(click_continuar.get_width()//2),650))
        enter=0
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                cerrar_juego()
            tecla_enter= pygame.key.get_pressed()    
            if tecla_enter[pygame.K_RETURN] and enter==0:
                pantalla_intro= False
                pantalla_historia= True
                enter+=1
            if tecla_enter[pygame.K_ESCAPE]:
                cerrar_juego()
        pygame.display.update()
       
    #pantalla de la historia, relata el contexto del juego
    while pantalla_historia:
        reloj.tick(60)
        ventana.blit(pygame.transform.scale(historia,(1300,720)), (0,0))
        texto= texto_intro.render("Presione [ENTER] para continuar", 1,BLANCO)
        ventana.blit(texto,((ANCHO//2)-(texto.get_width()//2),650))
        salir=texto_salir.render("[ESC]=SALIR",1,BLANCO)
        ventana.blit(salir,[900,10])
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                cerrar_juego() 
            tecla_enter = pygame.key.get_pressed()
            if tecla_enter[pygame.K_RETURN] and enter==1:
               pantalla_historia = False
               pantalla_instrucciones= True
               enter+=1
            if tecla_enter[pygame.K_ESCAPE]:
                cerrar_juego()  
        pygame.display.update()
    #pantalla de instrucciones    
    while pantalla_instrucciones:
        reloj.tick(60)
        ventana.blit(pygame.transform.scale(instrucciones,(1300,720)), (0,0))
        texto= texto_intro.render("Presione [ENTER] para continuar", 1,BLANCO)
        ventana.blit(texto,((ANCHO//2)-(texto.get_width()//2),650))
        salir=texto_salir.render("[ESC]=SALIR",1,BLANCO)
        ventana.blit(salir,[900,10])
       
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                cerrar_juego()
              
            tecla_enter = pygame.key.get_pressed()
            if tecla_enter[pygame.K_RETURN] and enter==2:
               pantalla_instrucciones = False
               jugando1= True
               jugando2= True
            if tecla_enter[pygame.K_ESCAPE]:
                cerrar_juego()
        pygame.display.update()
    #pantalla de juego
    while jugando1 and jugando2:
        pygame.display.flip()
        reloj.tick(60)
        ventana.blit(pygame.transform.scale(fondo_juego,(1300,720)), (0,0))
        ventana.blit(pygame.transform.scale(imagen_sumi,(300,300)),(1000,420))
        texto_puntos = pygame.font.SysFont("console", 50, True)
        puntos = texto_puntos.render("Puntaje: "+ str(puntaje),1 ,BLANCO)
        ventana.blit(puntos, (780,200))
        texto_vidas=texto_puntos.render("Vidas",1 ,BLANCO)
        ventana.blit(texto_vidas,(850,50))
        salir=texto_salir.render("[ESC]=SALIR",1,BLANCO)
        reiniciar=texto_salir.render("[R]=REINICIAR",1,BLANCO)
        ventana.blit(salir,[750,670])
        ventana.blit(reiniciar,[750,600])
        
        #Generación de tablero 
        for i in range(len(matriz)):
            for j in range(len(matriz)):
                #Pintar Todo el tablero
                ventana.blit(pygame.transform.scale(piso,(60,60)),((j*70)+15, (i*70)+15))
                #Pintar los Obstaculos
                if matriz[i][j] == -1:
                    ventana.blit(pygame.transform.scale(obstaculo,(60,60)),((j*70)+15, (i*70)+15))
                #Pintar Estado Apagado
                if matriz [i][j] == 0:
                    ventana.blit(pygame.transform.scale(moneda,(50,50)),(j*70+20,i*70+20))
                #Pintar Estado Encendido
                if matriz [i][j] == 1:
                    ventana.blit(pygame.transform.scale(piso,(60,60)),((j*70)+15, (i*70)+15))

             
        #Mostrar vidas        
        a=0
        if vidas == 0:
            colision= 3
            corriendo= False
            pantalla_derrota= True
        
        if vidas == 1:
            colision=2
            ventana.blit(pygame.transform.scale(vidas_imagen,(70,70)), (800,90))
        if vidas == 2:
            colision=1
            for i in range(2):
                ventana.blit(pygame.transform.scale(vidas_imagen,(70,70)), (800+a,90))
                a=a+90
        if vidas == 3:
            colision=0
            for i in range (3):
                ventana.blit(pygame.transform.scale(vidas_imagen,(70,70)), (800+a,90))
                a=a+90       
      
                  
        #Personaje
        ventana.blit(pygame.transform.scale(piso,(60,60)),((xCuadradito+15, yCuadradito+15)))            
        ventana.blit(pygame.transform.scale(personaje,(50,50)),(xCuadradito+20,yCuadradito+20))
        #Enemigo 1
        ventana.blit(pygame.transform.scale(piso,(60,60)),((xEnemigo+15, yEnemigo+15))) 
        ventana.blit(pygame.transform.scale(enemigo_chino,(60,60)),(xEnemigo+15,yEnemigo+15))
        #Enemigo 2
        ventana.blit(pygame.transform.scale(piso,(60,60)),((xEnemigo2+15, yEnemigo2+15)))
        ventana.blit(pygame.transform.scale(enemigo_bitcoin,(60,60)),(xEnemigo2+15,yEnemigo2+15))
    
      
        #El puntaje aumentara en 100 cada vez que atrapes una moneda, el puntaje final sera el puntaje obtenido multipicado por las vidas restantes y por la division de 110/contador_puntaje, haciendo que obtengas mas puntos al ganar con menos movimientos.  
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                cerrar_juego()           
            pygame.display.flip()
            #Evento de Presionar la Tecla
            if event.type == pygame.KEYDOWN:
                teclap =pygame.key.name(event.key)
                tecla_esc=pygame.key.get_pressed()
                #Mover al jugador, sus restricciones y definir los estados 
                if teclap == "w" and yCuadradito > 0 and matriz [yP-1][xP]!=-1 :                      
                    yCuadradito -= PORTE
                    yP-=1
                    matriz=Estado(matriz,yP,xP)
                    sonido_pasos()
                    contador_puntaje+=1
                    yE,xE,yEnemigo, xEnemigo = mov(yE,xE, yEnemigo, xEnemigo,yE2, xE2,matriz)
                    yE2,xE2,yEnemigo2, xEnemigo2 = mov(yE2, xE2, yEnemigo2, xEnemigo2,yE,xE,matriz)
                    if yCuadradito > 0 and matriz [yP-1][xP]==0:
                        puntaje+=10
                        contador_puntaje
                if teclap == "a" and xCuadradito > 0 and matriz [yP][xP-1]!=-1:
                    xCuadradito -= PORTE
                    xP-=1
                    matriz=Estado(matriz,yP,xP)
                    sonido_pasos()
                    contador_puntaje+=1
                    yE,xE,yEnemigo, xEnemigo = mov(yE,xE, yEnemigo, xEnemigo,yE2, xE2,matriz)
                    yE2,xE2,yEnemigo2, xEnemigo2 = mov(yE2, xE2, yEnemigo2, xEnemigo2,yE,xE,matriz)
                    if xCuadradito > 0 and matriz [yP][xP-1]==0:
                        puntaje+=10
                if teclap == "s" and yCuadradito < 9*SIZE_BLOCK and matriz [yP+1][xP]!=-1:
                    yCuadradito += PORTE
                    yP+=1
                    matriz=Estado(matriz,yP,xP)
                    sonido_pasos()
                    contador_puntaje+=1
                    yE,xE,yEnemigo, xEnemigo = mov(yE,xE, yEnemigo, xEnemigo,yE2, xE2,matriz)
                    yE2,xE2,yEnemigo2, xEnemigo2 = mov(yE2, xE2, yEnemigo2, xEnemigo2,yE,xE,matriz)
                    if yCuadradito < 9*SIZE_BLOCK and matriz [yP+1][xP]== 0:
                        puntaje+=10
                if teclap == "d" and xCuadradito <9*SIZE_BLOCK and matriz [yP][xP+1]!=-1 :                    
                    xCuadradito += PORTE
                    xP+=1
                    matriz=Estado(matriz,yP,xP)
                    sonido_pasos()
                    contador_puntaje+=1
                    yE,xE,yEnemigo, xEnemigo = mov(yE,xE, yEnemigo, xEnemigo,yE2, xE2,matriz)
                    yE2,xE2,yEnemigo2, xEnemigo2 = mov(yE2, xE2, yEnemigo2, xEnemigo2,yE,xE,matriz)
                    if xCuadradito <9*SIZE_BLOCK and matriz [yP][xP+1]== 0:
                        puntaje+=10
                if tecla_esc[pygame.K_ESCAPE]:
                    cerrar_juego()
                if tecla_esc[pygame.K_r]:
                    main()
            #cuando el personaje choca con un enemigo, este vuelve a la posision[0][0], se resta una vida y suena un sonido        
            if colisiones (xCuadradito,yCuadradito,xEnemigo,yEnemigo):
                xCuadradito,yCuadradito,xP,yP=monito_choca()
                vidas-=1
                sonido_colision()
            if colisiones (xCuadradito,yCuadradito,xEnemigo2,yEnemigo2):
                xCuadradito,yCuadradito,xP,yP=monito_choca()
                vidas-=1
                sonido_colision()
                
        pantalla_victoria,jugando1,cont= victoria(matriz)     
        pantalla_derrota,jugando2= derrota(vidas)                
        condicion=0
        
    while pantalla_victoria:
        reloj.tick(60)
        pygame.mixer.music.stop()
        #es la condicion para que funcione el puntaje
        if condicion== 0:
            sonido_victoria()
            condicion=1
        texto_victoria= pygame.font.SysFont("console", 30, True)
        texto_victoria2= pygame.font.SysFont("console", 37, True)
        ventana.blit(pygame.transform.scale(victoria_imagen,(1300,720)), (0,0))
        texto= texto_victoria.render("Has consegido: "+str(round(puntaje*vidas+(1000*(130/contador_puntaje))))+str(" Dolares$$"), 1,BLANCO)
        texto2= texto_victoria2.render("¡¡¡Felicidades, puedes comprar la pc de tus sueños!!!", 1,BLANCO)
        ventana.blit(texto,((ANCHO//2+100),400))
        ventana.blit(texto2,((ANCHO//2-250)-(texto.get_width()//2),500))
        texto_repetir= texto_intro.render("Presione [R] para REPETIR", 1,BLANCO)
        ventana.blit(texto_repetir,((350),650))
        salir=texto_salir.render("[ESC]=SALIR",1,BLANCO)
        ventana.blit(salir,[10,10])
        puntuacion= puntaje*vidas
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                cerrar_juego()
        tecla_repetir= pygame.key.get_pressed()
        if tecla_repetir[pygame.K_r] :
                main()
                pantalla_victoria= False
        if tecla_repetir[pygame.K_ESCAPE]:
            cerrar_juego() 
        pygame.display.update()          
                
    while pantalla_derrota:
        reloj.tick(60)
        pygame.mixer.music.stop()
        #condicion para el puntaje, el puntaje siempre sera 0 si pierdes
        if condicion==0:
            sonido_derrota()
            condicion=1
            
        texto_derrota= pygame.font.SysFont("console", 35, True)
        ventana.blit(pygame.transform.scale(derrota_imagen,(1300,720)), (0,0))
        texto= texto_derrota.render("Has consegido: "+str(puntaje*vidas)+str(" Dolares$$"), 1,BLANCO)
        texto2= texto_derrota.render("Has perdido, conformate con el pc de tu hermanita", 1,BLANCO)
        ventana.blit(texto,((750),150))
        ventana.blit(texto2,((ANCHO//2+100)-(texto2.get_width()//2),520))
        texto_repetir= texto_intro.render("Presione [R] para REPETIR", 1,BLANCO)
        ventana.blit(texto_repetir,((350),650))
        salir=texto_salir.render("[ESC]=SALIR",1,BLANCO)
        ventana.blit(salir,[10,10])
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                cerrar_juego()
        tecla_repetir= pygame.key.get_pressed()
        if tecla_repetir[pygame.K_r] :
                main()
                pantalla_derrota= False
                pygame.mixer.Sound.stop()
        if tecla_repetir[pygame.K_ESCAPE]:
            cerrar_juego()
        pygame.display.update()
                                
    pygame.quit
                

main()

