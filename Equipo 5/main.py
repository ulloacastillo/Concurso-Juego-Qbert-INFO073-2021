import pygame
import random



ANCHO_VENTANA = 800
ALTO_VENTANA = 610
def win(x):
    for i in range (12):
        for j in range(12):
            if x[i][j]==0:
                return False
    return True

    
        
#Fuinciones comparacion de posiciones
def comparaMovimiento(A,ObstA,ObstB,ObstC):
    if (A in ObstA) or (A in ObstB) or (A in ObstC):
        return False
    else:
        return True

def ComparaPosicion(ObsA,ObsB):
    for a in range(len(ObsA)-1):
        if (ObsB[a] in ObsA)==True:
            return True
    return False
    

def ComparaTodos(ObstA,ObstB,ObstC):
    if (ComparaPosicion(ObstA,ObstB))==True:
        return True
    if (ComparaPosicion(ObstB,ObstC))==True:
        return True
    if (ComparaPosicion(ObstA,ObstC))==True:
        return True
    return False

      
#Funcion funcionamiento juego        
def main():
    #tablero 0 y 1
    tablero=[[9,9,9,9,9,9,9,9,9,9,9,9],
             [9,1,0,0,0,0,0,0,0,0,0,9],
             [9,0,0,0,0,0,0,0,0,0,0,9],
             [9,0,0,0,0,0,0,0,0,0,0,9],
             [9,0,0,0,0,0,0,0,0,0,0,9],
             [9,0,0,0,0,0,0,0,0,0,0,9],
             [9,0,0,0,0,0,0,0,0,0,0,9],
             [9,0,0,0,0,0,0,0,0,0,0,9],
             [9,0,0,0,0,0,0,0,0,0,0,9],
             [9,0,0,0,0,0,0,0,0,0,0,9],
             [9,0,0,0,0,0,0,0,0,0,0,9],
             [9,9,9,9,9,9,9,9,9,9,9,9]]

    vidas=3
    puntaje=1000000
    pygame.init()

    ventana= pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    pygame.display.set_caption("Qbert Mafia")
    ventana.fill((195,247,126)) 

    
    #qberto
    xCuadradito = 10
    yCuadradito = 10
    pygame.draw.rect(ventana,(255,255,255), pygame.Rect(xCuadradito,yCuadradito, 50,50))

    x=1
    y=1
    t=True
    Qbrt= tablero[y][x]

    #Imagenes
    img1= pygame.image.load("escenario.jpg")
    img2= pygame.image.load("Parte_derecha.jpg")
    obstucalo= pygame.image.load("Obstucalo_png.png")#esta bien escrito
    suelo=pygame.image.load("Suelo.jpg")
    sueloDinero=pygame.image.load("Suelo_dinero.jpg")
    Qberto=pygame.image.load("Qberto_mafia.png")
    enemigo1=pygame.image.load("enemigo_1.jpg")
    enemigo2=pygame.image.load("enemigo_2.jpg")
    vida= pygame.image.load("vida_corazon.jpg")

    Qberto= pygame.transform.scale(Qberto,(50,50))
    vida= pygame.transform.scale(vida,(35,35))


    #Asignacion pocisiones de obstaculos
    x1=random.randint(2,7)
    x2=random.randint(2,8)
    x3=random.randint(2,9)
    
    y1=random.randint(2,7)   
    y2=random.randint(2,8)
    y3=random.randint(2,9)
    #Confirmacion de no obstruccion spawn
    while (x1,y1)<(2,2):
        (x1,y1)=(2,2)
    while (x2,y2)<(2,2):
        (x2,y2)=(2,2)
    while(x3,y3)<(2,2):
        (x3,y3)=(2,2)
    #Direccion de obstaculo
    P1 = random.randint(0,1)
    if P1 == 0:
        H1= 1
        F1= 0
    if P1 == 1:
        H1= 0
        F1= 1
    
    P2 = random.randint(0,1)
    if P2 == 0:
        H2= 1
        F2= 0
    if P2 == 1:
        H2= 0
        F2= 1
    
    #Confirmacion de no superposicion de obstaculos
    Obst0=[[x1,y1],[x1+(1*H1),y1+(1*F1)],[x1+(2*H1),y1+(2*F1)]]
    Obst1=[[x2,y2],[x2+(1*H2),y2+(1*F2)]]
    Obst2=[[x3,y3],[-1]]
    while t==True:
        if (ComparaTodos(Obst0,Obst1,Obst2)==True):
            x1=random.randint(0,7)
            x2=random.randint(0,8)
            x3=random.randint(0,9)
    
            y1=random.randint(0,7)   
            y2=random.randint(0,8)
            y3=random.randint(0,9)
            
            while (x2,y2) == (x1,y1):
                (y2)=random.randint(0,9)
            while (x3,y3) == (x1,y1) or (x3,y3)==(x2,y2):
                (y3)=random.randint(0,9)
            while (x1,y1)<(1,1):
                x1=random.randint(0,7)
                y1=random.randint(0,7)
            while (x2,y2)<(1,1):
                x2=random.randint(0,8)
                y2=random.randint(0,8)
            while(x3,y3)<(1,1):
                x3=random.randint(0,9)
                y3=random.randint(0,9)
            P1 = random.randint(0,1)
            if P1 == 0:
                H1= 1
                F1= 0
            if P1 == 1:
                H1= 0
                F1= 1

            P2 = random.randint(0,1)
            if P2 == 0:
                H2= 1
                F2= 0
            if P2 == 1:
                H2= 0
                F2= 1
            Obst0=[[x1,y1],[x1+(1*H1),y1+(1*F1)],[x1+(2*H1),y1+(2*F1)]]
            Obst1=[[x2,y2],[x2+(1*H2),y2+(1*F2)]]
            Obst2=[[x3,y3],[-1]]       
            
        else:
            t=False

                
            
        pygame.draw.rect(ventana,(194, 6, 25), pygame.Rect(+ListaAnchoxAlto[0][x1][y1],+ListaAnchoxAlto[1][x1][y1],50,50))
        pygame.draw.rect(ventana,(194, 6, 25), pygame.Rect(+ListaAnchoxAlto[0][x1+(1*H1)][y1+(1*F1)],+ListaAnchoxAlto[1][x1+(1*H1)][y1+(1+F1)],50,50))
        pygame.draw.rect(ventana,(194, 6, 25), pygame.Rect(+ListaAnchoxAlto[0][x1+(2*H1)][y1+(2*F1)],+ListaAnchoxAlto[1][x1+(2*H1)][y1+(2*F1)],50,50))

        pygame.draw.rect(ventana,(194, 6, 25), pygame.Rect(+ListaAnchoxAlto[0][x2][y2],+ListaAnchoxAlto[1][x2][y2],50,50))
        pygame.draw.rect(ventana,(194, 6, 25), pygame.Rect(+ListaAnchoxAlto[0][x2+(1*H2)][y2+(1*F2)],+ListaAnchoxAlto[1][x2+(1*H2)][y2+(1*F2)],50,50))

        pygame.draw.rect(ventana,(194, 6, 25), pygame.Rect(+ListaAnchoxAlto[0][x3][y3],+ListaAnchoxAlto[1][x3][y3],50,50))
   
    pygame.display.flip()

    ObstA=[(ListaAnchoxAlto[0][x1][y1],ListaAnchoxAlto[1][x1][y1]),(ListaAnchoxAlto[0][x1+(1*H1)][y1+(1*F1)],ListaAnchoxAlto[1][x1+(1*H1)][y1+(1*F1)]),(ListaAnchoxAlto[0][x1+(2*H1)][y1+(2*F1)],ListaAnchoxAlto[1][x1+(2*H1)][y1+(1*F1)])]
    ObstB=[(ListaAnchoxAlto[0][x2][y2],ListaAnchoxAlto[1][x2][y2]),(ListaAnchoxAlto[0][x2+(1*H2)][y2+(1*F2)],ListaAnchoxAlto[1][x2+(1*H2)][y2+(1*F2)])]
    ObstC=[(ListaAnchoxAlto[0][x3][y3],ListaAnchoxAlto[1][x3][y3])]


    corriendo = True


    #Enemigo1
    
    xE1= random.randint(2,9)
    yE1= random.randint(2,9)
    xyE1=(xE1,yE1)
    while comparaMovimiento(xyE1,ObstA,ObstB,ObstC)==False:
        xE= random.randint(2,9)
        yE= random.randint(2,9)
    x1Enemigo=ListaAnchoxAlto[0][xE1][yE1]
    y1Enemigo=ListaAnchoxAlto[1][xE1][yE1]
    pygame.draw.rect(ventana,(230, 128, 5), pygame.Rect(ListaAnchoxAlto[0][xE1][yE1],ListaAnchoxAlto[1][xE1][yE1], 50,50))
    


    #Enemigo2
    xE2= random.randint(2,9)
    yE2= random.randint(2,9)
    xyE2=(xE2,yE2)
    while comparaMovimiento(xyE2,ObstA,ObstB,ObstC)==False:
        xE2= random.randint(2,9)
        yE2= random.randint(2,9)
    x2Enemigo=ListaAnchoxAlto[0][xE2][yE2]
    y2Enemigo=ListaAnchoxAlto[1][xE2][yE2]
    pygame.draw.rect(ventana,(230, 128, 5), pygame.Rect(ListaAnchoxAlto[0][xE2][yE2],ListaAnchoxAlto[1][xE2][yE2], 50,50))
    

    #Inicio juego
    while (corriendo):
        puntaje=puntaje-10
        ventana.fill((0,0,0))
        puntajeI=str(puntaje)
        #Dubuja Puntaje
        ventana.blit(img1,(0,0))
        ventana.blit(img2,(610,0))
        fuente=pygame.font.SysFont("Arial",35)
        Puntaje=fuente.render("Puntaje: ",False,(255,255,255)) 
        PuntajeI=fuente.render(puntajeI,False,(255,255,255)) 
        ventana.blit(Puntaje,(630,80))
        ventana.blit(PuntajeI,(630,130))       
        
        #Dibujo de tablero
        for i in range(10):
            for j in range(10):
                if tablero[i+1][j+1]==1:
                    ventana.blit(suelo,(ListaAnchoxAlto[0][i][j],ListaAnchoxAlto[1][i][j]))
                    F=1
                else:
                    ventana.blit(sueloDinero,(ListaAnchoxAlto[0][i][j],ListaAnchoxAlto[1][i][j]))
                    F=0
            

        #Dibuja obstaculos en ventana
        ventana.blit(obstucalo,(+ListaAnchoxAlto[0][x1][y1],+ListaAnchoxAlto[1][x1][y1]))
        ventana.blit(obstucalo,(+ListaAnchoxAlto[0][x1+(1*H1)][y1+(1*F1)],+ListaAnchoxAlto[1][x1+(1*H1)][y1+(1*F1)]))
        ventana.blit(obstucalo,(+ListaAnchoxAlto[0][x1+(2*H1)][y1+(2*F1)],+ListaAnchoxAlto[1][x1+(2*H1)][y1+(2*F1)]))

        ventana.blit(obstucalo,(+ListaAnchoxAlto[0][x2][y2],+ListaAnchoxAlto[1][x2][y2]))
        ventana.blit(obstucalo,(+ListaAnchoxAlto[0][x2+(1*H2)][y2+(1*F2)],+ListaAnchoxAlto[1][x2+(1*H2)][y2+(1*F2)]))

        ventana.blit(obstucalo,(+ListaAnchoxAlto[0][x3][y3],+ListaAnchoxAlto[1][x3][y3]))
        



        

        #Obstaculos en el tablero de 0 y 1
        tablero[x3+1][y3+1]=2
            
        tablero[x2+1][y2+1]=2
        tablero[x2+(1*H2)+1][y2+(1*F2)+1]=2

        tablero[x1+1][y1+1]=2
        tablero[x1+(1*H1)+1][y1+(1*F1)+1]=2
        tablero [x1+(2*H1)+1][y1+(2*F1)+1]=2

        
         #Movimiento Qbert       
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                corriendo = False
            if event.type == pygame.KEYDOWN:
                tecla_presionada = pygame.key.name(event.key) 
                if tecla_presionada=="escape":
                    return "True",puntaje



                if tecla_presionada == "w" and yCuadradito != 10 and  comparaMovimiento((xCuadradito,yCuadradito-60),ObstA,ObstB,ObstC):
                    yCuadradito -= 60
                    puntaje =puntaje-100
                if tecla_presionada == "a" and xCuadradito != 10  and comparaMovimiento((xCuadradito-60,yCuadradito),ObstA,ObstB,ObstC):
                    xCuadradito -= 60
                    puntaje =puntaje-100
                if tecla_presionada == "s" and yCuadradito != 550 and comparaMovimiento((xCuadradito,yCuadradito+60),ObstA,ObstB,ObstC):
                    yCuadradito += 60
                    puntaje =puntaje-100
                if tecla_presionada == "d" and xCuadradito != 550 and comparaMovimiento((xCuadradito+60,yCuadradito),ObstA,ObstB,ObstC):
                    xCuadradito += 60
                    puntaje =puntaje-100
                    
                
                

             

        #Movimiento de Qbert en tablero 0 y 1                                    
                if tecla_presionada == "w" and tablero[y-1][x]!= 9 and tablero[y-1][x]!=2 : 
                    y= y-1
                    if tablero[y][x]==0:
                        tablero[y][x]=1
                    else:
                        tablero[y][x]=0
                if tecla_presionada == "a" and tablero[y][x-1]!=9 and tablero[y][x-1]!=2 :
                    x= x-1
                    if tablero[y][x]==0:
                        tablero[y][x]=1
                    else:
                        tablero[y][x]=0
                if tecla_presionada == "s" and tablero[y+1][x]!=9 and tablero[y+1][x]!=2 :
                    y= y+1
                    if tablero[y][x]==0:
                        tablero[y][x]=1
                    else:
                        tablero[y][x]=0
                if tecla_presionada == "d" and tablero[y][x+1]!=9 and tablero[y][x+1]!=2 :
                    x= x+1
                    if tablero[y][x]==0:
                        tablero[y][x]=1
                    else:
                        tablero[y][x]=0

                    
                    



            #movimiento 1° enemigo ventana
                if tecla_presionada == "d" or tecla_presionada == "s" or tecla_presionada == "a" or tecla_presionada == "w":
                    mover=random.randint(0,1)
                    direccion=random.randint(0,1)
                    
                if direccion==0:
                    direc=0
                    if mover==0 and x1Enemigo!=10  and comparaMovimiento((x1Enemigo-60,y1Enemigo),ObstA,ObstB,ObstC):
                        x1Enemigo=x1Enemigo-60 
                        direc=6
                    if mover==1 and x1Enemigo!=550 and comparaMovimiento((x1Enemigo+60,y1Enemigo),ObstA,ObstB,ObstC):
                        x1Enemigo=x1Enemigo+60
                        direc=6
                        
                    if direc==0:
                        if mover==0 and y1Enemigo!=10 and comparaMovimiento((x1Enemigo,y1Enemigo-60),ObstA,ObstB,ObstC):
                            y1Enemigo=y1Enemigo-60
                            direc=6
                        if mover==1 and y1Enemigo!=550 and comparaMovimiento((x1Enemigo,y1Enemigo+60),ObstA,ObstB,ObstC):
                            y1Enemigo=y1Enemigo+60
                            direc=6                        
                    



                    
                else:
                    direc=0
                    if mover==0 and y1Enemigo!=10 and comparaMovimiento((x1Enemigo,y1Enemigo-60),ObstA,ObstB,ObstC):
                        y1Enemigo=y1Enemigo-60
                        direc=6
                    if mover==1 and y1Enemigo!=550 and comparaMovimiento((x1Enemigo,y1Enemigo+60),ObstA,ObstB,ObstC):
                        y1Enemigo=y1Enemigo+60
                        direc=6
                        
                    if direc==0:
                        if mover==0 and x1Enemigo!=10  and comparaMovimiento((x1Enemigo-60,y1Enemigo),ObstA,ObstB,ObstC):
                            x1Enemigo=x1Enemigo-60 
                            direc=6
                        if mover==1 and x1Enemigo!=550 and comparaMovimiento((x1Enemigo+60,y1Enemigo),ObstA,ObstB,ObstC):
                            x1Enemigo=x1Enemigo+60
                            direc=6
                
            #movimiento 2° enemigo ventana
                if tecla_presionada == "d" or tecla_presionada == "s" or tecla_presionada == "a" or tecla_presionada == "w":
                    mover=random.randint(0,1)
                    direccion=random.randint(0,1)
                    
                    if direccion==0:
                        direc=0
                        if mover==0 and x2Enemigo!=10  and comparaMovimiento((x2Enemigo-60,y2Enemigo),ObstA,ObstB,ObstC):
                            x2Enemigo=x2Enemigo-60 
                            direc=6
                        if mover==1 and x2Enemigo!=550 and comparaMovimiento((x2Enemigo+60,y2Enemigo),ObstA,ObstB,ObstC):
                            x2Enemigo=x2Enemigo+60
                            direc=6
                        
                        if direc==0:
                            if mover==0 and y2Enemigo!=10 and comparaMovimiento((x2Enemigo,y2Enemigo-60),ObstA,ObstB,ObstC):
                                y2Enemigo=y2Enemigo-60
                                direc=6
                            if mover==1 and y2Enemigo!=550 and comparaMovimiento((x2Enemigo,y2Enemigo+60),ObstA,ObstB,ObstC):
                                y2Enemigo=y2Enemigo+60
                                direc=6                        
                    



                    
                    if direccion==1:
                        direc=0
                        if mover==0 and y2Enemigo!=10 and comparaMovimiento((x2Enemigo,y2Enemigo-60),ObstA,ObstB,ObstC):
                            y2Enemigo=y2Enemigo-60
                            direc=6
                        if mover==1 and y2Enemigo!=550 and comparaMovimiento((x2Enemigo,y2Enemigo+60),ObstA,ObstB,ObstC):
                            y2Enemigo=y2Enemigo+60
                            direc=6
                        
                        if direc==0:
                            if mover==0 and x2Enemigo!=10  and comparaMovimiento((x2Enemigo-60,y2Enemigo),ObstA,ObstB,ObstC):
                                x2Enemigo=x2Enemigo-60 
                                direc=6
                            if mover==1 and x2Enemigo!=550 and comparaMovimiento((x2Enemigo+60,y2Enemigo),ObstA,ObstB,ObstC):
                                x2Enemigo=x2Enemigo+60
                                direc=6                          



            
            
            
            #Enemigo toca a Qbert
            if (y1Enemigo,x1Enemigo)== (yCuadradito,xCuadradito) or (y2Enemigo,x2Enemigo)== (yCuadradito,xCuadradito):
                yCuadradito=10
                xCuadradito=10
                y=1
                x=1
                xE1= random.randint(2,9)
                yE1= random.randint(2,9)
                while comparaMovimiento(xyE1,ObstA,ObstB,ObstC)==False:
                    xE= random.randint(2,9)
                    yE= random.randint(2,9)
                x1Enemigo=ListaAnchoxAlto[0][xE1][yE1]
                y1Enemigo=ListaAnchoxAlto[1][xE1][yE1]
                pygame.draw.rect(ventana,(230, 128, 5), pygame.Rect(ListaAnchoxAlto[0][xE1][yE1],ListaAnchoxAlto[1][xE1][yE1], 50,50))
    


                #Enemigo2 
                xE2= random.randint(2,9)
                yE2= random.randint(2,9)
                while comparaMovimiento(xyE2,ObstA,ObstB,ObstC)==False:
                    xE2= random.randint(2,9)
                    yE2= random.randint(2,9)
                x2Enemigo=ListaAnchoxAlto[0][xE2][yE2]
                y2Enemigo=ListaAnchoxAlto[1][xE2][yE2]
                pygame.draw.rect(ventana,(230, 128, 5), pygame.Rect(ListaAnchoxAlto[0][xE2][yE2],ListaAnchoxAlto[1][xE2][yE2], 50,50))


                vidas=vidas-1
        for i in range (vidas):
            ventana.blit(vida,((630+(45*i)),20))
                    
        Qbert=[yCuadradito,xCuadradito]


        
         #dibujo Qbert        
        ventana.blit(Qberto,(xCuadradito,yCuadradito))
        
        #Dibujo enemigo
        ventana.blit(enemigo1,(x1Enemigo,y1Enemigo))
        ventana.blit(enemigo2,(x2Enemigo,y2Enemigo))
        
        pygame.display.flip()
        


        estado = win(tablero)
        if estado == True:
            return True,puntaje
            
        if vidas== 0:
            return False,puntaje
            
    pygame.quit()

#Funcion que hace que corra el juego y todas sus funciones
def inicio():

    #Pantallas
    perdido= pygame.image.load("perdido.jpg")
    ganado=  pygame.image.load("Ganadoxd.png")
    inicio=  pygame.image.load("Pantalla_inicio.jpg")
    istrucciones= pygame.image.load("Instrucciones.jpg")

    perdido=pygame.transform.scale(perdido,(800,610))
    ganado= pygame.transform.scale(ganado,(800,610))
    inicio= pygame.transform.scale(inicio,(800,610))
 
    pygame.init()
    
    ventana= pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
    pygame.display.set_caption("Qbert Mafia")
    ventana.fill((0,0,0))
    
    #img1= pygame.image.load("escenario.jpg")
    #img2= pygame.image.load("Parte derecha.jpg")

    H=0
    corriendo= True
    while (corriendo):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                corriendo = False

            if event.type == pygame.KEYDOWN:
                tecla_presionada = pygame.key.name(event.key)
                if tecla_presionada=="escape":
                    H=0
                    
                
                if tecla_presionada== "return":
                    F,puntaje=main()
                    print(puntaje)
                    if F == True:
                        H=1
                    if F== False:
                        H=4

                if tecla_presionada== "i":                
                    H=2

                
        if H==0:#inicio
            ventana.fill((0,0,0))
            ventana.blit(inicio,(0,0))
            pygame.display.flip()

            
        if H==1:#Ganado
            
            ventana.fill((200,200,200))
            ventana.blit(ganado,(0,0))
            #Dubuja Puntaje
            fuente=pygame.font.SysFont("Arial",35)
            Puntaje=fuente.render("Puntaje: ",False,(255,255,255)) 
            PuntajeI=fuente.render(str(puntaje),False,(255,255,255)) 
            ventana.blit(Puntaje,(500,30))
            ventana.blit(PuntajeI,(500,80))  
            pygame.display.flip()
            
        if H==2:#Instrucciones

            ventana.fill((255,255,255))
            ventana.blit(istrucciones,(0,0))
            pygame.display.flip()

        if H==4:#perdido
            ventana.fill((120,120,120))
            ventana.blit(perdido,(0,0))
            #Dubuja Puntaje
            fuente=pygame.font.SysFont("Arial",35)
            Puntaje=fuente.render("Puntaje: ",False,(255,255,255)) 
            PuntajeI=fuente.render("0",False,(255,255,255)) 
            ventana.blit(Puntaje,(630,50))
            ventana.blit(PuntajeI,(630,100))  
            pygame.display.flip()
            
    pygame.quit()


 
#tablero en ventana
x=10
y=10
ListaAlto=[]
ListaAncho=[]
ListaAnchoxAlto=[ListaAncho,ListaAlto]
for i in range(10):
    ListaAncho.append([])
    for j in range (10):
        ListaAncho[i].append(x)
        x=x+60
    x=10
    
for i in range(10):
    ListaAlto.append([])
    for j in range (10):
        ListaAlto[i].append(y)

    y=y+60


#Funcion juego
inicio()
