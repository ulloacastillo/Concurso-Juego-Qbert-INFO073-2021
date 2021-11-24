import pygame
import sys
import random



#Funciones para generar coordenadas
def obstaculo1 ():
    Obstaculo1_1=[]
    Obstaculo1=[]
    for i in range (1):
        Obstaculo1_y=(random.randrange(1,10))
        Obstaculo1_x=(random.randrange(10))
        while Obstaculo1_y == 0 and Obstaculo1_x == 0: #Valida que las cordenadas del primer obstaculo no sean (0,0)
            Obstaculo1_y=(random.randrange(1,10))
            Obstaculo1_x=(random.randrange(10))
        Obstaculo1_1.append (Obstaculo1_x)
        Obstaculo1_1.append (Obstaculo1_y)
        Obstaculo1.append (Obstaculo1_1)
    return Obstaculo1 

def obstaculo2 ():
    Obstaculo2=[]
    for i in range (2):
        Obstaculo2_y=(random.randrange(1,10))
        Obstaculo2_x=(random.randrange(10))
        while Obstaculo2_x == 0 and Obstaculo2_y == 0: #Valida que las primeras cordenadas del segundo obstaculo no sea (0,0)
            Obstaculo2_x=(random.randrange(10))
            Obstaculo2_y=(random.randrange(1,10))
        if i<1:                                        #Para el primer segmento del segundo obstaculo simplemente guarda las coordenadas
            Obstaculo2_1=[]
            Obstaculo2_1.append (Obstaculo2_x)
            Obstaculo2_1.append (Obstaculo2_y)
            Obstaculo2.append (Obstaculo2_1)
        if i>=1:                                       #Para el segundo segmento del segundo obstaculo realiza mas pasos antes de guardar las coordenadas
            Obstaculo2_2=[]
            while Obstaculo2_y != Obstaculo2[0][1] and Obstaculo2_x != Obstaculo2[0][0]: #Verifica que las coordenadas tengan un eje en comun con el primer segmento
                Obstaculo2_y=(random.randrange(1,10))
                Obstaculo2_x=(random.randrange(10))
            if Obstaculo2_x == Obstaculo2 [0][0]:      
                while (Obstaculo2_y - 1 != Obstaculo2 [0][1] and Obstaculo2_y + 1 != Obstaculo2[0][1]) or (Obstaculo2_y==0 and Obstaculo2_y==0): #Para las coordenadas del segundo segmento revisa que esté conectado al primer segmento y sea distinto de (0,0)
                    Obstaculo2_y=(random.randrange(1,10))
            if Obstaculo2_y == Obstaculo2[0][1]:
                while (Obstaculo2_x - 1 != Obstaculo2 [0][0] and Obstaculo2_x + 1 != Obstaculo2[0][0]) or ((Obstaculo2_x==0 and Obstaculo2_x==0)):
                    Obstaculo2_x=(random.randrange(10))
            Obstaculo2_2.append (Obstaculo2_x)
            Obstaculo2_2.append (Obstaculo2_y)
            Obstaculo2.append (Obstaculo2_2)
    return Obstaculo2
def obstaculo3 ():
    Obstaculo3 = []
    for i in range (3):
        Obstaculo3_y=(random.randrange(1,10))
        Obstaculo3_x=(random.randrange(10))
        while (Obstaculo3_x ==0 and Obstaculo3_y ==0) or (Obstaculo3_y==0):
            Obstaculo3_x=(random.randrange(10))
            Obstaculo3_y=(random.randrange(1,10))
        if i<1:
            Obstaculo3_1=[]
            Obstaculo3_1.append (Obstaculo3_x)
            Obstaculo3_1.append (Obstaculo3_y)
            Obstaculo3.append (Obstaculo3_1)
        if i>=1:
            Obstaculo3_2=[]
            while Obstaculo3_y != Obstaculo3[0][1] and Obstaculo3_x != Obstaculo3[0][0]:
                Obstaculo3_y=(random.randrange(1,10))
                Obstaculo3_x=(random.randrange(10))
            if Obstaculo3_x == Obstaculo3 [0][0]:
                while (Obstaculo3_y - 1 != Obstaculo3 [0][1] and Obstaculo3_y + 1 != Obstaculo3[0][1]) or (Obstaculo3_y==-1) or (Obstaculo3_y==0) or (Obstaculo3_y>=10):
                    Obstaculo3_y=(random.randrange(Obstaculo3[0][1]-1, Obstaculo3[0][1]+2))
                if i>1:                 #Para tercer segmento verifica que no sea igual al segundo
                    if Obstaculo3_y == Obstaculo3 [1][1]: #Verifica que el tercer segmento no se vea obstaculizado para generarse 
                        Obstaculo3_y==Obstaculo3[0][1]
                        while (Obstaculo3_x == Obstaculo3[1][0]) or (Obstaculo3_x - 1 != Obstaculo3 [0][0] and Obstaculo3_x + 1 != Obstaculo3[0][0]) or (Obstaculo3_x<=-1) or (Obstaculo3_x>=10): 
                            Obstaculo3_x = (random.randrange(Obstaculo3[0][0]-1, Obstaculo3[0][0]+2))
                        if Obstaculo3_y==0:
                            while Obstaculo3_x==0:  
                                Obstaculo3_x=(random.randrange(Obstaculo3[0][0]-1, Obstaculo3[0][0]+2))
                    else:
                        while (Obstaculo3_y == Obstaculo3 [1][1]) or (Obstaculo3_y - 1 != Obstaculo3[0][1] and Obstaculo3_y + 1 != Obstaculo3[0][1]) or (Obstaculo3_y==-1) or (Obstaculo3_y==0) or (Obstaculo3_y>=10):
                            Obstaculo3_y=(random.randrange(Obstaculo3[0][1]-1, Obstaculo3[0][1]+2))  
                            if Obstaculo3_x==0:
                                while (Obstaculo3_y==0):
                                    Obstaculo3_y=(random.randrange(Obstaculo3[0][1]-1, Obstaculo3[0][1]+2))
                            
            if Obstaculo3_y == Obstaculo3[0][1]:
                while (Obstaculo3_x - 1 != Obstaculo3 [0][0] and Obstaculo3_x + 1 != Obstaculo3[0][0]) or (Obstaculo3_x==-1) or (Obstaculo3_x>=10):
                    Obstaculo3_x=(random.randrange(Obstaculo3[0][0]-1, Obstaculo3[0][0]+2,2))
                if i>1:                     #Para el tercer segmento verifica que no sea igual al segundo
                    if Obstaculo3_x == Obstaculo3[1][0]:             #Verifica que el tercer segmento no se vea obstaculizado para generarse
                        Obstaculo3_x==Obstaculo3[0][0]
                        while (Obstaculo3_y == Obstaculo3 [1][1]) or (Obstaculo3_y - 1 != Obstaculo3[0][1] and Obstaculo3_y + 1 != Obstaculo3[0][1]) or (Obstaculo3_y==-1) or (Obstaculo3_y>=10):
                            Obstaculo3_y=(random.randrange(Obstaculo3[0][1]-1, Obstaculo3[0][1]+2))  
                            if Obstaculo3_x==0:
                                while (Obstaculo3_y==0):
                                    Obstaculo3_y=(random.randrange(Obstaculo3[0][1]-1, Obstaculo3[0][1]+2))
                    else:
                        while (Obstaculo3_x == Obstaculo3[1][0]) or (Obstaculo3_x - 1 != Obstaculo3 [0][0] and Obstaculo3_x + 1 != Obstaculo3[0][0]) or (Obstaculo3_x==-1)or (Obstaculo3_x>=10): 
                            Obstaculo3_x = (random.randrange(Obstaculo3[0][0]-1, Obstaculo3[0][0]+2))
                            if Obstaculo3_y==0:
                                while Obstaculo3_x==0:
                                    Obstaculo3_x=(random.randrange(Obstaculo3[0][0]-1, Obstaculo3[0][0]+2))
                    
            Obstaculo3_2.append (Obstaculo3_x)
            Obstaculo3_2.append (Obstaculo3_y)
            Obstaculo3.append (Obstaculo3_2)
    return Obstaculo3

def movrandom(x,y,tablero):
  flag=True
  while flag:
    eleccion=random.randrange(1,5)
    if eleccion==1 and x<9 and tablero[y][x+1]!=2:
        x=x+1
        flag=False
    elif eleccion==2 and x>0 and tablero[y][x-1]!=2:
        x=x-1
        flag=False
    elif eleccion==3 and y<9 and tablero[y+1][x]!=2:
        y=y+1
        flag=False
    elif eleccion==4 and y>0 and tablero[y-1][x]!=2:
        y=y-1
        flag=False
  return(x,y)






ANCHO=900
ALTO=600

def main():

    pygame.init()

    
    #Creacion de obstaculos (Coordenadas)
    Obs1=obstaculo1 ()
    Obs2=obstaculo2 ()
    while Obs2[0] == Obs1[0] or Obs2 [1] == Obs1[0]:
        Obs2=obstaculo2 ()
    Obs3=obstaculo3 ()
    for i in range (3):
        for j in range(2):
            while Obs3[i] == Obs2[j] or Obs3[i] == Obs1[0]:
                Obs3=obstaculo3 ()
    if Obs3[2][1]==0:
        Obs3=obstaculo3 ()
        for i in range (3):
            for j in range(2):
                while Obs3[i] == Obs2[j] or Obs3[i] == Obs1[0]:
                    Obs3=obstaculo3 ()


        


    GRIS=(123,123,123)
    ventana= pygame.display.set_mode((ANCHO,ALTO))
    pygame.display.set_caption("Tutorial")
    ventana.fill(GRIS)

    ##Creación del tablero
    ##  1 = desmarcado
    ## -1 = marcado
    ##  2 = obstaculo
    tablero = []
    for i in range(10):
      fila = []
      for j in range(10):
        fila.append(1)
      tablero.append(fila)
    tablero[0][0]=-1 #Bloque de aparicion marcado

    #Creacion de obstaculos en tablero
    tablero[Obs1[0][0]][Obs1[0][1]]=2

    for i in range (2):
        tablero[Obs2[i][0]][Obs2[i][1]]=2
    for i in range (3):
        tablero [Obs3[i][0]][Obs3[i][1]]=2
        

    #Colores
    ROJO=(255,0,0)
    VERDE=(31, 204, 33)
    NEGRO=(0,0,0)
    AMARILLO=(244, 255, 36)
    MORADOOSCU=(67, 13, 74)
    BLANCO=(255,255,255)
    

    #Variables utiles
    vidas=3
    help=1
    instrucciones=False
    contador=0
    puntaje=30000

    #Variables de texto
    #"chiller" , bauhaus93""
    pygame.font.get_fonts()
    fuente=pygame.font.Font(None,30)
    fuenteG=pygame.font.Font(None,50)
    fuenteP=pygame.font.Font(None,20)
    fuenteVidasPunt=pygame.font.Font(None,130)
    fuenteNumPunt=pygame.font.Font(None,100)
    fuenteVictoria=pygame.font.SysFont('goudystout', 67, bold=False, italic=False)
    fuenteGoudy=pygame.font.SysFont('goudystout', 100, bold=False, italic=False)
    titulo=fuenteG.render("Instrucciones",1,BLANCO)
    textoA1=fuente.render("-Si Q*bert completa el tablero de color verde, se",1,BLANCO)
    textoB1=fuente.render("consigue la victoria.",1,BLANCO)
    texto3=fuente.render("-Cuidado con los obstáculos y los enemigos!!!",1,BLANCO)
    texto4=fuente.render("-Para moverte utiliza las teclas W, A, S, D.",1,BLANCO)
    textoA2=fuente.render("-Por cada movimiento que hagas, perderás 10",1,BLANCO)
    textoB2=fuente.render("puntos, y si pierdes una vida, perderás 105 pts.",1,BLANCO)
    texto7=fuenteG.render("Pulsa [i] para volver",1,AMARILLO)
    textoPresI=fuente.render("Instrucciones [ i ]",1,BLANCO)
    textoPresR=fuente.render("Reiniciar [ R ]",1,BLANCO)
    textoMarcado=fuenteP.render("Marcado",1,BLANCO)
    textoEnemigo=fuenteP.render("Enemigo",1,BLANCO)
    textoDesmarcado=fuenteP.render("Desmarcado",1,BLANCO)
    textoObstaculo=fuenteP.render("Obstáculo",1,BLANCO)
    textoVidas=fuenteVidasPunt.render("VIDAS",1,BLANCO)
    textoPerdiste=fuenteGoudy.render("GAME",1,BLANCO)
    textoPerdiste2=fuenteGoudy.render("OVER",1,BLANCO)
    textoPuntaje1=fuente.render("Puntaje final:",1,BLANCO)
    textoPuntajeActual=fuenteNumPunt.render(str(puntaje),1,BLANCO)
    textoPuntaje=fuenteVidasPunt.render("Puntaje",1,BLANCO)
    textoVictoria=fuenteVictoria.render("Victoria",1,BLANCO)
    textoImagenes=fuenteP.render("*Las imagenes fueron sacadas de internet*",1,BLANCO)
    textoVidasRestantes=fuenteG.render("Vidas restantes:",1,BLANCO)

    #Imagenes
    imgQbert=pygame.image.load("qbertChico.png")
    imgFantasma=pygame.image.load("fantasmita.png")
    imgFantasmaM=pygame.image.load("fantasmitaM.png")
    imgFantasmaDoble=pygame.image.load("doblefantasma.png")
    imgCorazon=pygame.image.load("Corazon.png")
    imgCorazonVacio=pygame.image.load("CorazonVacio.png")

    
    
    #variables de dibujo
    separacion_tablero = 51
    ancho_tablero = 41

     
    #Posiciones en el tablero
    pos_jugador_x = 0
    pos_jugador_y = 0


    #Posiciones enemigo1
    pos_enem_x=random.randrange(1,9)
    pos_enem_y=random.randrange(1,9)
    while tablero[pos_enem_y][pos_enem_x]==2:
      pos_enem_x=random.randrange(1,9)
      pos_enem_y=random.randrange(1,9)


    #Posiciones enemigo2
    pos_enem_x2=random.randrange(1,9)
    pos_enem_y2=random.randrange(1,9)
    while tablero[pos_enem_y2][pos_enem_x2]==2 or (pos_enem_y2==pos_enem_y)and(pos_enem_x2==pos_enem_x):
      pos_enem_x2=random.randrange(1,9)
      pos_enem_y2=random.randrange(1,9)

    


    pygame.display.flip()

    reloj=pygame.time.Clock()


    corriendo=True
    ##################################################################################################################
    while corriendo:
        reloj.tick(60)
        
        ventana.fill(GRIS)
      
        for event in pygame.event.get():
            if(event.type == (pygame.QUIT)):
                corriendo =False
            if (event.type==(pygame.KEYDOWN)):
                tecla=pygame.key.name(event.key)
                if tecla=="i":#help=1
                    help*=-1
                    if (help==1):
                        instrucciones=False
                    if(help==-1):
                        instrucciones=True
                if tecla=="r" and help==1:#Con el help==1, evita el reinicio dentro de las instrucciones
                    #Recrear tablero
                    tablero = []
                    for i in range(10):
                        fila = []
                        for j in range(10):
                            fila.append(1)
                        tablero.append(fila)
                    tablero[0][0]=-1 

                    #Variables al valor original
                    pos_jugador_x=0
                    pos_jugador_y=0
                    vidas=3
                    puntaje=30000
                    contador=0

                    #Recrear obstaculos
                    Obs1=obstaculo1 ()
                    Obs2=obstaculo2 ()
                    while Obs2[0] == Obs1[0] or Obs2 [1] == Obs1[0]:
                        Obs2=obstaculo2 ()
                    Obs3=obstaculo3 ()
                    for i in range (3):
                        for j in range(2):
                            while Obs3[i] == Obs2[j] or Obs3[i] == Obs1[0]:
                                Obs3=obstaculo3 ()
                    if Obs3[2][1]==0:
                        Obs3=obstaculo3 ()
                        for i in range (3):
                            for j in range(2):
                                while Obs3[i] == Obs2[j] or Obs3[i] == Obs1[0]:
                                    Obs3=obstaculo3 ()

                    tablero[Obs1[0][0]][Obs1[0][1]]=2
                    for i in range (2):
                        tablero[Obs2[i][0]][Obs2[i][1]]=2
                    for i in range (3):
                        tablero [Obs3[i][0]][Obs3[i][1]]=2
                    
                    #Posiciones enemigo1
                    pos_enem_x=random.randrange(1,9)
                    pos_enem_y=random.randrange(1,9)
                    while tablero[pos_enem_y][pos_enem_x]==2:
                        pos_enem_x=random.randrange(1,9)
                        pos_enem_y=random.randrange(1,9)


                    #Posiciones enemigo2
                    pos_enem_x2=random.randrange(1,9)
                    pos_enem_y2=random.randrange(1,9)
                    while tablero[pos_enem_y2][pos_enem_x2]==2 or (pos_enem_y2==pos_enem_y)and(pos_enem_x2==pos_enem_x):
                        pos_enem_x2=random.randrange(1,9)
                        pos_enem_y2=random.randrange(1,9)
                    
                    

            if(vidas>0):            
                if help==1 and contador!=94: #Evita el movimiento mientras se ven las instrucciones y la pantalla de victoria
                    #Movimiento del personaje y enemigo
                    if event.type == pygame.KEYDOWN:
                        tecla_presionada= pygame.key.name(event.key)
                        if tecla_presionada=="w" and pos_jugador_y > 0:
                        #Validar que no haya un obstaculo en la siguente posicion
                            if tablero[pos_jugador_y-1][pos_jugador_x ] != 2:
                                pos_jugador_y -= 1
                                #Marcar el cuadrado de color verde
                                tablero[pos_jugador_y][pos_jugador_x] *= -1
                                pos_enem_x,pos_enem_y=movrandom(pos_enem_x,pos_enem_y,tablero)
                                pos_enem_x2,pos_enem_y2=movrandom(pos_enem_x2,pos_enem_y2,tablero)
                                #Validar que los enemigos no esten en la misma posicion y tampoco en el inicio
                                if(pos_enem_x==pos_enem_x2) and (pos_enem_y==pos_enem_y2) or (pos_enem_x==0)and(pos_enem_y==0) or (pos_enem_x2==0)and(pos_enem_y2==0):
                                    pos_enem_x2,pos_enem_y2=movrandom(pos_enem_x2,pos_enem_y2,tablero)
                                puntaje-=10
                                #Volver al inicio al personaje, conteo de vidas
                                if(pos_enem_x==pos_jugador_x)and(pos_enem_y==pos_jugador_y)or(pos_enem_x2==pos_jugador_x)and(pos_enem_y2==pos_jugador_y):
                                    pos_jugador_x=0
                                    pos_jugador_y=0
                                    vidas=vidas-1
                                    #Arrgelo puntaje si pierdes vida
                                    puntaje-=105
                                #Comprobar Victoria
                                for i in range(10):
                                    for j in range(10):
                                        if tablero[i][j] == -1:
                                            contador+=1  
                                        elif tablero[i][j] == 1:
                                            contador-=1
                                if contador!=94:
                                    contador=0
                                

                                    
                                    
                                    


                        
                        
                        if tecla_presionada=="a" and pos_jugador_x > 0:
                            if tablero[pos_jugador_y][pos_jugador_x-1] != 2:
                                pos_jugador_x -= 1
                                tablero[pos_jugador_y][pos_jugador_x] *= -1
                                pos_enem_x,pos_enem_y=movrandom(pos_enem_x,pos_enem_y,tablero)
                                pos_enem_x2,pos_enem_y2=movrandom(pos_enem_x2,pos_enem_y2,tablero)
                                if(pos_enem_x==pos_enem_x2) and (pos_enem_y==pos_enem_y2) or (pos_enem_x==0)and(pos_enem_y==0) or (pos_enem_x2==0)and(pos_enem_y2==0):
                                    pos_enem_x2,pos_enem_y2=movrandom(pos_enem_x2,pos_enem_y2,tablero)
                                puntaje-=10
                                if(pos_enem_x==pos_jugador_x)and(pos_enem_y==pos_jugador_y)or(pos_enem_x2==pos_jugador_x)and(pos_enem_y2==pos_jugador_y):
                                    pos_jugador_x=0
                                    pos_jugador_y=0
                                    vidas=vidas-1
                                    puntaje-=105
                                for i in range(10):
                                    for j in range(10):
                                        if tablero[i][j] == -1:
                                            contador+=1  
                                        elif tablero[i][j] ==1:
                                            contador-=1
                                if contador!=94:
                                    contador=0

                                    
                                    


                        

                        if tecla_presionada=="s" and pos_jugador_y < 9: 
                            if tablero[pos_jugador_y+1][pos_jugador_x] != 2:
                                pos_jugador_y += 1
                                tablero[pos_jugador_y][pos_jugador_x] *= -1
                                pos_enem_x,pos_enem_y=movrandom(pos_enem_x,pos_enem_y,tablero)
                                pos_enem_x2,pos_enem_y2=movrandom(pos_enem_x2,pos_enem_y2,tablero)
                                if(pos_enem_x==pos_enem_x2) and (pos_enem_y==pos_enem_y2) or (pos_enem_x==0)and(pos_enem_y==0) or (pos_enem_x2==0)and(pos_enem_y2==0):
                                    pos_enem_x2,pos_enem_y2=movrandom(pos_enem_x2,pos_enem_y2,tablero)
                                puntaje-=10
                                if(pos_enem_x==pos_jugador_x)and(pos_enem_y==pos_jugador_y)or(pos_enem_x2==pos_jugador_x)and(pos_enem_y2==pos_jugador_y):
                                    pos_jugador_x=0
                                    pos_jugador_y=0
                                    vidas=vidas-1
                                    puntaje-=105
                                for i in range(10):
                                    for j in range(10):
                                        if tablero[i][j] == -1:
                                            contador+=1  
                                        elif tablero[i][j] == 1:
                                            contador-=1
                                if contador!=94:
                                    contador=0
                                    
                                    
                                    


                        
                            
                        if tecla_presionada=="d" and pos_jugador_x < 9:
                            if tablero[pos_jugador_y][pos_jugador_x+1] != 2:
                                pos_jugador_x += 1
                                tablero[pos_jugador_y][pos_jugador_x] *= -1
                                pos_enem_x,pos_enem_y=movrandom(pos_enem_x,pos_enem_y,tablero)
                                pos_enem_x2,pos_enem_y2=movrandom(pos_enem_x2,pos_enem_y2,tablero)
                                if(pos_enem_x==pos_enem_x2) and (pos_enem_y==pos_enem_y2) or (pos_enem_x==0)and(pos_enem_y==0) or (pos_enem_x2==0)and(pos_enem_y2==0):
                                    pos_enem_x2,pos_enem_y2=movrandom(pos_enem_x2,pos_enem_y2,tablero)
                                puntaje-=10
                                if(pos_enem_x==pos_jugador_x)and(pos_enem_y==pos_jugador_y)or(pos_enem_x2==pos_jugador_x)and(pos_enem_y2==pos_jugador_y):
                                    pos_jugador_x=0
                                    pos_jugador_y=0
                                    vidas=vidas-1
                                    puntaje-=105
                                for i in range(10):
                                    for j in range(10):
                                        if tablero[i][j] == -1:
                                            contador+=1  
                                        elif tablero[i][j] == 1:
                                            contador-=1
                                if contador!=94:
                                    contador=0


        textoPuntajeActual=fuenteNumPunt.render(str(puntaje),1,BLANCO)
        
 
    
        ##Dibujar el tablero y cambio de color
        for i in range(10):
          for j in range(10):
            if tablero[i][j] == 1:
              color = ROJO    
            elif tablero[i][j] == -1:
              color = VERDE
            elif tablero[i][j] == 2:
              color = NEGRO
            pygame.draw.rect(ventana, color, pygame.Rect(j * separacion_tablero, i *separacion_tablero, ancho_tablero, ancho_tablero))

        

        #Jugador y enemigo
        ventana.blit(imgQbert,(((pos_jugador_x)*51)+3,((pos_jugador_y)*51)+3))
        ventana.blit(imgFantasma,(((pos_enem_x)*51)+1,((pos_enem_y)*51)+1))  
        ventana.blit(imgFantasmaM,(((pos_enem_x2)*51)+1,((pos_enem_y2)*51)+1))
        
        
        #TEXTO
        ventana.blit(textoPresI,(290,520)) 
        ventana.blit(textoPresR,(290,565))
        ventana.blit(textoVidas,(565,50))
        ventana.blit(textoPuntaje,(540,300))
        ventana.blit(textoPuntajeActual,(600,410))
        ventana.blit(textoImagenes,(626,580))
        #Definicion colores
        pygame.draw.rect(ventana,VERDE, pygame.Rect(20,515,30,30)) 
        ventana.blit(textoMarcado,(55,522))
        pygame.draw.rect(ventana,ROJO, pygame.Rect(20,560,30,30)) 
        ventana.blit(textoDesmarcado,(55,567))
        pygame.draw.rect(ventana,NEGRO, pygame.Rect(160,515,30,30)) 
        ventana.blit(textoObstaculo,(195,522))
        ventana.blit(imgFantasmaDoble,(153,555)) 
        ventana.blit(textoEnemigo,(195,567))#160,560


        #VIDAS
        if (vidas==3):
            ventana.blit(imgCorazon,(550,160))
            ventana.blit(imgCorazon,(655,160))
            ventana.blit(imgCorazon,(760,160))
            
            
        if (vidas==2):
            ventana.blit(imgCorazon,(550,160))
            ventana.blit(imgCorazon,(655,160))
            ventana.blit(imgCorazonVacio,(760,160))

        if (vidas==1):
            ventana.blit(imgCorazon,(550,160))
            ventana.blit(imgCorazonVacio,(655,160))
            ventana.blit(imgCorazonVacio,(760,160))
            

        #Pantalla De victoria
        if(contador==94):
            ventana.fill(GRIS)
            pygame.draw.rect(ventana,NEGRO, pygame.Rect(120,120,700,400))
            pygame.draw.rect(ventana,MORADOOSCU, pygame.Rect(100,100,700,400))
            if (vidas==3):
                ventana.blit(imgCorazon,(253,270))
                ventana.blit(imgCorazon,(403,270))
                ventana.blit(imgCorazon,(553,270)) 
            if (vidas==2):
                ventana.blit(imgCorazon,(253,270))
                ventana.blit(imgCorazon,(403,270))
                ventana.blit(imgCorazonVacio,(553,270))
            if (vidas==1):
                ventana.blit(imgCorazon,(253,270))
                ventana.blit(imgCorazonVacio,(403,270))
                ventana.blit(imgCorazonVacio,(553,270))
            ventana.blit(textoVidasRestantes,(320,225))
            ventana.blit(textoVictoria,(130,130))
            ventana.blit(textoPresR,(550,410))
            ventana.blit(textoPuntaje1,(240,400))
            textoPuntajeFinal=fuente.render(str(puntaje),1,BLANCO)
            ventana.blit(textoPuntajeFinal,(280,430))



        #Pantalla de Derrota
        if(vidas==0):
            ventana.fill(GRIS)
            pygame.draw.rect(ventana,NEGRO, pygame.Rect(120,120,700,400))
            pygame.draw.rect(ventana,MORADOOSCU, pygame.Rect(100,100,700,400))
            ventana.blit(textoPerdiste,(177,130))
            ventana.blit(textoPerdiste2,(197,260))
            ventana.blit(textoPresR,(515,420))
            ventana.blit(textoPuntaje1,(250,400))
            textoPuntajeFinal=fuente.render(str(puntaje),1,BLANCO)
            ventana.blit(textoPuntajeFinal,(290,430))
            

       
        #Instrucciones
        if instrucciones==True: 
            pygame.draw.rect(ventana,GRIS, pygame.Rect(0,0,ANCHO,ALTO))
            pygame.draw.rect(ventana,NEGRO, pygame.Rect(220,120,500,300))
            pygame.draw.rect(ventana,MORADOOSCU, pygame.Rect(200,100,500,300)) 

            ventana.blit(titulo,(340,110))
            ventana.blit(textoA1,(212,156))
            ventana.blit(textoB1,(217,178))
            ventana.blit(texto3,(212,214))
            ventana.blit(texto4,(212,250))
            ventana.blit(textoA2,(212,286))
            ventana.blit(textoB2,(217,308))
            ventana.blit(texto7,(290,350))
        
        
       

        pygame.display.flip()
        
    sys.exit()
    
main()

"""
LINK IMAGENES

Enemigos (solo le cambie el color)
https://www.stickpng.com/es/img/juegos/pacman/pacman-fantasma-amarilla

Qbert
http://pixelartmaker.com/art/f9593c7fa46f2e2

Corazon
https://pixabay.com/es/illustrations/pixel-coraz%C3%B3n-coraz%C3%B3n-p%C3%ADxeles-2779422/
"""
