import cx_Freeze
import sys

cx_Freeze.setup(
	name="Main.py",
	version="0.5.5",
	options={"build_exe": {"packages": ["pygame","os","sys","random"],
						   "include_files":["Sprites/SQ_L.png", "Sprites/Frog_L.png","Sprites/Frog_R.png","Background\MP_0.png","Background\MP_1.png",
                                                    "Background\MP_2.png","Background\MP_3.png","Background\MP_4.png","Background\MP_5.png","Background\MP_6.png",
                                                    "Background\MP_7.png","Background\MP_8.png","Background\MP_9.png","Background\MP_10.png","Background\MP_11.png",
                                                    "Background\MP_12.png","Background\MP_13.png","Background\MP_14.png","Sprites/roca.png","Sprites/RT1.png",
                                                    "Sprites/Roca punta Sangre.png","Sprites/ArañitaFinal_L.png","Sprites/ArañitaFinal_R.png","Sprites/SQ_L.png",
                                                    "Sprites/SQ_R.png","Sprites/Frog_L.png","Sprites/Frog_R.png","Sprites/Corazon_Vida.png","Sprites/Corazon_Vacio.png",
                                                    "Background/Cueva.jpg","Sprites/Titulo_Juego.png","Sprites/cabeza_araña2.png","Background\P_CARGA.png",
                                                    "Sprites\C1.png","Sprites\C2.png","Sprites\C3.png","Sprites\C4.png","Sprites\C5.png","Sprites\C6.png",
                                                    "Sprites\C7.png","Sprites\C8.png","Sprites/Feliz_L.png","Sprites/Feliz_R.png"]}
		    },
	executables=[cx_Freeze.Executable("Main.py")]
)
