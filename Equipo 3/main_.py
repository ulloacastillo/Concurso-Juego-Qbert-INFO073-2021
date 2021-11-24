# Main 2.6

# Modulos externos #
import pygame as pg
import random as rd
from sys import exit

# Dibujar mapa y cubo #
def map_regen(window_res):
    suelo1 = pg.image.load("data/Sprites/suelo1.png").convert()
    suelo1.set_colorkey((0,0,255))
    for w in range(10):
        k = 70 * w
        for i in range(10):
            f = 70 * i
            window_res.blit(suelo1, [80 + k, 20 + f])

# Dibuja la posición del jugador, recarga el mapa #
def player_pos(x_scr, y_scr, window_res, dir):
    
    if dir == "arr":
        sprite = pg.image.load("data/Sprites/wua4.png").convert()
    if dir == "abj":
        sprite = pg.image.load("data/Sprites/wua1.png").convert()
    if dir == "izq":
        sprite = pg.image.load("data/Sprites/wua3.png").convert()
    if dir == "der":
        sprite = pg.image.load("data/Sprites/wua2.png").convert()
    sprite.set_colorkey((0,0,0))
    window_res.blit(sprite,[x_scr + 11, y_scr + 1]) 
    pg.display.flip() 


# Pinta los cuadros donde esté el jugador, si ya estaba pintado, lo limpia
# Mantiene los cuadros anteriores.
def pintar(x_cord, y_cord, x_scr, y_scr, window_res, tab, state):
    suelo1 = pg.image.load("data/Sprites/suelo1.png").convert()
    suelo2 = pg.image.load("data/Sprites/suelo2.png").convert()
    suelo1.set_colorkey((0,0,255))
    suelo2.set_colorkey((0,0,255))
    if state == "current":
        if tab[y_cord-1][x_cord-1] == 0:
            tab[y_cord-1][x_cord-1] = 1
            window_res.blit(suelo2, [x_scr, y_scr])
        elif tab[y_cord-1][x_cord-1] == 1:
            tab[y_cord-1][x_cord-1] = 0
            window_res.blit(suelo1, [x_scr, y_scr])
    if state == "last":
        if tab[y_cord-1][x_cord-1] == 1:
            window_res.blit(suelo2, [x_scr, y_scr])
        elif tab[y_cord-1][x_cord-1] == 0:
            window_res.blit(suelo1, [x_scr, y_scr])
    suelo1.set_colorkey((0,0,255))
    suelo2.set_colorkey((0,0,255))
    pg.display.flip()

# Genera una lista de listas para las funciones de pintar y obstaculos #
def tab_gen(lim_x, lim_y):
    tab = []
    for y in range(lim_y):
        tab.append([])
        for x in range(lim_x):
            tab[y].append(0)
    return tab

# Revisa si se pintaront todos los cuadros necesarios para ganar.
def end(tablero):
    p = 0
    for j in range(10):
        for k in tablero[j]:
            p += k
    if p == 106:
        return False, True
    else:
        return True, None

# Genera obstaculos en una matriz 2 x 2
def obsc(max,tab):

    is_val = False
    while not is_val:
        generados = []
        for repeticiones in range(max):
            gen = 0
            tab2 = tab_gen(2,2)
            pos_x, pos_y = valida("obs",generados)
            while gen < max - repeticiones:
                x, y = rd.randint(0,1), rd.randint(0,1)
                tab2[y][x] = 1
                gen = 0
                tab[y+pos_y][x+pos_x] = 2
                for w in range(len(tab2)):
                    for z in tab2[w]:
                        gen += tab2[w][z]       
            generados.append([pos_x, pos_y])
        print("checking chunks: ", generados)
        is_val = valida("dif2", generados)
    print(generados,"is valid, looking for overlap.")

# Calcula el puntaje #
def puntos(tab, x_cord, y_cord, puntaje, handicap):
    if tab[y_cord - 1][x_cord - 1] == 1:
        puntaje += 50 * handicap
    if tab[y_cord - 1][x_cord - 1] == 0:
        puntaje -= ( 50 * handicap + 25)
    if puntaje < 0:
        puntaje = 0
    return puntaje


# Valida las entradas de la función obsc
def valida(cosa, generados):

    if cosa == "obs":

        x_pos, y_pos = 0 , 0
        if max == 1:
            while x_pos == 0 and y_pos == 0:
                x_pos = rd.randint(0,8)
                y_pos = rd.randint(0,8)
            return x_pos, y_pos

        else:
            while (x_pos == 0 or x_pos == 8) and (y_pos == 0 or y_pos == 8):
                x_pos = rd.randint(0,8)
                y_pos = rd.randint(0,8)
            return x_pos, y_pos
    
    if cosa == "dif2": # Valida que la diferencia en X de los obstaculos sea > 2
        v2 = 0
        for j in range(len(generados)):
            for i in range(len(generados)):
                vd = abs(generados[i][0] - generados[j][0])
                vd2= abs(generados[i][1] - generados[j][1])
                if vd > 2 or vd2 > 2: 
                    v2 += 1
        if v2 > 5:
            return True
        else:
            return False

# Dibuja los obstaculos en pantalla.        
def draw_obs(tab, window_res):
    block = pg.image.load("data/Sprites/block.png").convert()
    block.set_colorkey((0,0,0))

    for x in range(len(tab)):
        w=0
        for y in tab[x]:
            w += 1
            if y == 2:
                k = 69 * (w-1)
                f = 67 * x
                window_res.blit(block, [78 + k, 23 + f])

# Suma todos los valores de una matriz.
def sum(tablero):
    p = 0
    for j in range(len(tablero)):
        for k in tablero[j]:
            p += k
    return p

# Mueve un enemigo y valida su salida
def enemy_mov(x1, y1, tab, pos_ene):

    valid = False
    while not valid:
        
        x, y = x1, y1
        dir, mov = rd.randrange(2), rd.randrange(2)
        valid = True

        if dir == 1:
            if mov == 1:
                x += 1
            else:
                x -= 1
        else:
            if mov == 1:
                y += 1
            else:
                y -= 1
                
        if (x > 9) or (y > 9) or (x < 0) or (y < 0):
            valid = False
        else: 
            if tab[y][x] == 2:
                valid = False
            for h in pos_ene:
                if h == [x,y]:
                    valid = False
        if x == 0 and y == 0:
            valid = False

    return x, y

# Genera a los enemigos
def enemigos(cantidad, tabla):
    pos_ene = []

    for i in range (cantidad):
        f = True
        
        while f:
            f = False

            x = rd.randint(2,9)
            y = rd.randint(2,9)

            if tabla[y][x] == 2:
                f =True
            for h in pos_ene:
                if h == [x,y]:
                    f = True

        pos_ene.append([x,y])
    
    return pos_ene

# Controla las vidas
def perder_vida(vidas):
    vidas -= 1
    x_scr, y_scr =  80 , 20
    x_cord, y_cord = 1 , 1

    return vidas, x_scr, y_scr, x_cord, y_cord

# Pinta las vidas
def pintar_vidas(vidas, window_res, color, wario):
    fuente = pg.font.SysFont("Fixedsys", 100)
    if color == "actual":
        text = str(int(vidas))
        coloreo = fuente.render(text, 0, (255, 255, 0))
        window_res.blit(coloreo, (1090,120))
        text = "="
        coloreo = fuente.render(text, 0, (255, 255, 0))
        window_res.blit(coloreo, (1040,115))   
    if not wario:          
        if color == "anterior":
            text = str(int(vidas))
            coloreo = fuente.render(text, 0, (75, 21, 132))
            window_res.blit(coloreo, (1090,120))
    if wario:
         if color == "anterior":
            text = str(int(vidas))
            coloreo = fuente.render(text, 0, (122, 34, 112))
            window_res.blit(coloreo, (1090,120))       


# Redibuja los cuadros tras los enemigos
def pintar_enemigos(x_enemigo, y_enemigo, window_res, pos_ene_x, pos_ene_y, tablero):
    enemigo = pg.image.load("data/Sprites/en1.png").convert()
    suelo1 = pg.image.load("data/Sprites/suelo1.png").convert()
    suelo2 = pg.image.load("data/Sprites/suelo2.png").convert()
    enemigo.set_colorkey((0,0,0))
    suelo1.set_colorkey((0,0,255))
    suelo2.set_colorkey((0,0,255))

    if tablero[pos_ene_y][pos_ene_x] == 0:
        window_res.blit(suelo1, [pos_ene_x * 70 + 80, pos_ene_y * 70 + 20])
    if tablero[pos_ene_y][pos_ene_x] == 1:
        window_res.blit(suelo2, [pos_ene_x * 70 + 80, pos_ene_y * 70 + 20])
    
    window_res.blit(enemigo, [x_enemigo * 70 + 80 , y_enemigo * 70 + 20 ])

# Calcula la posicion de todos los enemigos y los dibuja.
def inpos(pos_ene,window_res):
    for k in range (len(pos_ene)):
        enemigo = pg.image.load("data/Sprites/en1.png").convert()
        enemigo.set_colorkey((0,0,0))
        x_enemigo = pos_ene[k][0]
        y_enemigo = pos_ene[k][1]
        window_res.blit(enemigo, [x_enemigo * 70 + 80 , y_enemigo * 70 + 20 ])
    return x_enemigo, y_enemigo

# Genera Pantalla de Victoria y Derrota
def imagespvd(opts,background,window_res,x):
    if x == True:
        if opts == 0:
            background = pg.image.load("data/pvd/v1.png").convert()
        if opts == 1:
            background = pg.image.load("data/pvd/v2.png").convert()
        if opts == 2:
            background = pg.image.load("data/pvd/v3.png").convert()
    else:
        if opts == 0:
            background = pg.image.load("data/pvd/d1.png").convert()
        if opts == 1:
            background = pg.image.load("data/pvd/d2.png").convert()
        if opts == 2:
            background = pg.image.load("data/pvd/d3.png").convert()


    window_res.blit(background, [0,0])    
    pg.display.flip()  

# Genera Pantalla de Victoria y Derrota
def pantallavd(window_res,x, puntaje):
    pg.font.init()
    def dibujar_puntajevd():
        if x == True:
            window_res.blit(mensaje, (595, 238))
        else:
            window_res.blit(mensaje, (985, 250))
        pg.display.flip()

    if x == True:
        background = pg.image.load("data/pvd/v1.png").convert()
        sound("win")
    else:
        background = pg.image.load("data/pvd/d1.png").convert()
        sound("gameover")
    Running = True
    opts = 0
    imagespvd(opts,background,window_res,x)

    
    while Running:
        for event in pg.event.get():
            
            fuente = pg.font.Font(None, 120)
            text = str(puntaje)
            mensaje = fuente.render(text, 0, (255, 255, 255))
            if x == True:
                window_res.blit(mensaje, (595, 238))
            else:
                window_res.blit(mensaje, (985, 250))
            dibujar_puntajevd()


            if event.type == pg.QUIT:  # Exit button
                exit()
            
            if event.type == pg.KEYDOWN:
                key = pg.key.name(event.key)  # If key is pressed then: 

                if key == "s":
                    if opts < 3:
                        opts += 1
                        if opts == 3:
                            opts = 0
                
                if key == "w":
                    if opts > -1:
                        opts -= 1
                        if opts == -1:
                            opts = 2

                if key in ["backspace","escape"]:
                    opts = 2

                if key in ["e","space","return"]:
                    if opts == 0:
                        sound("reintentar")
                        return False
                    if opts == 1:
                        return True
                    if opts == 2:
                        exit()

                imagespvd(opts,background,window_res,x)
                dibujar_puntajevd()

# Agrega efectos de sonido
def sound(sonido):
    igm = pg.mixer.music
    igs = pg.mixer.Sound
    if sonido == "win":
        win1 = ("data/sound/win/win (1).wav")
        win2 = ("data/sound/win/win (2).wav")
        soundwin = [win1, win2]
        igs(rd.choice(soundwin)).play()
        igm.load("data/sound/win/winmusic.mp3")
        igm.set_volume(-3)
        igm.play(-1)
    if sonido == "gameover":
        igs("data/sound/gameover/gameover.mp3").play()
        igm.load("data/sound/gameover/pd.mp3")
        igm.set_volume(1)
        igm.play(-1)
    if sonido == "reintentar":
        igs("data/sound/reintentar.mp3").play()
    if sonido == "daño":
        dmg1 = ("data/sound/dmg/dmg (1).wav")
        dmg2 = ("data/sound/dmg/dmg (2).wav")
        dmg3 = ("data/sound/dmg/dmg (3).wav")
        sounddmg = [dmg1, dmg2, dmg3]
        igs(rd.choice(sounddmg)).play()
    if sonido == "wario":
        igs("data/sound/wario.mp3").play()


# Genera Pantalla de Instrucciones 
def instrucciones(window_res):
    genericfade(window_res,"out","inst")
    Running = True
    accept = ["e","return","space"]
    opt = 0
    background = pg.image.load("data/Instrucciones/waInstrucciones.png").convert()
    window_res.blit(background, [0,0])    
    instructionframes(opt,window_res) 
    while Running:
        for event in pg.event.get():
                if event.type == pg.QUIT:
                    exit()
                if event.type == pg.KEYDOWN:
                    key = pg.key.name(event.key)
                    if key in accept:      
                        return True

                    if key == "a":
                        background = pg.image.load("data/Instrucciones/waInstruccionesA.png").convert()
                    if key == "w":
                        background = pg.image.load("data/Instrucciones/waInstruccionesW.png").convert()
                    if key == "s":
                        background = pg.image.load("data/Instrucciones/waInstruccionesS.png").convert()  
                    if key == "d":
                        background = pg.image.load("data/Instrucciones/waInstruccionesD.png").convert()

                    if key == "left":
                        opt -= 1
                    if key == "right":
                        opt += 1
                    if opt == -1:
                        opt = 6
                    if opt == 7:
                        opt = 0
                    
                    window_res.blit(background, [0,0])  
                    instructionframes(opt,window_res)  
                    pg.display.flip()
                    pg.time.delay(50)
        background = pg.image.load("data/Instrucciones/waInstrucciones.png").convert()
        window_res.blit(background, [0,0])    
        instructionframes(opt,window_res)

# Dibuja en pantalla el multiplicador de puntos
def multiplicador(handicap, window_res):
    fuen = pg.font.SysFont("Fixedsys", 100)
    text = str("{:.2f}".format(handicap))
    coloreo = fuen.render(text, 0, (166, 66, 255))
    window_res.blit(coloreo, (850,185))    
    pg.display.flip()

# Dibuja a wario y borra sus pisadas
def pintar_wario(x_wario, y_wario, window_res, war_x, war_y, tablero):
    wario = pg.image.load("data/Sprites/war4.png").convert()
    suelo1 = pg.image.load("data/Sprites/suelo1.png").convert()
    suelo2 = pg.image.load("data/Sprites/suelo2.png").convert()
    wario.set_colorkey((0,0,255))
    suelo1.set_colorkey((0,0,255))
    suelo2.set_colorkey((0,0,255))
    if tablero[war_y][war_x] == 0:
        window_res.blit(suelo1, [war_x * 70 + 80, war_y * 70 + 20])
    if tablero[war_y][war_x] == 1:
        window_res.blit(suelo2, [war_x * 70 + 80, war_y * 70 + 20])
    window_res.blit(wario, [x_wario * 70 + 90, y_wario * 70 + 20 ])

# Dibuja a Wario
def in_war(war, window_res):
    wario = pg.image.load("data/Sprites/war4.png").convert()
    wario.set_colorkey((0,0,255))
    x_wario = war[0][0]
    y_wario = war[0][1]
    window_res.blit(wario, [x_wario * 70 + 90 , y_wario * 70 + 20 ])
    return x_wario, y_wario

# Spookydance :D
def spookydance(frame,window_res):
    pg.font.init()
    if frame == 4:
        frame = 0
    if frame == -1:
        frame = 3

    if frame == 0:
        img = pg.image.load("data/sprites/spooky1.png")
    if frame == 1:
        img = pg.image.load("data/sprites/spooky2.png")
    if frame == 2:
        img = pg.image.load("data/sprites/spooky3.png")
    if frame == 3:
        img = pg.image.load("data/sprites/spooky2.png")

    frame += 1
    img.set_colorkey((56,250,48))
    window_res.blit(img,[900,500])

    pg.display.flip()
    return frame

# Dibuja el manual de instrucciones #
def instructionframes(opt,window_res):
    drawbutton = pg.image.load("data/press.png")
    if opt == 0:
        img = pg.image.load("data/instrucciones/pag1.png").convert()
    if opt == 1:
        img = pg.image.load("data/instrucciones/pag2.png").convert()
    if opt == 2:
        img = pg.image.load("data/instrucciones/pag3.png").convert()
    if opt == 3:
        img = pg.image.load("data/instrucciones/pag4.png").convert()
    if opt == 4:
        img = pg.image.load("data/instrucciones/pag5.png").convert()
    if opt == 5:
        img = pg.image.load("data/instrucciones/pag_punt.png").convert()
    if opt == 6:
        img = pg.image.load("data/instrucciones/pag6.png").convert()
    reescalar = pg.transform.scale(img,(500,620))
    reescalar.set_colorkey((0,255,0))
    window_res.blit(drawbutton,[60,400])
    window_res.blit(reescalar,[700,40])
    pg.display.flip()

# Crea la pantallla de carga
def loadscreen():

    def image():
        loadscr = pg.image.load("data/loadingscralt.png")
        scr.blit(loadscr,[0,0])
    def fade(c,scr):
        if c == 0:
            fading = pg.image.load("data/fade/fade1.png")
        if c == 1:
            fading = pg.image.load("data/fade/fade2.png")
        if c == 2:
            fading = pg.image.load("data/fade/fade3.png")
        if c == 3:
            fading = pg.image.load("data/fade/fade4.png")
        scr.blit(fading,[0,0])
        
    scr = pg.display.set_mode((1280,720))  
    pg.display.flip()      
    for x in range(4):
        image()
        fade(x,scr)
        pg.display.flip()
        pg.time.delay(1)
    image()
    pg.display.flip()

def genericfade(scr,state,go):
    if go == "inst":
        background = pg.image.load("data/fade/fakeinst.png")
    if go == "opt":
        background = pg.image.load("data/fade/fakeopt.png")
    if state == "in":
        for c in range(4):
            if c == 0:
                fading = pg.image.load("data/fade/fade4.png")
            if c == 1:
                fading = pg.image.load("data/fade/fade3.png")
            if c == 2:
                fading = pg.image.load("data/fade/fade2.png")
            if c == 3:
                fading = pg.image.load("data/fade/fade1.png")
            scr.blit(fading,[0,0])
            pg.time.delay(1)
            pg.display.flip()
    if state == "out":
        for c in range(3):
            if c == 0:
                fading = pg.image.load("data/fade/fade2.png")
            if c == 1:
                fading = pg.image.load("data/fade/fade3.png")
            if c == 2:
                fading = pg.image.load("data/fade/fade4.png")
            scr.blit(background,[0,0])
            scr.blit(fading,[0,0])
            pg.time.delay(1)
            pg.display.flip()