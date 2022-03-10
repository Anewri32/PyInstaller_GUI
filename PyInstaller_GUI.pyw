from tkinter import BooleanVar, Tk, Frame, StringVar, Label, Entry, Button, Menu, \
    Checkbutton, filedialog, Toplevel
from tkinter.messagebox import showinfo, showwarning
from subprocess import call
from os.path import dirname # Devuelve el directorio de un archivo

# ------------------------------------------------------CORE_INTERFACE---------------------------------------------
root = Tk()
root.iconbitmap('lib/icon.ico')
barra_menu = Menu(root)
root.config(menu=barra_menu)
root.title("PyInstaller GUI v2.0")
root.resizable(0, 0)
frame = Frame(root).grid(row=0, column=0)

root2 = None
# -----------------------------------------------------VARIABLES---------------------------------------------------
windowed = BooleanVar()
onefile = BooleanVar()
icon = BooleanVar()
file_ico = StringVar()
file_py = StringVar()
file = 'lib/data.py'
key = StringVar()
clean = BooleanVar()
admin = BooleanVar()
directorio_actual = ""


entry1_a = StringVar()#Aqui va la ruta del archivo o carpeta de origen
entry1_b = StringVar()#Aqui va la carpeta de destino
entry2_a = StringVar()
entry2_b = StringVar()
entry3_a = StringVar()
entry3_b = StringVar()
entry4_a = StringVar()
entry4_b = StringVar()
entry5_a = StringVar()
entry5_b = StringVar()
entry6_a = StringVar()
entry6_b = StringVar()

#Variables para las opciones avanzadas "Archivo de version"

var_file_version = BooleanVar()
var_status_file_version = StringVar()
var_status_file_version.set("?")
file_version_name = "lib/VSVersionInfo.temp"


CompanyName = StringVar()
FileDescription = StringVar()
FileVersion = StringVar()
InternalName = StringVar()
LegalCopyright = StringVar()
OriginalFilename = StringVar()
ProductName = StringVar()
ProductVersion = StringVar()
# ------------------------------------------------------IDIOMA----------------------------------------------------

try:
    archivo = open(file, "r")
    datos_guardados = eval(archivo.read())
    archivo.close()

    language = datos_guardados[0] #0
    file_py.set(datos_guardados[1]) #1
    windowed.set(datos_guardados[2]), #2
    onefile.set(datos_guardados[3]), #3
    icon.set(datos_guardados[4]), #4
    file_ico.set(datos_guardados[5]), #5
    key.set(datos_guardados[6]), #6
    clean.set(datos_guardados[7]), #7
    entry1_a.set(datos_guardados[8]), #8
    entry1_b.set(datos_guardados[9]), #9
    entry2_a.set(datos_guardados[10]), #10
    entry2_b.set(datos_guardados[11]), #11
    entry3_a.set(datos_guardados[12]), #12
    entry3_b.set(datos_guardados[13]), #13
    entry4_a.set(datos_guardados[14]), #14
    entry4_b.set(datos_guardados[15]), #15
    entry5_a.set(datos_guardados[16]), #16
    entry5_b.set(datos_guardados[17]), #17
    entry6_a.set(datos_guardados[18]), #18
    entry6_b.set(datos_guardados[19]), #19
    admin.set(datos_guardados[20]), #20

    directorio_actual = datos_guardados[21], #21

    var_file_version.set(datos_guardados[22]), #22
    CompanyName.set(datos_guardados[23]), #23
    FileDescription.set(datos_guardados[24]), #24
    FileVersion.set(datos_guardados[25]), #25
    InternalName.set(datos_guardados[26]), #26
    LegalCopyright.set(datos_guardados[27]), #27
    OriginalFilename.set(datos_guardados[28]), #28
    ProductName.set(datos_guardados[29]), #29
    ProductVersion.set(datos_guardados[30]), #30
    


except:
    datos_guardados = ["", #0
    "", #1
    False, #2
    False, #3
    False, #4
    "", #5
    "", #6
    False, #7
    "", #8
    "", #9
    "", #10
    "", #11
    "", #12
    "", #13
    "", #14
    "", #15
    "", #16
    "", #17
    "", #18
    "", #19
    False, #20
    "", #21
    False, #22
    "", #23
    "", #24
    "", #25
    "", #26
    "", #27
    "", #28
    "", #29
    "", #30
    ]
    language="en"   

def Set_idioma():
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
            "No pueden haber espacios en el apartado 'key'" #21
        )
        
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
            "There can be no spaces in the 'key' section" #21
        )
    return words


words = Set_idioma()


def Cambiar_idioma(op):
    def cambio_idioma(op1):
        global words, datos_guardados
        file_language = open(file, "w+")
        datos_guardados[0] = op1
        file_language.write(str(datos_guardados))
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


def Abrir_archivo_py():
    global directorio_actual
    open_file = filedialog.askopenfilename(initialdir=directorio_actual, title=words[14], filetypes=(("python files", "*.py"), ("python files", "*.pyw")))
    if ".py" in open_file:
        file_py.set(open_file)
        directorio_actual = dirname(open_file)

def abrir_archivo_spec():
    global directorio_actual
    open_file = filedialog.askopenfilename(initialdir=directorio_actual, title=words[14], filetypes=(("pyinstaller files", "*.spec"), ("", "*.*")))
    if ".spec" in open_file:
        call("pyinstaller "+open_file)        
        directorio_actual = dirname(open_file)

def Abrir_icono():
    global directorio_actual
    open_icon = filedialog.askopenfilename(initialdir=directorio_actual, title=words[14], filetypes=((".ico", "*.ico"), (".ico", "*.ico")))
    if ".ico" in open_icon:
        file_ico.set(open_icon)
        directorio_actual = dirname(open_icon)

def asignar_entrys(valor):

    if entry1_a.get()=="":
        entry1_a.set(valor)
    elif entry2_a.get()=="":
        entry2_a.set(valor)
    elif entry3_a.get()=="":
        entry3_a.set(valor)
    elif entry4_a.get()=="":
        entry4_a.set(valor)
    elif entry5_a.get()=="":
        entry5_a.set(valor)
    elif entry6_a.get()=="":
        entry6_a.set(valor)
    else:
        showwarning("Error", "No hay espacio para agregar mas archivos de forma individual, intente agregarlos utilizando la opcion de 'Agregar carpeta' para agregar grandes cantidades de archivos.")
        return False


def preparando_archivos():
    diccionario = {}

    temp_entry1_a = entry1_a.get()
    temp_entry1_b = entry1_b.get()
    if temp_entry1_b=="":
        temp_entry1_b = "."
    
    temp_entry2_a = entry2_a.get() 
    temp_entry2_b = entry2_b.get()
    if temp_entry2_b=="":
        temp_entry2_b = "."
    
    temp_entry3_a = entry3_a.get() 
    temp_entry3_b = entry3_b.get()
    if temp_entry3_b=="":
        temp_entry3_b = "."
    
    temp_entry4_a = entry4_a.get() 
    temp_entry4_b = entry4_b.get()
    if temp_entry4_b=="":
        temp_entry4_b = "."
    
    temp_entry5_a = entry5_a.get() 
    temp_entry5_b = entry5_b.get()
    if temp_entry5_b=="":
        temp_entry5_b = "."
    
    temp_entry6_a = entry6_a.get() 
    temp_entry6_b = entry6_b.get()
    if temp_entry6_b=="":
        temp_entry6_b = "."



    if temp_entry1_a:
        diccionario[temp_entry1_a]=temp_entry1_b
    if temp_entry2_a:
        diccionario[temp_entry2_a]=temp_entry2_b
    if temp_entry3_a:
        diccionario[temp_entry3_a]=temp_entry3_b
    if temp_entry4_a:
        diccionario[temp_entry4_a]=temp_entry4_b
    if temp_entry5_a:
        diccionario[temp_entry5_a]=temp_entry5_b
    if temp_entry6_a:
        diccionario[temp_entry6_a]=temp_entry6_b

    instrucciones = ""
    for key, value in diccionario.items():
        instrucciones+= "--add-data="+key+";"+value+" "

    return instrucciones



def agregar_archivos():
    archivo = filedialog.askopenfilenames(initialdir=directorio_actual, title="Agregar archivos", filetypes=((".", "*.*"), ("All files", "*.*")))
    for i in archivo:
        if asignar_entrys(i)==False:
            break
        
    #Devuelve una tupla

def agregar_carpeta():
    global directorio_actual
    archivo = filedialog.askdirectory(initialdir=directorio_actual, title="Agregar directorio")
    asignar_entrys(archivo)
    directorio_actual = archivo

    #Devuelve la direccion de una carpeta sin comillas

def Icon():
    if icon.get():
        icono_boton.grid(row=2, column=0)
        icono_entrada.grid(row=2, column=1, columnspan=8, ipadx=250)
    else:
        icono_boton.grid_remove()
        icono_entrada.grid_remove()



def opciones_avanzadas(op):
    global var_status_file_version
    def start():
        global root2
        root2 = Toplevel()
        root2.iconbitmap('lib/icon.ico')
        root2.title("PyInstaller GUI v1.1 - Archivo de version")
        root2.resizable(0, 0)


		

        global CompanyName, FileDescription, FileVersion, InternalName, LegalCopyright, OriginalFilename, ProductName, ProductVersion, FileDescription_entry, FileVersion_entry, InternalName_entry, LegalCopyright_entry, OriginalFilename_entry, ProductName_entry, ProductVersion_entry, var_status_file_version
        
        label1 = Label(root2, text="CompanyName:")
        entry1 = Entry(root2, width=66, textvariable=CompanyName)
        label2 = Label(root2, text="FileDescription:")
        entry2 = Entry(root2, width=66, textvariable=FileDescription)
        label3 = Label(root2, text="FileVersion:")
        entry3 = Entry(root2, width=66, textvariable=FileVersion)
        label4 = Label(root2, text="InternalName:")
        entry4 = Entry(root2, width=66, textvariable=InternalName)
        label5 = Label(root2, text="LegalCopyright:")
        entry5 = Entry(root2, width=66, textvariable=LegalCopyright)
        label6 = Label(root2, text="OriginalFilename:")
        entry6 = Entry(root2, width=66, textvariable=OriginalFilename)
        label7 = Label(root2, text="ProductName:")
        entry7 = Entry(root2, width=66, textvariable=ProductName)
        label8 = Label(root2, text="ProductVersion:")
        entry8 = Entry(root2, width=66, textvariable=ProductVersion)
        Button(root2, text="Guardar", command=lambda:opciones_avanzadas("03")).grid(row=8, column=0, columnspan=2)
        Button(root2, text="Cancelar", command=lambda:opciones_avanzadas("02")).grid(row=8, column=2, columnspan=2)




        label1.grid(row=0, column=0, pady=2.5)
        entry1.grid(row=0, column=1, pady=2.5, columnspan=5)
        label2.grid(row=1, column=0, pady=2.5)
        entry2.grid(row=1, column=1, pady=2.5, columnspan=5)
        label3.grid(row=2, column=0, pady=2.5)
        entry3.grid(row=2, column=1, pady=2.5, columnspan=5)
        label4.grid(row=3, column=0, pady=2.5)
        entry4.grid(row=3, column=1, pady=2.5, columnspan=5)
        label5.grid(row=4, column=0, pady=2.5)
        entry5.grid(row=4, column=1, pady=2.5, columnspan=5)
        label6.grid(row=5, column=0, pady=2.5)
        entry6.grid(row=5, column=1, pady=2.5, columnspan=5)
        label7.grid(row=6, column=0, pady=2.5)
        entry7.grid(row=6, column=1, pady=2.5, columnspan=5)
        label8.grid(row=7, column=0, pady=2.5)
        entry8.grid(row=7, column=1, pady=2.5, columnspan=5)


        root2.mainloop()

		

    def stop():
        if root2:
            root2.destroy()

    if op=="01":
        if var_file_version.get():
            start()
        else:
            stop()
    elif op=="02":
        stop()

    elif op=="03":
        
        global CompanyName, FileDescription, FileVersion, InternalName, LegalCopyright, OriginalFilename, ProductName, ProductVersion, FileDescription_entry, FileVersion_entry, InternalName_entry, LegalCopyright_entry, OriginalFilename_entry, ProductName_entry, ProductVersion_entry, var_status_file_version
        

        CompanyName2 = CompanyName.get()
        FileDescription2 = FileDescription.get()
        FileVersion2 = FileVersion.get()
        FL = FileVersion2
        
        FL = FL.replace(".", ",").replace("v", "").replace("V", "")

        FL = eval("["+FL+"]")

        num = len(FL)

        if num > 4:
            showinfo("Error",
                "'ProductVersion' solo admite 4 fracciones separadas por punto.\n\nEjemplo: '1.0.0.0', '5.432.567.12'")
            return

        else:
            while num < 4:
                FL.append(0)
                num += 1

        FL = str(FL)
        FL = FL.replace("[", "").replace("]", "")
  

        InternalName2 = InternalName.get()
        LegalCopyright2 = LegalCopyright.get()
        OriginalFilename2 = OriginalFilename.get()
        ProductName2 = ProductName.get()
        ProductVersion2 = ProductVersion.get()


        file_version = """
VSVersionInfo(
	ffi=FixedFileInfo(
		filevers=("""+FL+"""),
		prodvers=("""+FL+"""),
		mask=0x3f,
		flags=0x0,
		OS=0x40004,
		fileType=0x1,
		subtype=0x0,
		date=(0, 0)
	),
	kids=[
		StringFileInfo(
            [
                StringTable(
                    u'040904B0',
                    [StringStruct(u'CompanyName', u'"""+CompanyName2+"""'),
                        StringStruct(u'FileDescription', u'"""+FileDescription2+"""'),
                        StringStruct(u'FileVersion', u'"""+FileVersion2+""" (win7sp1_rtm.101119-1850)'), 
                        StringStruct(u'InternalName', u'"""+InternalName2+"""'),
                        StringStruct(u'LegalCopyright', u'"""+LegalCopyright2+"""'),
                        StringStruct(u'OriginalFilename', u'"""+OriginalFilename2+"""'),
                        StringStruct(u'ProductName', u'"""+ProductName2+"""'),
                        StringStruct(u'ProductVersion', u'"""+ProductVersion2+"""')
                    ]
                )
            ]
        ), 
        VarFileInfo([VarStruct(u'Translation', [1033, 1200])])
    ]
)"""
        archivo = open(file_version_name, "w")
        archivo.write(file_version)
        archivo.close()
        var_status_file_version.set("*ArchivoVersion creado")


def Build():
    global datos_guardados
    clave = key.get()




    if ".py" not in file_py.get():
        showinfo(words[10], words[11])
        
    else:
        ordenes = "pyinstaller "

        if clave:
            if " " in clave:
                showinfo(words[10], words[21])
                return

            elif len(clave) > 16:    
                showinfo("Advertencia", "La 'key' solo admite 16 caracteres.")
                return


            else:
                call("pip install tinyaes")
                ordenes += "--key=" + clave + " "
        
        
        if windowed.get():
            ordenes += "--windowed "
        if onefile.get():
            ordenes += "--onefile "

        if icon.get() and (".ico" in file_ico.get()):
            ordenes += "--icon=" + file_ico.get() + " "
        

        if clean.get():
            ordenes+="--clean "

        if admin.get():
            ordenes+= "--uac-admin "

        #La siguiente funcion recolecta los archivos y carpetas para ser añadidas al ejecutable
        ordenes+=preparando_archivos()       

        if var_file_version.get() and var_status_file_version.get()!="?":
            ordenes+=" --version-file=" + file_version_name + " "

        ordenes += file_py.get()

        try:
            datos_guardados = [language, #0
                file_py.get(), #1
                windowed.get(), #2
                onefile.get(), #3
                icon.get(), #4
                file_ico.get(), #5
                clave, #6
                clean.get(), #7
                entry1_a.get(), #8
                entry1_b.get(), #9
                entry2_a.get(), #10
                entry2_b.get(), #11
                entry3_a.get(), #12
                entry3_b.get(), #13
                entry4_a.get(), #14
                entry4_b.get(), #15
                entry5_a.get(), #16
                entry5_b.get(), #17
                entry6_a.get(), #18
                entry6_b.get(), #19
                admin.get(), #20
                directorio_actual, #21

                var_file_version.get(), #22
                CompanyName.get(), #23
                FileDescription.get(), #24
                FileVersion.get(), #25
                InternalName.get(), #26
                LegalCopyright.get(), #27
                OriginalFilename.get(), #28
                ProductName.get(), #29
                ProductVersion.get(), #30
            ]

            archivo = open(file, "w")
            archivo.write(str(datos_guardados))
            archivo.close()

            call(ordenes)

        except FileNotFoundError:
            Prueba(ordenes)


# --------------------------------------------------------INTERFACE------------------------------------------------
file_menu = Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label=words[0], menu=file_menu)
file_menu.add_command(label=words[1], command=Abrir_archivo_py)
file_menu.add_command(label="Ejecutar .spec", command=abrir_archivo_spec)
file_menu.add_command(label=words[2], command=lambda: root.destroy())

idioma_menu = Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label=words[9], menu=idioma_menu)
idioma_menu.add_command(label="Spanish", command=lambda: Cambiar_idioma(1))
idioma_menu.add_command(label="English", command=lambda: Cambiar_idioma(2))

#--------------------------------------------------------------------------------------------



Label(frame, text=words[3]).grid(row=0, column=0, pady=2.5, padx=2.5)

Entry(frame, textvariable=file_py).grid(row=0, column=1, columnspan=8, pady=2.5, padx=2.5, ipadx=250)


Checkbutton(frame, text=words[6], variable=icon, command=Icon).grid(row=1, column=0)

Checkbutton(frame, text=words[5], variable=onefile).grid(row=1, column=1)



Checkbutton(frame, text=words[4], variable=windowed).grid(row=1, column=3)

Label(frame, text="key:", anchor="e").grid(row=1, column=4, pady=2.5)

Entry(frame, textvariable=key).grid(row=1, column=5, pady=2.5)

Checkbutton(frame, text="Administrador", variable=admin).grid(row=1, column=6)

Checkbutton(frame, text="Limpiar cache", variable=clean).grid(row=1, column=7)






icono_boton = Button(frame, text=words[8], command=Abrir_icono)
icono_entrada = Entry(frame, textvariable=file_ico)



Label(frame, text="Directorios de origen ( Archivos o carpetas) para incluir en el exe.").grid(row=4, column=1, columnspan=5,pady=5)


Entry(frame, width=66, textvariable=entry1_a).grid(row=5, column=1, columnspan=5)
Entry(frame, width=66, textvariable=entry2_a).grid(row=6, column=1, columnspan=5)
Entry(frame, width=66, textvariable=entry3_a).grid(row=7, column=1, columnspan=5)
Entry(frame, width=66, textvariable=entry4_a).grid(row=8, column=1, columnspan=5)
Entry(frame, width=66, textvariable=entry5_a).grid(row=9, column=1, columnspan=5)
Entry(frame, width=66, textvariable=entry6_a).grid(row=10, column=1, columnspan=5)

Label(frame, text="Directorios de destino:").grid(row=4, column=6)
Entry(frame, textvariable=entry1_b).grid(row=5, column=6, padx=5)
Entry(frame, textvariable=entry2_b).grid(row=6, column=6, padx=5)
Entry(frame, textvariable=entry3_b).grid(row=7, column=6, padx=5)
Entry(frame, textvariable=entry4_b).grid(row=8, column=6, padx=5)
Entry(frame, textvariable=entry5_b).grid(row=9, column=6, padx=5)
Entry(frame, textvariable=entry6_b).grid(row=10, column=6, padx=5)




Button(frame, text="Agregar archivos", command=agregar_archivos).grid(row=5, column=0, rowspan=3)
Label(frame, text="o").grid(row=6, column=0, rowspan=4)
Button(frame, text="Agregar carpeta", command=agregar_carpeta).grid(row=8, column=0, rowspan=3)




Checkbutton(frame, text="Archivo de version", variable=var_file_version, command=lambda:opciones_avanzadas("01")).grid(row=5, column=7)
caja_resultado = Label(frame, textvariable=var_status_file_version)
caja_resultado.grid(row=6, column=7)


Button(frame, text=words[7], command=Build, font=12, bd=5).grid(row=9, column=7, padx=10, rowspan=2)






Icon()
root.mainloop()




