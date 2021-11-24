
###############################################################################
#
# En esta ventana se programan las transiciones, de modo que al ejecutarlo se abre todo el juego
# Version 1.1 ->
#   - Imágenes en tablero
#   - Sonido
#   - Transiciones
#
# **Todos los archivos se cargan al importar pantallas y tablero**
#
###############################################################################



import pygame

import pantallas
import tablero


##############################################################################

# Inicializacion de pygame y el mixer

pygame.init()
pygame.mixer.init()


pygame.display.set_caption("Soy Qbertito 1.1")

icono = pygame.image.load("imagenes/qbertito.png")
pygame.display.set_icon(icono)


pantalla = pygame.display.set_mode((650*5//3, 650)) # Pantalla principal
clock = pygame.time.Clock() 


# Juego

def qbertito(pantalla, clock):
    
    # Contiene cada transicion de pantalla según lo planeado
    # Mejores puntajes solo se mantiene mientras el juego esté abierto
    
    pantalla_actual = "menu_principal"  # Pantalla a mostrar
    puntaje = 0 
    mejores_puntajes = [0, 0, 0]
    
    while True:
        if pantalla_actual == "menu_principal":
            pantalla_actual = pantallas.menu_principal(pantalla, clock)
    
        
        elif pantalla_actual == "instrucciones":
            pantalla_actual = pantallas.instrucciones(pantalla, clock)
            
            pygame.mixer.stop()
            
        
        elif pantalla_actual == "historia":
            pantalla_actual = pantallas.historia(pantalla, clock)
            
            pygame.mixer.stop()
            
        
        elif pantalla_actual == "tablero":
            pantalla_actual, puntaje = tablero.main(pantalla, clock)
            
            # Actualizacion de mejores puntajes
            
            mejores_puntajes.append(puntaje)
            mejores_puntajes.sort(reverse=True)
            mejores_puntajes.pop()
            
            pygame.mixer.stop() 
            
            
        elif pantalla_actual == "victoria":
            pantalla_actual = pantallas.victoria(pantalla, clock, puntaje)
            pantallas.mejores_puntajes(pantalla, clock, puntaje, mejores_puntajes)
            
            pygame.mixer.stop()
            
            
        elif pantalla_actual == "derrota":
            pantalla_actual = pantallas.derrota(pantalla, clock)
            
            pygame.mixer.stop()
            
# Ejecución del juego
# Si hay algún error, se cierra pygame y se evita el cierre manual de la ventana         

try:
    qbertito(pantalla, clock)
    
finally:
    pygame.quit()
    

