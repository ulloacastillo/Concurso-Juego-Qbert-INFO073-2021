import cx_Freeze
import sys

cx_Freeze.setup(
	name="WALUIGI DASH!",
	version="3.1",
	options={"build_exe": {"packages": ["pygame"],
						   "include_files":["./data","./Templates", "save.ini"]}
		    },
	executables=[cx_Freeze.Executable("WALUIGI_DASH.py", icon="Logo.ico", base = "Win32GUI")]
)