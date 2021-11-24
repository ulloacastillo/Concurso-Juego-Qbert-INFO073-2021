import cx_Freeze
import sys

cx_Freeze.setup(
	name="Qbear In The Space",
	version="0.0.1",
	options={"build_exe": {"packages": ["pygame","sys","random"],
						   "include_files":["fuente/8-bit Arcade In.ttf", "mejorespuntajes.txt","images/fondo.png",
                                                                    "images/ovni.png","images/panda.png","images/enemigo.png","images/enemigo2.png",
                                                                    "images/plataformaverde.png","images/Corazon.png","images/pausa.png","images/plataforma.png",
                                                                    "images/ranking.png","images/victoria.png","images/game_over.png","images/intrucciones.png",
                                                                    "images/menu.png","sounds/music.mp3","sounds/menu.mp3","sounds/of.mp3","sounds/start.mp3"]}
		    },
	executables=[cx_Freeze.Executable("Qbear in the space.py")]
)
