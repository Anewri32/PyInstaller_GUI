from tkinter import BooleanVar, Tk, Frame, PhotoImage, StringVar, Label, Entry, Button, Menu, \
    Checkbutton, filedialog
from tkinter.messagebox import showinfo, showwarning
from subprocess import call

# ------------------------------------------------------CORE_INTERFACE---------------------------------------------
root = Tk()
root.iconbitmap('lib/icon.ico')
bg = PhotoImage(file="lib/BG.png")
Label(root, image=bg).grid(row=0, column=0, columnspan=4, rowspan=4)
barra_menu = Menu(root)
root.config(menu=barra_menu)
root.title("PyInstaller GUI v1.1")
root.attributes("-alpha", 0.9)
root.resizable(0, 0)
frame = Frame(root).grid(row=0, column=0)

# -----------------------------------------------------VARIABLES---------------------------------------------------
windowed = BooleanVar()
onefile = BooleanVar()
icon = BooleanVar()
file_ico = StringVar()
file_py = StringVar()
#guardado = StringVar()
#guardar = False
file = 'lib/language.txt'


# ------------------------------------------------------IDIOMA----------------------------------------------------


def Set_idioma():
    try:
        file_language = open(file, "r+")
        language = file_language.read()
        file_language.close()
    except:
        file_language = open(file, "w+")
        file_language.write("en")
        language = "en"
        file_language.close()

    while True:
        if language == "es":
            words = (
                "Archivo",  # 0
                "Abrir archivo",  # 1
                "Salir",  # 2
                "Nombre del archivo:",  # 3
                "Ventaneado",  # 4
                "Un archivo",  # 5
                "Icono",  # 6
                "Construir",  # 7
                "Seleccionar icono",  # 8
                "Idioma",  # 9
                "Error",  # 10
                "No hay archivos seleccionados",  # 11
                "Cambios aplicados",  # 12
                "Es necesario reiniciar el programa para aplicar los cambios",  # 13
                "Seleccione archivo",  # 14
                "Directorio de archivo a crear:",  # 15
                "Ubicacion del\narchivo saliente:",  # 16
                "Faltan archivos", # 17
                "Pyinstaller no esta instalado en el equipo, se procedera a instalarse", #18
                "Puede que no este conectado a internet", #19
                "Error desconocido", #20
            )
            break
        elif language == "en":
            words = (
                "File",  # 0
                "Open file",  # 1
                "Exit",  # 2
                "File name:",  # 3
                "Windowed",  # 4
                "One file",  # 5
                "Icon",  # 6
                "Build",  # 7
                "Select icon",  # 8
                "Language",  # 9
                "Error",  # 10
                "No files selected",  # 11
                "Changes applied",  # 12
                "It is necessary to restart the program to apply the changes",  # 13
                "Select file",  # 14
                "File directory to create:",  # 15
                "Outgoing file\nlocation:",  # 16
                "Missing files", #17
                "Pyinstaller is not installed on the computer, it will proceed to install", #18
                "It may not be connected to the internet", #19
                "Unknown error", #20
            )
            break
        else:
            file_language = open(file, "w+")
            file_language.write("en")
            language = "en"
            file_language.close()
    return language, words


language, words = Set_idioma()


def Cambiar_idioma(op):
    def cambio_idioma(op1):
        file_language = open(file, "w+")
        file_language.write(op1)
        file_language.close()
        showinfo(words[12], words[13])
        root.destroy()

    if op == 1 and language != "es":
        cambio_idioma('es')


    elif op == 2 and language != "en":
        cambio_idioma('en')


# ------------------------------------------------------CORE_PROGRAM-----------------------------------------------

def Prueba(ordenes):
    try:
        call("pyinstaller")

    except FileNotFoundError:
        showinfo(words[17], words[18])
        if call("pip install pyinstaller")==1:
            showwarning(words[10], words[19])
        else:
            try:
                call(ordenes)
            except:
                showwarning(words[10], words[20])

"""def Guardar_archivo():
    save_file = filedialog.askdirectory(initialdir="/", title=words[15])
    if ":" in save_file:
        guardado.set(save_file + "/")
        guardar = True"""


def Abrir_archivo():
    open_file = filedialog.askopenfilename(initialdir="/", title=words[14], filetypes=(("python files", "*.py"), ("python files", "*.pyw")))
    if ".py" in open_file:
        file_py.set(open_file)


def Abrir_icono():
    open_icon = filedialog.askopenfilename(initialdir="/", title=words[14], filetypes=((".ico", "*.ico"), (".ico", "*.ico")))
    if ".ico" in open_icon:
        file_ico.set(open_icon)


def Icon():
    if icon.get():
        Button(frame, text=words[8], command=Abrir_icono).grid(row=2, column=1, padx=2.5)
        Entry(frame, textvariable=file_ico, state="readonly").grid(row=2, column=2, padx=2.5)


def Build():
    if ".py" in file_py.get():
        ordenes = "pyinstaller "
        if windowed.get():
            ordenes += "--windowed "
        if onefile.get():
            ordenes += "--onefile "
        if icon.get() and ".ico" in file_ico.get():
            ordenes += ("--icon=" + str(file_ico.get()) + " ")

        
        ordenes += str(file_py.get())

        try:
            call(ordenes)
        except FileNotFoundError:
            Prueba(ordenes)
    else:
        showinfo(words[10], words[11])


# --------------------------------------------------------INTERFACE------------------------------------------------
file_menu = Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label=words[0], menu=file_menu)
file_menu.add_command(label=words[1], command=Abrir_archivo)
file_menu.add_command(label=words[2], command=lambda: root.destroy())

idioma_menu = Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label=words[9], menu=idioma_menu)
idioma_menu.add_command(label="Spanish", command=lambda: Cambiar_idioma(1))
idioma_menu.add_command(label="English", command=lambda: Cambiar_idioma(2))

Label(frame, text=words[3]).grid(row=0, column=1, pady=2.5, padx=2.5)
Entry(frame, textvariable=file_py, state="readonly").grid(row=0, column=2, columnspan=2, pady=2.5, padx=2.5, ipadx=45)

Checkbutton(frame, text=words[4], variable=windowed).grid(row=1, column=3)
Checkbutton(frame, text=words[5], variable=onefile).grid(row=1, column=2)
Checkbutton(frame, text=words[6], variable=icon, command=Icon).grid(row=1, column=1)

Button(frame, text=words[7], command=Build, font=12).grid(row=2, column=3, columnspan=2, padx=10)

#Button(frame, text=words[16], command=Guardar_archivo).grid(row=3, column=1, pady=2.5, padx=2.5)
#Entry(frame, textvariable=guardado, state="readonly").grid(row=3, column=2, columnspan=2, pady=2.5, padx=2.5, ipadx=45)

root.mainloop()
