from tkinter import BooleanVar, Tk, Frame, messagebox, PhotoImage, StringVar, IntVar, Label, Entry, Button, Menu, Checkbutton, filedialog
from subprocess import call

#------------------------------------------------------CORE_INTERFACE---------------------------------------------
root=Tk()
bg=PhotoImage(file="BG.png")
Label(root, image=bg).grid(row=0, column=0, columnspan=4, rowspan=4)
barra_menu=Menu(root)
root.config(menu=barra_menu)
root.title("PyInstaller GUI v1.1")
root.attributes("-alpha", 0.9)
root.resizable(0,0)
frame=Frame(root).grid(row=0, column=0)

#-----------------------------------------------------VARIABLES---------------------------------------------------
windowed=BooleanVar()
onefile=BooleanVar()
icon=BooleanVar()
file_ico=StringVar()
file_py=StringVar()
guardado=StringVar()
guardar=False
#------------------------------------------------------IDIOMA----------------------------------------------------


try:
	file_language=open("language.txt", "r+")
	language=file_language.read()
except AttributeError:
	file_language=open("language.txt", "w+")
	file_language.write("en")
	language="en"	
except FileNotFoundError:
	file_language=open("language.txt", "w+")
	file_language.write("en")
	language="en"
file_language.close()



if language=="es":
	#Aqui se crea una tupla con 5 palabras en cada linea, y se llaman mas adelante por sus indices
	words=("Archivo", "Abrir archivo", "Salir", "Nombre del archivo:", "Ventaneado", 
	"Un archivo", "Icono", "Construir", "Seleccionar icono", "Idioma",
	"Error", "No hay archivos seleccionados", "Cambios aplicados", "Es necesario reiniciar el programa para aplicar los cambios", "Seleccione archivo",
	"Directorio de archivo a crear:", "Ubicacion del\narchivo saliente:")
elif language=="en":
	#Here a tuple is created with 5 words in each line, and they are later called by their indices
	words=("File", "Open file", "Exit", "File name:", "Windowed",
	"One file", "Icon", "Build", "Select icon", "Language",
	"Error", "No files selected", "Changes applied", "It is necessary to restart the program to apply the changes", "Select file",
	"File directory to create:", "Outgoing file\nlocation:")




def Cambiar_idioma(op):
	def Cambio_idioma():
		file_language.close()
		messagebox.showinfo(words[12], words[13])
		root.destroy()

	if op==1 and language!="es":
		file_language=open("language.txt", "w+")
		file_language.write("es")
		Cambio_idioma()


	elif op==2 and language!="en":
		file_language=open("language.txt", "w+")
		file_language.write("en")
		Cambio_idioma()


#------------------------------------------------------CORE_PROGRAM-----------------------------------------------
def Guardar_archivo():
	save_file=filedialog.askdirectory(initialdir="/", title=words[15])
	if ":" in save_file:
		guardado.set(save_file)
		guardar=True
def Abrir_archivo():
	open_file=filedialog.askopenfilename(initialdir="/", title=words[14], filetypes=(("python files", "*.py"), ("python files", "*.pyw")))
	if ".py" in open_file.get():
		file_py.set(open_file)
def Abrir_icono():
	open_icon=filedialog.askopenfilename(initialdir="/", title=words[14], filetypes=((".ico", "*.ico"), (".ico", "*.ico")))
	if ".ico" in open_icon.get():
		file_ico.set(open_icon)
def Icon():
	if icon.get():
		Button(frame, text=words[8], command=Abrir_icono).grid(row=2, column=1, padx=2.5)
		Entry(frame, textvariable=file_ico, state="readonly").grid(row=2, column=2, padx=2.5)
def Build():
	if ".py" in file_py.get():	
		ordenes="py_extencion.exe "
		if windowed.get():
			ordenes+="--windowed "
		if onefile.get():
			ordenes+="--onefile "
		if icon.get() and ".ico" in file_ico:
			ordenes+=("--icon="+str(file_ico.get())+" ")

		ordenes+=str(file_py.get())
		call(ordenes)
		if guardar:
			call("move dist "+guardado)
	else:
		messagebox.showinfo(words[10], words[11])
		
#--------------------------------------------------------INTERFACE------------------------------------------------
file_menu=Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label=words[0], menu=file_menu)
file_menu.add_command(label=words[1], command=Abrir_archivo)
file_menu.add_command(label=words[2], command=lambda:root.destroy())

idioma_menu=Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label=words[9], menu=idioma_menu)
idioma_menu.add_command(label="Spanish", command=lambda:Cambiar_idioma(1))
idioma_menu.add_command(label="English", command=lambda:Cambiar_idioma(2))

Label(frame, text=words[3]).grid(row=0, column=1, pady=2.5, padx=2.5)
Entry(frame, textvariable=file_py, state="readonly").grid(row=0, column=2, columnspan=2, pady=2.5, padx=2.5, ipadx=45)


Checkbutton(frame, text=words[4], variable=windowed).grid(row=1, column=3)
Checkbutton(frame, text=words[5], variable=onefile).grid(row=1, column=2)
Checkbutton(frame, text=words[6], variable=icon, command=Icon).grid(row=1, column=1)


Button(frame, text=words[7], command=Build, font=12).grid(row=2, column=3, columnspan=2, padx=10)

Button(frame, text=words[16], command=Guardar_archivo).grid(row=3, column=1, pady=2.5, padx=2.5)
Entry(frame, textvariable=guardado, state="readonly").grid(row=3, column=2, columnspan=2, pady=2.5, padx=2.5, ipadx=45)

root.mainloop()
