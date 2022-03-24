from tkinter import StringVar, BooleanVar, filedialog
from tkinter.messagebox import showinfo, showwarning
from subprocess import call
from os.path import dirname
try:
    from cryptocode import encrypt, decrypt
except:
    call("pip install cryptocode")
    from cryptocode import encrypt, decrypt


class Core:

    def __init__(self):
        # Utilizada para encryptar el archivo 'data.dat'
        # Puede ser cambiada pero recuerde que NO es la 'key' con la que se cifra el archivo 'exe'.
        self.__passkey = '6@2%*mNGf7rk@F'

        self.windowed = BooleanVar()
        self.onefile = BooleanVar()
        self.icon = BooleanVar()
        self.file_ico = StringVar()
        self.file_py = StringVar()
        self.file = 'lib/data.dat'
        self.key = StringVar()
        self.clean = BooleanVar()
        self.admin = BooleanVar()
        self.directorio_actual = ""

        # 'entry*_a' Aqui va la ruta del archivo o carpeta de origen
        self.entry1_a = StringVar()
        # 'entry*_b' Aqui va la carpeta de destino
        self.entry1_b = StringVar()
        self.entry2_a = StringVar()
        self.entry2_b = StringVar()
        self.entry3_a = StringVar()
        self.entry3_b = StringVar()
        self.entry4_a = StringVar()
        self.entry4_b = StringVar()
        self.entry5_a = StringVar()
        self.entry5_b = StringVar()
        self.entry6_a = StringVar()
        self.entry6_b = StringVar()

        #Variables del Archivo de version

        self.var_file_version = BooleanVar()
        self.var_status_file_version = StringVar()
        self.var_status_file_version.set("?")
        self.file_version_name = "lib/VSVersionInfo.temp"

        self.CompanyName = StringVar()
        self.FileDescription = StringVar()
        self.FileVersion = StringVar()
        self.InternalName = StringVar()
        self.LegalCopyright = StringVar()
        self.OriginalFilename = StringVar()
        self.ProductName = StringVar()
        self.ProductVersion = StringVar()



        try:
            archivo = open(self.file, "r")
            self.__datos_guardados = eval(decrypt(archivo.read(), self.__passkey))
            archivo.close()

            self.language = self.__datos_guardados[0] #0
            self.file_py.set(self.__datos_guardados[1]) #1
            self.windowed.set(self.__datos_guardados[2]), #2
            self.onefile.set(self.__datos_guardados[3]), #3
            self.icon.set(self.__datos_guardados[4]), #4
            self.file_ico.set(self.__datos_guardados[5]), #5
            self.key.set(self.__datos_guardados[6]), #6
            self.clean.set(self.__datos_guardados[7]), #7
            self.entry1_a.set(self.__datos_guardados[8]), #8
            self.entry1_b.set(self.__datos_guardados[9]), #9
            self.entry2_a.set(self.__datos_guardados[10]), #10
            self.entry2_b.set(self.__datos_guardados[11]), #11
            self.entry3_a.set(self.__datos_guardados[12]), #12
            self.entry3_b.set(self.__datos_guardados[13]), #13
            self.entry4_a.set(self.__datos_guardados[14]), #14
            self.entry4_b.set(self.__datos_guardados[15]), #15
            self.entry5_a.set(self.__datos_guardados[16]), #16
            self.entry5_b.set(self.__datos_guardados[17]), #17
            self.entry6_a.set(self.__datos_guardados[18]), #18
            self.entry6_b.set(self.__datos_guardados[19]), #19
            self.admin.set(self.__datos_guardados[20]), #20

            self.directorio_actual = self.__datos_guardados[21], #21

            self.var_file_version.set(self.__datos_guardados[22]), #22
            self.CompanyName.set(self.__datos_guardados[23]), #23
            self.FileDescription.set(self.__datos_guardados[24]), #24
            self.FileVersion.set(self.__datos_guardados[25]), #25
            self.InternalName.set(self.__datos_guardados[26]), #26
            self.LegalCopyright.set(self.__datos_guardados[27]), #27
            self.OriginalFilename.set(self.__datos_guardados[28]), #28
            self.ProductName.set(self.__datos_guardados[29]), #29
            self.ProductVersion.set(self.__datos_guardados[30]), #30
            


        except:
            self.language = "es"

            # La sigueinte variable se utiliza para guardar los datos, esta va cambiando en el
            # transcurso de la ejecucion.
            self.__datos_guardados = [self.language, #0
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
        
        # La siguiente instruccion se utiliza para manejar el idioma, se planea exportar
        # esta instruccion a un archivo externo para que sea mas personalizable.
        if self.language == "es":
            self.words = (
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
            
        elif self.language == "en":
            self.words = (
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
            

    def Cambiar_idioma(self, op):
        def cambio_idioma(op1):
            file_language = open(self.file, "w+")
            self.__datos_guardados[0] = op1
            file_language.write(encrypt(str(self.__datos_guardados), self.__passkey))
            file_language.close()
            showinfo(self.words[12], self.words[13])
            
            

        if op == 1 and self.language != "es":
            cambio_idioma('es')
            return True


        elif op == 2 and self.language != "en":
            cambio_idioma('en')
            return True

        else:
            return False

    def Prueba(self, ordenes):
        try:
            call("pyinstaller")

        except FileNotFoundError:
            showinfo(self.words[17], self.words[18])
            if call("pip install pyinstaller")==1:
                showwarning(self.words[10], self.words[19])
            else:
                try:
                    call(ordenes)
                except:
                    showwarning(self.words[10], self.words[20])


    def Abrir_archivo_py(self):
        open_file = filedialog.askopenfilename(initialdir=self.directorio_actual, title=self.words[14], filetypes=(("python files", "*.py"), ("python files", "*.pyw")))
        if ".py" in open_file:
            self.file_py.set(open_file)
            self.directorio_actual = dirname(open_file)

    def abrir_archivo_spec(self):
        open_file = filedialog.askopenfilename(initialdir=self.directorio_actual, title=self.words[14], filetypes=(("pyinstaller files", "*.spec"), ("", "*.*")))
        if ".spec" in open_file:
            call("pyinstaller "+open_file)        
            self.directorio_actual = dirname(open_file)

    def Abrir_icono(self):
        open_icon = filedialog.askopenfilename(initialdir=self.directorio_actual, title=self.words[14], filetypes=((".ico", "*.ico"), (".ico", "*.ico")))
        if ".ico" in open_icon:
            self.file_ico.set(open_icon)
            self.asignar_entrys(open_icon)
            self.directorio_actual = dirname(open_icon)

    def asignar_entrys(self, valor):

        if (self.entry1_a.get() == valor) or (self.entry2_a.get() == valor) or (self.entry3_a.get() == valor) or (self.entry4_a.get() == valor) or (self.entry5_a.get() == valor) or (self.entry6_a.get() == valor):
            return
        elif self.entry1_a.get()=="":
            self.entry1_a.set(valor)
        elif self.entry2_a.get()=="":
            self.entry2_a.set(valor)
        elif self.entry3_a.get()=="":
            self.entry3_a.set(valor)
        elif self.entry4_a.get()=="":
            self.entry4_a.set(valor)
        elif self.entry5_a.get()=="":
            self.entry5_a.set(valor)
        elif self.entry6_a.get()=="":
            self.entry6_a.set(valor)
        else:
            showwarning("Error", "No hay espacio para agregar mas archivos de forma individual, intente agregarlos utilizando la opcion de 'Agregar carpeta' para agregar grandes cantidades de archivos.")
            return False


    def __preparando_archivos(self):
        diccionario = {}

        temp_entry1_a = self.entry1_a.get()
        temp_entry1_b = self.entry1_b.get()
        if temp_entry1_b=="":
            temp_entry1_b = "."
        
        temp_entry2_a = self.entry2_a.get() 
        temp_entry2_b = self.entry2_b.get()
        if temp_entry2_b=="":
            temp_entry2_b = "."
        
        temp_entry3_a = self.entry3_a.get() 
        temp_entry3_b = self.entry3_b.get()
        if temp_entry3_b=="":
            temp_entry3_b = "."
        
        temp_entry4_a = self.entry4_a.get() 
        temp_entry4_b = self.entry4_b.get()
        if temp_entry4_b=="":
            temp_entry4_b = "."
        
        temp_entry5_a = self.entry5_a.get() 
        temp_entry5_b = self.entry5_b.get()
        if temp_entry5_b=="":
            temp_entry5_b = "."
        
        temp_entry6_a = self.entry6_a.get() 
        temp_entry6_b = self.entry6_b.get()
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



    def agregar_archivos(self):
        archivo = filedialog.askopenfilenames(initialdir=self.directorio_actual, title="Agregar archivos", filetypes=((".", "*.*"), ("All files", "*.*")))
        for i in archivo:
            if self.asignar_entrys(i)==False:
                break
            
        #Devuelve una tupla

    def agregar_carpeta(self):
        archivo = filedialog.askdirectory(initialdir=self.directorio_actual, title="Agregar directorio")
        self.asignar_entrys(archivo)
        self.directorio_actual = archivo

        #Devuelve la direccion de una carpeta sin comillas

    


    def Build(self):
        clave = self.key.get()




        if ".py" not in self.file_py.get():
            showinfo(self.words[10], self.words[11])
            
        else:
            ordenes = "pyinstaller "

            if clave:
                if " " in clave:
                    showinfo(self.words[10], self.words[21])
                    return

                elif len(clave) > 16:    
                    showinfo("Advertencia", "La 'key' solo admite 16 caracteres.")
                    return


                else:
                    #Necesita tener instalado 'tinyaes'
                    call("pip install tinyaes")
                    ordenes += "--key=" + clave + " "
            
            
            if self.windowed.get():
                ordenes += "--windowed "
            if self.onefile.get():
                ordenes += "--onefile "

            if self.icon.get() and (".ico" in self.file_ico.get()):
                ordenes += "--icon=" + self.file_ico.get() + " "
            

            if self.clean.get():
                ordenes+="--clean "

            if self.admin.get():
                ordenes+= "--uac-admin "

            #La siguiente funcion recolecta los archivos y carpetas para ser añadidas al ejecutable
            ordenes+=self.__preparando_archivos()       

            if self.var_file_version.get() and self.var_status_file_version.get()!="?":
                ordenes+=" --version-file=" + self.file_version_name + " "

            ordenes += self.file_py.get()

            try:
                self.__datos_guardados = [self.language, #0
                    self.file_py.get(), #1
                    self.windowed.get(), #2
                    self.onefile.get(), #3
                    self.icon.get(), #4
                    self.file_ico.get(), #5
                    clave, #6
                    self.clean.get(), #7
                    self.entry1_a.get(), #8
                    self.entry1_b.get(), #9
                    self.entry2_a.get(), #10
                    self.entry2_b.get(), #11
                    self.entry3_a.get(), #12
                    self.entry3_b.get(), #13
                    self.entry4_a.get(), #14
                    self.entry4_b.get(), #15
                    self.entry5_a.get(), #16
                    self.entry5_b.get(), #17
                    self.entry6_a.get(), #18
                    self.entry6_b.get(), #19
                    self.admin.get(), #20
                    self.directorio_actual, #21

                    self.var_file_version.get(), #22
                    self.CompanyName.get(), #23
                    self.FileDescription.get(), #24
                    self.FileVersion.get(), #25
                    self.InternalName.get(), #26
                    self.LegalCopyright.get(), #27
                    self.OriginalFilename.get(), #28
                    self.ProductName.get(), #29
                    self.ProductVersion.get(), #30
                ]

                archivo = open(self.file, "w")
                archivo.write(encrypt(str(self.__datos_guardados), self.__passkey))
                archivo.close()

                call(ordenes)

            except FileNotFoundError:
                self.Prueba(ordenes)


    def crear_file_version(self):
        CompanyName2 = self.CompanyName.get()
        FileDescription2 = self.FileDescription.get()
        FileVersion2 = self.FileVersion.get()
        fv = FileVersion2

        fv = fv.replace(".", ",").replace("v", "").replace("V", "")

        fv = eval("["+fv+"]")

        num = len(fv)

        if num > 4:
            showinfo("Error",
                "'ProductVersion' solo admite 4 fracciones separadas por punto.\n\nEjemplo: '1.0.0.0', '5.432.567.12'")
            return

        else:
            while num < 4:
                fv.append(0)
                num += 1

        fv = str(fv)
        fv = fv.replace("[", "").replace("]", "")
  

        InternalName2 = self.InternalName.get()
        LegalCopyright2 = self.LegalCopyright.get()
        OriginalFilename2 = self.OriginalFilename.get()
        ProductName2 = self.ProductName.get()
        ProductVersion2 = self.ProductVersion.get()


        file_version = """
VSVersionInfo(
	ffi=FixedFileInfo(
		filevers=("""+fv+"""),
		prodvers=("""+fv+"""),
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
        archivo = open(self.file_version_name, "w")
        archivo.write(file_version)
        archivo.close()
        self.var_status_file_version.set("*ArchivoVersion creado")





