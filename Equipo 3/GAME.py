# Version 2.5
import pygame as pg
from sys import exit
import main_ as mn

# Resources #
def GAME(window_res,enemigos,vidas,wario):

    pg.font.init()

    # Adjusts #
    min_pts = 12 # 16, 4 (3 obstaculos, 4,2,1.),  # 12 , 3 (3 obstaculos, 3,2,1.) 
    obs_num = 3
    handicap = (enemigos + 1) / vidas
    puntaje = 0

    print("wario: ",wario)

    # Shortcuts
    def color(state):
        mn.pintar(x_cord, y_cord, x_scr, y_scr, window_res, tab, state)
    def player(dir):
        mn.player_pos(x_scr, y_scr, window_res, dir)
    def mov():
        for a in range (len(pos_ene)):
            x_enemigo, y_enemigo = mn.enemy_mov(pos_ene[a][0], pos_ene[a][1], tab, pos_ene)
            mn.pintar_enemigos(x_enemigo, y_enemigo, window_res, pos_ene[a][0], pos_ene[a][1], tab)
            pos_ene[a][0] = x_enemigo
            pos_ene[a][1] = y_enemigo
        color("current")
        player(direc)
    def mov_wario(v):
        if wario:
            while v:
                v = False
                x_wario, y_wario = mn.enemy_mov(war[0][0], war[0][1], tab, war)
                for r in pos_ene:
                    while war == r:
                        x_wario, y_wario = mn.enemy_mov(war[0][0], war[0][1], tab, war)
                mn.pintar_wario(x_wario, y_wario, window_res, war[0][0], war[0][1], tab)
                war[0][0] = x_wario
                war[0][1] = y_wario
                player(direc)
                
    def CalcPuntos(puntaje,pluspoint):
        aux = puntaje
        punt = mn.puntos(tab, x_cord, y_cord, puntaje, handicap)
        if punt > aux:
            pluspoint = True
        else:
            pluspoint = False  
        return punt, pluspoint    

    def dibuja_puntaje():
        window_res.blit(card,[850,530])
        fuente = pg.font.SysFont("Fixedsys", 120)
        text = str(int(puntaje))
        if pluspoint:
            puntospant = fuente.render(text, 0, (255, 255, 0))
        else:
            puntospant = fuente.render(text,0,(255,0,0))
        window_res.blit(puntospant, (950,580))
        pg.display.flip()


    # Sprites
    if wario == True:
        background = pg.image.load("data/background2.png").convert()
    else:
        background = pg.image.load("data/background.jpg").convert()
    suelo2 = pg.image.load("data/Sprites/suelo2.png").convert()
    heart = pg.image.load("data/Sprites/heart.png").convert()
    card = pg.image.load("data/card.jpg")
    heart.set_colorkey((0,0,0))
    suelo2.set_colorkey((0,0,255))

    # Player generation cords #
    x_scr, y_scr =  80 , 20
    x_cord, y_cord = 1 , 1

    # Startup #
    window_res.blit(background, [0,0])
    sum = 0
    while sum != min_pts:
        mn.map_regen(window_res)
        tab = mn.tab_gen(10,10)
        mn.obsc(obs_num,tab)
        sum = mn.sum(tab)
    print("Generation successful")
    window_res.blit(heart, [975, 125, 50, 50])
    mn.pintar_vidas(vidas, window_res, "actual", wario)
    Running = True
    pluspoint = True
    tab[0][0] = 1
    mn.draw_obs(tab, window_res)
    window_res.blit(suelo2, [x_scr, y_scr])
    pos_ene = mn.enemigos(enemigos,tab)
    mn.inpos(pos_ene,window_res)
    v = True
    g = True
    if wario:    
        war = mn.enemigos(1, tab)
        for i in pos_ene:
            if war == i:
                war = mn.enemigos(1, tab)
        mn.in_war(war, window_res)     
    direc = "der"
    dibuja_puntaje()
    player(direc)

    # Screen reload, moving and exit.
    while Running:

        for event in pg.event.get():

                if event.type == pg.QUIT:  # Exit button
                    exit()
                
                if event.type == pg.KEYDOWN:
                    key = pg.key.name(event.key)  # If key is pressed then: 
                    if key in ["escape","backspace"]:
                        vidas = 0
                        key = "w"
                    if key in "wasd":
                        
                        if key == "w" and y_cord > 1:
                            if tab[y_cord-2][x_cord-1] != 2:
                                color("last")
                                y_scr -= 70
                                y_cord -= 1
                                direc = "arr"
                                mov()
                                mov_wario(v)
                                puntaje, pluspoint = CalcPuntos(puntaje,pluspoint)                                
                        if key == "s" and y_cord < 10:
                            if tab[y_cord][x_cord-1] != 2:
                                color("last")
                                y_scr += 70
                                y_cord += 1
                                direc = "abj"
                                mov()
                                mov_wario(v)
                                puntaje, pluspoint = CalcPuntos(puntaje,pluspoint)
                        if key == "a" and x_cord > 1:
                            if tab[y_cord-1][x_cord-2] != 2:
                                color("last")
                                x_scr -= 70
                                x_cord -= 1
                                direc = "izq"
                                mov()
                                mov_wario(v)        
                                puntaje, pluspoint = CalcPuntos(puntaje,pluspoint)                  
                        if key == "d" and x_cord < 10:
                            if tab[y_cord-1][x_cord] != 2:
                                color("last")
                                x_scr += 70
                                x_cord += 1
                                direc = "der"
                                mov()
                                mov_wario(v)
                                puntaje, pluspoint = CalcPuntos(puntaje,pluspoint)


                        # Hace funcionar el sistema de puntos y vidas #
                        for w in range (len(pos_ene)):
                            if x_cord - 1 == pos_ene[w][0] and y_cord - 1 == pos_ene[w][1]:
                                mn.pintar_vidas(vidas, window_res, "anterior", wario)
                                vidas, x_scr, y_scr, x_cord, y_cord = mn.perder_vida(vidas)
                                mn.pintar_vidas(vidas, window_res, "actual", wario)
                                mn.sound("daño")
                                mn.pintar_enemigos(pos_ene[w][0], pos_ene[w][1], window_res, pos_ene[w][0], pos_ene[w][1], tab)
                                player("abj")
                                if tab[y_cord - 1][x_cord - 1] == 1:
                                    puntaje -= 50 * handicap
                                if tab[y_cord - 1][x_cord - 1] == 0:
                                    puntaje += (50 * handicap + 25)
                                puntaje -= 200  
                                if puntaje < 0:
                                    puntaje = 0
                                pluspoint = False

                        if wario:
                            if x_cord - 1 == war[0][0] and y_cord - 1 == war[0][1]:
                                while g:
                                    g = False
                                    puntaje += 1000
                                    v = False
                                    player(direc)
                                    mn.sound("wario")
                            
                        dibuja_puntaje()

                        Running, victory = mn.end(tab)

                        if vidas == 0:
                            Running = False
                            puntaje = int(puntaje)
                            return False, puntaje


    puntaje = int(puntaje)

    if victory:
        print("Ganaste...")
        maxpt = open("save.ini","r")
        max = int(maxpt.read())
        maxpt.close()
        if puntaje > int(max):
            maxpt = open("save.ini","w")
            maxpt.write(str(puntaje))
            maxpt.close()
        return True, puntaje