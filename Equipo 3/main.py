

# Recursos externos:
    # Imagen Waluigi menu: https://www.vidaextra.com/accion/13-asistentes-super-smash-bros-ultimate-que-se-merecian-ser-luchadores-nuestras-alternativas
    # Imagen fondo juego: https://cutewallpaper.org/download.php?file=/21/waluigi-wallpaper/Waluigi-Wallpaper-free-to-use-KRMS-Illustrations-ART-.png y https://www.shutterstock.com/es/image-illustration/grass-tiles-seamless-pixel-retro-art-1580846293
    # Fondo de Wario: https://wallpapersafari.com/w/TJPYdn
    # Tipografía de ajuestes: https://cooltext.com/Logo-Design-Miami
    # Sprites waluigi: https://www.deviantart.com/igotanewaccountomg/art/The-other-Waluigi-sprite-sheet-780926409
    # Sprites enemigos: http://www.mariouniverse.com/sprites-snes-yi/ 
    # Sprites plataformas: http://vignette1.wikia.nocookie.net/mario/images/0/06/Bloque_golpeado.PNG/revision/latest?cb=20130702202645&path-prefix=es y https://es.seaicons.com/32051/
    # Sprites obstaculos: https://www.spriters-resource.com/custom_edited/mariocustoms/sheet/36889/
    # Sprite Wario: http://www.mariouniverse.com/sprites-gba-wl4/ 
    # Imagen settings: https://www.wallpapertip.com/es/TJmbTR/
    # Musica de fondo (menu): https://www.youtube.com/watch?v=KM7sP5ctfJY 
    # Musica in game: https://www.youtube.com/watch?v=IaFbTEJxmTQ
    # PNG moneda: https://www.pngfind.com/mpng/bomhbm_mario-coin-png-mario-coin-pixel-art-transparent/
    # Fondo tras puntaje (ingame): https://pngtree.com/freebackground/purple-gradient-geometric-flat-business-card-background_1089985.html
    # Musica de victoria: https://www.youtube.com/watch?v=-Zl_TIv7drg
    # Musica de derrota versión editada por nosotros.
    # Efectos de sonido: Wii - Mario Kart Wii - Waluigi Sound
    # Todos los personajes exepto Skid y Pump pertenecen a Nintendo.
    # Skid y Pump pertenece a "Sr Pelo": https://www.youtube.com/watch?v=PmzwhVE5Ly4
    # Las demás imágenes fueron creadas por nosotros.

# Recursos
import pygame as pg
from sys import exit
import GAME as gm
import time
import main_ as mn


# Titulo y versión
version_title = "Waluigi DASH!"
pg.display.set_caption(version_title)  
logo = pg.image.load("Templates/Logo.png")
pg.display.set_icon(logo)                   
                                
# Genera los cambios de botones en el menú principal
def images(opt,window_res, modo):
    if modo == True:
        if opt == 0:
            menuBackground = pg.image.load("data/mventana/waMenu1.jpg").convert()
        if opt == 1:
            menuBackground = pg.image.load("data/mventana/waMenu2.jpg").convert()
        if opt == 2:
            menuBackground = pg.image.load("data/mventana/waMenu3.jpg").convert()
        if opt == 3:
            menuBackground = pg.image.load("data/mventana/waMenu4.jpg").convert()
    else:
        if opt == 0:
            menuBackground = pg.image.load("data/mfullscreen/waMenu1.jpg").convert()
        if opt == 1:
            menuBackground = pg.image.load("data/mfullscreen/waMenu2.jpg").convert()
        if opt == 2:
            menuBackground = pg.image.load("data/mfullscreen/waMenu3.jpg").convert()
        if opt == 3:
            menuBackground = pg.image.load("data/mfullscreen/waMenu4.jpg").convert()
    if opt == 10:
        menuBackground = pg.image.load("data/waSettings.png").convert()

    window_res.blit(menuBackground, [0,0])
    return modo

# Coloca cualquier canción y ajusta los volumenes
def musica(pista):
    igm = pg.mixer.music
    if pista == "menu":
        igm.load("data/bgmenumusic.mp3")
        igm.set_volume(1)
        igm.play(-1)
    if pista == "igm":
        igm.load("data/igm.mp3")
        igm.set_volume(0.3)
    igm.play(-1)

# Carga texturas
def num_sprites(m):
    if m == 1:
        number = pg.image.load("data/num/1.png")
    if m == 2:
        number = pg.image.load("data/num/2.png")
    if m == 3:
        number = pg.image.load("data/num/3.png")
    if m == 4:
        number = pg.image.load("data/num/4.png")
    if m == 5:
        number = pg.image.load("data/num/5.png")
    if m == 6:
        number = pg.image.load("data/num/6.png")
    if m == 7:
        number = pg.image.load("data/num/7.png")
    if m == 8:
        number = pg.image.load("data/num/8.png")
    if m == 9:
        number = pg.image.load("data/num/9.png")
    if m == 11:
        number = pg.image.load("data/num/si.png")
    if m == 12:
        number = pg.image.load("data/num/no.png")
    
    return number

# Controla las selecciones del menu de opciones
def opciones(opc,sel,window_res):
    pg.font.init()
    coin = pg.image.load("data/coin2.png")
    coin.set_colorkey((0,255,0))
    cords = [30,120]

    if opc == 1:
        cords = [30,200]
    if opc == 2:
        cords = [30,290]
    if opc == 3:
        cords = [400,420]
    if opc == 4:
        cords = [400,490]
    
    c = 0

    images(10,window_res,None)
    for num in sel:
        m = num_sprites(num)
        
        if c == 0:
            window_res.blit(m,[530,130])
        if c == 1:
            window_res.blit(m,[400,210])
        if c == 2:
            if num == 11:        
                window_res.blit(m,[415,290])
            else:
                window_res.blit(m,[410,290])       
        c += 1

    window_res.blit(coin,cords)

# Rota las selecciones para el menu de ajustes
def rotar_selecciones(sel):
    for i in range(2):
        if sel[i] < 1:
            sel[i] = 9
        if sel[i] > 9:
            sel[i] = 1
    if sel[2] == 13:
        sel[2] = 11
    if sel[2] == 10:
        sel[2] = 12
    
    return sel

# Inicia el menu de opciones para arrancar el juego #
def init(window_res,accept):

    def max_puntaje():
        fuente = pg.font.Font(None, 120)
        text = str(puntaje)
        mensaje = fuente.render(text, 0, (166, 66, 255))
        window_res.blit(mensaje, (830, 310))
        pg.display.flip()

    def option():
        opciones(opc,sel,window_res)

    mn.genericfade(window_res,"out","opt")
    puntaux = open("save.ini","r")
    puntaje = int(puntaux.read())
    puntaux.close()

    enemigos = 3
    vidas = 3
    wario = False
    sel = [3,3,12]
    opc = 0
    option()
    end = False
    handicap = (enemigos + 1) / vidas
    mn.multiplicador(handicap, window_res)
    max_puntaje()

    while not end:
            
        for event in pg.event.get():

            if event.type == pg.QUIT:
                exit()
            
            if event.type == pg.KEYDOWN:
                key = pg.key.name(event.key)

                if key in ["escape","backspace"]:
                    return

                if key == "w" and opc > -1:
                    opc -=1
                    if opc == -1:
                        opc = 4
                    
                if key == "s" and opc < 5:
                    opc += 1
                    if opc == 5:
                        opc = 0

                if opc == 0:
                    if key == "d":
                        sel[0] += 1                   
                    if key == "a":
                        sel[0] -= 1                   
                if opc == 1:
                    if key == "d":
                        sel[1] += 1                   
                    if key == "a":
                        sel[1] -= 1                    
                if opc == 2:
                    if key == "d":
                        sel[2] += 1                      
                    if key == "a":
                        sel[2] -= 1

                sel = rotar_selecciones(sel)
                enemigos = sel[0]
                vidas = sel[1]    
                handicap = (enemigos + 1) / vidas
                mn.multiplicador(handicap, window_res)
            
                if key in accept:
                    if opc == 3:
                        musica("igm")
                        time.sleep(1)
                        enemigos = sel[0]
                        vidas = sel[1]
                        if sel[2] == 11:
                            wario = True
                        else:
                            wario = False

                        opcion,puntaje = gm.GAME(window_res,enemigos,vidas,wario)
                        Running = mn.pantallavd(window_res,opcion,puntaje)

                        if Running == False:
                            musica("menu")                            
                        if Running == True:
                            return
                    if opc == 4:
                        return
                
                option()
        max_puntaje()
        mn.multiplicador(handicap, window_res)
    print("iniciado")

# Arranque principal del juego, inicia el menu.
def menu():
    Running = True
    musica("menu")
    time.sleep(2)
    window_res = pg.display.set_mode((1280,720))
    opt = 0
    modo = True
    images(opt,window_res,modo)
    frame = 0
    frame = mn.spookydance(frame,window_res)
    accept = ["e","return","space"]
    while Running:
        

        for event in pg.event.get():

                if event.type == pg.QUIT:
                    Running = False
                
                if event.type == pg.KEYDOWN:
                    key = pg.key.name(event.key)  

                    if key == "s":
                        if opt < 4:
                            opt += 1
                        if opt == 4:
                            opt = 0
                    
                    if key == "w":
                        if opt > -1:
                            opt -= 1
                        if opt == -1:
                            opt = 3

                    if key in ["escape","backspace"]:
                        opt = 2

                    if key in accept:
                        if opt == 0:
                            mn.genericfade(window_res,"in","opt")        
                            init(window_res,accept)
                        if opt == 1:
                            mn.genericfade(window_res,"in","inst")
                            mn.instrucciones(window_res)
                        if opt == 2:
                            Running = False
                        if opt == 3:
                            if modo == False:
                                modo = True
                            else:
                                modo = False
                            pg.display.toggle_fullscreen()
                    images(opt,window_res,modo)   
                    frame = mn.spookydance(frame,window_res)
    pg.display.flip()

# Orden de arranque #
pg.mixer.init()
pg.font.init()
mn.loadscreen()
pg.time.delay(100)
menu()
