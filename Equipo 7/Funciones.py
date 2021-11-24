import pygame,sys,random,os
from Funciones_enemigos import *
from Victoria import *
from Derrota import *
from Pantalla_de_carga import *

#colores
blanco=[255,255,255]
negro=[0,0,0]
rojo=[255,0,0]
verde=[0,255,0]
azul=[0,0,255]
verdeazul=[0, 200, 70]

###Funciones###

#crear boton
def crear_boton(pantalla,boton,texto,tamaño):
    fuente1=pygame.font.SysFont("Times New Roman",tamaño)
    if boton.collidepoint(pygame.mouse.get_pos()):
        pygame.draw.rect(pantalla,[225, 38, 180],boton,0)
    else:
        pygame.draw.rect(pantalla,[174, 15, 135],boton,0)
    ren=fuente1.render(texto,True,(255,255,255))
    pantalla.blit(ren,(boton.x+(boton.width-ren.get_width())/2,boton.y+(boton.height-ren.get_height())/2))

#imprime texto en pantalla
def escribir_texto_time(pantalla,localizacion,texto,tamaño):
    fuente1=pygame.font.SysFont("Times New Roman",tamaño)
    ren2=fuente1.render(texto,True,(0,0,0))
    pantalla.blit(ren2,((localizacion[0]-(ren2.get_width()/2)),(localizacion[1]-(ren2.get_height()/2))))

#juego
def ejecucion_juego(ventana):

    Pantalla_carga(ventana)
    
    game_over=0
    puntaje=7
    pygame.init()
    lista1=[]
    movx=0
    movy=0
    corazones=3
    piñera_presidente=True
    f_muro=0
    fotograma=0
    generacion_final=[]
    igual=True
    igual2=True
    xd=0
    dx=0
    v=0

# ? ------- LISTA DEL TABLERO ------- ? #
    for i in range(10):
        lista1.append([])   
        for j in range(10):
            x = 135 + (70*i)
            y = 120 + (60*j)
            lista1[i].append([x,y,0])

# * ------- OBSTACULOS ------- * #
    obstaculo_pos=[(random.randint(2,8)),(random.randint(2,8))]

    obstaculo2_pos=[(random.randint(2,9)),(random.randint(2,9))]
    obstaculo2_1_pos=[obstaculo2_pos[0],obstaculo2_pos[1]-1]

    obstaculo3_pos=[(random.randint(2,9)),(random.randint(2,9))]
    obstaculo3_1_pos=[obstaculo3_pos[0],obstaculo3_pos[1]-1]
    obstaculo3_2_pos=[obstaculo3_pos[0]-1,obstaculo3_pos[1]]

    obstaculo3=[obstaculo3_pos,obstaculo3_1_pos,obstaculo3_2_pos]

    obstaculoslista=[obstaculo_pos,obstaculo2_pos,obstaculo2_1_pos,obstaculo3_pos,obstaculo3_1_pos,obstaculo3_2_pos]

# ? IMPRIME OBBSTACULOS Y COMPRUEBA ? #
    while piñera_presidente:
        if igual==False and igual2==False:
            piñera_presidente=False
        if obstaculo2_pos==obstaculo_pos or obstaculo2_1_pos==obstaculo_pos:
            obstaculo2_pos=[(random.randint(2,8)),(random.randint(2,8))]
        else:
            igual=False
        while igual2:
            for obstaculo in obstaculo3:
                while obstaculo==obstaculo_pos:
                    obstaculo3_pos=[(random.randint(2,8)),(random.randint(2,8))]
                while obstaculo==obstaculo2_pos:
                    obstaculo3_pos=[(random.randint(2,8)),(random.randint(2,8))]
                while obstaculo==obstaculo2_1_pos:
                    obstaculo3_pos=[(random.randint(2,8)),(random.randint(2,8))]
            igual2=False
        generacion_final=[obstaculo_pos,obstaculo2_pos,obstaculo2_1_pos,obstaculo3[0],obstaculo3[1],obstaculo3[2]]
    
    #generacion lista
    for a in generacion_final:
        lista1[a[0]][a[1]][2]=1

    #generacion enemigos
    localizacion_enemigo=generacion_enemigos(lista1)
    moex=localizacion_enemigo[0]
    moey=localizacion_enemigo[1]
    localizacion_enemigo2=generacion_enemigos(lista1)
    moex2=localizacion_enemigo2[0]
    moey2=localizacion_enemigo2[1]
        
# * ------- IMAGEN DE FONDO------- * #
    background=[pygame.image.load(os.path.dirname(os.path.abspath(__file__))+"\\Background\MP_0.png").convert_alpha(),
                pygame.image.load(os.path.dirname(os.path.abspath(__file__))+"\\Background\MP_1.png").convert_alpha(),
                pygame.image.load(os.path.dirname(os.path.abspath(__file__))+"\\Background\MP_2.png").convert_alpha(),
                pygame.image.load(os.path.dirname(os.path.abspath(__file__))+"\\Background\MP_3.png").convert_alpha(),
                pygame.image.load(os.path.dirname(os.path.abspath(__file__))+"\\Background\MP_4.png").convert_alpha(),
                pygame.image.load(os.path.dirname(os.path.abspath(__file__))+"\\Background\MP_5.png").convert_alpha(),
                pygame.image.load(os.path.dirname(os.path.abspath(__file__))+"\\Background\MP_6.png").convert_alpha(),
                pygame.image.load(os.path.dirname(os.path.abspath(__file__))+"\\Background\MP_7.png").convert_alpha(),
                pygame.image.load(os.path.dirname(os.path.abspath(__file__))+"\\Background\MP_8.png").convert_alpha(),
                pygame.image.load(os.path.dirname(os.path.abspath(__file__))+"\\Background\MP_9.png").convert_alpha(),
                pygame.image.load(os.path.dirname(os.path.abspath(__file__))+"\\Background\MP_10.png").convert_alpha(),
                pygame.image.load(os.path.dirname(os.path.abspath(__file__))+"\\Background\MP_11.png").convert_alpha(),
                pygame.image.load(os.path.dirname(os.path.abspath(__file__))+"\\Background\MP_12.png").convert_alpha(),
                pygame.image.load(os.path.dirname(os.path.abspath(__file__))+"\\Background\MP_13.png").convert_alpha(),
                pygame.image.load(os.path.dirname(os.path.abspath(__file__))+"\\Background\MP_14.png").convert_alpha()]
    background[0] = pygame.transform.scale(background[0],(960,800))
    background[1] = pygame.transform.scale(background[1],(960,800))
    background[2] = pygame.transform.scale(background[2],(960,800))
    background[3] = pygame.transform.scale(background[3],(960,800))
    background[4] = pygame.transform.scale(background[4],(960,800))
    background[5] = pygame.transform.scale(background[5],(960,800))
    background[6] = pygame.transform.scale(background[6],(960,800))
    background[7] = pygame.transform.scale(background[7],(960,800))
    background[8] = pygame.transform.scale(background[8],(960,800))
    background[9] = pygame.transform.scale(background[9],(960,800))
    background[10] = pygame.transform.scale(background[10],(960,800))
    background[11] = pygame.transform.scale(background[11],(960,800))
    background[12] = pygame.transform.scale(background[12],(960,800))
    background[13] = pygame.transform.scale(background[13],(960,800))
    background[14] = pygame.transform.scale(background[14],(960,800))

# ? ------- ROCA ------- ? #
    roca = pygame.image.load(os.path.dirname(os.path.abspath(__file__))+"\\Sprites/roca.png").convert_alpha()
    roca = pygame.transform.scale(roca,(70,60))

# ?  ------- ROCA CON TELEARAÑA ------- ? #
    roca2 = pygame.image.load(os.path.dirname(os.path.abspath(__file__))+"\\Sprites/RT1.png").convert_alpha()
    roca2 = pygame.transform.scale(roca2,(70,60))

# ? ------- ROCA OBSTACULO ------- ? #
    rocaObs = pygame.image.load(os.path.dirname(os.path.abspath(__file__))+"\\Sprites/Roca punta Sangre.png").convert_alpha()
    rocaObs = pygame.transform.scale(rocaObs,(70,60))

# * ------- ARAÑA ------- * #
    araña = [pygame.image.load(os.path.dirname(os.path.abspath(__file__))+"\\Sprites/ArañitaFinal_L.png").convert_alpha()
            ,pygame.image.load(os.path.dirname(os.path.abspath(__file__))+"\\Sprites/ArañitaFinal_R.png").convert_alpha()]
    araña[0] = pygame.transform.scale(araña[0],(45,45))
    araña[1] = pygame.transform.scale(araña[1],(45,45))

    pokemon = [pygame.image.load(os.path.dirname(os.path.abspath(__file__))+"\\Sprites/SQ_L.png").convert_alpha()
            ,pygame.image.load(os.path.dirname(os.path.abspath(__file__))+"\\Sprites/SQ_R.png").convert_alpha()]
    pokemon[0] = pygame.transform.scale(pokemon[0],(50,50))
    pokemon[1] = pygame.transform.scale(pokemon[1],(50,50))

    sapo = [pygame.image.load(os.path.dirname(os.path.abspath(__file__))+"\\Sprites/Frog_L.png").convert_alpha()
            ,pygame.image.load(os.path.dirname(os.path.abspath(__file__))+"\\Sprites/Frog_R.png").convert_alpha()]
    sapo[0] = pygame.transform.scale(sapo[0],(50,50))
    sapo[1] = pygame.transform.scale(sapo[1],(50,50))

    vida_T = pygame.image.load(os.path.dirname(os.path.abspath(__file__))+"\\Sprites/Corazon_Vida.png").convert_alpha()
    vida_F = pygame.image.load(os.path.dirname(os.path.abspath(__file__))+"\\Sprites/Corazon_Vacio.png").convert_alpha()

    # * ------- AQUI ES DONDE SE CARGA LA MUSICA DE FONDO ------- * #
    pygame.mixer.music.load(os.path.dirname(os.path.abspath(__file__))+"\\Musica/mus_spider.wav")
    pygame.mixer.music.play(-1,0.0)
    pygame.mixer.music.set_volume(0.04)

    Muerte = pygame.mixer.Sound(os.path.dirname(os.path.abspath(__file__))+"\\Sonidos/GolpeEnemigo.wav")
    Muerte.set_volume(0.1)

# * --------- FUNCION COLISIÓN --------- ! 
    lista1[0][0][2]=2
    clock = pygame.time.Clock()

    run=True
    while run:
    # * --------- IMAGEN DE FONDO --------- * #
        ventana.fill((132,130,128))
        ventana.blit(background[fotograma],[0,0])  
        f_muro+=1
        if(f_muro==10):
            fotograma+=1
            f_muro=0
        if(fotograma==14):
            fotograma=0

        clock.tick(60)      
        
    # * --------- TABLERO JUEGO --------- * #
        for c in lista1:
            for u in c:
                if u[2]==0:
                    ventana.blit(roca,[u[0],u[1]])
                else:
                    if u[2]==2:
                        ventana.blit(roca2,[u[0],u[1]])
                    if u[2]==1:
                        ventana.blit(rocaObs,[u[0],u[1]])

        if detectar_jugadorenemigo(moex,moey,movx,movy,lista1) or detectar_jugadorenemigo(moex2,moey2,movx,movy,lista1):
            movx=0
            movy=0
            corazones-=1
            Muerte.play()

        #corazones
        if corazones==0:
            ventana.blit(vida_F,(705,10))
            ventana.blit(vida_F,(760,10))
            ventana.blit(vida_F,(815,10))
        else:
            if corazones==1:
                ventana.blit(vida_F,(705,10))
                ventana.blit(vida_F,(760,10))
                ventana.blit(vida_T,(815,10))
            else:
                if corazones==2:
                    ventana.blit(vida_F,(705,10))
                    ventana.blit(vida_T,(760,10))
                    ventana.blit(vida_T,(815,10))
                else:
                    ventana.blit(vida_T,(705,10))
                    ventana.blit(vida_T,(760,10))
                    ventana.blit(vida_T,(815,10))
                    
    # ? --------- TECLAS --------- ? #
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.mixer.music.stop()
                sys.exit()
    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:# ! --------- SALIR DEL JUEGO --------- ! #
                    pygame.mixer.music.stop()
                    run = False
            #* --------- MOVIMIENTO JUGADOR --------- *#
                tecla_presionada = pygame.key.name(event.key)

                if tecla_presionada=="w" or tecla_presionada=="a" or tecla_presionada=="s" or tecla_presionada=="d":
                    movimiento=movimiento_enemigo(moex,moey,moex2,moey2,lista1,xd)
                    moex=movimiento[0]
                    moey=movimiento[1]
                    xd=movimiento[2]
                    movimiento2=movimiento_enemigo(moex2,moey2,moex,moey,lista1,xd)
                    moex2=movimiento2[0]
                    moey2=movimiento2[1]
                    dx=movimiento[2]
                    
                if tecla_presionada == "w":# ? ----------- ARRIBA ----------- ? #
                    if detectar_colision("w",movx,movy,lista1)=="w":
                        if lista1[movx][movy-1][2]==0:
                            lista1[movx][movy-1][2]=2
                            puntaje+=7
                        else:
                            lista1[movx][movy-1][2]=0
                            puntaje-=7
                        movy-=1
                    else:
                        movy+=0
                if tecla_presionada == "a": # ? ----------- IZQUIERDA ----------- ? #
                    if detectar_colision("a",movx,movy,lista1)=="a":
                        if lista1[movx-1][movy][2]==0:
                            lista1[movx-1][movy][2]=2
                            puntaje+=7
                            v=0
                        else:
                            lista1[movx-1][movy][2]=0
                            puntaje-=7
                            v=0
                        movx-=1
                    else:
                        movx+=0
                        v=0
                if tecla_presionada == "s": # ? ----------- ABAJO ----------- ? #
                    if detectar_colision("s",movx,movy,lista1)=="s":
                        if lista1[movx][movy+1][2]==0:
                            lista1[movx][movy+1][2]=2
                            puntaje+=7
                        else:
                            lista1[movx][movy+1][2]=0
                            puntaje-=7
                        movy+=1
                    else:
                        movy+=0
                if tecla_presionada == "d": # ? ----------- DERECHA ----------- ? #
                    if detectar_colision("d",movx,movy,lista1)=="d":
                        if lista1[movx+1][movy][2]==0:
                            lista1[movx+1][movy][2]=2
                            puntaje+=7
                            v=1
                        else:
                            lista1[movx+1][movy][2]=0
                            puntaje-=7
                            v=1
                        movx+=1
                    else:
                        movx+=0
                        v=1
        
        if puntaje==658:
            pygame.mixer.music.stop()
            victoria(ventana,puntaje)
            run=False

        if corazones==0:
            pygame.mixer.music.stop()
            Derrota(ventana,puntaje)
            run=False

        escribir_texto_time(ventana,[770,77],"Puntaje: ",40)
        escribir_texto_time(ventana,[850,77],str(puntaje),40)
        ventana.blit(pokemon[xd],(lista1[moex][moey][0]+15,lista1[moex][moey][1]-39))
        ventana.blit(sapo[dx],(lista1[moex2][moey2][0]+15,lista1[moex2][moey2][1]-39))
        ventana.blit(araña[v],(lista1[movx][movy][0]+18,lista1[movx][movy][1]-33)) # * --------- IMPRIME POSICION ARAÑA --------- * #
        pygame.display.flip()
