def installDepend():
	#Check if an dependency has mixin.
	from subprocess import call
	import sys
	import platform
	system_type = platform.system()
	print("Operating system is {}".format(system_type))
	depend1 = call("pip install future~=0.18.2", shell=True)
	depend2 = call("pip install pyinstaller~=5.1", shell=True)
	if ((depend1 != 0 and 1) or (depend2 != 0 and 1)):
		check = call("pip", shell=True)
		if check == 127:
			print("pip has not installed, you can try write 'sudo apt-get install python3-pip'")
		else:
			print("Unknown error.")
		sys.exit()
	try:
		from tkinter import Tk
	except:
		if system_type.lower() in "linux":
			print("Failed to import tkinter, you need to install this dependency, you can try write 'sudo apt-get install python3-tk'")
		else:
			print("Failed to import tkinter.")
		sys.exit()
