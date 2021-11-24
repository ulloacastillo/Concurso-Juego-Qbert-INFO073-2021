

from funciones import *
from sprites import *
import pygame
import sys
import random
import os

ANCHO_VENTANA = 640
ALTO_VENTANA = 480
NOMBRE_DISPLAY = "K*bert"
FPS = 60

def main():
    pygame.init()

    ventana = pygame.display.set_mode((ANCHO_VENTANA,ALTO_VENTANA))
    pygame.display.set_caption(NOMBRE_DISPLAY)
    ventana.fill((147,90,71))

    sprPlayerDown   = imgLoad("sprites\playerDown.png")
    pygame.display.set_icon(sprPlayerDown)

    reloj = pygame.time.Clock()

    gameOpen = True
    ejecutando = "startup"

    while gameOpen == True:

        while ejecutando == "startup":

            mostrarInstrucciones = False
            win = False
            pause = False

            #variables Sonidos
            musicPlaying = False #musica resultados
            gameMusic = False #musica juego
            soundSet = False

            #contador resultados
            resContador = 0
            resSegundos = 0

            #Datos puntajes
            saved = False
            name = ""

            filePuntajes = open(os.path.join(sys.path[0], "scores.korbo"), "r")
            tablaPuntajes = filePuntajes.read()
            tablaPuntajes = tablaPuntajes.split()
            tablaPuntajes[1] = int(tablaPuntajes[1])
            tablaPuntajes[3] = int(tablaPuntajes[3])
            tablaPuntajes[5] = int(tablaPuntajes[5])
            print(tablaPuntajes)


            #variables efectos
            fxDelay = 1
            fxPlay = True
            fxSpeed = 20
            fxColor = 0,0,0
            fxAlto = 0
            fxAncho = ANCHO_VENTANA

            
            numObstaculos = 3
            mainGrid = cuadricula(10,10)
            mainGrid = obstaculos(numObstaculos,mainGrid)
            printGrid(mainGrid)
            while (mainGrid[0][1] == 1) and (mainGrid[1][0] == 1):
                mainGrid = cuadricula(10,10)
                print("Jugador atrapadooooo, nooo aaa")
                mainGrid = obstaculos(numObstaculos,mainGrid)
                printGrid(mainGrid)
            mainGrid[0][0] = 2
            pintado = 1 #cantidad de cuadrados pintados


            #calcular cantidad de espacios por los que te puedes mover
            totalEspacios = len(mainGrid)*len(mainGrid[0])
            espaciosOcupados = 0
            for i in range(numObstaculos):
                espaciosOcupados += (i+1)

            espaciosLibres = totalEspacios - espaciosOcupados
            print("total espacios:",espaciosLibres)

            #sprites
            #sprImagen = pygame.image.load(open(os.path.join(sys.path[0], "sprites\imagen.png"), "r"))
            sprEspacio      = imgLoad("sprites\espacio.png")
            sprPintado      = imgLoad("sprites\pintado.png")
            sprObstaculo    = imgLoad("sprites\obstaculo.png")
            sprPlayerLeft   = imgLoad("sprites\playerLeft.png")
            sprPlayerRight  = imgLoad("sprites\playerRight.png")
            sprPlayerUp     = imgLoad("sprites\playerUp.png")
            sprPlayerDown   = imgLoad("sprites\playerDown.png")
            sprEnemy1       = imgLoad("sprites\enemy1.png")
            sprEnemy2       = imgLoad("sprites\enemy2.png")
            sprVidaLlena    = imgLoad("sprites\_vidaLLena.png")
            sprVidaVacia    = imgLoad("sprites\_vidaVacia.png")
            sprPause        = imgLoad("sprites\pause.png")
            sprPauseText    = imgLoad("sprites\pauseText.png")
            sprKorboBig     = imgLoad("sprites\korboBig.png")
            sprBotones      = imgLoad("sprites\_botones.png")
            sprStartText    = imgLoad("sprites\startText.png")
            sprPuntajes     = imgLoad("sprites\puntajes.png")
            sprKorboLose    = imgLoad("sprites\korboLose.png")
            sprKorboWin     = imgLoad("sprites\korboWin.png")
            sprInstrucciones= imgLoad("sprites\instrucciones.png")

            playerDraw = sprPlayerLeft


            font = pygame.font.Font(os.path.join(sys.path[0], "arcade.TTF"), 31)

            clrLibre = 255,255,255
            clrPintado = 121,3,125
            clrObstaculo = 0,40,0
            clrPlayer = 237,83,222
            clrEnemy = 252,48,3


            playerGridX = 0 #Posicion X del jugador dentro del grid
            playerGridY = 0 #Posicion Y del jugador dentro del grid

            enemigos = genEnemy(2,mainGrid)
            vidaTotal = 3
            vidas = vidaTotal
            puntaje = 0

            contador = 0 #contador de fotogramas
            segundos = 0 #contador de segundos

            contadorMenu = 0
            segundosMenu = 0

            ejecutando = "menu"


        while ejecutando == "menu":
            
            reloj.tick(FPS)


            ventana.fill((146,211,255))

            (contadorMenu,segundosMenu) = contadorSeg(contadorMenu,segundosMenu,FPS)

            #Mostrar korbo
            drawSplashImage = sprKorboBig
            drawSplashImage = pygame.transform.scale(drawSplashImage, (176, 220))
            ventana.blit(drawSplashImage, (80,30,40, 40))

            #mostrar botones
            drawBotones = sprBotones
            drawBotones = pygame.transform.scale(drawBotones, (292, 124))
            ventana.blit(drawBotones, (320,330,40, 40))

            #Mostrar "press y to start"
            if (contadorMenu <= FPS/2):
                drawStart = sprStartText
                drawStart = pygame.transform.scale(drawStart, (252, 16))
                ventana.blit(drawStart, (35,380,40, 40))
            
            #Mostrar panel puntajes
            drawPuntajes = sprPuntajes
            drawPuntajes = pygame.transform.scale(drawPuntajes, (312, 212))
            ventana.blit(drawPuntajes, (305,30,40, 40))

            textPuntaje1 = tablaPuntajes[0] + " " + str(tablaPuntajes[1])
            textPuntaje2 = tablaPuntajes[2] + " " + str(tablaPuntajes[3])
            textPuntaje3 = tablaPuntajes[4] + " " + str(tablaPuntajes[5])

            drawTextPuntaje1 = font.render(textPuntaje1, False, (255,255,255))
            ventana.blit(drawTextPuntaje1,(310,89))

            drawTextPuntaje2 = font.render(textPuntaje2, False, (255,255,255))
            ventana.blit(drawTextPuntaje2,(310,145))

            drawTextPuntaje3 = font.render(textPuntaje3, False, (255,255,255))
            ventana.blit(drawTextPuntaje3,(310,200))

            if mostrarInstrucciones == True:
                sprInstrucciones = pygame.transform.scale(sprInstrucciones, (ANCHO_VENTANA, ALTO_VENTANA))
                ventana.blit(sprInstrucciones,(0,0))
            


            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    ejecutando = "none"
                    gameOpen = False
                
                if (event.type == pygame.KEYDOWN):
                    tecla_presionada =  pygame.key.name(event.key)

                    if tecla_presionada == "y":
                        if mostrarInstrucciones == False:
                            mostrarInstrucciones = True
                    
                    if tecla_presionada == "return":
                        if mostrarInstrucciones == True:
                            soundSet = False
                            ejecutando = "juego"

                    if tecla_presionada == "escape":
                        ejecutando = "none"
                        gameOpen = False
            
            pygame.display.flip()

        while ejecutando == "juego":

            reloj.tick(FPS)

            ventana.fill((52, 191, 145))

            #musica
            if soundSet == False:
                fxMusic     = sndLoad("sounds\music.mp3")
                soundSet = True

            #Variables del grid
            gridPosX = 22 #Posicion X de creación del grid
            gridPosY = 22 #Posicion Y de creación del grid
            gridInter = 4 #Espacio entre cada cuadrado
            tamCuadrado = 40 #Tamaño de los cuadrados

            if gameMusic == False:
                fxMusic = pygame.mixer.music.play(-1)
                gameMusic = True

            

            #Dibujado de cuadricula
            for i in range(len(mainGrid)):
                for j in range(len(mainGrid[0])):
                    #definir color
                    if mainGrid[i][j] == 1:
                        color = clrObstaculo
                        sprite = sprObstaculo
                    else:
                        if mainGrid[i][j] == 0:
                            color = clrLibre
                            sprite = sprEspacio
                        else:
                            if mainGrid[i][j] == 2:
                                color = clrPintado
                                sprite = sprPintado
                    
                    #Dibujado del espacio en la cuadricula segun color
                    #pygame.draw.rect(ventana, color, pygame.Rect(gridPosX, gridPosY, tamCuadrado, tamCuadrado))
                    sprite = pygame.transform.scale(sprite, (tamCuadrado, tamCuadrado))
                    ventana.blit(sprite, (gridPosX, gridPosY, tamCuadrado, tamCuadrado))
                    gridPosX += (tamCuadrado + gridInter)
                gridPosX -= (tamCuadrado + gridInter)*len(mainGrid[0])
                gridPosY += (tamCuadrado + gridInter)
            gridPosY -= (tamCuadrado + gridInter)*len(mainGrid) 

            #Posición en pixeles del jugador
            playerPosX= gridPosX + playerGridX * (tamCuadrado + gridInter)
            playerPosY= gridPosY + playerGridY * (tamCuadrado + gridInter)
            #Dibujar jugador en pantalla
            playerDraw = pygame.transform.scale(playerDraw, (tamCuadrado, tamCuadrado))
            ventana.blit(playerDraw, (playerPosX,playerPosY-8,tamCuadrado, tamCuadrado))

            #pygame.draw.rect(ventana, clrPlayer, pygame.Rect(playerPosX + 2,playerPosY + 2,tamCuadrado -4, tamCuadrado - 4)) #Dibujado de jugador (sin sprite)

            for i in range(len(enemigos)):
                #Posición en pixeles del enemigo
                enemyPosX= gridPosX + enemigos[i][1] * (tamCuadrado + gridInter)
                enemyPosY= gridPosY + enemigos[i][0] * (tamCuadrado + gridInter)
                #Dibujar enemigo en pantalla
                if i % 2 == 0:
                    enemyDraw = sprEnemy1
                else:
                    enemyDraw = sprEnemy2
                
                #pygame.draw.rect(ventana, clrEnemy, pygame.Rect(enemyPosX + 2,enemyPosY + 2,tamCuadrado -4, tamCuadrado - 4)) #Dibujado de enemigo (sin sprite)
                enemyDraw = pygame.transform.scale(enemyDraw, (tamCuadrado, tamCuadrado))
                ventana.blit(enemyDraw, (enemyPosX,enemyPosY-8,tamCuadrado, tamCuadrado))
            


            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    ejecutando = "none"
                    gameOpen = False

                if (event.type == pygame.KEYDOWN):
                    tecla_presionada =  pygame.key.name(event.key)
                    
                    '''
                    if tecla_presionada == "t":
                        win = True
                        ejecutando = "resultado"
                        soundSet = False
                    '''

                    if tecla_presionada == "escape":
                        pause = not(pause)
                        print("pausa:",pause)
                    
                    if tecla_presionada == "w":
                        if pause == False:
                            if (playerGridY -1) >= 0:
                                if mainGrid[playerGridY - 1][playerGridX] != 1:
                                    #pintar
                                    if mainGrid[playerGridY - 1][playerGridX] == 0:
                                        mainGrid[playerGridY - 1][playerGridX] = 2
                                        pintado += 1
                                    else:
                                        mainGrid[playerGridY - 1][playerGridX] = 0
                                        pintado -= 1
                                    playerGridY -=1

                                    playerDraw = sprPlayerUp #Definir sprite arriba
                                    print("🡩")
                                    enemigos = randomMove(enemigos,mainGrid)
                        
                    if tecla_presionada == "a":
                        if pause == False:
                            if (playerGridX -1) >= 0:
                                if mainGrid[playerGridY][playerGridX -1] != 1:
                                    if mainGrid[playerGridY][playerGridX -1] == 0:
                                        mainGrid[playerGridY][playerGridX -1] = 2
                                        pintado += 1
                                    else:
                                        mainGrid[playerGridY][playerGridX -1] = 0
                                        pintado -= 1
                                    playerGridX -=1

                                    playerDraw = sprPlayerLeft #Definir sprite izquierda
                                    print("🡠")
                                    enemigos = randomMove(enemigos,mainGrid)

                    if tecla_presionada == "s":
                        if pause == False:
                            if (playerGridY +1) <= len(mainGrid)-1:
                                if mainGrid[playerGridY + 1][playerGridX] != 1:
                                    if mainGrid[playerGridY + 1][playerGridX] == 0:
                                        mainGrid[playerGridY + 1][playerGridX] = 2
                                        pintado += 1
                                    else:
                                        mainGrid[playerGridY + 1][playerGridX] = 0
                                        pintado -= 1
                                    playerGridY +=1

                                    playerDraw = sprPlayerDown #Definir sprite abajo
                                    print("🡣")
                                    enemigos = randomMove(enemigos,mainGrid)

                    if tecla_presionada == "d":
                        if pause == False:
                            if (playerGridX +1) <= len(mainGrid[0])-1:
                                if mainGrid[playerGridY][playerGridX + 1] != 1:
                                    if mainGrid[playerGridY][playerGridX + 1] == 0:
                                        mainGrid[playerGridY][playerGridX + 1] = 2
                                        pintado += 1
                                    else:
                                        mainGrid[playerGridY][playerGridX + 1] = 0
                                        pintado -= 1
                                    playerGridX +=1

                                    playerDraw = sprPlayerRight #Definir sprite derecha
                                    print("🡢")
                                    enemigos = randomMove(enemigos,mainGrid)

                    print("pintado:",pintado)

                    (playerGridY,playerGridX,vidas) = compruebaPos(enemigos, playerGridY, playerGridX, vidas) #regresar a 0,0 y perder una vida al chocar con enemigo
            
            #Calcular puntaje
            if pause == False:
                (contador,segundos) = contadorSeg(contador, segundos, FPS)
                puntaje = (pintado*1000)//(segundos+1)

            pygame.draw.rect(ventana, (0,0,0), pygame.Rect(480,0,160,480)) #Dibujado panel con estadisticas

            textoPuntaje = font.render('score', False, (255,255,255))
            ventana.blit(textoPuntaje,(486,22))

            drawPuntaje = font.render(str(puntaje), False, (255,255,255))
            ventana.blit(drawPuntaje,(486,55))

            #mostrar vidas
            vidasX = 486
            vidasY = 150
            for i in range(vidaTotal):
                if i+1 <= vidas:
                    drawVidas = sprVidaLlena
                else:
                    drawVidas = sprVidaVacia
                drawVidas = pygame.transform.scale(drawVidas, (52, 48))
                ventana.blit(drawVidas,(vidasX,vidasY))
                vidasX += 48
            
            panelEnemyX = 495
            panelEnemyY = 220
            for j in range(2):
                if j%2 == 0:
                    drawPanelEnemy = sprEnemy1
                else:
                    drawPanelEnemy = sprEnemy2
                drawPanelEnemy = pygame.transform.scale(drawPanelEnemy, (64, 64))
                ventana.blit(drawPanelEnemy,(panelEnemyX,panelEnemyY))
                panelEnemyX += 64
            
            #Calcular  y mostrar porcentaje de completado
            porcentaje = int((pintado/espaciosLibres)*100)

            drawPorcentaje = font.render(str(porcentaje)+"%", False, (255,255,255))
            ventana.blit(drawPorcentaje,(516,300))

            #mostrar boton pausa
            drawPause = sprPause
            drawPause = pygame.transform.scale(sprPause, (160, 96))
            ventana.blit(drawPause,(480,384))


            #Indicar pausa al estar activo
            if pause == True:
                sprPauseText = pygame.transform.scale(sprPauseText, (162, 44))
                ventana.blit(sprPauseText,(159,218))

            if porcentaje == 100:
                win = True
            
            if (porcentaje == 100) or (vidas == 0):
                if fxDelay == 0:
                    ejecutando = "resultado"
                    soundSet = False
                else:
                    fxDelay -= 1
                



            '''
            textoVidas = font.render('vidas '+ str(vidas), False, (255,255,255))
            ventana.blit(textoVidas,(500,66))

            textoPuntaje = font.render('score '+ str(puntaje), False, (255,255,255))
            ventana.blit(textoPuntaje,(500,88))
            '''
            

            pygame.display.flip()

        while ejecutando == "resultado":
            reloj.tick(FPS)
            #mostrar transicion "fx"
            if soundSet == False:
                if win == True:
                    fxResult = sndLoad("sounds\win.mp3")
                    soundSet = True

                else: 
                    fxResult = sndLoad("sounds\lose.mp3")
                    soundSet = True

            if fxPlay == True:
                pygame.draw.rect(ventana, fxColor, pygame.Rect(0,0, fxAncho,fxAlto)) #Dibujado de efecto
                if fxAlto < ALTO_VENTANA:
                    fxAlto += fxSpeed
                else:
                    fxPlay = False
                    print ("listo!")
            else:
                ventana.fill((0,0,0))
                #Sonidos
                if musicPlaying == False:
                    fxResult = pygame.mixer.music.play(0)
                    musicPlaying = True
                #imagen con sonido
                if (resSegundos > 1):
                    if win == False:
                        sprKorboLose = pygame.transform.scale(sprKorboLose,(348,252))
                        ventana.blit(sprKorboLose,(250,30))
                    else:
                        sprKorboWin = pygame.transform.scale(sprKorboWin,(348,252))
                        ventana.blit(sprKorboWin,(250,30))
                    
                else:
                    (resContador,resSegundos) = contadorSeg(resContador,resSegundos,FPS)

                #mostrar puntaje
                textoPuntaje = font.render('score', False, (255,255,255))
                ventana.blit(textoPuntaje,(32, 50))

                drawScore = font.render(str(puntaje), False, (255,255,255))
                drawScore = ventana.blit(drawScore,(32, 100))

                #mostrar vidas
                vidasX = 32
                vidasY = 150
                for i in range(vidaTotal):
                    if i+1 <= vidas:
                        drawVidas = sprVidaLlena
                    else:
                        drawVidas = sprVidaVacia
                    drawVidas = pygame.transform.scale(drawVidas, (52, 48))
                    ventana.blit(drawVidas,(vidasX,vidasY))
                    vidasX += 48
                
                #mostrar tiempo
                textoTime = font.render('time', False, (255,255,255))
                ventana.blit(textoTime,(32, 230))

                drawTime = font.render(str(segundos)+ " sec", False, (255,255,255))
                drawTime = ventana.blit(drawTime,(32, 280))

                #mostrar porcentaje
                if win == False:
                    saved = True
                    textoPorcentaje = font.render('completed', False, (255,255,255))
                    ventana.blit(textoPorcentaje,(32, 340))

                    drawPorcentaje = font.render(str(porcentaje)+"%", False, (255,255,255))
                    ventana.blit(drawPorcentaje,(32,390))
                else:
                    #mostrar nombre
                    if len(name) < 3:
                        fullTextName = "name: "+ name
                        textName = font.render(fullTextName,False, (255,255,255))
                        ventana.blit(textName,(32,390))
                    else:
                        if saved == False:
                            tablaPuntajes = compruebaPuntaje(tablaPuntajes,int(puntaje),name)
                            tablaPuntajes = listaString(tablaPuntajes)
                            filePuntajes = open(os.path.join(sys.path[0], "scores.korbo"), "w")
                            filePuntajes.write(tablaPuntajes)
                            saved = True

                        fullTextName = "saved!"
                        textName = font.render(fullTextName,False, (255,255,255))
                        ventana.blit(textName,(32,390))



            for event in pygame.event.get():
                if (event.type == pygame.QUIT):
                    ejecutando = "none"
                    gameOpen = False

                if (event.type == pygame.KEYDOWN):
                    tecla_presionada =  pygame.key.name(event.key)
                    print(tecla_presionada,win,saved,ejecutando)

                    if tecla_presionada.isalpha() and len(tecla_presionada) == 1 and (win == True) and saved == False: #Permite escribir nombre de jugador siempre que este haya ganado, la tecla presionada sea una letra, y que el nombre no haya sido previamente guardado
                        name += tecla_presionada

                    if (tecla_presionada == "return"):
                        print("enter!")
                        if saved==True:
                            pygame.mixer.music.stop()
                            ejecutando = "startup"
                            print(ejecutando)

            pygame.display.flip()


    sys.exit()

main()
