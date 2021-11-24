import cx_Freeze
import sys

cx_Freeze.setup(
	name="Project Crossover",
	version="0.0.1",
	options={"build_exe": {"packages": ["pygame"],
						   "include_files":["0GG.png", "1GG.png","2GG.png","3GG.png","4GG.png","5GG.png","Agent_Backward.png","Agent_Front.png","Agent_Left.png","Agent_Right.png","control.png","controles.png","corazones.png","derrota.png","fondo.png","icono.png","Ingenier_Backward.png","Ingenier_Front.png","Ingenier_Left.png","Ingenier_Right.png","instru.png","Instrucciones.png","movimiento.mp3","muerte.mp3","Obstaculo.png","Pasto.png","personaje_Left.png","personaje_Right.png","Principal.png","puntos.png","siguiente.mp3","Tierra.png","Victoria.png","Wasted.mp3","win.mp3"]}
		    },
	executables=[cx_Freeze.Executable("Grupo10.py")]
)