from tkinter import Tk, Frame, messagebox, PhotoImage, StringVar, IntVar, Label, Entry, Button, Menu, Checkbutton, filedialog
from subprocess import call

#------------------------------------------------------CORE_INTERFACE---------------------------------------------
root=Tk()
bg=PhotoImage(file="BG.png")
Label(root, image=bg).grid(row=0, column=0, columnspan=4, rowspan=4)
barra_menu=Menu(root)
root.config(menu=barra_menu)
root.title("PyInstaller GUI")
root.attributes("-alpha", 0.9)
root.resizable(0,0)
frame=Frame(root).grid(row=0, column=0)

#-----------------------------------------------------VARIABLES---------------------------------------------------
windowed=IntVar()
onefile=IntVar()
icon=IntVar()
file_ico=StringVar()
file_py=StringVar()
#guardado=StringVar()
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

if language=="es":
	op1="Archivo"
	op2="Abrir archivo"
	op3="Salir"
	op4="Nombre del archivo:"
	op5="Ventaneado"
	op6="Un archivo"
	op7="Icono"
	op8="Construir"
	op9="Localizacion del archivo:"
	op10="Seleccionar icono"
elif language=="en":
	op1="File"
	op2="Open file"
	op3="Exit"
	op4="File name:"
	op5="Windowed"
	op6="One file"
	op7="Icon"
	op8="Build"
	op9="File location:"
	op10="Select icon"

file_language.close()

def Cambiar_idioma(op):
	if op==1 and language!="es":
		file_language=open("language.txt", "w+")
		file_language.write("es")
		file_language.close()
		messagebox.showinfo("Cambios aplicados","Es necesario reiniciar el programa para aplicar los cambios")
		root.destroy()

	elif op==2 and language!="en":
		file_language=open("language.txt", "w+")
		file_language.write("en")
		file_language.close()
		messagebox.showinfo("Changes applied","It is necessary to restart the program to apply the changes")
		root.destroy()

#------------------------------------------------------CORE_PROGRAM-----------------------------------------------

def Abrir_archivo():
	open_file=filedialog.askopenfilename(initialdir="/", title="Seleccione archivo", filetypes=(("python files", "*.py"), ("python files", "*.pyw")))
	file_py.set(open_file)
def Abrir_icono():
	open_icon=filedialog.askopenfilename(initialdir="/", title="Seleccione archivo", filetypes=((".ico", "*.ico"), (".ico", "*.ico")))
	file_ico.set(open_icon)
def Icon():
	if icon.get()==1:
		Button(frame, text=op10, command=Abrir_icono).grid(row=2, column=1, padx=2.5)
		Entry(frame, textvariable=file_ico, state="readonly").grid(row=2, column=2, padx=2.5)
def Build():
	if ".py" in file_py.get():	
		ordenes="py_extencion.exe "
		if windowed.get()==1:
			ordenes+="--windowed "
		if onefile.get()==1:
			ordenes+="--onefile "
		if icon.get()==1:
			ordenes+=("--icon="+str(file_ico.get())+" ")

		ordenes+=str(file_py.get())
		call(ordenes)
	else:
		messagebox.showinfo("Error","No hay archivos seleccionados")
		
#--------------------------------------------------------INTERFACE------------------------------------------------
file_menu=Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label=op1, menu=file_menu)
file_menu.add_command(label=op2, command=Abrir_archivo)
file_menu.add_command(label=op3, command=lambda:root.destroy())

idioma_menu=Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Idioma", menu=idioma_menu)
idioma_menu.add_command(label="Spanish", command=lambda:Cambiar_idioma(1))
idioma_menu.add_command(label="English", command=lambda:Cambiar_idioma(2))

Label(frame, text=op4).grid(row=0, column=1, pady=2.5, padx=2.5)
Entry(frame, textvariable=file_py, state="readonly").grid(row=0, column=2, columnspan=2, pady=2.5, padx=2.5, ipadx=45)


Checkbutton(frame, text=op5, variable=windowed).grid(row=1, column=3)
Checkbutton(frame, text=op6, variable=onefile).grid(row=1, column=2)
Checkbutton(frame, text=op7, variable=icon, command=Icon).grid(row=1, column=1)


Button(frame, text=op8, command=Build, font=12).grid(row=2, column=3, columnspan=2, padx=10)

#Button(Frame, text=op9).grid(row=3, column=1, pady=2.5, padx=2.5)
#Entry(Frame, textvariable=guardado, state="readonly").grid(row=3, column=2, columnspan=2, pady=2.5, padx=2.5, ipadx=45)

root.mainloop()
