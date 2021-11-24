
import pygame,sys,random

pygame.init()

ancho_ventana = 1280
alto_ventana = 720
tablero = []
xjugador = 0    #posicion en la matriz
yjugador = 0
x_enemigo = 0
y_enemigo = 0
x_enemigo2= 0
y_enemigo2= 0
vidas = 3
puntos=3000
pasos = 0
ranking=[0,0,0]
punt_max=ranking[0]

fuente = pygame.font.Font("fuente/8-bit Arcade In.ttf",100)
fuente1 = pygame.font.Font("fuente/8-bit Arcade In.ttf",80)
fuente2 = pygame.font.Font("fuente/8-bit Arcade In.ttf",60)
Vida = fuente.render("Vidas",True,(164,215,0))

reloj = pygame.time.Clock()
ventana = pygame.display.set_mode((ancho_ventana,alto_ventana))

def ordenar_puntos(a,b):
    for i in range(2,-1, -1):
        if a>b[i] and i==2:
            b[i]=a
        if a>b[i] and i==1:
            temp=b[i]
            b[i]=a
            b[i+1]=temp
        if a>b[i] and i==0:
            temp=b[i]
            b[i]=a
            b[i+1]=temp

def escribir_puntos(a, b ,c, d, e):
    text_a= fuente1.render("Puntaje ", True, (164,215,0))
    text_b= fuente1.render(str(b), True, (164,215,0))
    text_rect=text_a.get_rect()
    text_rect.midtop=(d, e)
    text_rectb = text_b.get_rect()
    text_rectb.midtop=(d+50, e+50)
    a.blit(text_a, text_rect)
    a.blit(text_b,text_rectb)

def enemigo_xy(a,b,c,d,e,f):
    x=random.uniform(0,1)
    y=random.randint(1,2)
    z=[0,0]
    enemigo2=[f,e]

    if x<= 0.5:
        if y==1 and a < 890 and tablero[d][c+1] != 1 and z != [d,c+1] and enemigo2 != [d,c+1] :
            a += 60
            c += 1
        elif y==2 and a > 360 and tablero[d][c-1] != 1 and z != [d,c-1] and enemigo2 != [d,c-1]:
            a -= 60
            c -= 1
        else:
            if y==1 and a > 360 and tablero[d][c-1] != 1 and z != [d,c-1] and enemigo2 != [d,c-1]:
                a -= 60
                c -= 1
            if y==2 and a < 890 and tablero[d][c+1] != 1 and z != [d,c+1] and enemigo2 != [d,c+1]:
                a += 60
                c += 1
    else:
        if y==1 and b < 625 and tablero[d+1][c] != 1 and z != [d+1,c] and enemigo2 != [d+1,c]:
            b += 65
            d +=1
        elif y==2 and b > 40 and tablero[d-1][c] != 1 and z != [d-1,c] and enemigo2 != [d-1,c]:
            b -= 65
            d -=1
        else:
            if y==1 and b > 40 and tablero[d-1][c] != 1 and z != [d-1,c] and enemigo2 != [d-1,c]:
                b -= 65
                d -=1

            if y==2 and b < 625 and tablero[d+1][c] != 1 and z != [d+1,c] and enemigo2 != [d+1,c]:
                b += 65
                d +=1
            
    return a,b,c,d
    
def verificar(a,b,c,d):     #Verifica si el personaje pisa un bloque pintado volviendolo normal, o este pisa un bloque normal pintandolo
    if tablero[a+b][c+d] == 3:
            tablero[a+b][c+d] = 0
    else:
        tablero[a+b][c+d] = 3

def tabla(x_enemigo, y_enemigo, x_enemigo2, y_enemigo2):

    if tablero != []:
        for i in range(10): #Generar el tablero en la ventana creada
            for z in range(10):
                if tablero[i][z] == 0:
                    tablero[i][z] = 0
                if tablero[i][z] == 1:
                    tablero[i][z] = 0
                if tablero[i][z] == 3:
                    tablero[i][z] = 0

    else:
        for i in range(10): #Genera la matriz (Lista de lista) con 0
            tablero.append([])
            for j in range(10):
                tablero[i].append(0)

    tablero[xjugador][yjugador]=3 #Ubica al jugador en el (0,0)

    x1= 0
    y1= 0

    x1 = random.randint(1,8)    #Genera numeros (x,y) aleatorio para el obstaculo de 3
    y1= random.randint(2,8)

    tablero[y1][x1] = 1   #Generacion de obstaculo de 3 bloques
    tablero[y1][x1-1] = 1
    tablero[y1+1][x1-1] = 1

    x2 = 0
    y2 = 0

    x2 = random.randint(0,8)    #Genera numeros(x,y) aleatorios para el obstaculo de 2
    y2 = random.randint(2,9)

    while tablero[y2][x2] == 1 and tablero[y2][x2+1] == 1  : #Verifica si en las coordenadas que genero no sean 1 en la matriz 
        x2 = random.randint(0,8)
        y2 = random.randint(2,9)

    tablero [y2][x2] = 1     #Generacion del obstaculo de 2 bloques
    tablero [y2][x2+1] = 1

    x3 = random.randint(1,9)    #Genera numeros (x,y) aleatorio para el obstaculo de 1
    y3 = random.randint(2,9)

    while tablero[y3][x3] == 1:     #Verifica si en las coordenadas que genero no sean 1 en la matriz 
        x3 = random.randint(1,9)
        y3 = random.randint(1,9)

    tablero [y3][x3] = 1    #Obstaculo solito

    x_enemigo=random.randint(1,9)
    y_enemigo=random.randint(1,9)

    while tablero [y_enemigo][x_enemigo] == 1:
        x_enemigo=random.randint(1,9)
        y_enemigo=random.randint(1,9)
    
    tablero[y_enemigo][x_enemigo]=0

    x_enemigo2=random.randint(1,9)
    y_enemigo2=random.randint(1,9)

    while tablero [y_enemigo2][x_enemigo2] == 1 or (x_enemigo2 == x_enemigo and y_enemigo2 == y_enemigo):
        x_enemigo2=random.randint(1,9)
        y_enemigo2=random.randint(1,9)
    
    tablero[y_enemigo2][x_enemigo2]=0
    
    return (x_enemigo, y_enemigo, x_enemigo2, y_enemigo2) #Returna

def tablero_principal(reloj,ventana,x_enemigo,y_enemigo,x_enemigo2,y_enemigo2,vidas,puntos, pasos):
    movimientox = 0
    movimientoy = 0

    movx_enemigo = x_enemigo*60 + 359
    movy_enemigo = y_enemigo*65 + 40
    movx_enemigo2 = x_enemigo2*60 + 359
    movy_enemigo2 = y_enemigo2*65 + 40

    pygame.display.set_caption("Q*Bear In The Space")   #Nombre de la ventana
        
    fondo = pygame.image.load("images/fondo.png") #Cargar el fondo para que se vea
    ventana.blit(pygame.transform.scale(fondo,(1280,720)),(0,0))

    plataforma = pygame.image.load("images/plataforma.png") #Plataforma
    plataforma = pygame.transform.scale(plataforma,(58,58))

    ovni = pygame.image.load("images/ovni.png") #Ovni
    ovni = pygame.transform.scale(ovni,(58,58))

    panda = pygame.image.load("images/panda.png") #Panda (Personaje del juego)
    panda = pygame.transform.scale (panda,(58,58))

    enemigo = pygame.image.load("images/enemigo.png")
    enemigo =pygame.transform.scale (enemigo,(58,58))

    enemigo2 = pygame.image.load("images/enemigo2.png")
    enemigo2 =pygame.transform.scale (enemigo2,(58,58))

    plataforma_verde = pygame.image.load("images/plataformaverde.png") #Plataforma verde ("La plataforma pintada")
    plataforma_verde = pygame.transform.scale (plataforma_verde,(58,58))

    corazon = pygame.image.load("images/Corazon.png")
    corazon = pygame.transform.scale(corazon,(80,80))


    xPanda = 350 #Cordenadas del panda (Personaje del juego)
    yPanda = 40 

    corriendo = True
    contador= 0
    pintado = 0
    pasos
    puntos
    
    while corriendo:
        
        reloj.tick(30)#fps
        corriendo = True
        contador +=1
        pintado = 0
        victoria = False

        Pandaxy = [xPanda,yPanda]
        enemigoxy=[movx_enemigo-9,movy_enemigo]
        enemigo2xy=[movx_enemigo2-9,movy_enemigo2]

        ventana.blit(pygame.transform.scale(fondo,(1280,720)),(0,0))  #Muestra el fondo en la ventana 

        for i in range(10): #Generar el tablero en la ventana creada
            for z in range(10):
                if tablero[i][z] == 0:
                    ventana.blit(plataforma,(350+60*z,40+65*i))
                if tablero[i][z] == 1:
                    ventana.blit(ovni,(350+60*z,40+65*i))
                if tablero[i][z] == 3:
                    ventana.blit(plataforma_verde,(350+60*z,40+65*i))

        ventana.blit(panda,(xPanda,yPanda))#Muestra al panda (El personaje) en la ventana
        ventana.blit(pygame.transform.scale(enemigo,(58,58)),(movx_enemigo,movy_enemigo))
        ventana.blit(pygame.transform.scale(enemigo2,(58,58)),(movx_enemigo2,movy_enemigo2))
        ventana.blit(Vida,(1015,20))

        for i in range(10): #Generar el tablero en la ventana creada
            for z in range(10):
                if tablero[i][z] == 0:
                    pintado += 1

        if pintado ==  0:
            victoria = True
            corriendo = False

        if vidas == 3:
            ventana.blit(corazon,(1000,100))
            ventana.blit(corazon,(1080,100))
            ventana.blit(corazon,(1160,100))
            
        if vidas == 2:
            ventana.blit(corazon,(1000,100))
            ventana.blit(corazon,(1080,100))
            
        if vidas == 1:
            ventana.blit(corazon,(1000,100))

        if Pandaxy[0] == enemigoxy[0] and Pandaxy[1] == enemigoxy[1]:
            vidas -= 1
            corriendo = False

        if Pandaxy[0] == enemigo2xy[0] and Pandaxy[1] == enemigo2xy[1]:
            vidas -= 1
            corriendo = False

        escribir_puntos(ventana, str(puntos), 100 , 180 , 80)  
        
        for event in pygame.event.get(): #Pygame detecta un evento

            if event.type == pygame.KEYDOWN:
                tecla_presionada = pygame.key.name(event.key)   #Pygame detecta si hay una tecla presionada

                if tecla_presionada == "f11":   #Fullscreen(Pantalla completa)
                    pygame.display.toggle_fullscreen()

                if  tecla_presionada == "w" and yPanda > 50 and tablero[yjugador+movimientoy-1][xjugador+movimientox] != 1:     #Mueve al personaje hacia arriba
                    yPanda -= 65
                    movimientoy = movimientoy - 1
                    verificar(yjugador, movimientoy, xjugador, movimientox)
                    movx_enemigo,movy_enemigo,x_enemigo,y_enemigo = enemigo_xy(movx_enemigo,movy_enemigo,x_enemigo,y_enemigo,x_enemigo2,y_enemigo2)
                    movx_enemigo2,movy_enemigo2,x_enemigo2,y_enemigo2 = enemigo_xy(movx_enemigo2,movy_enemigo2,x_enemigo2,y_enemigo2,x_enemigo,y_enemigo)
                    pasos = pasos + 1
                    if puntos > 0:
                        puntos = puntos - 10

                if  tecla_presionada == "a" and xPanda > 360 and tablero[yjugador+movimientoy][xjugador+movimientox-1] != 1:    #Mueve el personaje hacia la izquierda
                    xPanda -= 60
                    movimientox = movimientox - 1
                    verificar(yjugador, movimientoy, xjugador, movimientox)
                    movx_enemigo,movy_enemigo,x_enemigo,y_enemigo = enemigo_xy(movx_enemigo,movy_enemigo,x_enemigo,y_enemigo,x_enemigo2,y_enemigo2)
                    movx_enemigo2,movy_enemigo2,x_enemigo2,y_enemigo2 = enemigo_xy(movx_enemigo2,movy_enemigo2,x_enemigo2,y_enemigo2,x_enemigo,y_enemigo)
                    pasos = pasos + 1
                    if puntos > 0:
                        puntos = puntos - 10

                if  tecla_presionada == "s" and yPanda < 625 and tablero[yjugador+movimientoy+1][xjugador+movimientox] != 1:    #Mueve el personaje hacia abajo
                    yPanda += 65
                    movimientoy = movimientoy + 1
                    verificar(yjugador, movimientoy, xjugador, movimientox)
                    movx_enemigo,movy_enemigo,x_enemigo,y_enemigo = enemigo_xy(movx_enemigo,movy_enemigo,x_enemigo,y_enemigo,x_enemigo2,y_enemigo2)
                    movx_enemigo2,movy_enemigo2,x_enemigo2,y_enemigo2 = enemigo_xy(movx_enemigo2,movy_enemigo2,x_enemigo2,y_enemigo2,x_enemigo,y_enemigo)
                    pasos = pasos + 1
                    if puntos > 0:
                        puntos = puntos - 10

                if  tecla_presionada == "d" and xPanda < 890 and tablero[yjugador+movimientoy][xjugador+movimientox+1] != 1:    #Mueve el personaje hacia la derecha
                    xPanda += 60
                    movimientox = movimientox + 1
                    verificar(yjugador, movimientoy, xjugador, movimientox)
                    movx_enemigo,movy_enemigo,x_enemigo,y_enemigo = enemigo_xy(movx_enemigo,movy_enemigo,x_enemigo,y_enemigo,x_enemigo2,y_enemigo2)
                    movx_enemigo2,movy_enemigo2,x_enemigo2,y_enemigo2 = enemigo_xy(movx_enemigo2,movy_enemigo2,x_enemigo2,y_enemigo2,x_enemigo,y_enemigo)
                    pasos = pasos + 1
                    if puntos > 0:
                        puntos = puntos - 10
                if tecla_presionada == "p":
                    pausa_fun()
        
            if (event.type == pygame.QUIT):
                corriendo = False
                pygame.quit()
                sys.exit()

        pygame.display.flip()
    return vidas,victoria,puntos,pasos

def menu_1(reloj,ventana,highscore):
    menu = True
    pygame.display.set_caption("Q*Bear In The Space")
    menu_imagen = pygame.image.load("images/menu.png")

    pygame.mixer.music.load ("sounds/menu.mp3")
    pygame.mixer.music.set_volume(0.1)
    pygame.mixer.music.play (1000,0,5)

    start = pygame.mixer.Sound ("sounds/start.mp3")
    start.set_volume(0.2)
    
    if highscore < ranking[0]:
        highscore = ranking[0]
        with open("mejorespuntajes.txt","w") as f:
            f.write(str(highscore))

    while menu:
        reloj.tick(30)

        ventana.blit(menu_imagen,(0,0))

        for event in pygame.event.get():
            
            if event.type == pygame.KEYDOWN:
                tecla_presionada = pygame.key.name(event.key)   
                
                if tecla_presionada == "return":
                    start.play ()
                    pygame.mixer.music.fadeout (2000)
                    menu = False
                
                if tecla_presionada == "i":
                    instrucciones(reloj,ventana)

                if tecla_presionada == "r":
                    ranking_fun(ranking)
            
            if(event.type==pygame.QUIT):
                menu = False
                pygame.quit()
                sys.exit()

        pygame.display.flip()

def victoria_f(reloj,ventana,puntos,pasos):
    if pasos <= 150:
        puntos = puntos + 1000
    if pasos <= 250 and pasos > 140:
        puntos = puntos + 500
    ordenar_puntos(puntos, ranking)
    print(ranking)
    text_a= fuente2.render("Tu puntaje fue de ", True, (164,215,0))
    text_b = fuente2.render(str(puntos),True,(164,215,0))
    text_rect=text_a.get_rect()
    text_rectb=text_b.get_rect()

    text_rect.midtop=(750, 450)
    text_rectb.midtop=(760, 500)

    victoria = True
    pygame.display.set_caption("Q*Bear In The Space")
    victory =pygame.image.load("images/victoria.png")

    while victoria:
        reloj.tick(30)

        ventana.blit(victory,(0,0))
        ventana.blit(text_a, text_rect)
        ventana.blit(text_b, text_rectb)

        for event in pygame.event.get():
            
            if event.type == pygame.KEYDOWN:
                tecla_presionada = pygame.key.name(event.key)   
        
                if tecla_presionada == "return":
                    victoria = False

            if (event.type==pygame.QUIT):
                victoria = False
                pygame.quit()
                sys.exit()

        pygame.display.flip()
    
def game_over(reloj,ventana,puntos):
    ordenar_puntos(puntos, ranking)
    text_a= fuente2.render("Tu puntaje fue de ", True, (164,215,0))
    text_b = fuente2.render(str(puntos),True,(164,215,0))
    text_rect=text_a.get_rect()
    text_rectb=text_b.get_rect()

    text_rect.midtop=(670, 300)
    text_rectb.midtop=(680, 400)

    pygame.display.set_caption("Q*Bear In The Space")
    gameover = pygame.image.load("images/game_over.png")

    game_over = True
    while game_over:
        
        reloj.tick(30)
        ventana.blit(gameover,(0,0))
        ventana.blit(text_a, text_rect)
        ventana.blit(text_b, text_rectb)
        
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                tecla_presionada = pygame.key.name(event.key)   
                
                if tecla_presionada == "return":
                    game_over = False
            
            if (event.type==pygame.QUIT):
                    game_over = False
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()

def instrucciones(reloj,ventana):
    pygame.display.set_caption("Q*Bear In The Space")
    intrucciones_image = pygame.image.load("images/intrucciones.png")

    instrucciones = True
    while instrucciones:

        reloj.tick(30)
        ventana.blit(intrucciones_image,(0,0))
        
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                tecla_presionada = pygame.key.name(event.key)   
            
                if tecla_presionada == "return":
                    instrucciones = False
            
            if (event.type==pygame.QUIT):
                    instrucciones = False
                    pygame.quit()
                    sys.exit()  

        pygame.display.flip()

def principal(x_enemigo,y_enemigo,x_enemigo2,y_enemigo2):
    vidas = 3
    victoria = False
    puntos=3000
    pasos=0

    x_enemigo,y_enemigo,x_enemigo2,y_enemigo2 = tabla(x_enemigo,y_enemigo,x_enemigo2,y_enemigo2)

    pygame.mixer.music.load ("sounds/music.mp3")
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play (5,0,5)

    of = pygame.mixer.Sound("sounds/of.mp3")

    while vidas != 0 and victoria == False:
        vidas,victoria,puntos,pasos = tablero_principal(reloj,ventana,x_enemigo,y_enemigo,x_enemigo2,y_enemigo2,vidas,puntos,pasos)
        if vidas != 0:
            of.play()

    if vidas == 0:
        pygame.mixer.music.fadeout (2000)
        game_over(reloj,ventana,puntos)

    if victoria == True:
        victoria_f(reloj,ventana,puntos,pasos)

def pausa_fun():
    pygame.display.set_caption("Q*Bear In The Space")
    pausa_image = pygame.image.load ("images/pausa.png")
    pausa = True
    pygame.mixer.music.set_volume(0.01111111)

    while pausa:
        reloj.tick(30)
        ventana.blit(pausa_image,(0,0))
        
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                tecla_presionada = pygame.key.name(event.key)   

                if tecla_presionada == "return":
                    pygame.mixer.music.set_volume(0.2)
                    pausa = False

            if (event.type==pygame.QUIT):
                    pausa = False
                    pygame.quit()
                    sys.exit()  
        pygame.display.flip()

def mejorespuntajes():
        with open("mejorespuntajes.txt","r") as f:
            return f.read()

def ranking_fun(ranking):
    pygame.display.set_caption("Q*Bear In The Space")
    ranking_image = pygame.image.load ("images/ranking.png")
    ranking_t = True
    highscore = 0

    if highscore != ranking[0]:
        highscore = ranking[0]
        with open("mejorespuntajes.txt","w") as f:
            f.write(str(highscore))

    text_1= fuente1.render("1 Mejor Puntaje  ", True, (164,215,0))
    text_2= fuente1.render("2 ", True, (164,215,0))
    text_3= fuente1.render("3 ", True, (164,215,0))
    text_4= fuente1.render("Puntajes recientes ", True, (164,215,0))

    f = open("mejorespuntajes.txt", "r")
    puntajemayor = f.readline()
    f.close()

    text_b = fuente1.render(str(puntajemayor)+" PTS",True,(164,215,0))
    text_c = fuente1.render(str(ranking[1])+" PTS",True,(164,215,0))
    text_d = fuente1.render(str(ranking[2])+" PTS",True,(164,215,0))

    text_rect1=text_1.get_rect()
    text_rect2=text_1.get_rect()
    text_rect3=text_1.get_rect()
    text_rect4=text_1.get_rect()

    text_rectb=text_b.get_rect()
    text_rectc=text_c.get_rect()
    text_rectd=text_d.get_rect()

    text_rect1.midtop=(500, 200)
    text_rect2.midtop=(600, 450)
    text_rect3.midtop=(700, 550)
    text_rect4.midtop=(500, 350)

    text_rectb.midtop=(1000, 200)
    text_rectc.midtop=(700, 450)
    text_rectd.midtop=(800, 550)

    while ranking_t:
        reloj.tick(30)
        ventana.blit(ranking_image,(0,0))

        ventana.blit(text_1, text_rect1)
        ventana.blit(text_2, text_rect2)
        ventana.blit(text_3, text_rect3)
        ventana.blit(text_4, text_rect4)

        ventana.blit(text_b, text_rectb)
        ventana.blit(text_c, text_rectc)
        ventana.blit(text_d, text_rectd)
        
        for event in pygame.event.get():

            if event.type == pygame.KEYDOWN:
                tecla_presionada = pygame.key.name(event.key)   
                
                if tecla_presionada == "return":
                    ranking_t = False

            if (event.type==pygame.QUIT):
                    ranking_t = False
                    pygame.quit()
                    sys.exit()  

        pygame.display.flip()
    
def main():
    main_juego = True
    f = open("mejorespuntajes.txt", "r")
    highscore = int(f.readline())
    f.close()

    while main_juego:
        
        menu_1(reloj,ventana,highscore)

        principal(x_enemigo,y_enemigo,x_enemigo2,y_enemigo2)

main()
